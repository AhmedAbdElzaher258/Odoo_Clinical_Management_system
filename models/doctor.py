from odoo import fields,models

class DoctorClinical(models.Model):

    _name="doctor.clinical"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(string="Doctor Name",required=True)

    specialty=fields.Selection([
        ('internal_medicine','Internal Medicine'),
        ('general_practice','General Practice'),
        ('cardiology','Cardiology'),
        ('dermatology','Dermatology')

    ],string="Specialty",required=True,default='internal_medicine')

    resource_calendar_id = fields.Many2one('resource.calendar', string='Working Schedule')
    phone=fields.Char(string="Phone Number")

    image = fields.Image(string="Profile Photo")
    bio = fields.Html(string="Biography")

