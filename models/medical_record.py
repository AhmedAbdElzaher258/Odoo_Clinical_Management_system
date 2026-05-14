from odoo import fields,models

class MedicalRecord(models.Model):
    _name="medical.record"
    _inherit=['mail.thread','mail.activity.mixin']

    patient_id=fields.Many2one('clinical.patient',string="Patient",required=True)
    doctor_id=fields.Many2one('doctor.clinical',string="Doctor",required=True)
    appointment_id=fields.Many2one('clinical.appointment',string="Appointment",required=True)
    diagnosis=fields.Text(string='Diagnosis',required=True)
    prescription=fields.Html(string='Prescription',required=True)
    date=fields.Date(string='Date',required=True)
