from odoo import api, fields, models


class HrRank(models.Model):
    _inherit = "hr.employee"

    rank_id = fields.Many2one('hr.rank', string="Rank", required=True)

    # min_salary = fields.Integer(string='Min', related='name_id.min_salary', tracking=True)
    # max_salary = fields.Integer(string='Max', related='name_id.max_salary', tracking=True)
    min_salary = fields.Integer(string='Min', tracking=True)
    max_salary = fields.Integer(string='Max', tracking=True)

    # How to set onchange function
    @api.onchange('rank_id')
    def onchange_rank_id(self):
        if self.rank_id:
            if self.rank_id.min_salary:
                self.min_salary = self.rank_id.min_salary
                if self.rank_id.max_salary:
                    self.max_salary = self.rank_id.max_salary
        else:
            self.min_salary = ''
            self.max_salary = ''
