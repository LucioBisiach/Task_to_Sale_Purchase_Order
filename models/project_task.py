# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    sale_order_ids = fields.One2many('sale.order', 'task_id', 'Sales Orders')
    purchase_orders_ids = fields.One2many('purchase.order', 'task_id', 'Purchases Orders')

    total_ventas = fields.Integer(compute='get_tot_sales', store=False)
    total_compras = fields.Integer(compute='get_tot_purchases', store=False)

    provider = fields.Many2one('res.partner', domain="[('supplier', '=', True)]", store=True, string="Supplier")

    @api.one
    @api.depends('sale_order_ids')
    def get_tot_sales(self):
        self.total_ventas = sum(order.amount_total for order in self.sale_order_ids.filtered(
            lambda s: s.state in ('sale')))

    @api.multi
    def act_show_sales(self, context=None):
        action = self.env.ref('sale.action_orders')

        result = {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'target': action.target,
            'res_model': action.res_model,
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_task_id': self.ids[0],
                'default_date_order': self.date_assign,
                'default_validity_date': self.date_assign
            }
        }
        result['domain'] = "[('id','in',[" + \
            ','.join(map(str, self.sale_order_ids.ids))+"])]"
        return result

    @api.multi
    def act_show_purchases(self):
        action = self.env.ref('purchase.purchase_form_action')

        result = {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'target': action.target,
            'res_model': action.res_model,
            'context': {
                'default_partner_id': self.provider.id,
                'default_task_id': self.ids[0],
                'default_date_order': self.date_assign,
                'default_date_planned': self.date_assign
            }
        }
        result['domain'] = "[('id','in',[" + \
            ','.join(map(str, self.purchase_orders_ids.ids))+"])]"
        return result

    # Total de Compras
    @api.one
    @api.depends('purchase_orders_ids')
    def get_tot_purchases(self):
        self.total_compras = sum(order.amount_total for order in self.purchase_orders_ids.filtered(
            lambda s: s.state in ('purchase')))
