from odoo import api, fields, models


class DivisionDepartment(models.Model):
    _inherit = "hr.department"

    # for add division id inside department

    division_id = fields.Many2one('company.division', string="Division", required=True)
