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
# Name:        test_taudem.py
# Purpose:     This file is the unittest of taudem.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")


class test_taudem(unittest.TestCase):
    def setUp(self):
        pass

    def test_PitRemove(self):
        """
        test_PitRemove
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(PitRemove(...) , True)
        # end function

    def test_D8FlowDir(self):
        """
        test_D8FlowDir
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(D8FlowDir(...) , True)
        # end function

    def test_AreaD8(self):
        """
        test_AreaD8
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(AreaD8(...) , True)
        # end function

    def test_Threshold(self):
        """
        test_Threshold
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Threshold(...) , True)
        # end function

    def test_StreamNet(self):
        """
        test_StreamNet
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(StreamNet(...) , True)
        # end function

    def test_SlopeAveDown(self):
        """
        test_SlopeAveDown
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(SlopeAveDown(...) , True)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
