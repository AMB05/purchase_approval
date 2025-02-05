from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[
        ("waiting_approval", "Waiting Approval")
    ], ondelete={"waiting_approval": "set default", "approved": "set default"})

    approved_by = fields.Many2one('res.users', string="Approved By", readonly=True)

    def button_confirm(self):
        """Override tombol Confirm Order agar memerlukan approval jika total lebih dari $5000."""
        for order in self:
            if order.amount_total > 5000:
                order.state = "waiting_approval"
            else:
                super(PurchaseOrder, order).button_confirm()

    def action_approve(self):
        """Approve the purchase order jika dalam status 'Waiting Approval'."""
        for order in self:
            if order.state != "waiting_approval":
                raise UserError(_("Only orders in 'Waiting Approval' state can be approved."))
            if not self.env.user.has_group('purchase.group_purchase_manager'):
                raise UserError(_("Only managers can approve this order."))

            order.state = "approved"
            order.approved_by = self.env.user

    def action_force_confirm(self):
        """Force confirm an approved order."""
        for order in self:
            if order.state != "approved":
                raise UserError(_("Only 'Approved' orders can be confirmed."))
            super(PurchaseOrder, order).button_confirm()