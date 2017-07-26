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
# Name:        test_gdal_utils.py
# Purpose:     This file is the unittest of gdal_utils.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")


class test_gdal_utils(unittest.TestCase):
    def setUp(self):
        pass

    def test_ProjFrom(self):
        """
        test_ProjFrom
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(ProjFrom(...) , True)
        # end function

    def test_Reproj(self):
        """
        test_Reproj
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Reproj(...) , True)
        # end function

    def test_ReProject(self):
        """
        test_ReProject
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(ReProject(...) , True)
        # end function

    def test_MapToPixel(self):
        """
        test_MapToPixel
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(MapToPixel(...) , True)
        # end function

    def test_GetValueAt(self):
        """
        test_GetValueAt
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GetValueAt(...) , True)
        # end function

    def test_readmssqlstring(self):
        """
        test_readmssqlstring
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(readmssqlstring(...) , True)
        # end function

    def test_GDAL_SIZE(self):
        """
        test_GDAL_SIZE
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GDAL_SIZE(...) , True)
        # end function

    def test_GDAL_META(self):
        """
        test_GDAL_META
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GDAL_META(...) , True)
        # end function

    def test_GDAL_QUERY(self):
        """
        test_GDAL_QUERY
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GDAL_QUERY(...) , True)
        # end function

    def test_GDAL2Numpy(self):
        """
        test_GDAL2Numpy
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GDAL2Numpy(...) , True)
        # end function

    def test_Numpy2GTiff(self):
        """
        test_Numpy2GTiff
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Numpy2GTiff(...) , True)
        # end function

    def test_Numpy2AAIGrid(self):
        """
        test_Numpy2AAIGrid
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Numpy2AAIGrid(...) , True)
        # end function

    def test_Numpy2Gdal(self):
        """
        test_Numpy2Gdal
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Numpy2Gdal(...) , True)
        # end function

    def test_GetNoData(self):
        """
        test_GetNoData
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GetNoData(...) , True)
        # end function

    def test_StreamBurning(self):
        """
        test_StreamBurning
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(StreamBurning(...) , True)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
