# -*- coding: utf-8 -*-

{
    'name': 'OM Hospital',
    'summary': """ Render a WebPage Using Controllers in Odoo. """,
    'description': """
How To Write Controllers And Render WebPage Using Controllers in Odoo.
From a tutorial of Odoo Mates youtube channel.
csrf_token
In Odoo, ‘Controllers’ are used to configure the frontend modules.
These frontend modules come integrated with the backend modules.
For example, if one needs to bring the sales order details to the website,
he can’t use the functionality of ‘Models’ in Odoo. However, via using the controllers,
he can get the sales order details from the backend.
Modules like ‘Website sale’, ‘Website blog’, ‘Website forum’, etc are using the controllers
to extend their functionality. By using controllers, one can easily define the link between any URL and the webpages.

from: https://www.cybrosys.com/blog/web-controllers-in-odoo
""",
    'author': 'Ahlem Mehri',
    'website': "http://www.mehriahlem-dz.com",
    'category': 'Developpement - Version Odoo 14',
    'version': '0.1',
    'sequence': '1',
    'depends': ['website',],
    'data': [
        # demo : data for demontration
        'demo/doctor_demo.xml',
        # data : files to load at module install
        'data/patient_form.xml',
        'data/om_hospital_data.xml',
        # Security : always load groups first
        #          : load access rights after groups
        'security/ir.model.access.csv',
        # templates
        'views/om_hospital.xml',
        'views/patient_template.xml',
        # views
        'views/patient_patient_views.xml',
        'views/doctor_doctor_views.xml',
        # menus
        'views/om_hospital_menuitem.xml',
        # reports
        # wizard
    ],
    # 'qweb': [
    # ],
    # 'images': [
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
