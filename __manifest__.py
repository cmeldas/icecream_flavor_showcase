{
    'name': 'Ice Cream Flavor Showcase',
    'version': '18.0.1.0.0',
    'category': 'Website',
    'summary': 'Showcase available ice cream flavors on your website',
    'description': """
Ice Cream Flavor Showcase
=========================

Manage your ice cream flavors in the backend and display the featured ones
on your website using custom building blocks.

Features
--------
* Backend model with kanban (default), list and form views
* Chatter support for each flavor (track changes, log notes)
* Fields: name, description, ingredients, picture
* Mark up to 2 flavors as **Featured** to show them on the website
* Two website snippet types:
    - **Compact** — picture, name and description
    - **Detailed** — picture, name, description *and* ingredients
* Czech language on all public-facing text
    """,
    'author': 'My Company',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/icecream_flavor_views.xml',
        'views/icecream_flavor_log_views.xml',
        'views/icecream_menus.xml',
        'views/icecream_kiosk.xml',
        'views/snippets/s_icecream_small.xml',
        'views/snippets/s_icecream_big.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'icecream_flavor_showcase/static/src/snippets/**/*.js',
            'icecream_flavor_showcase/static/src/scss/**/*.scss',
        ],
    },
    'installable': True,
    'application': True,
}
