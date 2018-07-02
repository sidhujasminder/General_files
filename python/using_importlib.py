import os
# import json
# 
# # from api_server.controllers import (configuration, data, event, files,
# #                                         health_tree, notification,
# #                                         override, playbook, rule, inspect)
# import inspect
# 
# def _get_all_functions():
# 
#     try:
#         with open('external_api.json') as f:
#             data = json.load(f)
# 
#         list_all_functions = []
# 
#         for swag_def in list(data['paths'].values()):
#             if swag_def.get('get'):
#                 list_all_functions.append(swag_def['get']['operationId'].replace('-','_'))
#             if swag_def.get('post'):
#                 list_all_functions.append(swag_def['post']['operationId'].replace('-','_'))
#             if swag_def.get('put'):
#                 list_all_functions.append(swag_def['put']['operationId'].replace('-','_'))
#             if swag_def.get('delete'):
#                 list_all_functions.append(swag_def['delete']['operationId'].replace('-','_'))
#         return list_all_functions
#     except Exception as exc:
#         err = '{}: {}'.format(type(exc).__name__, exc)
#         print(err)
# 
# def create_router_file():
#     """
#     This function generates the controller file router.py using the
#     definitions from external_api.json file.
#     """
#     import importlib
# 
#     # all_controllers = [configuration, data, event, files, health_tree, playbook, inspect, notification, override, rule]
#     results = []
#     processed = set()
#     controller_path = ['controllers']
#     all_files = os.listdir('/Users/jasminder/testing_jfit/env/jfit-api-server/api_server/controllers')
#     os.chdir('/Users/jasminder/testing_jfit/env/jfit-api-server/')
#     my_import = importlib.import_module('api_server.controllers.data')
#     func_list = _get_all_functions()
#     
#     
#     with open('router.py', 'w+') as f:
#         f.write("""from api_server.controllers import (configuration, data, event, files,
#                                         health_tree, inspect, notification,
#                                         override, playbook, rule)\n\n""")
#         for a in all_controllers:
#             y = os.path.basename(a.__file__)
#             x = inspect.getmembers(a, predicate=inspect.isfunction)
#             for i in x:
#                 pair = (i[0], y.rstrip(".py"))  # function and file name
#                 if i[0] in func_list:
#                     results.append(pair)
#                     processed.add(i[0])
#         not_found = set(func_list) - set(processed)
#         if len(not_found):
#             print(not_found)
#         results.sort(key=lambda one: one[0])
#         for val in results:
#             f.write(val[0] + " = " + val[1] + '.' + val[0])
#             f.write("\n")
# 
# create_router_file()




import os
import json
import inspect

source_dir = os.getenv("PYTHONPATH")
api_server_src = os.path.join(source_dir, 'api_server')
external_api_file = os.path.join(source_dir, 'external_api.json')
tmp_router_file = os.path.join(source_dir, 'scripts', 'tmp', 'router.py')


def _get_all_functions():
    """
    Get all the functions called as per request.
    Function name is value of the key operationID in external_api.json

    :return: list of all functions defined in external_api.json
    """
    try:
        with open(external_api_file) as f:
            data = json.load(f)

        list_all_functions = []

        for swag_def in list(data['paths'].values()):
            if swag_def.get('get'):
                list_all_functions.append(swag_def['get']['operationId'].replace('-', '_'))
            if swag_def.get('post'):
                list_all_functions.append(swag_def['post']['operationId'].replace('-', '_'))
            if swag_def.get('put'):
                list_all_functions.append(swag_def['put']['operationId'].replace('-', '_'))
            if swag_def.get('delete'):
                list_all_functions.append(swag_def['delete']['operationId'].replace('-', '_'))
        return list_all_functions
    except Exception as exc:
        err = '{}: {}'.format(type(exc).__name__, exc)
        print(err)


def create_router_file():
    """
    This function generates the controller file router.py using the
    definitions from external_api.json file.
    """
    import importlib
    results = []
    processed = set()
    controller_path = ['controllers']
    func_list = _get_all_functions()
    with open(tmp_router_file, 'w+') as f1:
        f1.write("""from api_server.controllers import (configuration, data, event, files,
                                        health_tree, inspect, notification,
                                        override, playbook, rule)\n\n""")

        for ctrl in controller_path:
            all_files = os.listdir(os.path.join(api_server_src, ctrl))
            exclude_files = ['__init__.py', 'router.py']

            for f in all_files:
                if '.py' in f and f not in exclude_files:
                    my_import = importlib.import_module('api_server.{0}.{1}'.format(ctrl, f.rstrip(".py")))
                    y = f.rstrip(".py")  # Module name
                    x = inspect.getmembers(my_import, predicate=inspect.isfunction)
                    for i in x:
                        pair = (i[0], y.rstrip(".py"))  # function and file name
                        if i[0] in func_list:
                            results.append(pair)
                            processed.add(i[0])
        not_found = set(func_list) - set(processed)
        if len(not_found):
            print(not_found)
        results.sort(key=lambda one: one[0])
        for val in results:
            f1.write(val[0] + " = " + val[1] + '.' + val[0])
            f1.write("\n")

create_router_file()

