"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add) -> dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes) -> dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates: dict) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    ready_to_send = dict()
    for k, v in cart.items():
        ready_to_send[k] = list([v, *aisle_mapping[k]])

    return dict(sorted(ready_to_send.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    new_inventory = store_inventory.copy()
    for k, v in fulfillment_cart.items():
        new_inventory[k][0] = store_inventory[k][0] - fulfillment_cart[k][0]
        if new_inventory[k][0] == 0:
            new_inventory[k][0] = 'Out of Stock'

    return new_inventory
