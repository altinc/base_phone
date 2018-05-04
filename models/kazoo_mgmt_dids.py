# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models, api
from .. import fields


class kazoo_dids(models.Model):
    _inherit = 'kazoo_mgmt.dids'
    _phone_name_sequence = 10

    x_tn = fields.Phone(string="Telephone Number", country_field='x_country_id', partner_field='x_owner',required=True)

    @api.multi
    def name_get(self):
        if self._context.get('callerid'):
            res = []
            for partner in self:
                if partner.parent_id and partner.parent_id.is_company:
                    name = u'%s (%s)' % (partner.name, partner.parent_id.name)
                else:
                    name = partner.name
                res.append((partner.id, name))
            return res
        else:
            return super(kazoo_dids, self).name_get()
