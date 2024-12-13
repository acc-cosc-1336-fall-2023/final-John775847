import unittest

from src.question_a.question_a import test_config
from src.question_b.question_b import get_most_likely_ancestor_consensus
from src.question_c.question_c import create_mulitiplication_table

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus(self):
        self.assertEqual((2, 4, 10), get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT"))

    def test_create_mulitiplication_table(self):
        self.assertEqual([0, 1, 2, "\n", 1, 1, 2, "\n", 2, 2, 4, "\n"], create_mulitiplication_table(2, 2))
