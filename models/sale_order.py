# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class saleInherit(models.Model):
    _inherit = 'sale.order'

    task_id = fields.Many2one('project.task', string="Task", states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
