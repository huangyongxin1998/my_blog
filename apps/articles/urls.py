from django.urls import path
from articles import views

urlpatterns=[
    #调用views.py中的index函数 返回页面和
    path('index/',views.index,name='index'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
]