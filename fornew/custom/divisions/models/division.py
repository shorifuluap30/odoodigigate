from odoo import api, fields, models


class CompanyDivision(models.Model):
    _name = "company.division"
    _description = "Company Division"

    description = fields.Text(string='Description')
    name = fields.Char(string='Title', required=True)
