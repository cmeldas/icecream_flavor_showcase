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

    @api.depends('featured_log_ids', 'featured_log_ids.date_from', 'featured_log_ids.date_to')
    def _compute_total_featured_days(self):
        today = fields.Date.context_today(self)
        year_start = today.replace(month=1, day=1)
        for flavor in self:
            total = 0
            for log in flavor.featured_log_ids:
                start = log.date_from or year_start
                end = log.date_to or today
                # Clip to current year
                start = max(start, year_start)
                end = max(end, year_start)
                if start <= end:
                    total += (end - start).days + 1
            flavor.total_featured_days = total

    def write(self, vals):
        """Track featured changes: open/close log entries."""
        if 'is_featured' in vals:
            today = fields.Date.context_today(self)
            for flavor in self:
                old_val = flavor.is_featured
                new_val = vals['is_featured']
                if not old_val and new_val:
                    # Becoming featured → open a new log entry
                    self.env['icecream.flavor.log'].create({
                        'flavor_id': flavor.id,
                        'date_from': today,
                    })
                elif old_val and not new_val:
                    # No longer featured → close the open log entry
                    open_log = self.env['icecream.flavor.log'].search([
                        ('flavor_id', '=', flavor.id),
                        ('date_to', '=', False),
                    ], limit=1)
                    if open_log:
                        open_log.date_to = today
        return super().write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        """If created as featured, open a log entry."""
        records = super().create(vals_list)
        today = fields.Date.context_today(self)
        for rec in records:
            if rec.is_featured:
                self.env['icecream.flavor.log'].create({
                    'flavor_id': rec.id,
                    'date_from': today,
                })
        return records
