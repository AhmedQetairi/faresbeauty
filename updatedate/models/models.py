-*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    isbirthday = fields.Boolean("IS THIS MONTH YOUR BIRTHDAY")
    
    
    @api.model
    def updatefield(self, vals):
        for rec in self:
            rec.isbirthday = True