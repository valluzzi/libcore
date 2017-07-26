# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2017 Luzzi Valerio for Gecosistema S.r.l.
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#
# Name:        test_unittest_generator.py
# Purpose:     This file is the unittest of unittest_generator.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")


class test_unittest_generator(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_functions(self):
        """
        test_list_functions
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(list_functions(...) , True)
        # end function

    def test_create_all(self):
        """
        test_create_all
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(create_all(...) , True)
        # end function

    def test_create_unittest(self):
        """
        test_create_unittest
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(create_unittest(...) , True)
        # end function

    def test_setUp(self):
        """
        test_setUp
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(setUp(...) , True)
        # end function

    def test_exists_unittest(self):
        """
        test_exists_unittest
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(exists_unittest(...) , True)
        # end function

    def test_add_unittest(self):
        """
        test_add_unittest
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(add_unittest(...) , True)
        # end function

    def test_test_{fname}(self)

    :
    """
    test_test_{fname}
    - added at 26/07/2017 10:18
    """


# self.assertEqual(test_{fname}(...) , True)
# end function


def test_find_unittest(self):
    """
    test_find_unittest
    - added at 26/07/2017 10:18
    """
    # self.assertEqual(find_unittest(...) , True)
    # end function


def test_remove_unittest(self):
    """
    test_remove_unittest
    - added at 26/07/2017 10:18
    """
    # self.assertEqual(remove_unittest(...) , True)
    # end function

    # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
