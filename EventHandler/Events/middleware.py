from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponse

import requests

def check_token(request): #True if admin, False if volunteer
    if request == None:
        return False
    #TODO: pull jwt token
    """ jwt ='kbkcmbkcmbkcbc9ic9vixc9vixc9v'
    hed = {'Authorization': 'Bearer ' + jwt}
    data = {}

    url = 'http://authenticator-team1.xmpknwihw4.ap-southeast-1.elasticbeanstalk.com/accounts/me'
    response = requests.post(url, json=data, headers=hed)
    json_response = response.json() """

    json_response = {
        "authorities": [
            {
                "authority": "admin"
            }
        ],
        "details": {
            "remoteAddress": "0:0:0:0:0:0:0:1",
            "sessionId": "8B60A1E434983E649BBB02DFA2B20814",
            "tokenValue": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1Njk3MTI4NDQsInVzZXJfbmFtZSI6IjUiLCJhdXRob3JpdGllcyI6WyJhZG1pbiJdLCJqdGkiOiJmY2M3ODJhNC0xYjQ1LTQ1ZDUtYjk3NS0xMDcwMmIyNWI2MTMiLCJjbGllbnRfaWQiOiJ0ZXN0X2NsaWVudF8xMjMiLCJzY29wZSI6WyJ1c2VyX2luZm8iXX0.TLWXaq79QnTjeArwcusdNi2-zx_WKJHls-rHaDXGGxk",
            "tokenType": "Bearer",
            "decodedDetails": 'null'
        },
        "authenticated": True,
        "userAuthentication": {
            "authorities": [
                {
                    "authority": "admin"
                }
            ],
            "details": 'null',
            "authenticated": True,
            "principal": "5",
            "credentials": "N/A",
            "name": "5"
        },
        "principal": "5",
        "oauth2Request": {
            "clientId": "test_client_123",
            "scope": [
                "user_info"
            ],
            "requestParameters": {
                "client_id": "test_client_123"
            },
            "resourceIds": [],
            "authorities": [],
            "approved": True,
            "refresh": False,
            "redirectUri": 'null',
            "responseTypes": [],
            "extensions": {},
            "grantType": 'null',
            "refreshTokenRequest": 'null'
        },
        "credentials": "",
        "clientOnly": False,
        "name": "5"
    }

    result = json_response['authorities'][0]['authority']
    
    return result

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        '''
        POST /events
        DELETE /events/id/
        PUT /events/id/
        POST /categories
        PUT /categories/id/
        DELETE /categories/id/
        GET /events/id/feedback
        '''

        url = request.META.get('PATH_INFO')
        request_method = request.META.get('REQUEST_METHOD')

        if ((url == '/events/' or url == '/categories/') and request_method == 'GET'):
            
            
            token = request.META.get('HTTP_AUTHORIZATION', None)
            #token = 'asdasdas'
            is_admin = check_token(token)
            if is_admin:
                return None
            return HttpResponse('401 Unauthorized', status=401)
