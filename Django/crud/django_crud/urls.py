from django.urls import path
from . import views
urlpatterns=[
   path('hellow', views.hellow_world, name='hellow_world'),
      path('landing_page', views.render_page, name='hellow_world'),
   path('<str:name>',views.brian,name='brian')
]