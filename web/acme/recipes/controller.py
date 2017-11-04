class RecipesController(object):
    """A controller implementing application logic for recipes"""

    def __init__(self, recipes_repo):
        """
        Args:
            recipes_repo (obj): A repository object
        """
        self.recipes_repo = recipes_repo

    def get_recipe(self, recipe_id):
        """
            Retrieve a recipe by id

            Args:
                recipe_id: (str): A recipe id
        """
        return self.recipes_repo.find_recipe_by_id(recipe_id)

    def find_recipes(self, query=None, sort={'name': 'ascending'}, page=0,
                     page_size=10):
        """
            List recipes, can search for recipes matching a search query if
            provided. The result can be sorted and paginated.

            Args:
                query: (dict of str:str): A dictionary containing zero or more
                    parameters to match, default None
                sort: (dict of str:str): A dictionary containing zero or more
                    keys to sort by and sort directions,
                    default {'name': 'ascending'}
                page: (int): Page number, default 0
                page_size (int): Page size, default 10

            Example:
                >>> controller = RecipesController(repository)
                >>> query = {
                        name: 'recipe name',
                        prep_time: 15,
                        difficulty: 2,
                        vegetarian: False
                    }
                >>> sort = {
                        'name': 'ascending'
                        'prep_time': 'ascending',
                        'difficulty': 'descending'
                    }
                >>> controller.find_recipes(query, sort)
                [
                    <acme.recipes.model.Recipe at 0x7f391ccabdd0>,
                    <acme.recipes.model.Recipe at 0x7f391cf6b850>,
                    <acme.recipes.model.Recipe at 0x7f391cf6bad0>
                ]
        """
        return self.recipes_repo.find_recipes(query, sort, page, page_size)

    def add_recipe(self, recipe):
        """
            Add a recipe

            Args:
                recipe (obj:Recipe): A recipe object
        """
        return self.recipes_repo.insert_recipe(recipe)

    def update_recipe(self, recipe_id, recipe):
        """
            Update a recipe by id

            Args:
                recipe_id: (str): A recipe id
                recipe (obj:Recipe): A recipe object
        """
        return self.recipes_repo.update_recipe(recipe_id, recipe)

    def delete_recipe(self, recipe_id):
        """
            Delete a recipe by id

            Args:
                recipe_id: (str): A recipe id
        """
        return self.recipes_repo.delete_recipe(recipe_id)
