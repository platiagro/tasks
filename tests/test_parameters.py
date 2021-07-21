import unittest
import sys
import json

# we need import this way just because python can handle well '-' character in import
sys.path.append("./init-job")

import notebook 

class TestParameters(unittest.TestCase):

    def test_parameters_reading(self):
        a = notebook.parse_parameters('tests/resources/parameters.ipynb')
        
        j = json.loads( 'tests/resources/expected_parameters.json')
        print(j)        
        
        
        print(a)

       