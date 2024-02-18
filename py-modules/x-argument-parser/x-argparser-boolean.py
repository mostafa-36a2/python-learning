from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser()

    parser.add_argument(
        "--flag",
        default=False,
        dest="flag",
        action="store_true",
        help="Flag to enable something",
    )

    parser.add_argument(
        "--disable-something",
        default=True,
        dest="disable_sth",
        action="store_false",
        help="Flag to enable something",
    )

    arguments = parser.parse_args()

    return arguments.flag, arguments.disable_sth


flag, diable_sth = get_arguments()

print("Flag value:", flag)
print("diable_sth value:", diable_sth)
