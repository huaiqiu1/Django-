# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
         public function get_person_info($jz_person_info_number, $case){		
		$sql = "SELECT * FROM `jz_person_info` WHERE `jz_person_info_number` = '{$jz_person_info_number}'";
		$res = $this->db->query($sql);
		$person_info = $res->result_array();
		$sql = "SELECT * FROM `jz_person_more_view` WHERE `jz_person_info_number` = '{$jz_person_info_number}'";
		$res = $this->db->query($sql);
		$card_info = $res->result_array();
	 }
        
```
