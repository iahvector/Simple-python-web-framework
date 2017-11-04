from unittest import TestCase
from uuid import UUID
from ..model import Recipe


class RecipesModelTest(TestCase):
    def test_create_recipe(self):
        name = "Omeltte"
        prep_time = 10
        difficulty = 1
        vegetarian = True
        recipe = Recipe(name=name, prep_time=prep_time, difficulty=difficulty,
                        vegetarian=vegetarian)
        self.assertIsInstance(recipe, Recipe)
        self.assertIsInstance(recipe.id, UUID)
        self.assertEqual(recipe.id.version, 4)
        self.assertEqual(recipe.name, name)
        self.assertEqual(recipe.prep_time, prep_time)
        self.assertEqual(recipe.difficulty, difficulty)
        self.assertEqual(recipe.vegetarian, vegetarian)
