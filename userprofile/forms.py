# 引入表单类
from django import forms
# 引入User模型
from django.contrib.auth.models import User
from .models import Profile
# 登录表单 继承了forms.Form类
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

# 注册表单
class UserRegisterForm(forms.ModelForm):
    # 由于注册的时候需要和数据库直接进行交互，所以继承的表单类是ModelForm
    # 复写User的密码
    password=forms.CharField()
    password2=forms.CharField()
    class Meta:
        model=User
        fields=('username','email')

    def clean_password2(self):
        data=self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('phone','avatar','bio')
