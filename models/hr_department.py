from odoo import fields, models


class HrDepartment(models.Model):
    _inherit = "hr.department"

    equipment_lot_ids = fields.One2many(
        'stock.lot',
        'department_id',
        string="Medical Equipment & Assets"
    )