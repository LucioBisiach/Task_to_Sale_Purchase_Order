# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    task_id = fields.Many2one('project.task', string="Task", readonly=True, states={
                                  'draft': [('readonly', False)]})
