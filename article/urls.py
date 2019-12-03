from article import views

from django.urls import path
# 和urls 里面的namespace相对应 两者必须要有  否则会报错
app_name='article'
urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article-list'),
#     文章详情
    path('article-detail/<int:id>/',views.article_detail,name='article_detail'),
]