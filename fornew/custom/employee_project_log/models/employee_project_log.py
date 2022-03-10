from odoo import api, fields, models

class EmployeeProjectLog(models.Model):
    _name = 'employee.project.log'

    @api.onchange('company_id')
    def onchange_company_id(self):
        if self.company_id:
            for rec in self:
                return {'domain': {'manager_id': [('company_id', '=', rec.company_id.id)]}}

    company_id = fields.Many2one('res.company', string='Company', required=True)
    project_name = fields.Many2one('project.project', string='Project Name')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    manager_id = fields.Many2one('hr.employee', string='Manager')
    employee_ids = fields.Many2many('hr.employee', string='Employees')
    employee_company_id = fields.Many2one('res.company', related='manager_id.company_id')