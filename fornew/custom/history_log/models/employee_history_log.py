from datetime import datetime
from odoo import models, api, fields, _
from odoo.exceptions import UserError

class DepartmentDetails(models.Model):
    _inherit = 'hr.employee'
    @api.onchange('mobile_phone')
    def _onchange_mobile_phone(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self._origin.id)])
        vals = {
            'employee_id': self._origin.id,
            'employee_name': employee_id.name,
            'updated_date': datetime.now(),
            'changed_field': 'Mobile',
            'current_value': self.mobile_phone
        }
        self.env['employee.history.log'].sudo().create(vals)

    @api.onchange('work_email')
    def _onchange_work_email(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self._origin.id)])
        vals = {
            'employee_id': self._origin.id,
            'employee_name': employee_id.name,
            'updated_date': datetime.now(),
            'changed_field': 'Email Address',
            'current_value': self.work_email
        }
        self.env['employee.history.log'].sudo().create(vals)

    @api.onchange('job_title')
    def _onchange_job_title(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self._origin.id)])
        vals = {
            'employee_id': self._origin.id,
            'employee_name': employee_id.name,
            'updated_date': datetime.now(),
            'changed_field': 'Designation',
            'current_value': self.job_title
        }
        self.env['employee.history.log'].sudo().create(vals)

    @api.onchange('address_home_id')
    def _onchange_address_home_id(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self._origin.id)])
        vals = {
            'employee_id': self._origin.id,
            'employee_name': employee_id.name,
            'updated_date': datetime.now(),
            'changed_field': 'Address',
            'current_value': self.address_home_id.name
        }
        self.env['employee.history.log'].sudo().create(vals)

    @api.onchange('rank_id')
    def _onchange_rank_id(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self._origin.id)])
        vals = {
            'employee_id': self._origin.id,
            'employee_name': employee_id.name,
            'updated_date': datetime.now(),
            'changed_field': 'Rank',
            'current_value': self.rank_id.name
        }
        self.env['employee.history.log'].sudo().create(vals)

class EmployeeHistoryLog(models.Model):
    _name = 'employee.history.log'

    employee_id = fields.Char(string='Employee Id', help="Employee")
    employee_name = fields.Char(string='Employee Name', help="Name")
    changed_field = fields.Char(string='Field Name')
    current_value = fields.Char(string='Value', help="Display the value")
    updated_date = fields.Date(string='Date', help="Display the date")

