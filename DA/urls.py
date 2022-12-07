from django.urls import path,include
from .views import phone,ChargerModelViewSet
from rest_framework.routers import DefaultRouter
from DA import views
router = DefaultRouter()
router.register('chargerapi',views.ChargerModelViewSet,basename='charger')
urlpatterns = [
    path("ab/",include(router.urls))


]