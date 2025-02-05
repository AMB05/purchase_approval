from odoo import http
from odoo.http import request
import json

class ProductAPIController(http.Controller):

    @http.route('/api/products', type='http', auth='public', methods=['GET'], csrf=False)
    def get_products(self, category_id=None, category_name=None, **kwargs):
        #GET API Product Filter Category_ID & Category_Name
        query = """
            SELECT p.id, pt.name, pt.list_price, c.name as category
            FROM product_product p
            JOIN product_template pt ON p.product_tmpl_id = pt.id
            LEFT JOIN product_category c ON pt.categ_id = c.id
        """
        params = []
        conditions = []
        # Category_ID
        if category_id:
            conditions.append("pt.categ_id = %s")
            params.append(int(category_id))
        # Category_Name
        if category_name:
            conditions.append("c.name ILIKE %s")  # Gunakan ILIKE agar case-insensitive
            params.append(f"%{category_name}%")  # Mendukung pencarian sebagian nama
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        request.env.cr.execute(query, tuple(params))
        products = request.env.cr.dictfetchall()
        # return json data
        return request.make_response(
            json.dumps({"status": "success", "products": products}, indent=4),
            headers=[('Content-Type', 'application/json')]
        )
