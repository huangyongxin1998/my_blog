from django.urls import path
from articles import views

urlpatterns=[
    path('list/',views.index,name='list'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('concate/',views.concate,name='concate'),
    path('about/',views.about,name='about'),
]