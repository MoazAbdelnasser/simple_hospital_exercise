# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """ Hospital Management software """,
    'sequence': 0,
    'description': """ Hospital Based Management Software   """,
    'author': "Moaz Abdelnasser",
    'website': "http://www.Simple_Tech.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_sequence.xml',
        'data/appointment_sequence.xml',
        'views/patient.xml',
        'views/appointments.xml',
        'views/hospital_Menu.xml',
        'views/res_partner.xml',
        'reports/patient_card.xml',
        'reports/report.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
