from pymongo import MongoClient
from acme import settings
from acme.app.router import Router
from acme.app.api.v1 import recipes_api

# Open Database connection
client = MongoClient(settings.MONGO['HOST'],
                     settings.MONGO['PORT'])
db = client.get_database(settings.MONGO['DB_NAME'])

# Initialize the router
app = Router()

# Add routes to the router
# Get a recipe by id
app.use('/api/v1/recipes/{id}',
        Router.METHOD_GET,
        recipes_api.get_recipe_by_id,
        db=db)

# Get recipes list and search recipes
app.use('/api/v1/recipes/',
        Router.METHOD_GET,
        recipes_api.find_recipes,
        db=db)

# Create a new recipe
app.use('/api/v1/recipes/',
        Router.METHOD_POST,
        recipes_api.create_recipe,
        db=db)
