from odoo import api, fields, models


class EmployeeProjectLog(models.Model):
    _name = "employee.project.log"
    _description = "Employee Project Log"

    company_id = fields.Many2one('res.company', string='Company', required=True)
    project_name = fields.Many2one('project.project', string='Project Name')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    manager_id = fields.Many2one('hr.employee', string='Manager')
    employee_ids = fields.Many2many('hr.employee', string='Employees')