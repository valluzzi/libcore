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
# Name:        test_gdal_wrappers.py
# Purpose:     This file is the unittest of gdal_wrappers.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")


class test_gdal_wrappers(unittest.TestCase):
    def setUp(self):
        pass

    def test_gdalwarp(self):
        """
        test_gdalwarp
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdalwarp(...) , True)
        # end function

    def test_gdal_grid(self):
        """
        test_gdal_grid
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_grid(...) , True)
        # end function

    def test_gdal_crop(self):
        """
        test_gdal_crop
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_crop(...) , True)
        # end function

    def test_gdal_nodata(self):
        """
        test_gdal_nodata
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_nodata(...) , True)
        # end function

    def test_gdal_mosaic(self):
        """
        test_gdal_mosaic
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_mosaic(...) , True)
        # end function

    def test_gdal_translate(self):
        """
        test_gdal_translate
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_translate(...) , True)
        # end function

    def test_gdal_rasterize(self):
        """
        test_gdal_rasterize
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_rasterize(...) , True)
        # end function

    def test_gdal_lzw(self):
        """
        test_gdal_lzw
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(gdal_lzw(...) , True)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
