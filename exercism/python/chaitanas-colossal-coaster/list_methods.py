"""Chaitana's Colossal Coaster

Chaitana owns a very popular theme park. She only has one ride in the very center of beautifully
landscaped grounds: The Biggest Roller Coaster in the World(TM). Although there is only this one
attraction, people travel from all over the world and stand in line for hours for the opportunity
to ride Chaitana's hypercoaster.

There are two queues for this ride, each represented as a list:

Normal Queue
Express Queue (also known as the Fast-track) - where people pay extra for priority access.

You have been asked to write some code to better manage the guests at the park. You need to implement
the following functions as soon as possible before the guests (and your boss, Chaitana!) get cranky.
"""


def add_me_to_the_queue(express_queue: list[str], normal_queue: list[str], ticket_type: int,
                        person_name: str) -> list[str]:
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    updated_list = []
    if ticket_type == 0:
        updated_list = normal_queue.copy()
    elif ticket_type == 1:
        updated_list = express_queue.copy()

    updated_list.append(person_name)
    return updated_list


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    return sorted(queue)
