import requests
from bs4 import BeautifulSoup

def get_std_html(id):
	url = "http://moed.gov.sy/sharie/rslt.php"
	data= {"gove":1,"stunum":id,"Submit":""}
	x = requests.post(url, data=data)
	return x.text

#JS

def get_std_info(html_text):
	parsed_html = BeautifulSoup(html_text)
	a_cells = parsed_html.body.find_all('div',attrs={'class':'a-cell'})
	
	id = a_cells[1].text
	gov = a_cells[3].text
	name = a_cells[5].text
	mother_name = = a_cells[7].text
	school = = a_cells[9].text
	result = a_cells[11].text[:4]
	print(id,gov,name,mother_name,school,result)

def get_std_marks(html_text):
	list_of_marks = []
	marks = parsed_html.body.find_all('div',attrs={'class':'mark'})
	marks = document.getElementsByClassName("mark")
	for i in range(12):
		list_of_marks.append(marks[index].text)
	return list_of_marks

std_html = get_std_html(700)
get_std_info(std_html)
marks = get_std_marks(std_html)
print(marks)

headers = [
"اللغة العربية",
"التفسير التحليلي",
"الحديث النبوي",
"العقيدة الإسلامية",
"الفقه",
"الدعوة والخطابة",
"التلاوة والاستحفاظ",
"اللغة الإنكليزية",
"اللغة الفرنسية",
"الاجتماعيات",
"العلوم العامة والصحة",
"الرياضيات",
"المجموع"]


