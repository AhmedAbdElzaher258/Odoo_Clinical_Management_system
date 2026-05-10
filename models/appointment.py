from odoo import fields,models

class Appointment(models.Model):

    _name="clinical.appointment"
    _inherit=['mail.thread','mail.activity.mixin']

    patient_id=fields.Many2one('clinical.patient',string="Patient",required=True)
    doctor_id=fields.Many2one('doctor.clinical',string="Doctor",required=True)
    appointment_date=fields.Datetime(string="Appointment Date",required=True)

    state=fields.Selection([
        ('waiting','Waiting'),
        ('confirmed','Confirmed'),
        ('finished','finished'),
        ('cancelled','Cancelled')
    ],default='waiting',tracking=True)

    notes=fields.Text(string="Notes")