import logging

class ActivityLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            logging.info(f'User {request.user.username} accessed {request.path}')
        return response
