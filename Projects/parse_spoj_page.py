import bs4 as bs
import requests


def get_problem_name(problem_link):
    response = requests.get(problem_link)
    soup = bs.BeautifulSoup(str(response.content), "lxml")
    return soup.find("h2", attrs={"id": "problem-name"}).text


# Open problem_link
def get_problems_by_user(user_id):
    response = requests.get(f"https://www.spoj.com/users/{user_id}/")
    soup = bs.BeautifulSoup(str(response.content), "lxml")
    result = []
    for a in soup.findAll("a"):
        href = a.attrs["href"]
        if len(href) > 11 and "problems" in href:
            problem_link = "https://www.spoj.com" + href
            problem_name = get_problem_name(problem_link)
            result.append((problem_link, problem_name))


lop = [
    "https://www.spoj.com/problems/AARTDARK/",
    "https://www.spoj.com/problems/ABNDNTNM/",
    "https://www.spoj.com/problems/ADABEHIVE/",
    "https://www.spoj.com/problems/BTCK/",
    "https://www.spoj.com/problems/BUET19B/",
    "https://www.spoj.com/problems/CHI_NATURAL/",
    "https://www.spoj.com/problems/CONGRAPH/",
    "https://www.spoj.com/problems/CPOD1/",
    "https://www.spoj.com/problems/DPRSDCDR/",
    "https://www.spoj.com/problems/DRNTEAGL/",
    "https://www.spoj.com/problems/ENGCD/",
    "https://www.spoj.com/problems/ENLCD/",
    "https://www.spoj.com/problems/FCTORISE/",
    "https://www.spoj.com/problems/FIZBBZIF/",
    "https://www.spoj.com/problems/FIZZFIZZ/",
    "https://www.spoj.com/problems/G11_2/",
    "https://www.spoj.com/problems/MAX10/",
    "https://www.spoj.com/problems/MOZSACL/",
    "https://www.spoj.com/problems/MUJEO/",
    "https://www.spoj.com/problems/MUJGEO/",
    "https://www.spoj.com/problems/OVISOD/",
    "https://www.spoj.com/problems/RETO6/",
    "https://www.spoj.com/problems/SERI07/",
    "https://www.spoj.com/problems/SHOCCUR/",
    "https://www.spoj.com/problems/SIMPACR/",
    "https://www.spoj.com/problems/SIMPLPRBLM/",
    "https://www.spoj.com/problems/SUMSCALC/",
    "https://www.spoj.com/problems/SUMUNZ/",
    "https://www.spoj.com/problems/VLN/",
    "https://www.spoj.com/problems/ZDIFFSQ2/",
]
for a in lop:
    print(get_problem_name(a))
exit()
problems = get_problems_by_user("khanhvh")
for problem in problems:
    problem[0]  # problem_link
    problem[1]  # problem_name
