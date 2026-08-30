---
name: solve-python-exercism
description: Use when implementing Python Excersim Exercise solution
---

# Solve Python Excersim exercise

## Overview

Implement the excerse solution in Python using TDD approach. Tests are already provided. Finished code must pass 
all tests and meet linter requirements.

## Execution order
* Download exercise from exercism.org (visit provided URL), search for `exercism download --track=python --exercise=<exercise_name>`, e.g. `exercism download --track=python --exercise=bowling`
* Working dir is the directory where exercise was downloaded, e.g. "C:\Users\rafal\PycharmProjects\learning\exercism\python\bowling"
* Implement target exercise
* Custom Linter: "check for C0104 disallowed-name, 1-2 letter long variables are forbidden"
* Run unit tests and fix issues
* Run linter and fix issues
* Run unit tests and fix issues
* Run linter 2 and fix issues
* Run unit tests and fix issues
* If linters are in conflict, prefer pylint over ruff
* Submit code to exercism.org using `exercism submit <exercise_name>.py`, e.g. `exercism submit bowling.py`
* Prepare commit message to align with pattern [Exercism][Python][<exercise_name_camelcase>] Done: <exercise_url> e.g. * [Exercism][Python][Bowling] Done: https://exercism.org/tracks/python/exercises/bowling
* Add test and linters results to the proposed commit message 

## Tools and standard
* Tests: unittest
* Linter pylint: pylint with the following plugins:
  * pylint.extensions.bad_builtin
  * pylint.extensions.broad_try_clause
  * pylint.extensions.check_elif
  * pylint.extensions.code_style
  * pylint.extensions.comparison_placement
  * pylint.extensions.confusing_elif
  * pylint.extensions.consider_refactoring_into_while_condition
  * pylint.extensions.consider_ternary_expression
  * pylint.extensions.dict_init_mutate
  * pylint.extensions.docparams
  * pylint.extensions.docstyle
  * pylint.extensions.dunder
  * pylint.extensions.empty_comment
  * pylint.extensions.eq_without_hash
  * pylint.extensions.for_any_all
  * pylint.extensions.magic_value
  * pylint.extensions.mccabe
  * pylint.extensions.no_self_use
  * pylint.extensions.overlapping_exceptions
  * pylint.extensions.private_import
  * pylint.extensions.redefined_loop_name
  * pylint.extensions.redefined_variable_type
  * pylint.extensions.set_membership
  * pylint.extensions.typing
  * pylint_celery
  * pylint_pydantic
* Linter pylint: with the following options:
  * --enable=all
  * --score=y
  * --reports=y
* Linter ruff: ruff check

## Expected outcome
* First summary of implementation with test statistic and linter score/results
* Explaining code and design decisions
* Ask human partner for further explanation 



