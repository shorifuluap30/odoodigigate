from odoo import api, fields, models


class EmployeeDetails(models.Model):
    _inherit = "hr.employee"

    division_id = fields.Many2one('company.division', string="Division", required=True)
    section_id = fields.Many2one('company.sections', string="Section")

    nick_name = fields.Char(string="Nick Name")
    father_name = fields.Char(string="Father Name")
    mother_name = fields.Char(string="Mother Name")
    mother_name = fields.Char(string="Mother Name")
    tax_code = fields.Char(string="TIN/Tax Code")
    permanent_address = fields.Char(string="Permanent Address")
    religion = fields.Char(string="Religion")
    blood_group = fields.Char(string="Blood Group")
    education_lines = fields.One2many('education.level', 'employee_id', string="Education Line")
    training_lines = fields.One2many('employee.training', 'employee_training_id', string="Training Line")
    job_lines = fields.One2many('job.history', 'employee_id_for_jod', string="Training Line")
    children_lines = fields.One2many('employee.children', 'employee_id_for_children', string="Training Line")

    emr_cont_relation = fields.Char(string="Relationship")
    emr_cont_address = fields.Char(string="Address")

    emr_cont_relation_2nd = fields.Char(string="Relationship")
    emr_cont_address_2nd = fields.Char(string="Address")
    emr_cont_contact_2nd = fields.Char(string="Emergency Contact")
    emr_cont_phone_2nd = fields.Char(string="Emergency Phone")

    wife_name = fields.Char(string="Name")
    wife_contact = fields.Char(string="Contact No (Mobile)")
    wife_profession = fields.Char(string="Profession")

    ref_name = fields.Char(string="Name")
    ref_position = fields.Char(string="Position")
    ref_organization = fields.Char(string="Organization")
    ref_address = fields.Char(string="Address")
    ref_contact = fields.Char(string="Contact No")
    ref_relationship = fields.Char(string="Relationship")

    ref_name2 = fields.Char(string="Name")
    ref_position2 = fields.Char(string="Position")
    ref_organization2 = fields.Char(string="Organization")
    ref_address2 = fields.Char(string="Address")
    ref_contact2 = fields.Char(string="Contact No")
    ref_relationship2 = fields.Char(string="Relationship")
    signature_image = fields.Binary(string="Signature of the employee")
    signature_date = fields.Date(string="Date")

class EducationLevel(models.Model):
    _name = 'education.level'
    exam_title = fields.Selection([
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('graduate', 'Graduate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctor'),
        ('other', 'Other'),
    ], 'Exam Title', default='other')
    subject = fields.Char(string="Subject/Group")
    board = fields.Char(string="Institute/Board")
    result = fields.Char(string="Result")
    year = fields.Integer(string="Year")
    employee_id = fields.Many2one('hr.employee', string="Employee Name")

class Training(models.Model):
    _name = 'employee.training'

    title = fields.Char(string="Title")
    institute = fields.Char(string="Institute")
    duration = fields.Char(string="Duration")
    year = fields.Char(string="Year")
    employee_training_id = fields.Many2one('hr.employee', string="Employee Name")

class EmploymentHistory(models.Model):
    _name = 'job.history'

    organization = fields.Char(string="Name of Organization")
    position = fields.Char(string="Position Held (Department)")
    service_period = fields.Char(string="Service Period")
    employee_id_for_jod = fields.Many2one('hr.employee', string="Employee Name")

class ChildrenInformation(models.Model):
    _name = 'employee.children'

    children_name = fields.Char(string="Name of Children")
    children_sex = fields.Char(string="Sex (Male/Femail)")
    children_date_of_birth = fields.Date(string="Date of Birth")
    employee_id_for_children = fields.Many2one('hr.employee', string="Employee Name")


class EmployeeReferences(models.Model):
    _name = 'employee.reference'

