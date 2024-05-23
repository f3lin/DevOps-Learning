from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def get_index():
    return {
        'method': 'get',
        'endpoint': '/'
    }

@api.get('/other')
def get_other():
    return {
        'method': 'get',
        'endpoint': '/other'
    }

##### Ici get_item_default sera toujours executé que la requete soit:
# curl -X GET -i http://127.0.0.1:8000/item/1234
# curl -X GET -i http://127.0.0.1:8000/item/my_item
# curl -X GET -i http://127.0.0.1:8000/item/1.2345
# en effet lorsque le type n'est pas specifier celui-ci est automatiquement un str 
# et l'ordre de définition est importante ici

# @api.get('/item/{itemid}')
# def get_item_default(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid,
#         'source': 'string'
#     }

# @api.get('/item/{itemid:int}')
# def get_item(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid
#     }

# @api.get('/item/{itemid:float}')
# def get_item_float(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid,
#         'source': 'float'
#     }

##### Ici get_item_default sera toujours executé que la requete soit:
#curl -X GET -i http://127.0.0.1:8000/item/1234
#curl -X GET -i http://127.0.0.1:8000/item/my_item
#curl -X GET -i http://127.0.0.1:8000/item/1.2345

@api.get('/item/{itemid:int}')
def get_item(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid
    }

@api.get('/item/{itemid:float}')
def get_item_float(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'float'
    }

@api.get('/item/{itemid}')
def get_item_default(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'string'
    }

@api.get('/item/{itemid}/description/{language}')
def get_item_language(itemid, language):
    if language == 'fr':
        return {
            'itemid': itemid,
            'description': 'un objet',
            'language': 'fr'
        }
    else:
        return {
            'itemid': itemid,
            'description': 'an object',
            'language': 'en'
        }
    
@api.post('/')
def post_index():
    return {
        'method': 'post',
        'endpoint': '/'
    }

@api.delete('/')
def delete_index():
    return {
        'method': 'delete',
        'endpoint': '/'
    }

@api.put('/')
def put_index():
    return {
        'method': 'put',
        'endpoint': '/'
    }

@api.patch('/')
def patch_index():
    return {
        'method': 'patch',
        'endpoint': '/'
    }