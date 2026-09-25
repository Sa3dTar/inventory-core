from odoo import fields, models, api
from odoo.exceptions import ValidationError


class EquipmentMeterLog(models.Model):
    _name = "equipment.meter.log"
    _description = "Manage the equipment meter log"

    equipment_id = fields.Many2one("stock.lot", required=True, string="Equipment")
    reading_date = fields.Datetime(default=fields.Datetime.now, string="Reading Date")
    
    # تحويله لقراءة العداد الحالية لتتمكن من حساب الفرق، أو جعله حقلاً محسوباً بناءً على قراءة سابقة
    current_meter_reading = fields.Float(string="Current Meter Reading", required=True)
    running_hours_added = fields.Float(
        compute="_compute_running_hours_added", 
        store=True, 
        string="Running Hours Added"
    )
    recorded_by = fields.Many2one("res.users", default=lambda self: self.env.user, string="Recorded By")

    @api.depends('equipment_id', 'current_meter_reading')
    def _compute_running_hours_added(self):
        for log in self:
            if not log.equipment_id:
                log.running_hours_added = 0.0
                continue
            
            # البحث عن آخر قراءة سابقة لنفس الجهاز (باستثناء السجل الحالي)
            last_log = self.search([
                ('equipment_id', '=', log.equipment_id.id),
                ('id', '!=', log._origin.id if log._origin else False)
            ], order='reading_date desc, id desc', limit=1)

            if last_log:
                diff = log.current_meter_reading - last_log.current_meter_reading
                if diff < 0:
                    raise ValidationError("قراءة العداد الحالية لا يمكن أن تكون أقل من القراءة السابقة!")
                log.running_hours_added = diff
            else:
                # لو دي أول قراءة للجهاز خالص
                log.running_hours_added = log.current_meter_reading