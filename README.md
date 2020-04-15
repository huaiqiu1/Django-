<h1 align="center"><a href="https://github.com/byteblogs168/plumemo" target="_blank">plumemo</a></h1>

> [Plumemo](https://www.plumemo.com/) 是一个轻量、易用、前后端分离的博客系统，为了解除开发人员对后端的束缚，真正做到的一个面向接口开发的博客系统。

<p align="center">
<a href="#"><img alt="JDK" src="https://img.shields.io/badge/JDK-1.8-yellow.svg?style=flat-square"/></a>
<a href="#"><img alt="GitHub release" src="https://img.shields.io/github/release/halo-dev/halo.svg?style=flat-square"/></a>
<a href="#"><img alt="GitHub All Releases" src="https://img.shields.io/github/downloads/halo-dev/halo/total.svg?style=flat-square"></a>
<a href="#"><img alt="Docker pulls" src="https://img.shields.io/docker/pulls/ruibaby/halo?style=flat-square"></a>
</p>

------------------------------
## 简介

**plumemo** [plumemo]，plume（羽） + memo（备忘录）

> 基于[SpringBoot](https://spring.io/projects/spring-boot/)实现零配置让系统的配置更简单，使用了[Mybatis-Plus](https://mp.baomidou.com/)快速开发框架，在不是复杂的查询操作下，无需写sql就可以快速完成接口编写。

> 后台管理系统使用了vue中流行的[ant](https://panjiachen.github.io/vue-element-admin-site/#/)，另外前后交互使用了[JWT](https://jwt.io/)作为令牌，进行权限、登录校验。。

> [官网](https://www.plumemo.com/) | [社区](https://www.byteblogs.com) | [QQ 交流群](https://shang.qq.com/wpa/qunwpa?idkey=4f8653da80e632ef86ca1d57ccf8751602940d1036c79b04a3a5bc668adf8864) |

## 背景

> 由于plumemo 是前后端分离的，那么对于部署来说就一件很头疼的事情，主题、管理系统、后端java服务都需要配置安装配置。除此之外还是jdk、mysql、nginx配置无疑给很多小伙伴照成了一定的阻碍；为此经过几天的努力pluemeo-v1.0.0 安装脚本诞生了。

## 下载脚本
• centos7、ubuntu16.04以上建议使用
```
# 仅在centos7及ubuntu16.04及以上版本测试成功
# 可以使用systemctl 或 service 的方式管理博客守护进程
# 日志位置：/logs
wget https://raw.githubusercontent.com/byteblogs168/plumemo-deploy/master/plumemo-v1.1.0.sh
```
• 通用无守护进程
```
# 日志目录：jar包目录下logs文件夹
wget https://raw.githubusercontent.com/byteblogs168/plumemo-deploy/master/plumemo-v1.0.0.sh
```

## 功能介绍
1. jdk
2. mysql
3. nginx
4. 主题
5. 管理系统
6. 博客数据库备份

## 操作步骤
1. 把脚本上传到服务器（不做介绍）
2. 添加可执行权限 ```chmod +x plumemo-v1.1.0.sh```
3. 执行脚本 ```sh plumemo-v1.1.0.sh```

下面您就可以根据你的选择进行安装:

## 安装jdk,版本:jdk-8u144-linux-x64
![QQ截图20200331222233.png](http://image.byteblogs.com/5d457dbe646179af7973fbec46e4c735.png)

## 安装mysql,版本:5.7.28
![QQ截图20200331224800.png](http://image.byteblogs.com/9aaa08107724f72a4476c954b89e7dd0.png)

## 安装nginx,版本:1.17.9
![QQ截图20200331225219.png](http://image.byteblogs.com/6b7bcabe5c1eb82389365609424b0d4e.png)

## 安装plumemo主题
![111.png](http://image.byteblogs.com/7269932fdd7f8ba760b50d8a119a60c0.png)

## 安装plumemo管理系统
![admin1.png](http://image.byteblogs.com/f9488ff8ea985d73d468f771c60a08b1.png)
![admin2.png](http://image.byteblogs.com/bba546a5eada5b57e31e3b588e5f19e6.png)

### 博客启动脚本
#### v1.1.0版本
```
systemctl start plumemo.service

或者

service plumemo.service start
```

#### v1.0.0版本
1. 添加可执行权限 ```chmod +x deploy.sh```
2. 执行脚本 ```sh deploy.sh```

![aa.png](http://image.byteblogs.com/321532365639f31b3b9f8ea8be0c6be2.png)

## 下载nginx配置文件
> 请勿随意修改配置文件内容，严格路径对照
> 默认下载位置 /usr/local/plumemo/nginx/conf，若自行安装nginx，请修改路径

```shell
wget -P /usr/local/plumemo/nginx/conf -N https://raw.githubusercontent.com/byteblogs168/plumemo-deploy/master/nginx.conf
```

## 备份博客数据
![备份.png](https://raw.githubusercontent.com/systemime/my_image/master/QQ%E6%88%AA%E5%9B%BE20200415144132.png)
