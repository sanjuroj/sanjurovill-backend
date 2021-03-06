from django.conf.urls import url, include
from rest_framework import routers
from .views import APIAll


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'^$', APIAll, 'api_all')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'api', APIAll.as_view(), name='api_all')
]
