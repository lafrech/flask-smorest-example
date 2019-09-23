"""Api extension initialization

Override base classes here to allow painless customization in the future.
"""
import marshmallow as ma
from marshmallow_sqlalchemy import ModelSchema as OrigModelSchema

from flask_smorest import Api as ApiOrig, Blueprint as BlueprintOrig, Page


class Blueprint(BlueprintOrig):
    """Blueprint override"""


class Api(ApiOrig):
    """Api override"""

    def __init__(self, app=None, *, spec_kwargs=None):
        super().__init__(app, spec_kwargs=spec_kwargs)

        # Register custom Marshmallow fields in doc
        # self.register_field(CustomField, 'type', 'format')

        # Register custom Flask url parameter converters in doc
        # self.register_converter(CustomConverter, 'type', 'format')


class Schema(ma.Schema):
    """Schema override"""


class ModelSchema(OrigModelSchema):
    """ModelSchema override"""

    # No-op make_instance
    def make_instance(self, data, **kwargs):
        return data

    class Meta:
        transient = True

class SQLCursorPage(Page):
    """SQL cursor pager"""

    @property
    def item_count(self):
        return self.collection.count()
