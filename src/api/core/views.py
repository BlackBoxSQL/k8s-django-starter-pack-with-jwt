from rest_framework.views import APIView


class CustomApiView(APIView):
    def get_serializer_class(self):
        pass
