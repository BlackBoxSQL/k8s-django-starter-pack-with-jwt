from core.views import CustomApiView
from core.response import CoreResponse
from django.conf import settings


class SomeProtectedRoutes(CustomApiView):
    def get(self, request):
        try:
            print(getattr(settings, 'SIMPLE_JWT'))
            return CoreResponse.send_200(
                dict(message='This is a protected route')
            )
        except Exception as exc:
            return CoreResponse.send_500(dict(
                status=500, message=str(exc)
            ))
