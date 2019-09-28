from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'category',views.CategoryView)
router.register(r'event',views.EventsView)
router.register(r'register',views.RegisterView)

<<<<<<< Updated upstream
urlpatterns = router.urls
=======
urlpatterns = router.urls
'''
from rest_framework import routers

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register(r'categories',views.CategoryView)
router.register(r'events',views.EventView)
router.register(r'register',views.RegisterView)

urlpatterns = router.urls

""" urlpatterns += [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()), """
    #path(r'registers/', views.RegisterList.as_view()),

#urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> Stashed changes
