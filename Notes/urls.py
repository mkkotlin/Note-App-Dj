from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('save',views.save),
    path('view_saved',views.view_saved,name='saved'),
    path('get_by_title/<slug:slug>/',views.get_by_title,name='get_by_title'),
    path('get_by_title/<slug:slug>/delete',views.delete,name='filter_view'),
    path('get_by_title/<slug:slug>/update',views.update),
]