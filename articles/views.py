from django.shortcuts import render

#Templates views视图
# Create your views here.
#FBV的形式 function based view 基于函数/类/django的视图 
def index(request):
    return render(request,'index.html')


#详情页面加id参数
def detail(request,pk):
    return render(request,'single_article.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
