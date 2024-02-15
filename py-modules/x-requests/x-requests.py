#https://stackoverflow.com/questions/27803503/get-html-using-python-requests
#https://stackoverflow.com/questions/11709079/parsing-html-using-python

import requests 
from bs4 import BeautifulSoup

urls = [
    "https://www.spoj.com/problems/KAMOL/",
    "https://www.spoj.com/problems/COUINF/",
    "https://www.spoj.com/problems/PRF00/",
    "https://www.spoj.com/problems/TESTINT/",
    "https://www.spoj.com/problems/CHITEST1/",
    "https://www.spoj.com/problems/SMPWOW/",
    "https://www.spoj.com/problems/AVRG/",
    "https://www.spoj.com/problems/DHRODD/",
    "https://www.spoj.com/problems/BSCXOR/",
    "https://www.spoj.com/problems/SMPSUM/",
    "https://www.spoj.com/problems/HRECURS/",
    "https://www.spoj.com/problems/ALCATRAZ1/",
    "https://www.spoj.com/problems/STRHH/",
    "https://www.spoj.com/problems/CPTTRN1/",
    "https://www.spoj.com/problems/CPTTRN2/",
    "https://www.spoj.com/problems/CPTTRN3/",
    "https://www.spoj.com/problems/CPTTRN4/",
    "https://www.spoj.com/problems/CPTTRN5/",
    "https://www.spoj.com/problems/CPTTRN6/",
    "https://www.spoj.com/problems/CPTTRN7/",
    "https://www.spoj.com/problems/SMPDIV/",
    "https://www.spoj.com/problems/SMPCIRC/",
    "https://www.spoj.com/problems/FUCT_IF_COMPARE/",
    "https://www.spoj.com/problems/HS12MBR/",
    "https://www.spoj.com/problems/PCROSS1/",
    "https://www.spoj.com/problems/FUCT_FOR_FNPN/",
    "https://www.spoj.com/problems/PRIONPRI",
    "https://www.spoj.com/problems/SMPSEQ3/",
    "https://www.spoj.com/problems/SMPSEQ4/",
    "https://www.spoj.com/problems/SMPSEQ5/",
    "https://www.spoj.com/problems/SMPSEQ6/",
    "https://www.spoj.com/problems/SMPSEQ7/",
    "https://www.spoj.com/problems/SMPSEQ8/",
    "https://www.spoj.com/problems/SMPSEQ9/",
    "https://www.spoj.com/problems/LASTDIG/",
    "https://www.spoj.com/problems/SMPCPH1/"
]

for url in urls:
    r = requests.get(url)

    html_page = r.text

    parsed_html = BeautifulSoup(html_page,features="lxml")

    problem_name = parsed_html.body.find('h2', attrs={'id':'problem-name'}).text

    print(problem_name)