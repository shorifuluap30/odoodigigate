from odoo import api, fields, models


class EmployeeDetails(models.Model):
    _inherit = "hr.employee"

    division_id = fields.Many2one('company.division', string="Division", required=True)
    division_name = fields.Char(string='Division Name')
