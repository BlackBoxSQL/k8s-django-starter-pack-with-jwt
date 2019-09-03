from django.urls import path

from .views import *

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += [
        path('protected-route', SomeProtectedRoutes.as_view(), name='some_protected_route'),
    ]
