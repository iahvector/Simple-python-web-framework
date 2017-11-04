class FakeRecipesRepository(object):
    """
        A Fake Recipes repository implementing the basic required functionality
        for writing unit tests for logic that requires a Recipes repository
    """
    recipes = {}

    def find_recipe_by_id(self, recipe_id):
        return self.recipes[recipe_id]

    def find_recipes(self, query, sort, page, page_size):
        return [r for r in self.recipes.values() if r.name == query.name]

    def insert_recipe(self, recipe):
        self.recipes[str(recipe.id)] = recipe
        return recipe

    def update_recipe(self, recipe_id, recipe):
        self.recipes[recipe_id] = recipe
        return recipe

    def delete_recipe(self, recipe_id):
        recipe = self.recipes[recipe_id]
        del self.recipes[recipe_id]
        return recipe
