from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
def login(request): # 第一次请求就是get
    error_msg=""
    # return render(request,"login.html") # 往下是baobao和login合并写法
    if request.method == "GET":# 必须大写
        return render(request,"login.html",{"error":error_msg})
    else:
        email = request.POST.get("email",None)
        pwd = request.POST.get("pwd",None) # 获取字典内容推荐方式
        # print(email,pwd)
        if email == "systemime@gmail.com" and pwd == "1":
            # return HttpResponse("OK")
            return redirect("https://www.baidu.com")
        else:
            # return render(request,"login.html")
            error_msg = "邮箱或密码错误"
            return render(request,"login.html",{"error":error_msg})

def baobao(resquest):# 会出现403错误，在设置文件中注释46行
    # 获取用户提交数据
    # print(resquest.POST)
    email = resquest.POST.get("email",None)
    pwd = resquest.POST.get("pwd",None) # 获取字典内容推荐方式
    # print(email,pwd)
    if email == "systemime@gmial.com" and pwd == "1":
        return HttpResponse("OK")
    else:
        return HttpResponse("Bat")