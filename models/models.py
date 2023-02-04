# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = ' Hospital Patient'
    ref = fields.Char()
    name = fields.Char(required=True, tracking=True)
    date_of_birth = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], default='male', required=True)
    notes = fields.Text(String="Description", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default='draft', tracking=True)
    active = fields.Boolean(default=True)
    patient_photo = fields.Image()

    def draft_action(self):
        self.state = 'draft'

    def confirm_action(self):
        # if self.state == 'draft':
        self.state = 'confirm'

    def done_action(self):
        # if self.state != 'done':
        self.state = 'done'

    def cancel_action(self):
        self.state = 'cancel'

    # Override Create function
    # @api.model
    # def create(self, formData):
    #   print(formData)
    #  return super(HospitalPatient, self).create(formData)
    # Override create function
    @api.model
    def create(self, vals):
        print(vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    def default_get(self, vals):
        result = super(HospitalPatient, self).default_get(vals)
        result['age'] = 20
        print("Default Get executed")
        return result

    # Computed field
    @api.depends('date_of_birth')
    def _compute_age(self):
        d = date.today()
        self.age = d.year - self.date_of_birth.year
