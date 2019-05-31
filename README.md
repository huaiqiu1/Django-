# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
  public function get_uploadrecord_list($case){
		$sql = "SELECT jz_uploadrecord_info_id, jz_uploadrecord_info_uploadoriginname, 
		       jz_uploadrecord_info_uploaddata 
		FROM jz_uploadrecord_info WHERE jz_uploadrecord_info_caseid = '{$case['id']}'";
		$res = $this->db->query($sql);
		$list = $res->result_array();
		$data['list']=$list;
		// var_dump($list);
		return $data;
	}
        
```
