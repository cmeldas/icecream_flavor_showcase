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
    featured_log_ids = fields.One2many(
        'icecream.flavor.log',
        'flavor_id',
        string='Featured History',
    )
    total_featured_days = fields.Integer(
        string='Total Days Featured (This Year)',
        compute='_compute_total_featured_days',
    )

    @api.depends('featured_log_ids', 'featured_log_ids.date_from')
    def _compute_total_featured_days(self):
        today = fields.Date.context_today(self)
        year_start = today.replace(month=1, day=1)
        for flavor in self:
            flavor.total_featured_days = self.env['icecream.flavor.log'].search_count([
                ('flavor_id', '=', flavor.id),
                ('date_from', '>=', year_start),
                ('date_from', '<=', today),
            ])

    @api.model
    def _cron_snapshot_featured(self):
        """Daily cron (runs at 15:00): record one log entry per featured flavor."""
        today = fields.Date.context_today(self)
        featured = self.search([('is_featured', '=', True)])
        LogModel = self.env['icecream.flavor.log']
        for flavor in featured:
            existing = LogModel.search_count([
                ('flavor_id', '=', flavor.id),
                ('date_from', '=', today),
            ])
            if not existing:
                LogModel.create({
                    'flavor_id': flavor.id,
                    'date_from': today,
                    'date_to': today,
                })
