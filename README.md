# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
                 $.ajax(
			url: "http://localhost/api/get_hierarchy_structure",  // 请求地址
			type: 'GET',
			dataType: 'json',
			success: function (data) {
				data0 = data['points0'].length < data['points1'].length ? data['points0']:
                            data['points1'].length < data['points2'].length?data['points1']: data['points2']
				data2 = data['points0'].length > data['points1'].length ? data['points0']:
                            data['points1'].length > data['points2'].length?data['points1']: data['points2']
				if (data['points0'].length!=data0.length && data['points0'].length!=data2.length){
					data1 = data['points0']
				}
				else{
					if (data['points1'].length!=data0.length && data['points1'].length!=data2.length){
						data1 = data['points1']
					}
					else{
						data1 = data['points2']
					}
				}
				drawgraph(data0,data1,data2);
				drawtable(data0,data1,data2);
				$('#loadingModal').modal("hide");
			}
		 }); 
        
```
