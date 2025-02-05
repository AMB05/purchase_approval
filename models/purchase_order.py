from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[
        ("waiting_approval", "Waiting Approval")
    ], ondelete={"waiting_approval": "set default"})

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
            if order.state == "waiting_approval":
                order.state = "purchase"
            else:
                raise UserError(_("Only orders in 'Waiting Approval' state can be approved."))
