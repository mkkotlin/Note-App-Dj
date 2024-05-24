from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('save',views.save),
    path('view_saved',views.view_saved),
    path('get_by_title/<slug:slug>/',views.get_by_title,name='get_by_title'),
]