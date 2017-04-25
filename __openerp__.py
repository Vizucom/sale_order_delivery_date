# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Delivery Date field for Sale Orders',
    'category': 'Sales',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale'],
    'description': """
Delivery Date field for Sale Orders
===================================
* Adds a new date field for SOs, indicating the promised delivery date
""",
    'data': [
        'views/sale_order.xml',
    ],
}
