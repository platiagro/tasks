import unittest
import sys
import json
# we need import this way just because python can't handle well '-' character in import
sys.path.append("./init-job")

import notebook

TEST_NOTEBOOK_FILEPATH = 'tests/resources/parameters.ipynb'


class TestParameters(unittest.TestCase):

    def test_parameters_reading(self):
        file = open('tests/resources/expected_parameters.json')

        result = notebook.parse_parameters(TEST_NOTEBOOK_FILEPATH)
        expected = json.load(file)

        # variables 'result' and 'expected' are list of dictionaries not a dictionary itself!
        self.assertListEqual(expected, result)

        file.close()
