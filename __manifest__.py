{
    'name':"Clinical Management",
    'author': "Ahmed Abd Elzaher",
    'category': 'Custom',
    'version': '17.0.0.1.0',
    'depends': ['base','mail'
                
                ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence_view.xml',
        'views/base_menu.xml',
        'views/patient_views.xml'
        

    ],
    'installable': True,
    'application': True

}