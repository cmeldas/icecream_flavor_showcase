# Ice Cream Flavor Showcase

Odoo 18 Community addon for managing and displaying ice cream flavors on your website.

## Features

### Backend
- **Ice Cream Flavor model** with fields: name, description, ingredients, picture
- **Kanban view** as default (with image preview and "Featured" badge)
- **Form view** with chatter (mail.thread + mail.activity.mixin)
- **List view** with drag-and-drop reordering
- Mark up to **2 flavors as Featured** to display them on the website

### Frontend (Website)
Two website building blocks (snippets), all text in **Czech**:

1. **Zmrzlina - kompaktní** (Ice Cream Compact)
   - Shows picture, name and description of featured flavors
   - Card-based layout

2. **Zmrzlina - detailní** (Ice Cream Detailed)
   - Shows picture, name, description **and ingredients**
   - Side-by-side layout with larger images

## Installation

1. Copy the `icecream_flavor_showcase` folder into your Odoo addons path
2. Update the module list: *Settings → Technical → Update Apps List*
3. Search for "Ice Cream Flavor Showcase" and install

## Usage

1. Go to **Ice Cream → Flavors** to create flavors
2. Toggle the **Featured on Website** checkbox on 1-2 flavors
3. Open the Website editor, drag the "Ice Cream Compact" or "Ice Cream Detailed" snippet onto any page
4. Save and publish — visitors will see the featured flavors

## Dependencies

- `website`
- `mail`
