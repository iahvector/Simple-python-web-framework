import random
import uuid
from factory import Factory, Faker
from acme.recipes.model import Recipe


class RecipeFactory(Factory):
    class Meta:
        model = Recipe

    id = uuid.uuid4()
    name = Faker('sentence', nb_words=5, variable_nb_words=True)
    prep_time = random.randrange(5, 600, 5)
    difficulty = random.choice([1, 2, 3])
    vegetarian = Faker('pybool')
