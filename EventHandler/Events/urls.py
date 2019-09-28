from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'category',views.CategoryView)
router.register(r'event',views.EventsView)
router.register(r'register',views.RegisterView)

urlpatterns = router.urls