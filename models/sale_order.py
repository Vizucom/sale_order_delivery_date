# -*- coding: utf-8 -*-
from openerp import models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    date_delivery = fields.Date('Delivery Date', help='''Delivery date promised to the customer''')
