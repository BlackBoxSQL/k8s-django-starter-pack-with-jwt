from rest_framework.response import Response
from rest_framework import status


class CoreResponse(object):
    @classmethod
    def send_200(cls, data):
        return Response(data, status=status.HTTP_200_OK)

    @classmethod
    def send_403(cls, data):
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    @classmethod
    def send_400(cls, data):
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def send_500(cls, data):
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def send_404(cls, data):
        return Response(data, status=status.HTTP_404_NOT_FOUND)
