from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[
            ("waiting_approval", "Waiting Approval"), 
            ("approved", "Approved")], 
            ondelete={"waiting_approval": "set default", "approved": "set default"})
    approved_by = fields.Many2one('res.users', string="Approved By", readonly=True)

    # button confirm
    def button_confirm(self):
        # Override Button Confirm Order if amount total >= $5000 waiting_approval
        for order in self:
            if order.amount_total >= 5000:
                order.state = "waiting_approval"
            else:
                super(PurchaseOrder, order).button_confirm()
    
    # approve manager if status waiting approval
    def action_approve(self):
        for order in self:
            if order.state != "waiting_approval":
                raise UserError(_("Only orders in 'Waiting Approval' state can be approved."))
            if not self.env.user.has_group('purchase.group_purchase_manager'):
                raise UserError(_("Only managers can approve this order."))

            order.state = "purchase"
            order.approved_by = self.env.user
