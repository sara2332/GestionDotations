{
    'name': 'Gestion des dotations',
    'summary': """gestion des dotations des employés""",
    'version': '1.0',
    'description': """Ce module est destiné pour gérer les dotations des employés.""",
    'author': 'Moussaoui Sara',
    'company': 'Moussaoui Sara',
    'website': 'http://www.moussaoui.com',
    'category': 'sale_management',
    'depends': [
	       'base', 
	       'sale_management',
		   'hr',
	],
    'license': 'AGPL-3',
    'data': [
        'views/dotation.xml',
		'views/employe.xml',
		'views/decharge.xml',
		'report/report.xml',
		'security/ir.model.access.csv',
		
    ],
    
    'installable': True,
    'auto_install': False,

}