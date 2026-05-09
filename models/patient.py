from odoo import fields,models,api

class ClinicalPatient(models.Model):
    _name="clinical.patient"
    _description = 'Clinical Patient'
    _inherit=['mail.thread','mail.activity.mixin']

    name=fields.Char(string="Patient name",required=True,tracking=True)
    patient_code=fields.Char(string="patient code",readonly=True,default="New")
    date_of_birth=fields.Date(string="Date Of Birth",required=True)
    age=fields.Integer(string="Age",compute="_compute_age",store=True)
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ],required=True)
    
   # appointment_ids = fields.One2many('clinical.appointment', 'patient_id', string='Appointments')

    phone=fields.Char(string="Phone",required=True)

    email=fields.Char(string="Email")
    address=fields.Text(string="Address")
    blood_type = fields.Selection([
        ('a+', 'A+'), ('a-', 'A-'),
        ('b+', 'B+'), ('b-', 'B-'),
        ('o+', 'O+'), ('o-', 'O-'),
        ('ab+', 'AB+'), ('ab-', 'AB-'),
    ], string='Blood Type')

    notes=fields.Text(string='medical notes')

    @api.depends('date_of_birth')

    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                from datetime import date
                today=date.today()
                rec.age=today.year - rec.date_of_birth.year
            else:
                rec.age = 0
    

    @api.model
    def create(self, vals):
        if vals.get('patient_code', 'New') == 'New':
            vals['patient_code'] = self.env['ir.sequence'].next_by_code('clinical.patient') or 'New'
        return super().create(vals)
