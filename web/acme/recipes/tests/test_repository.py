from unittest import TestCase
from pymongo import MongoClient
from acme import settings
from acme.recipes.model import Recipe
from acme.recipes.repository import RecipesMongoRepository
from acme.recipes.tests.factories import RecipeFactory


class RecipesMongoRepositoryTest(TestCase):
    def setUp(self):
        """Setup connection with test db and initialize the repository"""
        self.client = MongoClient(settings.MONGO['HOST'],
                                  settings.MONGO['PORT'])
        self.client.drop_database(settings.MONGO['TEST_DB_NAME'])
        db = self.client.get_database(settings.MONGO['TEST_DB_NAME'])
        self.repository = RecipesMongoRepository(db)

    def test_can_insert_and_retrieve_recipe(self):
        """Test that the repository can create and retrieve Recipes"""
        recipe = RecipeFactory()
        id = self.repository.insert_recipe(recipe)
        self.assertEqual(id, str(recipe.id))

        retrieved = self.repository.find_recipe_by_id(str(recipe.id))
        self.assertIsInstance(retrieved, Recipe)
        self.assertEqual(retrieved.id, recipe.id)
        self.assertEqual(retrieved.name, recipe.name)
        self.assertEqual(retrieved.prep_time, recipe.prep_time)
        self.assertEqual(retrieved.difficulty, recipe.difficulty)
        self.assertEqual(retrieved.vegetarian, recipe.vegetarian)

    def tearDown(self):
        """Close connection to the test db"""
        self.client.close()
