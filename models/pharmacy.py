from odoo import fields,models

class ClinincalPharmacy(models.Model):
    _name="clinical.pharmacy"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    drug_name=fields.Char(string="Drug Name",required=True)
    type=fields.Selection([
        ('capsules','Capsules'),
        ('syrup','Syrup'),
        ('injections','Injections')
    ],default='capsules',required=True)
    
    quantity=fields.Integer(string="Quantity",required=True)

    price=fields.Float(string="Price",required=True)

    barcode = fields.Char(string='Barcode')
    company_name = fields.Char(string='Company Name')
    is_imported = fields.Selection([
        ('imported', 'Imported'),
        ('local', 'Local')
    ], string='Type')
    size = fields.Char(string='Size')

    concentration = fields.Char(string='Concentration')
    active_ingredient = fields.Char(string='Active Ingredient')