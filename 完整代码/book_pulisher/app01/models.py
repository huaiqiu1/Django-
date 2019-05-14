from django.db import models

# Create your models here.
# ORM(数据库相关操作)相关的只能写在这个文件里，卸载文件里Django不识别
#  OPM对应关系：类对应数据表，对象对应数据行，属性对应字段
# 执行命令: python manage.py makemigrations
#           python manage.py migrate
# 这个类和ORM数据库操作才能对应进行
# Tool（工具）中的 Run manage.py TasK...可以直接运行

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建自增的一个主键
    name = models.CharField(null=False, max_length=32)
    # varchar且不能为空的字段

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True) # 创建自增的一个主键
    name = models.CharField(null=False, max_length=64, unique=True)  # varchar且不能为空的字段
    addr = models.CharField(max_length=128, default="凤凰路223号")  # default默认值

# 书本类
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    # 与出版社的外键关系字段
    # 在真实表中publisher会自动在末位增加"_id"，但代码中两者均可以使用
    # on_delete=models.CASCADE 防止报错
    # OMR中的ForeignKey为外键指向,to=为to那张表
    # ForeignKey实际数据库中会在publisher_id后面再加一个_id
    # Publisher外面加上引号表示在全局中搜索这个类（数据表）
    # 实际上只要上一个类在这个类之前，就不需要加上引号了

    # 打印这个类的时候返回类对象的title字段
    def __str__(self):
        return "<Book Object: {}>".format(self.title)

# 作者表
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    # ROM多表对应
    book = models.ManyToManyField(to="Books")

    def __str__(self):
        return "<Author Object: {}>".format(self.name)