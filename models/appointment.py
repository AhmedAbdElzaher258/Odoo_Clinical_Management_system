from odoo import fields,models,api, exceptions

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

@api.constrains('appointment_date', 'doctor_id')
def _check_doctor_availability(self):
    for rec in self:
        if rec.doctor_id and rec.appointment_date:
            calendar = rec.doctor_id.resource_calendar_id
            if calendar:
                day_of_week = str(rec.appointment_date.weekday())
                working_days = calendar.attendance_ids.mapped('dayofweek')
                import logging
                _logger = logging.getLogger(__name__)
                _logger.info(f'Day: {day_of_week}, Working Days: {working_days}')
                if day_of_week not in working_days:
                    raise exceptions.ValidationError(
                        f'الدكتور {rec.doctor_id.name} مش بيشتغل في اليوم ده!'
                    )
                    