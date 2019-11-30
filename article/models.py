from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 博客文章数据模型

# 文章作者，on_delete表示删除方式
# 博客文章数据模型
from django.utils import timezone


class ArticlePost(models.Model):
    # 文章作者，on_delete表示删除方式
    # Foreignkey用来解决一对多的关系  oneToOneField用来一对一  ManyToManyField用来解决多对多
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    # 文章标题
    title= models.CharField(max_length=100)
    # 文章正文
    body=models.TextField()
#     文章创建的时间  参数default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created=models.DateTimeField(default=timezone.now)
#     文章更新时间。参数auto_now=True指定每次数据更新字典填写当前时间
    updated=models.DateTimeField(auto_now=True)
    # meta类相当于对原来的类进行功能的添加。主要是为模型提供元数据。
    class Meta:
        # ordering表明排序的方式
        # -created表明应该倒序
        ordering=('-created',)
    def __str__(self):
        # 当对象定义str()时返回的值
        return self.title
