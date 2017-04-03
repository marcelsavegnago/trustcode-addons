# -*- coding: utf-8 -*-
# © 2017 Fillipe Ramos, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Pagamento de Royalties',
    'description': "Pagamento de Royalties",
    'summary': "Pagamento de Royalties",
    'version': '10.0.1.0.0',
    'category': "Taks",
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
        'Mackilem Van der Laan Soares <mack.vdl@gmail.com>'
    ],
    'depends': [
        'base',
        'product',
        'account'
    ],
    'data': [
        'views/product.xml',
        'views/res_partner_view.xml',
        'wizard/royalties_view.xml',
    ],
    'installable': True,
    'application': True,
}
