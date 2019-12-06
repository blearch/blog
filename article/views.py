from article.models import ArticlePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# 视图函数
from django.shortcuts import render, redirect
import markdown
from .forms import ArticlePostForm
def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)
def article_detail(request,id):
#     根据id 查询出相关的文章
    article=ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context={'article':article}
    return render(request,'article/detail.html',context)

# 写文章的视图
@login_required(login_url='/userprofile/login')
def article_create(request):
    # 判断用户是否提交数据
    if request.method=="POST":
        # 把用户提交的数据填入表格中
        article_post_form=ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但不提交到数据库中
            new_article=article_post_form.save(commit=False)
            new_article.author=User.objects.get(id=request.user.id)
            new_article.save()
            # 返回到文章列表
            return redirect("article:article-list")
        else:
            return HttpResponse("内容表单有误，请重新填写")
    else:
        # 创建表单类
        article_post_form=ArticlePostForm()
        # 赋值上下文
        context={'article_post_form':article_post_form}
        return  render(request,'article/create.html',context)
def article_delete(request,id):
    # 根据文章id来获取文章
    article=ArticlePost.objects.get(id=id)
    # 然后删除文章
    article.delete()
    # 在删除之后返回文章列表
    return redirect('article:article-list')

# 对文章进行更新
def article_update(request,id):
    """
    更新文章的视图函数
    通过post方法提交表单，更新title和body字段
    GET方法进入初始表单页面
    需要的id 则表示文章的id
    :param request:
    :param id:
    :return:
    """
    # 获取需要修改的文章对象
    article=ArticlePost.objects.get(id=id)
    # 判断用户的提交方式是不是POST
    if request.method=="POST":
        # 将提交的数据赋值到表单实例中
        article_post_form=ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型需求
        if article_post_form.is_valid():
            # 保存新写入的title\boby数据并保存
            article.title=request.POST['title']
            article.body=request.POST['body']
            article.save()
            # 在完成后返回到修改后的文章中。需要传入文章的id值
            return redirect("article:article_detail",id=id)
        else:
            return HttpResponse("表单有误，重新填写")
    else:
        # 如果不是提交，则创建表单类实例
        article_post_form=ArticlePostForm()
        context={'article':article,'article_post_form':article_post_form}
        return render(request,'article/update.html',context)