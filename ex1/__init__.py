def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    elements = [1,]
    for category_id in mapping["categoryIdsSorted"]:
        id = "category-" + category_id
        text = mapping["categories"][category_id]["name"]
        items = [{"id": i, "text": mapping["roles"][i]["name"]} for i in mapping["categories"][category_id]["roleIds"]]
        element = {"id": id, "text": text, "items": items}
        elements.append(element)

    return {'categories': elements}



