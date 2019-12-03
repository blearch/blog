from article.models import ArticlePost
from django.http import HttpResponse

# 视图函数
from django.shortcuts import render


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
    context={'article':article}
    return render(request,'article/detail.html',context)
