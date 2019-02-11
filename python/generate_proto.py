import importlib

import os

print("************1***********")

module_list = []
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith("_pb2.py"):
            module_list.append(os.path.splitext(filename)[0])

print(module_list)


print("*********2*********")


def recursive_function(f, prepend_name, final_list):
    for f in list(f.message_type.fields):
        prepend_name_re = prepend_name + '.' + f.name
        if f.message_type is not None:
            # print("recursive on ",f.name)
            # print(prepend_name_re)
            final_list.append(prepend_name_re)
            recursive_function(f, prepend_name_re, final_list)
            continue
        final_list.append(prepend_name_re)

final_list = []
method = None
for file_name in module_list:

    descriptor_import = importlib.import_module(file_name)

    for i, j in descriptor_import.DESCRIPTOR.extensions_by_name.items():
        head_name = i
        method = j.message_type.name
        # print(head_name)
        # print(method)
    mymethod = getattr(importlib.import_module(file_name), method)
    final_list.append(head_name)

    for f in mymethod.DESCRIPTOR.fields:
        prepend_name_first = head_name + '.' + f.name
        if f.message_type is not None:
            final_list.append(prepend_name_first)
            recursive_function(f, prepend_name_first, final_list)
            continue
        final_list.append(prepend_name_first)

from pprint import pprint
pprint(final_list)