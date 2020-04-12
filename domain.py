DOMAIN_SETTINGS = {
    "boxes": {
        "public_methods": ['GET', 'PATCH', 'PUT', 'DELETE'],
        "schema": {
            "name": {
                "type": "string",
                "required": True,
            },
            "picture": {
                "type": "media",
                "required": True,
            },
            "holder_box": {
                "type": "objectid",
                'data_relation': {
                    'resource': 'boxes',
                    'field': '_id',
                    'embeddable': True
                }
            }

        }
    },
    "items": {
        "url": "boxes/<regex('[a-f0-9]{24}'):box>/items",
        "schema": {
            "name": {
                "type": "string",
                "required": True,
            },
            "description": {
                "type": "string",
            },
            "image": {
                "type": "media",
            },
            "box": {
                "type": "objectid",
                "required": True,
                'data_relation': {
                    'resource': 'boxes',
                    'field': '_id',
                    'embeddable': False
                }
            }
        }
    },
    "user": {
        "allowed_write_roles": ["admin"],
        "allowed_item_write_roles": ['admin'],
        'schema': {
            'name': {
                'type': 'string',
                'unique': False,
            },
            'login': {
                "type": 'string',
                'unique': True,
            },
            "roles": {
                "type": "list",
                "default": ["user"],
                "allowed": ["user", "admin"]
            },
        },
    }
}
