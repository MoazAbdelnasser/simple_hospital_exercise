# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HospitalAppointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    appointment_serial = fields.Char(string="Serial", readonly=True)
    patient_name = fields.Many2one('hospital.patient')
    age = fields.Integer(related='patient_name.age', readonly=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], readonly=True, related='patient_name.gender')
    booking_date = fields.Date(default=lambda self: fields.Datetime.now())
    appointment_time = fields.Datetime(default=lambda self: fields.Datetime.now())
    prescription = fields.Html()  # priority
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', required=True)
    doctor = fields.Many2one('res.users')

    # Define Functions for buttons to control states
    def draft_appointment(self):
        self.state = 'draft'

    def confirm_appointment(self):
        self.state = 'confirmed'

    def consult_appointment(self):
        self.state = 'in_consultation'

    def done_appointment(self):
        self.state = 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Hope you still safe',
                'type': 'rainbow_man'
            }
        }

    def cancel_appointment(self):
        self.state = 'cancel'

    # Handle Sequences for appointments serial
    @api.model
    def create(self, vals):
        print(vals)
        vals['appointment_serial'] = self.env['ir.sequence'].next_by_code('hospital.appointments')
        return super(HospitalAppointments, self).create(vals)
    #
    # def write(self, vals):
    #     if not self.appointment_serial:
    #         vals['appointment_serial'] = self.env['ir.sequence'].next_by_code('hospital.appointments')
    #     return super(HospitalAppointments, self).write(vals)
