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

    arguments = parser.parse_args()

    return arguments.user, arguments.age


user_name, user_age = get_arguments()
if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")

user_name, user_age = get_arguments()
if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")

user_name, user_age = get_arguments()

if user_age is not None:
    print(f"Welcome to {user_name} with age {user_age}.")
else:
    print(f"We don't know the age for user: {user_name}")
