from odoo import fields, models, api


class StockLot(models.Model):
    _inherit = "stock.lot"

    equipment_status = fields.Selection([
        ("operational", "Operational"),
        ("maintance", "Maintance"),
        ("downtime", "Downtime")
    ])
    total_runing_hours = fields.Float(
        compute="_compute_total_running_hours", 
        store=True, 
        string="Total Running Hours"
    )

    is_locked_for_so = fields.Boolean(default=False)

    # reserved_work_order_id = fields.Many2one("equipment.work.order")

    department_id = fields.Many2one("hr.department")
    
    # حقل علاقي عكسي للربط مع سجلات العدادات
    meter_log_ids = fields.One2many(
        'equipment.meter.log', 
        'equipment_id', 
        string="Meter Logs"
    )

    @api.depends('meter_log_ids.running_hours_added')
    def _compute_total_running_hours(self):
        for lot in self:
            lot.total_runing_hours = sum(lot.meter_log_ids.mapped('running_hours_added'))