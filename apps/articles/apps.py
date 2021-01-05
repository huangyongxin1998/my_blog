from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'articles'
    #将网页的题目改为中文
    verbose_name='文章'
