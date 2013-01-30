<?php
//post方法测试发送信息
$post_data = array();
$post_data['msg'] = "请忽略哥，蛋疼测试中";
$url='http://127.0.0.1:8090/gtalk';
$o="";
foreach ($post_data as $k=>$v) {
    $o.= "$k=".urlencode($v)."&";
}
$post_data=substr($o,0,-1);
$ch = curl_init();
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_URL,$url);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
$result = curl_exec($ch)
?>

