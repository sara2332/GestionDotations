from odoo import models, fields, api


class Decharge(models.Model):
    _name = "decharge.decharge" # Table in DB => car_request
    _description = "Décharge"

    name = fields.Char(string="Request", required=True, )
    date_from = fields.Datetime(string="Date de début", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="Date de fin", required=False, )
    employe_id = fields.Many2one(comodel_name="hr.employee", string="Employé", required=True, )
    dotation_id = fields.Many2one(comodel_name="product.template", string="Dotation", required=True, )
    state = fields.Selection(string="Statut", selection=[('brouillon', 'Brouillon'),('validé', 'Validé'),  ], default="brouillon", track_visibility='onchange', )
                                               

    @api.multi
    def validate_request(self):
        self.state = 'validé'
