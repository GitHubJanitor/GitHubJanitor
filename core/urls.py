from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'status/', views.status, name='status'),
    url(r'github_test/', views.github_test, name='github_test'),
]