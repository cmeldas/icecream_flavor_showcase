from odoo import models, fields, api


class IcecreamFlavorLog(models.Model):
    _name = 'icecream.flavor.log'
    _description = 'Ice Cream Featured Log'
    _order = 'date_from desc'
    _rec_name = 'flavor_id'

    flavor_id = fields.Many2one(
        'icecream.flavor',
        string='Flavor',
        required=True,
        ondelete='cascade',
        index=True,
    )
    date_from = fields.Date(
        string='Featured From',
        required=True,
        default=fields.Date.context_today,
    )
    date_to = fields.Date(
        string='Featured Until',
    )
    days = fields.Integer(
        string='Days Featured',
        compute='_compute_days',
        store=True,
    )

    @api.depends('date_from', 'date_to')
    def _compute_days(self):
        today = fields.Date.context_today(self)
        for log in self:
            end = log.date_to or today
            if log.date_from:
                delta = (end - log.date_from).days + 1
                log.days = max(delta, 0)
            else:
                log.days = 0
