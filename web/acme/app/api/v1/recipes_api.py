import json
from webob import Response, exc
from PyExpress.router import Router
from acme.recipes.controller import RecipesController
from acme.recipes.repository import RecipesMongoRepository
from acme.recipes.serializers import RecipeSchema


recipes_serializer = RecipeSchema()


@Router.app
def get_recipe_by_id(req, id):
    db = req.extras['db']
    repository = RecipesMongoRepository(db)
    controller = RecipesController(repository)

    recipe = controller.get_recipe(req.urlvars['id'])

    if recipe:
        res_body = json.dumps(recipes_serializer.dump(recipe).data)
        return Response(body=res_body, content_type=Router.CONTENT_TYPE_JSON,
                        charset='UTF-8')
    else:
        return exc.HTTPNotFound()


@Router.app
def find_recipes(req):
    db = req.extras['db']
    repository = RecipesMongoRepository(db)
    controller = RecipesController(repository)

    query = {}
    if 'search_name' in req.GET:
        query['name'] = req.GET['search_name']
    if 'search_prep_time' in req.GET:
        query['prep_time'] = req.Get['search_prep_time']
    if 'search_difficulty' in req.GET:
        query['difficulty'] = req.GET['search_difficulty']
    if 'search_vegetarian' in req.GET:
        query['vegetarian'] = req.GET['search_vegetarian']

    sort = {}
    if 'sort' in req.GET:
        direction = 'ascending'
        if 'sort_direction' in req.GET:
            direction = req.GET['sort_direction']
        sort[req.GET['sort']] = direction

    page = 0
    if 'page' in req.GET:
        page = req.GET['page']

    page_size = 10
    if 'page' in req.GET:
        page_size = req.GET['page_size']

    recipes = controller.find_recipes(query=query, sort=sort, page=page,
                                      page_size=page_size)
    res_body = json.dumps(recipes_serializer.dump(recipes, many=True).data)
    return Response(body=res_body, content_type=Router.CONTENT_TYPE_JSON,
                    charset='UTF-8')


@Router.app
def create_recipe(req):
    db = req.extras['db']
    repository = RecipesMongoRepository(db)
    controller = RecipesController(repository)

    try:
        body = json.loads(req.body)
        recipe = recipes_serializer.load(body).data
        controller.add_recipe(recipe)
    except (json.JSONDecodeError, ValueError) as e:
        return exc.HTTPBadRequest(e)
    except Exception as e:
        return exc.HTTPInternalServerError(e)

    res_body = json.dumps(recipes_serializer.dump(recipe).data)
    return Response(status=201, body=res_body,
                    content_type=Router.CONTENT_TYPE_JSON, charset='UTF-8')
