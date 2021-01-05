from django.contrib import admin
#从模板中导入文章类
from .models import Articles,Category,Tag
# Register your models here.
#创建好的模板类字段没在admin后台管理系统中进行展示是因为没有在admin进行注册
#定义一个文章admin类继承admin的ModelAdmin
class ArticlesAdmin(admin.ModelAdmin):
    #以什么字段为表头
    list_display=('title','author','img','abstract','visited','created_at')
    #根据什么字段进行搜索
    search_fields=('title','author','abstract','content') 
    #根据什么信息进行筛选
    list_filter=list_display
     
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)