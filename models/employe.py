from odoo import api,models,fields

class Employe(models.Model):

    
	_inherit="hr.employee"

	nbDecharge=fields.Integer(string="Nombre Décharges")
	