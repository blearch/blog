# 引入表单
from django import forms
# 引入文章模型
from .models import ArticlePost
# 撰写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model=ArticlePost
        # 定义表单内包含的字段
        fields=('title','body')
