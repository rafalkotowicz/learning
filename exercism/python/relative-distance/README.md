# Relative Distance

Welcome to Relative Distance on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Introduction

You've been hired to develop **Noble Knots**, the hottest new dating app for nobility!
With centuries of royal intermarriage, things have gotten… _complicated_.
To avoid any _oops-we're-twins_ situations, your job is to build a system that checks how closely two people are related.

Noble Knots is inspired by Iceland's "[Islendinga-App][islendiga-app]," which is backed up by a database that traces all known family connections between Icelanders from the time of the settlement of Iceland.
Your algorithm will determine the **degree of separation** between two individuals in the royal family tree.

Will your app help crown a perfect match?

[islendiga-app]: https://web.archive.org/web/20250816223614/http://www.islendingaapp.is/information-in-english/

## Instructions

Your task is to determine the degree of separation between two individuals in a family tree.
This is similar to the pop culture idea that every Hollywood actor is [within six degrees of Kevin Bacon][six-bacons].

- You will be given an input, with all parent names and their children.
- Each name is unique, a child _can_ have one or two parents.
- The degree of separation is defined as the shortest number of connections from one person to another.
- If two individuals are not connected, return a value that represents "no known relationship."
  Please see the test cases for the actual implementation.

## Example

Given the following family tree:

```text
      ┌──────────┐            ┌──────────┐     ┌───────────┐
      │  Helena  │            │  Erdős   ├─────┤  Shusaku  │
      └───┬───┬──┘            └─────┬────┘     └────┬──────┘
      ┌───┘   └───────┐             └───────┬───────┘
┌─────┴────┐     ┌────┴───┐           ┌─────┴────┐
│   Isla   ├─────┤ Tariq  │           │   Kevin  │
└────┬─────┘     └────┬───┘           └──────────┘
     │                │
┌────┴────┐      ┌────┴───┐
│   Uma   │      │ Morphy │
└─────────┘      └────────┘
```

The degree of separation between Tariq and Uma is 2 (Tariq → Isla → Uma).
There's no known relationship between Isla and Kevin, as there is no connection in the given data.
The degree of separation between Uma and Isla is 1.

~~~~exercism/note
Isla and Tariq are siblings and have a separation of 1.
Similarly, this implementation would report a separation of 2 from you to your father's brother.
~~~~

[six-bacons]: https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon

## How this exercise is structured for the Python track

The tests for this exercise expect your solution to be implemented as a RelativeDistance `class` in Python.
If you are unfamiliar with `class`es in Python, [concept:python/classes]() and [`classes` in the official Python documentation][classes in python] are good places to start.


`RelativeDistance` should be initialized (_see [`__init__()`][init] for more information_) using `family_tree`, a dictionary where the `keys` are individuals and `values` are `list`s of that individual's children.
You will also need to implement a `degree_of_separation` [method][methods] which will return the degree of separation between `person_a` and `person_b` who are individuals in the passed-in family tree.


You are given a stubbed implementation for the `__init__` [special method][special-methods] used to create an instance of the `RelativeDistance` class, as well as a stub of the `degree_of_separation` method.
First, you will need to customize the `__init__` with an appropriate attribute on `self` (_the instance_) to represent the `family_tree` data.
Then you can add your logic to the `degree_of_separation` method to calculate the degree of separation between `person_a` and `person_b`.


## Exception messages

Sometimes it is necessary to [raise an exception][raising-exceptions].
When you do this, you should always include a **meaningful error message** to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types][base-error-classes], but should still include a meaningful message.

This particular exercise requires that you use the [raise statement][raise-statement] to "throw" multiple `ValueError`s.
In the first scenario, you will need to raise a `ValueError` when either one or both of the people passed to the `RelativeDistance.degree_of_separation` method are not present in the family tree.

```python
# Example when Person A is not in the tree.
raise ValueError("Person A not in family tree.")
```

If both people are present in the family tree, you will need to raise a `ValueError` when there is no valid connection between them as defined by the rules.

```python
# Example when there are no valid connections.
raise ValueError("No connection between person A and person B.")
```

The tests will only pass if you both `raise` the expected `exception` type and include the expected message with it.
Please check the tests and their expected results carefully, as these instructions are not exhaustive.

[base-error-classes]: https://docs.python.org/3/library/exceptions.html#base-classes
[classes in python]: https://docs.python.org/3/tutorial/classes.html
[init]: https://docs.python.org/3/reference/datamodel.html#object.__init__
[methods]: https://docs.python.org/3/tutorial/classes.html#class-definition-syntax
[raising-exceptions]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[special-methods]: https://docs.python.org/3.11/reference/datamodel.html#special-method-names

## Source

### Created by

- @BNAndras

### Based on

vaeng - https://github.com/exercism/problem-specifications/pull/2537