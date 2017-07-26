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
# Name:        test_gdal_shape.py
# Purpose:     This file is the unittest of gdal_shape.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")


class test_gdal_shape(unittest.TestCase):
    def setUp(self):
        pass

    def test_GetFeatures(self):
        """
        test_GetFeatures
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GetFeatures(...) , True)
        # end function

    def test_GetFeatureByFid(self):
        """
        test_GetFeatureByFid
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(GetFeatureByFid(...) , True)
        # end function

    def test_removeShape(self):
        """
        test_removeShape
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(removeShape(...) , True)
        # end function

    def test_SaveFeature(self):
        """
        test_SaveFeature
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(SaveFeature(...) , True)
        # end function

    def test_Extent2shp(self):
        """
        test_Extent2shp
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Extent2shp(...) , True)
        # end function

    def test_XYZ2Shp(self):
        """
        test_XYZ2Shp
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(XYZ2Shp(...) , True)
        # end function

    def test_XYZ2VRT(self):
        """
        test_XYZ2VRT
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(XYZ2VRT(...) , True)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
