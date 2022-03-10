{
    'name': 'employee_details_log',
    'author': 'Digigate360',
    'version': '1.1',
    'summary': 'Management Software',
    'sequence': 20,
    'description': """Management Software""",
    'category': 'Productivity',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/employee_project_log.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
