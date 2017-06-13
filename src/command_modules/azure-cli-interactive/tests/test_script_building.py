# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import six
from azclishell.util import parse_quotes
from azclishell.gather_commands import GatherCommands

def pass_gather(_):
    pass


GatherCommands.gather_from_files = pass_gather

class ScriptBuildingTest(unittest.TestCase):

    def test_parsing(self):
        pass

    def test_script_build(self):
        pass


if __name__ == '__main__':
    unittest.main()
