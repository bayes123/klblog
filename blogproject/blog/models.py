from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# Django 把那一套数据库的语法转换成了 Python 的语法形式，我们只要写 Python 代码就可以了，Django 会把 Python 代码翻译成对应的数据库操作语言。用更加专业一点的说法，就是 Django 为我们提供了一套 ORM（Object Relational Mapping）系统。#对象关系映射
class Category(models.Model):
    """
    django 要求模型必须继承models.Model类
    CharField 指定了分类名name的数据类型，CharField是字符型
    CharField 的max_length指定其最大长度，超过这个长度的分类名就不能被存放数据库
    其他数据类型：
    日期时间类型 DateTimeField  整数类型 IntegerField  CharField是字符型（存储较短文本） TextField存储较长文本
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    要继承models.Model
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# 文章 id	标题	正文	发表时间	分类	标签
# 1	title 1	text 1	2016-12-23	Django	Django 学习
# 2	title 2	text 2	2016-12-24	Django	Django 学习
# 3	title 3	text 3	2016-12-26	Python	Python 学习
# 分类 id	分类名
# 1	Django
# 2	Python
# 标签 id	标签名
# 1	Django 学习
# 2	Python 学习
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要,可为空
    excerpt = models.CharField(max_length=200,blank =True)
    #ForeignKey 一对多
    category = models.ForeignKey(Category)
    #ManyToManyField 多对多
    tags = models.ManyToManyField(Tag,blank = True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering = ['-created_time']




