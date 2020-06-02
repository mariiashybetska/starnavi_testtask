from social_network.models import Logger


class LoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.id:
            Logger.objects.create(
                user=request.user
            )

        return response
