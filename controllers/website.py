# -*- coding: utf-8 -*-

from odoo import http
# import this Controller '' to inherit it and make some changes
from odoo.addons.website.controllers.main import Website


class WebsiteInherit(Website):
    """
    It is a just test. Inheriting a controller and make changes
    to see if those changes are made or not.
    """

    @http.route(['/website/pages', '/website/pages/page/<int:page>'], type='http', auth="user", website=True)
    def pages_management(self, page=1, sortby='url', search='', **kw):
        """
        Those changes are here. you can add your changes as much as you want.
        I only add a 'print()' statement to test the inherited controller.
        """
        res = super(WebsiteInherit, self).pages_management(page=page, sortby=sortby, search=search, **kw)
        print("Test Inherit controller: Website......")
        return res