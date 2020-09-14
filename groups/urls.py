from django.urls import path

from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateView, name='create'),
    path('posts/in/<slug:slug>/', views.SingleGroup.as_view(), name='single'),
]
