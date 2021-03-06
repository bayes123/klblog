from django.conf.urls import url
from .import views

app_name='blog'
urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]

# 比如说我们本地开发服务器的域名是 http://127.0.0.1:8000，那么当用户输入网址 http://127.0.0.1:8000 后，Django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，此时只剩下一个空字符串，而 r'^$' 的模式正是匹配一个空字符串（这个正则表达式的意思是以空字符串开头且以空字符串结尾），于是二者匹配，Django 便会调用其对应的 views.index 函数。


# 我们首先从 django.conf.urls 导入了 url 函数，又从当前目录下导入了 views 模块。然后我们把网址和处理函数的关系写在了 urlpatterns 列表里。
#
# 绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址，第二个参数是处理函数），另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到。