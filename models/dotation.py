from odoo import api,models,fields

class Dotation(models.Model):

    
	_inherit="product.template"

	dote=fields.Boolean(string="Doté")
	employe_id = fields.Many2one(comodel_name="hr.employee", string="Employé", required=True, )
	
	