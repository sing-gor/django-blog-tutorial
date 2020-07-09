# Create your models here.
from django.db import models

class Articles(models.Model):
    DATASTATUS = (
        (0,'发布'),
        (1,'草稿'),
    )
    data_status = models.IntegerField(choices=DATASTATUS,verbose_name='是否显示',default=1)
    title = models.CharField(verbose_name='文章标题',
                             max_length=100)
    slug = models.SlugField(max_length=30, verbose_name='索引', unique=True)
    body = models.TextField(verbose_name='文章内容')
    author = models.CharField(verbose_name='作者',default='Sing',max_length=100)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    '''
    CREATE TABLE "articles"
        (
            "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            "data_status" integer NOT NULL,
            "title" varchar(100) NOT NULL,
            "slug" varchar(30) NOT NULL UNIQUE,
            "body" text NOT NULL,
            "author" varchar(100) NOT NULL,
            "created_time" datetime NOT NULL,
            "update_time" datetime NOT NULL
        );
    '''
    class Meta:
        db_table = 'articles'
        verbose_name = '文章'
        verbose_name_plural = '文章列表'

    def __str__(self):
        return self.title
