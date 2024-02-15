from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        "--user",
        type=str,
        dest="user",
        help=f"The user name",
        required=True,
    )
    parser.add_argument(
        "--age",
        type=int,
        dest="age",
        help="The Age for the user",
        required=False,
    )
    
    # Telling the type to be a list will also fail for multiple arguments,
    # but give incorrect results for a single argument.
    parser.add_argument('--files', nargs='+',type=str,dest="files",help="list of files paths [space separated]",required=True)

    arguments = parser.parse_args()

    return arguments.user, arguments.age, arguments.files


user_name, user_age, files = get_arguments()
if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")

user_name, user_age ,_= get_arguments()
if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")

user_name, user_age,_ = get_arguments()

if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")


print("Files: ",files)
