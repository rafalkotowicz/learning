"""Tests for the dominoes chain builder."""

# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/dominoes/canonical-data.json
# File last updated on 2023-07-19

import unittest

from dominoes import (
    can_chain,
)


class DominoesTest(unittest.TestCase):
    """Validate chain construction correctness for domino sets."""

    def test_empty_input_empty_output(self):
        """Returns an empty chain for empty input."""
        input_dominoes = []
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_singleton_input_singleton_output(self):
        """Returns the single domino when it already closes."""
        input_dominoes = [(1, 1)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_singleton_that_can_t_be_chained(self):
        """Rejects a single non-double domino."""
        input_dominoes = [(1, 2)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_three_elements(self):
        """Builds a valid chain for a simple three-domino cycle."""
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_can_reverse_dominoes(self):
        """Uses orientation reversal when needed."""
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_can_t_be_chained(self):
        """Returns None for non-chainable input."""
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_simple(self):
        """Rejects disconnected components."""
        input_dominoes = [(1, 1), (2, 2)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_double_loop(self):
        """Rejects two disconnected loops."""
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_single_isolated(self):
        """Rejects input with one isolated component."""
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_need_backtrack(self):
        """Finds a chain when backtracking is required."""
        input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_separate_loops(self):
        """Finds a chain across connected subloops."""
        input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_nine_elements(self):
        """Handles larger valid inputs."""
        input_dominoes = [
            (1, 2),
            (5, 3),
            (3, 1),
            (1, 2),
            (2, 4),
            (1, 6),
            (2, 3),
            (3, 4),
            (5, 6),
        ]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_separate_three_domino_loops(self):
        """Rejects disconnected three-domino loops."""
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    # Utility methods

    @staticmethod
    def normalize_dominoes(dominoes):
        """Return normalized domino tuples for multiset comparison."""
        return list(sorted(tuple(sorted(domino)) for domino in dominoes))

    def assert_same_dominoes(self, input_dominoes, output_chain):
        """Assert output uses exactly the input domino multiset."""
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
        output_normal = self.normalize_dominoes(output_chain)
        self.assertEqual(input_normal, output_normal, msg)

    def assert_consecutive_dominoes_match(self, output_chain):
        """Assert adjacent dominoes connect in order."""
        for i in range(len(output_chain) - 1):
            msg = (
                "In chain {}, right end of domino {} ({}) "
                "and left end of domino {} ({}) must match"
            )
            msg = msg.format(
                output_chain, i, output_chain[i], i + 1, output_chain[i + 1]
            )
            self.assertEqual(output_chain[i][1], output_chain[i + 1][0], msg)

    def assert_dominoes_at_ends_match(self, output_chain):
        """Assert first-left equals last-right for closure."""
        msg = (
            "In chain {}, left end of first domino ({}) and "
            "right end of last domino ({}) must match"
        )
        msg = msg.format(output_chain, output_chain[0], output_chain[-1])
        self.assertEqual(output_chain[0][0], output_chain[-1][1], msg)

    def assert_correct_chain(self, input_dominoes, output_chain):
        """Assert output is a valid closed chain using all input dominoes."""
        msg = f"There should be a chain for {input_dominoes}"
        self.assertIsNotNone(output_chain, msg)
        self.assert_same_dominoes(input_dominoes, output_chain)
        if not any(output_chain):
            return
        self.assert_consecutive_dominoes_match(output_chain)
        self.assert_dominoes_at_ends_match(output_chain)

    def refute_correct_chain(self, input_dominoes, output_chain):
        """Assert no valid closed chain exists for input."""
        msg = f"There should be no valid chain for {input_dominoes}"
        self.assertIsNone(output_chain, msg)
