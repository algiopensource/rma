# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2015 Vauxoo
#    Author: Yanina Aular
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models


class ClaimLine(models.Model):

    _inherit = 'claim.line'

    supplier_id = fields.Many2one(comodel_name='res.partner',
                                  related='prodlot_id.supplier_id',
                                  help="Supplier of good in claim")
    supplier_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        related="prodlot_id.supplier_invoice_line_id.invoice_id",
        help="Supplier invoice with the purchase of goods sold to customer")
