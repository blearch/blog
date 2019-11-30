from django.http import HttpResponse

# 视图函数
def article_list(request):
    return HttpResponse("Hello World!,nice to meet you")