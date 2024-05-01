from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewset, ProductViewset

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewset)
router.register(r'products', ProductViewset)

urlpatterns = [
    path('', include(router.urls))
]
