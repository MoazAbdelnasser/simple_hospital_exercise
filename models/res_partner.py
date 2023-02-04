# -*- coding: utf-8 -*-
from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    ss = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('owner', 'Owner')
    ], default='customer', string="Type")
