import pymongo
from acme.recipes.serializers import RecipeSchema


class RecipesMongoRepository(object):
    SORT_DIRECTIONS = {'ascending': pymongo.ASCENDING,
                       'descending': pymongo.DESCENDING}

    def __init__(self, db):
        """
        Initialize the repository with a pymongo db instance and initialize the
        serializer

        Args:
            db: (obj): A PyMongo database instance
        """
        self.db = db
        self.serializer = RecipeSchema(strict=True)

    def find_recipe_by_id(self, recipe_id):
        """
        Find a recipe by id from the mongo db

        Args:
            recipe_id: (str): ID of the recipe to find
        """
        doc = self.db.recipes.find_one({'_id': recipe_id})
        return self.serializer.load(doc).data if doc else None

    def find_recipes(self, query, sort, page, page_size):
        """
        Find a list of recipes matching `query` and sorted by `sort`

        Args::
                query: (dict of str:str): A dictionary containing zero or more
                    parameters to match
                sort: (dict of str:str): A dictionary containing zero or more
                    keys to sort by and sort directions
                page: (int): Page number
                page_size (int): Page size
        """
        q = {}
        if 'name' in query:
            q['$regex'] = '/{}/i'.format(query['name'])
        if 'prep_time' in query:
            q['prep_time'] = {'$lte': query['prep_time']}
        if 'difficulty' in query:
            q['difficulty'] = {'$lte': query['difficulty']}
        if 'vegetarian' in query:
            q['vegetarian'] = query['vegetarian']

        s = [(k, self.SORT_DIRECTIONS[v]) for k, v in sort] if sort else None

        skip = (page or 0) * page_size

        docs = self.db.recipes.find(q).skip(skip).limit(page_size)
        if s:
            docs.sort(s)

        return self.serializer.load(docs, many=True).data

    def insert_recipe(self, recipe):
        """
        Insert a recipe into the mongo db

        Args:
            recipe: (obj): A Recipe object
        """
        doc = self.serializer.dump(recipe).data
        return self.db.recipes.insert_one(doc).inserted_id

    def update_recipe(self, recipe_id, recipe):
        """
        Update a recipe by id

        Args:
            recipe_id: (str): The ID of the recipe to update
            recipe: (obj): A Recipe object
        """
        doc = self.serializer.dump(recipe).data
        return self.db.recipes.update_one({'_id': recipe_id}, {'$set': doc})

    def delete_recipe(self, recipe_id):
        """
        Delete a recipe by id

        Args:
            recipe_id: (str): The ID of the recipe to delete

        """
        return self.db.recipes.delete_one({'_id': recipe_id})
