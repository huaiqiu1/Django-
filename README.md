# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
        success: function (data) {
                $(that).siblings('.spinner').html(''); 
                var tbody = $('<tbody></tbody>');
                var tr_excel = $('<tr><td>上传文件字段</td></tr>');
                var tr_db = $('<tr><td>标准字段</td></tr>');
                $('.pre-table').empty();
                var select = $('<select ><option value="-1">无/不上传</option></select>');
                $.each(data.db, function (i, val) {
                    var option = $('<option value="' + i + '">' + val + '</option>');
                    $(select).append(option);
                });
```
