from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'categories',views.CategoryView, base_name='category')
router.register(r'events\/(?P<from_time>.+)\/(?P<to_time>.+)',views.EventsViewTime, base_name='event-search')
router.register(r'events',views.EventsView, base_name='event')
router.register(r'registers', views.RegisterView, base_name='register')


urlpatterns = router.urls