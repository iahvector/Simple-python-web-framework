from marshmallow import Schema, fields, post_load
from acme.recipes.model import Recipe


class RecipeSchema(Schema):
    """
        A serializer/deserialaizer to convert Recipe objects to dicts and back
    """

    id = fields.UUID(load_from='_id', dump_to='_id')
    name = fields.String()
    prep_time = fields.Integer()
    difficulty = fields.Integer()
    vegetarian = fields.Boolean()

    @post_load
    def create_object(self, data):
        """
            Create a Recipe object from deserialaized recipe data
        """
        return Recipe(**data)
