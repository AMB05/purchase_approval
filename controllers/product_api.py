import json
from odoo import http
from odoo.http import request

class ProductAPI(http.Controller):

    @http.route('/api/products', type='http', auth='public', methods=['GET'], csrf=False)
    def get_products(self, category=None, **kwargs):
        query = "SELECT id, name, list_price FROM product_product WHERE active=True"
        if category:
            query += " AND categ_id = %s" % category

        request.env.cr.execute(query)
        products = request.env.cr.dictfetchall()
        return request.make_response(json.dumps(products), headers=[('Content-Type', 'application/json')])
