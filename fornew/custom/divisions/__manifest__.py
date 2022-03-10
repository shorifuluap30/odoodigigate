{
    'name': 'company_divisions',
    'author': 'Digigate360',
    'version': '1.1',
    'summary': 'Management Software',
    'sequence': 20,
    'description': """Management Software""",
    'category': 'Productivity',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['mail', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/divisions.xml',
        'views/divisions_department.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
