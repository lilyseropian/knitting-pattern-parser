"""E2E tests for the parser."""

import os
import sys
import unittest

sys.path.append(os.path.join('..', 'classes'))
from pattern import *

sys.path.append(os.path.join('..', ''))
import knitparser

sys.path.append(os.path.join('.', 'test_files'))
import scarf_beginner
import scarf_intermediate
import scarf_advanced

class TestParser(unittest.TestCase):
    """Test the parser using real patterns."""

    def test_beginner_pattern(self):
        pattern_tree = scarf_beginner.PATTERN

        with open('test_files/scarf_beginner.txt') as pattern_file:
            pattern = pattern_file.read()
            parsed_pattern = knitparser.parse(pattern)
            self.assertEqual(pattern_tree, parsed_pattern)

    def test_intermediate_pattern(self):
        pattern_tree = scarf_intermediate.PATTERN

        with open('test_files/scarf_intermediate.txt') as pattern_file:
            pattern = pattern_file.read()
            parsed_pattern = knitparser.parse(pattern)
            self.assertEqual(pattern_tree, parsed_pattern)

    def test_advanced_pattern(self):
        pattern_tree = scarf_advanced.PATTERN

        with open('test_files/scarf_advanced.txt') as pattern_file:
            pattern = pattern_file.read()
            parsed_pattern = knitparser.parse(pattern)
            self.assertEqual(pattern_tree, parsed_pattern)

if __name__ == '__main__':
    unittest.main()