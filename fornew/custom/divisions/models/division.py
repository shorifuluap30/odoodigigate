from odoo import api, fields, models

class CompanyDivision(models.Model):
    _name = "company.division"
    _description = "Company Division"

    description = fields.Text(string='Description')
    title = fields.Char(string='Title', required=True)