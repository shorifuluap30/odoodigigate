from odoo import api, fields, models


class CompanySections(models.Model):
    _name = "company.sections"
    _description = "Company Sections"

    name_id = fields.Many2one('company.division', string="Division Id", required=True)
    name_id2 = fields.Many2one('hr.department', string="Department Id", required=True)
    company_id = fields.Many2one('res.company', string='Company Id', required=True)
    # division_id = fields.Char(string='Division Id', required=True)
    # department_id = fields.Char(string='Department Id', required=True)
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
