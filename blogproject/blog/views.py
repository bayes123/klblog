from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from .models import Post,Category
import markdown
# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("欢迎访问我的博客首页！")

# 我们前面说过，Web 服务器的作用就是接收来自用户的 HTTP 请求，根据请求内容作出相应的处理，并把处理结果包装成 HTTP 响应返回给用户。
#
# 这个两行的函数体现了这个过程。它首先接受了一个名为 request 的参数，这个 request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例。然后我们便直接返回了一个 HTTP 响应给用户，这个 HTTP 响应也是 Django 帮我们封装好的，它是类 HttpResponse 的一个实例，只是我们给它传了一个自定义的字符串参数。

# def index(request):
#     return render(request,'blog/index.html',context={
#         'title':'我的博客首页',
#         'welcome':'欢迎访问我的博客首页'
#     })

# 这里我们不再是直接把字符串传给 HttpResponse 了，而是调用 Django 提供的 render 函数。这个函数根据我们传入的参数来构造 HttpResponse。
#
# 我们首先把 HTTP 请求传了进去，然后 render 根据第二个参数的值 blog/index.html 找到这个模板文件并读取模板中的内容。之后 render 根据我们传入的 context 参数的值把模板中的变量替换为我们传递的变量的值，{{ title }} 被替换成了 context 字典中 title 对应的值，同理 {{ welcome }} 也被替换成相应的值。
#
# 最终，我们的 HTML 模板中的内容字符串被传递给 HttpResponse 对象并返回给浏览器（Django 在 render 函数里隐式地帮我们完成了这个过程），这样用户的浏览器上便显示出了我们写的 HTML 模板的内容。




def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(
        created_time__year = year,    #created_time 是 Python 的 date 对象，其有一个 year 和 month 属性.Python 中类实例调用属性的方法通常是 created_time.year，但是由于这里作为函数的参数列表，所以 Django 要求我们把点替换成了两个下划线，即 created_time__year
        created_time__month = month
    ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category = cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})