<?php
if(
    !isset(
        $_GET["password"]
            )
    ||
    $_GET["password"]!="mostafa"
    ||!isset($_GET["from"])
    ||!isset($_GET["to"])
)
{
    die("Ok, How are you?");
}
$from = $_GET["from"];
$to   = $_GET["to"];
echo "results from $from  to $to";
//die();

//https://www.the-art-of-web.com/php/http-get-contents/

function http_get_contents($id)
{
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_TIMEOUT, 1);
  curl_setopt($ch, CURLOPT_URL, "http://moed.gov.sy/sharie/result.php");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  curl_setopt($ch, CURLOPT_POSTFIELDS,"city=1&stdnum=$id&Submit=");
  if(FALSE === ($retval = curl_exec($ch))) {
    error_log(curl_error($ch));
  } else {
    return $retval;
  }
}
function print_header()
{
    $array = array(
        "النتيجة",
        "المجموع",
        "المجموع الكوني",
        "الرياضيات",
        "العلوم العامة",
        "الاجتماعيات",
        "اللغة الفرنسية",
        "اللغة الانكليزية",
        "اللغة العربية",
        "المجموع الشرعي",
        "التلاوة والاستحفاظ",
        "الدعوة والخطابة",
        "الفقه",
        "العقيدة الإسلامية",
        "الحديث النبوي",
        "التفسير التحليل",
        "اسم الطالب",
        "رقم"
    );
    
    $return ="";
    
    $notfirst = false;
    foreach( $array as  $head ) {
        if($notfirst)
            $return .= ",";
        $return .= $head;
        $notfirst=true;
    }
    $return .= "</br>\n";
    return $return;
}
function print_student($id)
{
    $indexes = array(38,115,0,109,103,97,91,85,43,1,79,73,67,61,55,49,29,23);
    $output = http_get_contents($id);
    $dom = new DOMDocument();
    $dom->loadHTML($output);
    $divs = $dom->getElementsByTagName("div"); 
    
    $array = array();
    foreach( $divs as  $div ) {
        $array[] = str_replace("الدرجة","",$div->textContent);
    }
    
    //TODO AUTOMATE INDEXES FROM $indexes ARRAY
    $array[0]=$array[109]+$array[103]+$array[97]+$array[91]+$array[85]+$array[43];
    $array[1]=$array[79]+$array[73]+$array[67]+$array[61]+$array[55]+$array[49];
    
    $return ="";
    $notfirst = false;
    $i = 0;
    foreach( $indexes as  $index ) {
        if($notfirst)
            $return .= ",";
        if($i == 0 || $i ==16){
            $return .= $array[$index];//name
        }else{
            $return .= $array[$index];
        }
        $notfirst=true;
    }
    $return .= "</br>\n";
    return $return;
}

set_time_limit(0);
$return = "";
$return .= '<!DOCTYPE html>';
$return .= '<html>';
$return .= '<head>';
$return .= "<title>نتائج امتحان شهادة التعليم الأساسي والإعدادية الشرعية لعام 2020</title>";
$return .= '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />';

$return .= print_header();
for($id=$from;$id<=$to;$id++){
    $return .= print_student($id);
}
$return .= '</head>';
$return .= '</html>';

echo $return;
file_put_contents("bdh.html", $return);
echo " <a href='bdh.html'>done</a>";
?>