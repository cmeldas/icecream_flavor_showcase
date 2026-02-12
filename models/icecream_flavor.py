from odoo import models, fields, api, _


class IcecreamFlavor(models.Model):
    _name = 'icecream.flavor'
    _description = 'Ice Cream Flavor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, name'

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True,
    )
    description = fields.Html(
        string='Description',
        sanitize_style=True,
    )
    ingredients = fields.Html(
        string='Ingredients',
        sanitize_style=True,
    )
    image = fields.Binary(
        string='Image',
        attachment=True,
    )
    is_featured = fields.Boolean(
        string='Featured on Website',
        default=False,
        tracking=True,
        help='If checked, this flavor will be displayed on the website.',
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )
    color = fields.Integer(
        string='Color Index',
    )
