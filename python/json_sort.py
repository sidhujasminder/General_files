def _order_json(obj):
    if isinstance(obj, dict):
        return sorted((k, _order_json(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(_order_json(x) for x in obj)
    else:
        return obj


def _check_diff(db_value, new_value):
    db_data_dump = json.loads(json.dumps(db_value, cls=JSONEncoder))
    new_content_json = json.loads(json.dumps(new_value, cls=JSONEncoder))
    if _order_json(db_data_dump) == _order_json(new_content_json):
        return JSONDiff(True)
    else:
        return False
