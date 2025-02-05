from odoo import http
from odoo.http import request
import json

class ProductAPIController(http.Controller):

    @http.route('/api/products', type='http', auth='public', methods=['GET'], csrf=False)
    def get_products(self, category_id=None, **kwargs):
        """API untuk mengambil produk dengan filter kategori."""
        query = """
            SELECT p.id, pt.name, pt.list_price, c.name as category
            FROM product_product p
            JOIN product_template pt ON p.product_tmpl_id = pt.id
            LEFT JOIN product_category c ON pt.categ_id = c.id
        """
        params = []

        if category_id:
            query += " WHERE pt.categ_id = %s"
            params.append(int(category_id))

        request.env.cr.execute(query, tuple(params))
        products = request.env.cr.dictfetchall()

        return request.make_response(
            json.dumps({"status": "success", "products": products}, indent=4),
            headers=[('Content-Type', 'application/json')]
        )
