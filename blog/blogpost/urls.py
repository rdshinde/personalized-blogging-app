from django.urls import path

from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts/<str:pk>',views.post, name='post')
    
]

#added manually
#urlpatterns += staticfiles_urlpatterns()