# Flask App
"""
- Idea
- Planning / UI
- Skeleton
- Basic Logic
- Storage

*6- Build a counter app (user/pass) (storage) -> view (frontend) [JS -> BE (save)]
- users? -

Frontend                                       data                            Backend              DB
user: sing up (username/password)             |-user/pass----------------->POST|store (first time) | (userid-user-password)

user: sign in username / password             |-user/pass----------------->GET |check              | (userid-user-password)
user: sign in username / password             |<-----success (user-id)-------- |check              | (userid-user-password)
user: sign in username / password             |<-----failed------------------- |check              | (userid-user-password)

user: show previews counting (just to know)   |--(userid)------------------>GET|get-count          | (userid-count-datetime)
user: show previews counting (just to know)   |<-(userid-count-datetime)-------|get-count          | (userid-count-datetime)

user: counting (javascript , change text)     |
user: save                                    |-(userid-count)------------>POST|save               | (userid-count-datetime)
user: reset   (javascript , change text)      |
"""

import datetime
import uuid
from typing import Tuple

users_dict :dict= {}

counts_dict :dict= {}
import os

USER_STORAGE_DICT_PATH = os.path.join(
    os.path.dirname(__file__),
    "users_storage.dict"
)
def generate_user_id(username):
    random_uid = str(uuid.uuid4())[:8]
    return f"{username}{random_uid}"

#TODO: Refactoring
def retrieve_users()->dict:
    global users_dict
    # read file and eval dict, return content
    try:
        with open(USER_STORAGE_DICT_PATH,'r') as file:
            content = file.read()
            try:
                users_dict = eval(content)
            except Exception:
                users_dict = {}
    except Exception:
        users_dict = {}

    return users_dict

# TODO: Store in DB
def store_user(username,password):
    user_id = generate_user_id(username)
    users_dict[username] = (password,user_id)
    # save user/pass/user_id in dictionary (in file)
    with open(USER_STORAGE_DICT_PATH,'w') as file:
        file.write(str(users_dict))
    # write dict the file
    return user_id

def sign_in(login_username, login_password)-> str | None:
    users :dict= retrieve_users()
    #1- check if username already exist ? 
    if login_username in users:
        user = users[login_username]
        user_password = user[0]
        user_id = user[1]
        #2- alreaedy exist return user_id
        if login_password == user_password:
            return user_id

    # either password is not correct OR user is not exist
    user_id = store_user(login_username,login_password)
    return user_id


# DRY: Dont repeat your self
#TODO: Refactoring
def read_count_dict():
    global counts_dict
    #TODO: Move filename to configurable place
    try:
        with open('count_stroage.dict','r') as file:
            content = file.read()
            try:
                counts_dict = eval(content)
            except Exception:
                counts_dict = {}
    except Exception:
        counts_dict = {}

    return counts_dict

def write_count_dict():
    try:
        with open('count_stroage.dict','w') as file:
            file.write(str(counts_dict))
    except Exception :
        return False
    return True

def get_count(user_id)-> Tuple[int,datetime.datetime]:
    # Read counting storage, get user storage 
    read_count_dict()
    if user_id in counts_dict:
        return counts_dict[user_id]
    # if user not exist: 0,now
    return 0,datetime.datetime.now()

def set_count(user_id,count)-> int:
    # Store count in dict (write)
    counts_dict[user_id]=(count,datetime.datetime.now())
    write_count_dict()
    return count

def user_interaction():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    user_id = sign_in(username,password)
    print(f"Welcome, your userid is: {user_id}")
    if user_id is None:
        print("Sorry, something wrong happened.")
        exit()
    
    # user_id is not None

    while True:
        user_count,last_edit = get_count(user_id)

        print(f"Your count is: {user_count}, last_edit : {last_edit}")
        user_choice = input("Do you want to [increase] or [reset] or [exit] ?")
        if user_choice == "increase":
            user_count = set_count(user_id,user_count+1)
        elif user_choice == "reset":
            user_count = set_count(user_id,0)
        elif user_choice == "exit":
            print("Bye Bye")
            exit()
        else:
            print("invalid userchoice")

from flask import Flask, render_template, request, url_for

my_app = Flask(__name__)

@my_app.route('/')
def home():
    return render_template("signin.html",title="Signin")

@my_app.route('/signin/',methods = ['POST'])
def signin_no_username():
    username = request.values.get('username')
    password = request.values.get('password')
    user_id = sign_in(username, password)
    last_count,last_time = get_count(user_id)
    return render_template("counter.html", title="Counter", username=username,user_id=user_id,
    last_count=last_count,last_time=last_time.strftime("%Y%m%d %H:%M:%S")
    )

@my_app.route('/save/<user_id>/<user_count>',methods = ['GET'])
def save(user_id,user_count):
    set_count(str(user_id),int(user_count))
    return datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")

@my_app.route('/reset/<user_id>',methods = ['GET'])
def reset_count(user_id):
    set_count(user_id,0)
    return datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")

if __name__ == "__main__":
    my_app.run()
