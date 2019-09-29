from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'categories',views.CategoryView, base_name='category')
router.register(r'events',views.EventsView, base_name='event')
#router.register(r'events/filter',views.EventsViewSearch, base_name='event-search')
router.register(r'registers',views.RegisterView, base_name='register')

urlpatterns = router.urls