{
    'name': 'Medical Equipment Inventory & Meter Management',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Extends Odoo 18 Inventory for medical serial tracking, running hours meters, and emergency spare part reservations',
    'description': """
        This custom module extends Odoo 18 Inventory management to support:
        - Advanced serial number lifecycle tracking (operational status, running hours, and department location).
        - Dedicated part reservation logic linking incoming purchase orders directly to specific emergency work orders.
        - Equipment meter logging to track running hours and feed preventive maintenance triggers.
        - Department integration with medical equipment and assets.
    """,
    'author': 'Saad Tarek',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'stock',
        'purchase',
        'my_purchase',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_meter_log.xml',
        'views/stock_lot.xml',
        'views/hr_department.xml',
        'views/menuitem.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}