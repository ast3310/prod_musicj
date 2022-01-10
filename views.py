from app import app
import flask
from config import VkConfig, BaseConfig
import vk_api
import json
import requests
from vkmuz import VkAndroidApi

vk = vk_api.VkApi(token=VkConfig.TOKEN)

vk_x = VkAndroidApi(login=VkConfig.USERNAME,password=VkConfig.PASSWORD)

@app.route('/getList', methods=['GET', 'POST'])
def index():
    id = flask.request.args.get('id')
    offset = flask.request.args.get('offset')

    result = vk.method('audio.get', {'user_id': id, 'count': 40, 'offset': offset})

    for i in range(0, len(result['items'])):
        if 'album' not in result['items'][i]:
            result['items'][i].update({'album': {'thumb': {'photo_68': False}}})


    response = flask.Response(json.dumps(result['items']))

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
    return response


@app.route('/getById', methods=['GET', 'POST'])
def dialog():
    id = flask.request.args.get('id')
    owner_id = flask.request.args.get('owner_id')
    
    result = vk.method('audio.getById', {'audios': f"{str(owner_id)}_{str(id)}"})

    url_hls = vk_x.method("audio.getById",audios=f"{str(owner_id)}_{str(id)}")

    if 'album' not in result[0]:
            result[0].update({'album': {'thumb': {'photo_68': False}}})
    
    result[0].update({'url_hls':url_hls['response'][0]['url']})

    response = flask.Response(json.dumps(result[0]))

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')

    return response


@app.route('/getSearch', methods=['GET', 'POST'])
def search():
    q = flask.request.args.get('q')
    offset = flask.request.args.get('offset')

    result = vk.method('audio.search', {'q': q, 'offset': offset, 'count': 40})

    for i in range(0, len(result['items'])):
        if 'album' not in result['items'][i]:
            result['items'][i].update({'album': {'thumb': {'photo_68': False}}})

    response = flask.Response(json.dumps(result['items']))

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')

    return response


@app.route('/getUser', methods=['GET', 'POST'])
def getUser():
    code = flask.request.args.get('code')

    params = {'client_id': VkConfig.CLIENT_ID, 'client_secret': VkConfig.CLIENT_SECRET, 'redirect_uri': BaseConfig.BASE_URL + 'auth', 'code': code}

    r = requests.get('https://oauth.vk.com/access_token', params=params)

    data = json.loads(r.text)
    
    print(data)

    result = {}
    if 'access_token' in data:
        token = data['access_token']
        id = data['user_id']

        vk_u = vk_api.VkApi(token=token)

        result = vk_u.method('users.get', {'user_ids': id, 'fields': 'photo_50'})[0]
        
        result['access_token'] = token
        print(result)
    else:
        result = {'error': 'Token invalid', 'access_token': False}
    print(result)
    response = flask.Response(json.dumps(result))

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')

    return response

@app.route('/checkAccess', methods=['GET', 'POST'])
def checkAccess():
    id = flask.request.args.get('id')

    try:
        result = vk.method('audio.get', {'user_id': id, 'count': 1, 'offset': 0})
        result = {'error': False}
    except vk_api.exceptions.ApiError:
        result = {'error': True}
    
    response = flask.Response(json.dumps(result))

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')

    return response