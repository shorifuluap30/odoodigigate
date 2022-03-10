from odoo import api, fields, models

class CompanySections(models.Model):
    _name = "company.sections"
    _description = "Company Sections"

    division_id = fields.Many2one('company.division', string="Division", required=True)
    department_id = fields.Many2one('hr.department', string="Department", required=True, domain="['&', ('division_id', '=', division_id), ('company_id', '=', company_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=True)
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
