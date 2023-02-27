# Copyright 2023-TODAY Rapsodoo Iberia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    validated_by = fields.Many2one('res.users', string='Validated by')

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            order.validated_by = self.env.user.id
        return res

    def button_cancel(self):
        res = super(PurchaseOrder, self).button_cancel()
        for order in self:
            order.validated_by = False
        return res
