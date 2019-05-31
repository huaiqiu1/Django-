# Django-1.11
Django学习记录
简单图书出版社作者管理
目前上传1.11 LTS版本代码
正在摸索2.15特性与区别，解决静态文件问题后代码再次上传

------

django版本更换2.2
完整代码已上传


```
       public function get_single_stat($card) {
		$sql = "SELECT `jz_doublecard_info_oppoaccount`, `jz_doublecard_info_intotal`,jz_doublecard_info_incount`,  
		       `jz_doublecard_info_inmax`, `jz_doublecard_info_inmedian`, `jz_doublecard_info_inaverage`,    
		       `jz_doublecard_info_outtotal`, `jz_doublecard_info_outcount`, `jz_doublecard_info_outmax`, 
		       `jz_doublecard_info_outmedian`, 
		       `jz_doublecard_info_outaverage`,`jz_doublecard_info_inshengoucount`+
		       `jz_doublecard_info_outshengoucount` AS 	 `jz_doublecard_info_shengoucount`, 
		       `jz_doublecard_info_infanlicount`+`jz_doublecard_info_outfanlicount` AS 
		       `jz_doublecard_info_fanlicount` FROM `jz_doublecard_info` WHERE 
		       `jz_doublecard_info_currentaccount` = '{$card}'";
		$res = $this->db->query($sql);
		$list_a2b = $res->result_array();
		$sql = "SELECT `jz_bankwater_qvzaoinfo_transcatdata`, `jz_bankwater_qvzaoinfo_transcatamount`, 
		       `jz_bankwater_qvzaoinfo_balance`, `jz_bankwater_qvzaoinfo_inoroutsign`, 
		       `jz_bankwater_qvzaoinfo_oppoaccount`,  `jz_bankwater_qvzaoinfo_abstract`, 
		       `jz_bankwater_qvzaoinfo_transactbankname` FROM `jz_bankwater_qvzaoinfo` WHERE 
		       `jz_bankwater_qvzaoinfo_productcode` = '{$card}'";
		$res = $this->db->query($sql);
		$list_single = $res->result_array();
		$sql = "SELECT `jz_cardopen_qvchonginfo_personname` FROM `jz_cardopen_qvchonginfo` WHERE 
		       `jz_cardopen_qvchonginfo_transcatcardnum` = '{$card}'";
		$res = $this->db->query($sql);
		$name = $res->result_array();
		$sql = "SELECT * FROM `jz_single_day_bankwater_info` WHERE
		      `jz_single_day_bankwater_info_productcode` = '{$card}'";
		$res = $this->db->query($sql);
		$singleday = $res->result_array();

		$data['a2b'] = $list_a2b;
		$data['single'] = $list_single;
		$data['card'] = $card;
		$data['name'] = $name[0]['jz_cardopen_qvchonginfo_personname'];
		$data['singleday'] = $singleday;
		return $data;
	}
```
