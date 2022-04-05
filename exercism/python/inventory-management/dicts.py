def create_inventory(items: list[str]) -> dict:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    inventory = dict()
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory: dict, items: list[str]) -> dict:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory: dict, items: list[str]) -> dict:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
            else:
                continue
        else:
            continue
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    inventory.pop(item, "Unknown item")
    return inventory


def list_inventory(inventory: dict) -> list:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]
