from django import forms
from django.forms import widgets
from djangofrontapp.models import DsUser

#회원가입 폼
class RegisterForm(forms.Form):
    userId = forms.CharField(
        max_length=30
    ,   required=False
    ,   widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" :"아이디를 입력해주세요",
                "id": "userId"
            }
        )
    ,   label="아이디"
    )
    userEmail = forms.EmailField(
        max_length=100
    ,   required=False
    ,   widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder" :"이메일을 입력해주세요",
                "id": "userEmail"
            }
        )
    )
    userPwd = forms.CharField(
        max_length=100
    ,   required=False
    ,   widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder" :"비밀번호을 입력해주세요",
                "id": "userPwd"
            }
        )
    )

    userPwd1 = forms.CharField(
        max_length=100
    ,   required=False
    ,   widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder" :"비밀번호 확인을 입력해주세요",
                "id": "userPwd1"
            }
        )
    )
    class Meta:
        model = DsUser
        fields = (
            "id"
        ,   "email"
        ,   "password"
        )

# 로그인
class LoginForm(forms.Form):
    userId = forms.CharField(
        max_length=30
    ,   required=False
    ,   widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" :"아이디를 입력해주세요",
                "id": "userId"
            }
        )
    ,   label="아이디"
    )
    userPwd = forms.CharField(
        max_length=100
    ,   required=False
    ,   widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder" :"비밀번호을 입력해주세요",
                "id": "userPwd"
            }
        )
     ,   label="비밀번호"
    )

class PostForm(forms.Form):
    
    postCts = forms.CharField(
        label="내용"
    ,   required=True
    ,   error_messages= {
            "required" :"내용은 필수입력 값입니다."
        }
    ,   widget= forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder" :"내용을 입력해주세요",
                "id": "postCts",
                "row" : 10,
                "cols" :50
            }
        )
    )
    postImg = forms.CharField(
        label ="이미지"
    ,   required=True
    ,   error_messages= {
            "required" :"이미지 주소는 필수입력 값입니다."
        }
    ,   widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" :"이미지 주소를 입력해주세요",
                "id": "postImg"
            }
        )
    )
    postTag = forms.CharField(
        label ="태그"
    ,   widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" :"태그를 입력해주세요",
                "id": "postTag"
            }
        )
    )

    

    