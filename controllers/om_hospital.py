# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Hospital(http.Controller):

    # Sample controller created
    @http.route(['/om_hospital/patients'], website=True, type='http', auth='public')
    def hospital_patient(self, **kwargs):
        """
        This Controller is only to render a list of Patients.
        To see the result, you just hit the URL: http://127.0.0.1:8069/om_hospital/patients
        """
        patients = request.env['patient.patient'].sudo().search([])
        res = request.render("om_hospital.patient_page", {'patients': patients})
        ### uncomment these two lines to see the result
        # res.qcontext.update({'patients': request.env['patient.patient'].sudo().browse(3)})
        # res.template = "om_hospital.patient_page_2"
        return res
        # return "Hello there.<br/><br/>Here we don't render anything, we just return this simple message."

    @http.route(['/patient_webform'], type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        """
        This controller is to render the list of doctors stored in database.
        To make the list available when the public user creates a patient.
        """
        doctors = request.env['doctor.doctor'].sudo().search([])
        return request.render('om_hospital.create_patient', {'doctors': doctors})

    @http.route(['/create/webpatient'], type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        """
        This controller stores patient info in database.
        Info: patient name, email and doctor.
        """
        request.env['patient.patient'].sudo().create(kw)
        return request.render('om_hospital.patient_thanks', {})
