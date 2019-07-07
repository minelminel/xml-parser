import os
import csv
from datetime import datetime
from xml.etree import ElementTree as ET


def make_name(fpath):
    """ fpath::absolute path of upload folder """
    file_name = f"converted-file-{datetime.now():%Y-%m-%d-%H-%M}"
    file_path = os.path.join(fpath,file_name)
    return file_name, file_path


def xml_to_list(root):
    """ root::tree.getroot() """
    # get list of all columns
    # for child in root, check if all cols present
    # assign default value if necessary
    # return a list of lists of rows
    pass


def list_to_csv(lists, as_csv):
    """ lists::list of lists to write as rows
        as_csv::asbpath of file to write """
   # open file to write
   # for lst in lists, write row
   # if unable to write, raise error
    pass


# tree = ET.parse(input_file_abspath)
# root = tree.getroot()
# print("root.tag :: {}".format(root.tag))
#
# for child in root:
#     print("child.find() :: {}".format(child.tag))
#     print("child.tag :: {}".format(child.tag))
#     print("child.attrib :: {}".format(child.attrib))
