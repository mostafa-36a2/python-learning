import pickle
import os
from collections import namedtuple
import re

BkpTuple = namedtuple("BkpTuple", ["dch_name", "type_dir", "bkp_dir"])


def valid_bkp_folder(bkp_folder_name: str):
    """
    Used in get_next_bkp_folder.

    >>> valid_bkp_folder("BKP_2022_12_03_1111111")
    True
    >>> valid_bkp_folder("BKP_2022-12-04_1111111")
    True
    >>> valid_bkp_folder("BKP_20221203_1111111")
    True
    >>> valid_bkp_folder("BKP_20221205_11_11_11")
    True
    >>> valid_bkp_folder("BKP_2022-12-03-1111111")
    True
    >>> valid_bkp_folder("BKP_2022_12_03_11:11:11")
    True
    >>> valid_bkp_folder("BKP_2022_12_03_11_11_11")
    True
    >>> valid_bkp_folder("BKP_2022/12/03_11_11_11")
    False
    >>> valid_bkp_folder("BKP_2022 12 03_11_11_11")
    False
    >>> valid_bkp_folder("BKP-20221203-11_11_11")
    False
    """
    return (
        bool(
            re.match(
                "BKP(_|-)[0-9]{4}(_|-)[0-9]{2}(_|-)[0-9]{2}(_|-).*", bkp_folder_name
            )
        )
        or bool(re.match("BKP_[0-9]{4}-[0-9]{2}-[0-9]{2}_.*", bkp_folder_name))
        or bool(re.match("BKP_[0-9]{8}_.*", bkp_folder_name))
    )


def valid_type_dir(type_dir) -> bool:
    """
    Used in get_next_bkp_folder.

    >>> valid_type_dir("RAP_IN")
    True
    >>> valid_type_dir("RAP_OUT")
    True
    >>> valid_type_dir("NRT_IN")
    True
    >>> valid_type_dir("TAP_OUT")
    True
    >>> valid_type_dir("RAP")
    True
    >>> valid_type_dir("RAPIN")
    False
    >>> valid_type_dir("..")
    False
    >>> valid_type_dir("test_file")
    False
    >>> valid_type_dir("wrong_file")
    False
    >>> valid_type_dir("")
    False
    """
    return bool(re.match("(TAP|RAP|ACK|NRT)_(IN|OUT)", type_dir)) or type_dir == "RAP"



def get_next_bkp_folder(root_path):
    """
    Generator to generate (DCH_NAME, type_dir, bkp_folder) tuple one by one, from the source path
    """
    for dch_name in os.listdir(root_path):
        dch_dir_path = os.path.join(root_path, dch_name)
        for type_dir in os.listdir(dch_dir_path):
            if not valid_type_dir(type_dir):
                print(f"Error, type_dir is invalid '{type_dir}' in {dch_dir_path}")
                continue
            type_dir_path = os.path.join(dch_dir_path, type_dir)
            for bkp_dir in os.listdir(type_dir_path):
                if not valid_bkp_folder(bkp_dir):
                    print(f"Error, bkp_dir is invalid '{bkp_dir}' in {type_dir_path}")
                    continue
                yield BkpTuple(dch_name, type_dir, bkp_dir)
                
old_path = "/home/sighub/sftp_backup"
new_path = "/home/sighub/sftp_backup2"

if not os.path.isfile('data.pkl'):
    generator =  get_next_bkp_folder(old_path)
    # Serialize the generator
    pickle.dump(generator, open('data.pkl', 'wb'))

# De-serialize the generator
generator = pickle.load(open('data.pkl', 'rb'))
generator()