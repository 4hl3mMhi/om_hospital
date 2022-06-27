# -*- coding: utf-8 -*-

from odoo import fields, models


class DoctorDoctor(models.Model):
    _name = "doctor.doctor"
    _inherit = ['image.mixin']
    _description = "Doctors"

    name = fields.Char(string="Doctor Name", required=True, index=True)
    code = fields.Char(string="Doctor Code", required=True)
