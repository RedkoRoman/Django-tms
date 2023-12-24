class BeforeRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'Request method: {request.method} \n Path: {request.path}')

        response = self.get_response(request)

        return response


class AfterRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        print(f'Response status code: {response.status_code}')

        return response