from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages  # 弹窗
from app01 import models  # 导入OPM的类，便于操作数据库

# from django.views.decorators.csrf import csrf_exempt # 解决校验问题造成的403错误
# setting.py文件中注释掉'django.middleware.csrf.CsrfViewMiddleware'（47行左右）
# 登陆界面打开
def baobao(request):
    error_msg = ""
    if request.method == "POST":
        print(request.POST)
    return HttpResponse("OK")

# @csrf_exempt #修饰器解决403报错（Django自身数据校验）
def login(request):
    error_msg = ""
    print(request.POST)
    if request.method == "POST":
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        if email == "1767474418@qq.com" and pwd == "123":
            return redirect("/publisher_list/")
            # 回复一个特殊的响应，让浏览器请求指定URL，跳转网页,也可以填写一个网站
        else:
            error_msg = "邮箱或密码错误"
    return render(request, "login.html", {"error": error_msg})  # render完成HTML界面替换

# 展示所创建的数据表中的内容（查）
def publisher_list(request):
    # order_by("id") 按照ID排序
    ret = models.Publisher.objects.all().order_by("id")
    # 数据库中查询所有用户，利用orm
    # print(ret[0].id, ret[0].name)
    # 得到的是两个UserInfo object对象,因为models的class对应的表中，暂时只有两条数据
    return render(request, "publisher_list.html", {"publisher_list": ret})

# 增加数据（增）
def add_publisher(request):#第一次请求页面的时候，返回一个页面，页面有两个填写框
    error_msg = ""
    if request.method == "POST":
        new_name = request.POST.get("publisher", None)# print(new_name)
        print("你添加的出版社名称为：{0}".format(new_name))
        if new_name in [name['name'] for name in models.Publisher.objects.values("name")]:
            error = "“" + new_name + "”" + "该出版社已存在!!!"
            print(error)
            messages.success(request, error)
            return render(request, "add_publisher.html", {"error": error})
        models.Publisher.objects.create(name=new_name)#数据库中新创建一条数据行
        return redirect("/publisher_list/")  # redirect返回方法 HttpResponse返回字符串
    else:
        error_msg = "出版社名称不能为空"
    return render(request, "add_publisher.html", {"error": error_msg})#render完成HTML界面替换

# 删除数据（删）
def delete_publisher(request):
    del_id = request.GET.get("id",None)
    del_name = request.GET.get("name",None)
    print("删除ID为{0},名称为‘{1}’的数据".format(del_id,del_name))
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("ERROR,检查数据后再试")

# 编辑出版社(更新操作)（改）
def edit_publisher (request):
    if request.method == "POST":
        print(request.POST)
        edit_id = request.POST.get("publisher_id")
        new_name = request.POST.get("publisher_name")
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()  # 把修改提交到数据库
        # 跳转到出版社列表页，查看是否修改
        return redirect("/publisher_list/")
    edit_id = request.GET.get("id")
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)  # 获取到数据内的这条记录，
        # 在html界面的替换语句那里加上.name表示，获取这条记录中的name值（套路）
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})

# 展示书列表
def book_list(request):
    all_book = models.Books.objects.all()
    return render(request, "book_list.html", {"all_book": all_book})

def add_book(request):
    ret = models.Publisher.objects.all()
    error = ""
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        if new_title in [title['title'] for title in models.Books.objects.values("title")]:
            error = "《" + new_title + "》" + "此书在" + models.Books.objects.get(id=new_publisher_id).publisher.name + "已存在!!!"
            messages.success(request, error)
            return render(request, "add_book.html", {"publisher_list": ret, "error": error})
        # 创建新书对象，自动提交
        models.Books.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect("/book_list/")
        # redirect返回方法 HttpResponse返回字符串
    return render(request, "add_book.html", {"publisher_list": ret, "error": error})  # render完成HTML界面替换

def delete_book(request):
    print(request)
    delete_id = request.GET.get("id")  # 从url中获取要删除的书的id
    delete_publisher_id = request.GET.get("publisher_id")
    # print(delete_id, "----", delete_publisher_id)
    # 去库删除
    print("删除了来自‘ {0} ’出版社的《{1}》".format(models.Publisher.objects.get(id=delete_publisher_id).name, models.Books.objects.get(id=delete_id)))
    models.Books.objects.get(id=delete_id).delete()
    return redirect("/book_list/")

def edit_book(request):
    if request.method == "POST":
        print(request.POST)
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # 更新
        edit_book_obj = models.Books.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher_id
        edit_book_obj.save()
        return redirect("/book_list/")
    edit_id = request.GET.get("id")  # 获取书的id
    edit_book = models.Books.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request, "edit_book.html", {"publisher_list": ret, "book_obj": edit_book})

def auther_list(request):
    all_auther = models.Author.objects.all()
    # print(models.Author.objects.get(id="1").book.all())
    return render(request, "author_list.html", {"author_list": all_auther})
    # return HttpResponse("OK")

def add_author(request):
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        books = request.POST.getlist("books")  # post提交数据包含多个值，使用getlist
        print(new_author_name, books)
        new_author_obj = models.Author.objects.create(name=new_author_name)
        new_author_obj.book.set(books)
        return redirect("/author_list/")
    ret = models.Books.objects.all()
    return render(request, "add_author.html", {"book_list": ret})

def delete_author(request):
    delete_id = request.GET.get("id")
    # 删除的同时删除对应关系
    models.Author.objects.get(id=delete_id).delete()
    return redirect("/author_list/")

def edit_author(request):
    # 如果编辑完提交数据过来
    if request.method == "POST":
        # 拿到提交过来的编辑后的数据
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        # 拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        # 根据ID找到当前编辑的作者对象
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        # 更新作者的名字
        edit_author_obj.name = new_author_name
        # 更新作者关联的书的对应关系
        edit_author_obj.book.set(new_books)
        # 将修改提交到数据库
        edit_author_obj.save()
        # 返回作者列表页,查看是否编辑成功
        return redirect("/author_list/")

    # 从URL里面取要编辑的作者的id信息
    edit_id = request.GET.get("id")
    # 找到要编辑的作者对象
    edit_author_obj = models.Author.objects.get(id=edit_id)
    # 查询所有的书籍对象
    ret = models.Books.objects.all()
    return render(request, "edit_author.html", {"book_list": ret, "author": edit_author_obj})

def test(request):
    new_publisher_id = 14
    a = models.Books.objects.get(id=new_publisher_id).publisher.name
    print(a)
    return HttpResponse("OK")