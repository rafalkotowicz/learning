def exchange_money(budget, exchange_rate):
    """
    Calculates how much foreign currency can be received with given budget and exchange rate.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate remaining budget after money exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate total amount received by providing number of bills and their denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    Calculate amount of exchanged bills from given budget and denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    exchange_rate_with_spread = exchange_rate + exchange_rate * (spread / 100)
    max_exchange = budget // exchange_rate_with_spread
    max_exchange_with_denomination = (max_exchange // denomination) * denomination
    return max_exchange_with_denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate non-exchangeable value (additional fee to the except the spread)

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    exchange_rate_with_spread = exchange_rate + exchange_rate * (spread / 100)
    max_exchange = budget // exchange_rate_with_spread
    max_exchange_with_denomination = (max_exchange // denomination) * denomination
    return max_exchange - max_exchange_with_denomination
