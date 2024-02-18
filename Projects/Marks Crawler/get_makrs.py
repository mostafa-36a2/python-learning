import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def get_std_html(id):
	url = "http://assasy2022.moed.gov.sy/sharie/rslt.php"
	data= {"gove":1,"stunum":id,"Submit":""}
	x = requests.post(url, data=data)
	x.encoding = x.apparent_encoding
	return x.text

def get_std_info(html_text):
	parsed_html = BeautifulSoup(html_text,features="lxml")
	a_cells = parsed_html.body.find_all('div',attrs={'class':'a-cell'})
	
	id = a_cells[1].text
	gov = a_cells[3].text
	name = a_cells[5].text
	print(f"Student: {name}")
	mother_name = a_cells[7].text
	school = a_cells[9].text
	result = a_cells[11].text[:4]
	return [id,name,result]

def get_std_marks(html_text):
	list_of_marks = []
	parsed_html = BeautifulSoup(html_text,features="lxml")
	marks = parsed_html.body.find_all('span',attrs={'class':'mark'})
	try:
		for index in range(13):
			list_of_marks.append(marks[index].text)
	except Exception as e:
		print(f"Exception for 	{marks} ! {e}")
		return [0 for i in range(13)]
	return list_of_marks

def get_students_results(start,end):
	all_results = []
	for std_id in range(start,end+1):
		print(f"Getting student: {std_id}") 
		std_html = get_std_html(std_id)
		std_info = get_std_info(std_html)
		marks = get_std_marks(std_html)
		std_info.extend(marks)
		all_results.append(std_info)
	return all_results

all_restuls = get_students_results(610,772)

headers = [
"الرقم التعريفي",
"الاسم",
"النتيجة",
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


output = tabulate(all_restuls, headers,tablefmt="tsv")
with open("results_2.csv","w") as output_file:
	output_file.write(output)

