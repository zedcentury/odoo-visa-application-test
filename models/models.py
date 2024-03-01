from odoo import models, fields


class VisaApplication(models.Model):
    _name = "visa_application"

    name = fields.Char("Name")
