from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'categories',views.CategoryView)
router.register(r'events',views.EventView)
router.register(r'register',views.RegisterView)

urlpatterns = router.urls
