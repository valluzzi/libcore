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
# Name:        test_execution.py
# Purpose:     This file is the unittest of execution.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")
from gecosistema_lite import *


class test_execution(unittest.TestCase):
    def setUp(self):
        pass

    def test_Exec(self):
        """
        test_Exec
        - added at 26/07/2017 10:18
        """
        self.assertEqual(Exec("gdalinfo"), True)
        # end function

    def test_mpiexec(self):
        """
        test_mpiexec
        - added at 26/07/2017 10:18
        """
        self.assertEqual(mpiexec("gdalinfo"), ())
        # end function

    def test_Python(self):
        """
        test_Python
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Python(...) , True)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
