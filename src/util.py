import os
import csv
from datetime import datetime
from xml.etree import ElementTree as ET


def make_name(fpath):
    file_name = f"converted-file-{datetime.now():%Y-%m-%d-%H-%M}"
    file_path = os.path.join(fpath,file_name)
    return file_name, file_path


def xml_to_list(root):
    pass


def list_to_csv(lists):
    pass




# input_file = "plant_catalog.xml"
# output_file = ""
#
#
# tree = ET.parse(input_file)
# root = tree.getroot()
# print("root.tag :: {}".format(root.tag))
#
# for child in root:
#     print("child.find() :: {}".format(child.tag))
#     print("child.tag :: {}".format(child.tag))
#     print("child.attrib :: {}".format(child.attrib))
