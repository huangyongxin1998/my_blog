from django.db import models
#谁登录谁就是作者
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=128,verbose_name='文章标题')
    #将登录作者作为作者也就是外键 级联删除
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='文章作者')
    #上传的路径为空 可以允许上传的图片为空 因为有照片所以下载pillow库
    img = models.ImageField(upload_to="",blank=True,null=True,verbose_name='文章配图')
    abstract = models.TextField(verbose_name='文章摘要')
    content = models.TextField(verbose_name='文章内容')
    #文章访问量默认为0
    visited = models.IntegerField(default=0,verbose_name='文章访问量')
    #自动添加当前的的时间 创建完之后直接添加现在的时间
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_at = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    #源编程起别名排序 按照自己喜欢的样式来设置
    class Meta:
        #将样式设置为中文
        verbose_name = '文章'
        #因为是中文所以没有复数直接赋值给verbose_name_plural
        verbose_name_plural = verbose_name
        #对文章进行排序以时间顺序为准
        ordering = ('-created_at',)

    #__str__将数据对象转化为具体的内容进行展示，方便查看
    def __str__(self):
        return self.title