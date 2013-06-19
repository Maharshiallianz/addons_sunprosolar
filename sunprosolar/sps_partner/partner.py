# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import fields
from openerp.osv import osv
from openerp import tools
from openerp.tools.translate import _

class res_partner(osv.osv):
    """ Model for Partner. """
    _inherit = "res.partner"
    
    _columns = {
        'ahj': fields.selection([ ('structure','Structural'),
                                    ('electric', 'Electrical')],
                                    string='AHJ', required=True, help="Authority Having Jurisdiction"),
        }
    
    _defaults = {
            'ahj': 'structure',
    }
    
res_partner()