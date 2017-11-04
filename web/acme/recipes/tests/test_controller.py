from unittest import TestCase
from acme.recipes.model import Recipe
from acme.recipes.controller import RecipesController
from acme.recipes.tests.mock import FakeRecipesRepository


class RecipesControllerTest(TestCase):
    def test_create_and_get_recipe(self):
        """ Test application logic for creating and retrieving a recipe"""

        name = 'Omlette'
        prep_time = 10
        difficulty = 1
        vegetarian = False
        recipe = Recipe(name=name, prep_time=prep_time, difficulty=difficulty,
                        vegetarian=vegetarian)
        repo = FakeRecipesRepository()
        controller = RecipesController(repo)
        controller.add_recipe(recipe)
        result = controller.get_recipe(str(recipe.id))
        self.assertIsInstance(result, Recipe)
        self.assertEqual(result.id, recipe.id)
        self.assertEqual(result.name, recipe.name)
