# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
     function changeAllState(tableId,state){
            table = $("#"+tableId);
            table.dataTable().fnDestroy();
            var userids=table[0].getElementsByTagName("input");
            var urls = new Array()
            var trs = new Array()
            for(var i=1;i<userids.length;i++){
                if(userids[i].checked){
                    var tr=$("#"+userids[i].value)
                    trs[trs.length] = tr
                    var tbody=tr.parent();
                    var table = tbody.parent();                    
                    var url = "/test/index.php/main/changeState?cardid="+userids[i].value+"&state="+state;
                    urls[urls.length] = url;                    
                }
                
            }
            for(var i=0;i<trs.length;i++){
                trs[i].remove();
            }
            reload(table);
            request(urls,0);
        }
        
```
