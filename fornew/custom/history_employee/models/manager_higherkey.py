from datetime import datetime
from odoo import models, api, fields, _
from odoo.exceptions import UserError
class ManagerHigherkey(models.Model):
    _inherit = 'hr.employee'