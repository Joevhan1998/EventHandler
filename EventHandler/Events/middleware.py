from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponse

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

        #def process_request(self, request):
        """ p = request.META
        print(p['HTTP_AUTHORIZATION'])
        print(p['REQUEST_METHOD']) """

        url = request.META.get('PATH_INFO')
        request_method = request.META.get('REQUEST_METHOD')
        if (url == '/events/' or url == '/categories/' and request_method == 'POST'):
            token = request.META.get('HTTP_AUTHORIZATION', None)
            print(token)
            if token is not None:
                print()
                #return None
            #response_data = {}
            #return JsonResponse(response_data, status=204)
            #return HttpResponseForbidden()
        #return HttpResponse('401 Unauthorized', status=401)
        return None