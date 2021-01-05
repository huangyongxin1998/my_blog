from django.shortcuts import render
#从models数据库中进行调用类 文章类 分类类 标签类
from .models import Articles,Category,Tag
from django.db.models import Q
from django.core.paginator import Paginator

#Templates views视图
# Create your views here.
#FBV的形式 function based view 基于函数/类/django的视图 
def index(request):
    #查找文章中的所有内容
    articles=Articles.objects.all()
    #每页上的条数限制为两条进行分页
    limited=2
    p=Paginator(articles,limited)
    #得到前端传过来的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1
    articles=p.get_page(page)


    #在首页展示最新更新的五篇文章
    lasted_articles=Articles.objects.all()[:5]
    #实例化Category并且获取所有数据和内容
    category=Category.objects.all()
    #实例化Tag并且获取所有数据和内容
    tags=Tag.objects.all()
    context = {
        'articles':articles,
        'lasted_articles':lasted_articles,
        'category':category,
        'tags':tags,
    }
    return render(request,'index.html',context)



#详情页面加id参数
def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    #调用访问量 打开页面一次访问量加一 函数直接进行调用
    article.increace_visited()
    print(article.get_absolute_url())
    lasted_articles=Articles.objects.all()[:5]
    category=Category.objects.all()
    tags=Tag.objects.all()

    context={
        'article':article,
        'lasted_articles':lasted_articles,
        'category':category,
        'tags':tags,
    }
    return render(request,'single_article.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    print('keyword=',keyword)
    if not keyword:
        error_msg= '请输入关键字'
        return render(request,'index.html',locals())
    articles=Articles.objects.filter(Q(title__icontains=keyword)|Q(abstract__icontains=keyword)|Q(content__icontains=keyword))
    limited=2
    p=Paginator(articles,limited)
    #得到前端传过来的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1
    
    articles=p.get_page(page)

    lasted_articles=articles[:5]
    #实例化Category并且获取所有数据和内容
    category=Category.objects.all()
    #实例化Tag并且获取所有数据和内容
    tags=Tag.objects.all()
    return render(request,'index.html',locals())

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
