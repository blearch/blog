from article.models import ArticlePost
from django.http import HttpResponse

# 视图函数
from django.shortcuts import render


def article_list(request):
    # return HttpResponse("Hello World!,nice to meet you")
    # 取出所有博客文章
    articles=ArticlePost.objects.all()
    # 传递给模板的对象
    context={'articles':articles}
    return render(request,'article/list.html',context)
