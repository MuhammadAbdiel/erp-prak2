{
    "name": "Training Odoo",
    "summary": """ Modul untuk latihan technical Odoo """,
    "description": """
      Modul ini berfungsi untuk menjalankan technical documentation pada website resmi odoo.com. Bahan yang dipelajari:
      - ORM
      - Berbagai View
      - Report
      - Wizard
      - dll
    """,
    "author": "Muhammad Abdiel Firjatullah",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
}
