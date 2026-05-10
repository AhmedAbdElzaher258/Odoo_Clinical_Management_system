from odoo import fields,models

class DoctorClinical(models.Model):

    _name="doctor.clinical"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(string="Doctor Name",required=True)

    specialty=fields.Char(string="Specialty",required=True)

    resource_calendar_id = fields.Many2one('resource.calendar', string='Working Schedule')
    phone=fields.Char(string="Phone Number")

    image = fields.Image(string="Profile Photo")
    bio = fields.Html(string="Biography")

