'''
from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'category',views.CategoryView)
router.register(r'event',views.EventsView)
router.register(r'register',views.RegisterView)

urlpatterns = router.urls
'''


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(r'category', views.CategoryList.as_view()),
    path(r'event', views.EventsList.as_view()),
    path(r'register', views.RegisterList.as_view()),
]




