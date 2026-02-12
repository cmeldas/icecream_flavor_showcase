import json

from odoo import http
from odoo.http import request, Response


class IcecreamController(http.Controller):

    @http.route('/icecream/featured', type='http', auth='public', website=True, sitemap=False)
    def get_featured_flavors(self):
        """Return the list of featured ice cream flavors as JSON."""
        flavors = request.env['icecream.flavor'].sudo().search([
            ('is_featured', '=', True),
            ('active', '=', True),
        ], order='sequence, name')
        result = []
        for flavor in flavors:
            result.append({
                'id': flavor.id,
                'name': flavor.name,
                'description': flavor.description or '',
                'ingredients': flavor.ingredients or '',
                'image_url': '/icecream/image/%d' % flavor.id if flavor.image else '',
            })
        return Response(
            json.dumps(result),
            content_type='application/json',
            status=200,
        )

    @http.route('/icecream/image/<int:flavor_id>', type='http', auth='public', website=True)
    def get_flavor_image(self, flavor_id, **kw):
        """Serve the image of a featured ice cream flavor publicly."""
        flavor = request.env['icecream.flavor'].sudo().browse(flavor_id)
        if not flavor.exists() or not flavor.image:
            return request.not_found()
        return request.env['ir.binary'].sudo()._get_image_stream_from(
            flavor, 'image',
        ).get_response()
