# -*- coding: utf-8 -*-

from odoo import fields, models


class PatientPatient(models.Model):
    _name = "patient.patient"
    _description = "Patient"

    name = fields.Char(string="Patient Name", required=True, index=True)
    email = fields.Char(string="Email Address", required=True)
    doctor_id = fields.Many2one(comodel_name="doctor.doctor", string="Doctor Name")