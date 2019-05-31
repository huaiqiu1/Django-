# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
        function request(urls,i){
            if(urls.length>i){
                $.ajax({
                    url:urls[i],
                    type:'GET',
                    success:function(data){
                        request(urls,i+1);
                    }
                });
            }

```
