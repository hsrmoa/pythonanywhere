from django.core import paginator
from django.shortcuts import get_object_or_404, render , redirect
from djangofrontapp.form import LoginForm, RegisterForm, PostForm
from djangofrontapp.models import DsUser, Post, Tag
from django.contrib.auth import login as authLogin, authenticate, logout
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

# index
def index(request):    
    page = request.GET.get("pIndex")
    posts = Post.objects.order_by('-createDt').all()    
    paginator = Paginator(posts,4);
    posts = paginator.get_page(page);
    postResult = {
        "list"      :  posts
    ,   "tagList"   :  []
    }
    lst = []
    for port in posts :
        tags = port.tag.all();        
        taObj ={
            "portId" : port
        ,   "tagNm"  : None
        }   
        tagName = ""
        for t in tags :  
            ta = t.tag + ",";
            tagName += ta                        
        taObj["tagNm"] =tagName[:-1]        
        lst.append(taObj)
    postResult["tagList"] = lst;    
    return render(
        request
    ,   "timeLine.html"
    ,   {
            "curPage"   :   "timeLine" 
        ,   "cardResult"  :    postResult
        }
    );

#회원가입
def register(request):                
    msg = ""    
    form = RegisterForm(request.POST or None);        
    if request.method == "POST" and form.is_valid() :            
        if request.POST["userId"] == "" or request.POST["userEmail"] == "" or request.POST["userPwd"] == ""  or request.POST["userPwd1"] == "" :
            msg = "모든 값을 입력해야 합니다"
        else :
            if request.POST["userPwd"] != request.POST["userPwd1"] :
                msg ="비밀번호가 다릅니다"
            else :                
                cd = form.cleaned_data
                data = DsUser(
                    user_id = cd["userId"]
                ,   email = cd["userEmail"]
                ,   password = make_password(cd["userPwd"])
                )
                data.save()
                return redirect("/");

    return render(
        request
    ,   "register.html"
    ,   {
            "msg"       :   msg 
        ,   "form"      :   form 
        ,   "curPage"   :   "register" 
        }
    )


#로그인
def login_view(request) :
    msg = "";
    isLogin = False;
    form = LoginForm(request.POST or None);
    if request.method == "POST" and form.is_valid() :
        usrid = form.cleaned_data.get("userId");
        usrPwd = form.cleaned_data.get("userPwd");                
        try :
            userInfo = DsUser.objects.get(user_id=usrid)            
        except DsUser.DoesNotExist :
            msg ="아이디가 없습니다.";
        else :
            if check_password(usrPwd,userInfo.password) :
                msg = None;
                authLogin(request, userInfo);
                isLogin = True     
                request.session["user"] = usrid
                #request.session.set_expiry(1000);
                return redirect("/");
            else :
                isLogin = False
                msg = "비밀번호가 다릅니다."
    return render(
        request
    ,   "login.html"
    ,   {
            "isLogin"   :   isLogin 
        ,   "msg"       :   msg
        ,   "form"      :   form
        ,   "curPage"   :   "loginView"
        }
    )
#로그아웃
def logoutAction(request) :    
    logout(request)
    return redirect("/");


#글작성
@login_required
def postWrite(request):
    msg = None  
    form = PostForm(request.POST or None);    
    
    if request.method == "POST" and form.is_valid()  :        
        
        user = DsUser.objects.get(user_id=request.session["user"]);        
        conts=form.cleaned_data["postCts"]
        imgUrl = form.cleaned_data["postImg"]
        tags = form.cleaned_data["postTag"]                
        
        addPost = Post.objects.create(writer=user,contents=conts,imageUrl=imgUrl);
        #print(addPost);                
        tagList = tags.split(",");
        for t in tagList :            
            try :
                Tag.objects.get(tag = t)
            except Tag.DoesNotExist :
                addTag = Tag.objects.create(tag=t);                            
            else :                
                addTag = Tag.objects.get(tag=t);
            addPost.tag.add(addTag);

        return redirect("/");
    return render(
        request
    ,   "postWrite.html"
    ,   {
            "msg"       :   msg
        ,   "form"      :   form
        ,   "curPage"   :   "postWrite"
        }
    )
def postDetail(request,pk) :    

    detail = get_object_or_404(Post,pk=pk);    
    tags = detail.tag.all();          
    return render(
        request
    ,   "postDetail.html"
    ,   {
        #    "msg"       :   msg
        #,   "form"      :   form        
            "curPage"    :   "timeLine"
        ,   "detail"     :  detail
        ,   "tags"        :  tags
        }
    )
