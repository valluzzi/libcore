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
# Name:        test_filesystem.py
# Purpose:     This file is the unittest of filesystem.py
#
# Author:      Luzzi Valerio
#
# Created:     26/07/2017
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.append("../..")
from gecosistema_lite import *


class test_filesystem(unittest.TestCase):
    def setUp(self):
        pass

    def test_isWindows(self):
        """
        test_isWindows
        - added at 26/07/2017 10:18
        """
        self.assertEqual(isWindows(), os.path.isfile("c:/windows/system32/drivers/etc/hosts"))
        # end function

    def test_isLinux(self):
        """
        test_isLinux
        - added at 26/07/2017 10:18
        """
        self.assertEqual(isLinux(), os.path.isfile("/etc/hosts"))
        # end function

    def test_isMac(self):
        """
        test_isMac
        - added at 26/07/2017 10:18
        """
        self.assertEqual(isMac(), os.path.isfile("/etc/hosts"))
        # end function

    def test_file(self):
        """
        test_file
        - added at 26/07/2017 10:18
        """
        self.assertTrue(file("c:/windows/system32/drivers/etc/hosts"))
        # end function

    def test_directory(self):
        """
        test_directory
        - added at 26/07/2017 10:18
        """
        self.assertTrue(directory("c:/windows/system32/drivers/etc"))
        # end function

    def test_normpath(self):
        """
        test_normpath
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(normpath(...) , True)
        # end function

    def test_justdrive(self):
        """
        test_justdrive
        - added at 26/07/2017 10:18
        """
        self.assertEqual(justdrive("c:/hello.world"), "c:")
        self.assertEqual(justdrive("c:\\hello.world"), "c:")
        self.assertEqual(justdrive("/hello/world"), "")
        # end function

    def test_justpath(self):
        """
        test_justpath
        - added at 26/07/2017 10:18
        """
        self.assertEqual(justpath("c:/hello/world/test.txt"), "c:/hello/world")
        # end function

    def test_justfname(self):
        """
        test_justfname
        - added at 26/07/2017 10:18
        """
        self.assertEqual(justfname("c:/hello/world/test.txt"), "test.txt")
        # end function

    def test_juststem(self):
        """
        test_juststem
        - added at 26/07/2017 10:18
        """
        self.assertEqual(juststem("c:/hello/world/test.txt"), "test")
        # end function

    def test_justext(self):
        """
        test_justext
        - added at 26/07/2017 10:18
        """
        self.assertEqual(justext("c:/hello/world/test.txt"), "txt")
        # end function

    def test_forceext(self):
        """
        test_forceext
        - added at 26/07/2017 10:18
        """
        self.assertEqual(forceext("test.txt", "tif"), "test.tif")
        # end function

    def test_name_without_ext(self):
        """
        test_name_without_ext
        - added at 26/07/2017 10:18
        """
        self.assertEqual(name_without_ext("c:/hello/world/test.txt"), "c:/hello/world/test")
        # end function

    def test_remove_suffix(self):
        """
        test_remove_suffix
        - added at 26/07/2017 10:18
        """
        self.assertEqual(remove_suffix("c:/hello/world/dem.fel", "fel"), "c:/hello/world/dem")
        # end function

    def test_strtofile(self):
        """
        test_strtofile
        - added at 26/07/2017 10:18
        """
        self.assertEqual(strtofile("hello world", "hello.world"), "hello.world")
        # end function

    def test_filetostr(self):
        """
        test_filetostr
        - added at 26/07/2017 10:18
        """
        self.assertEqual(filetostr("hello.world"), "hello world")
        # end function

    def test_filetoarray(self):
        """
        test_filetoarray
        - added at 26/07/2017 10:18
        """
        self.assertEqual(filetoarray("hello.world"), ["hello world"])
        # end function

    def test_filesize(self):
        """
        test_filesize
        - added at 26/07/2017 10:18
        """
        self.assertEqual(filesize("hello.world"), len("hello world"))
        # end function

    def test_rename(self):
        """
        test_rename
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(rename(...) , True)
        # end function

    def test_remove(self):
        """
        test_remove
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(remove(...) , True)
        # end function

    def test_mkdirs(self):
        """
        test_mkdirs
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(mkdirs(...) , True)
        # end function

    def test_chdir(self):
        """
        test_chdir
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(chdir(...) , True)
        # end function

    def test_ls(self):
        """
        test_ls
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(ls(...) , True)
        # end function

    def test_tempdir(self):
        """
        test_tempdir
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(tempdir(...) , True)
        # end function

    def test_tempname(self):
        """
        test_tempname
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(tempname(...) , True)
        # end function

    def test_Desktop(self):
        """
        test_Desktop
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Desktop(...) , True)
        # end function

    def test_Home(self):
        """
        test_Home
        - added at 26/07/2017 10:18
        """
        # self.assertEqual(Home(...) , True)
        # end function

    def test_md5sum(self):
        """
        test_md5sum
        - added at 26/07/2017 10:18
        """
        self.assertEqual(md5sum("hello.world"), "5eb63bbbe01eeed093cb22bb8f5acdc3")
        # end function

    def test_filehaschanged(self):
        """
        test_filehaschanged
        - added at 26/07/2017 10:18
        """
        self.assertEqual(filehaschanged("hello.world", '', True), False)
        # end function

        # <!-- new testcase here -->


if __name__ == "__main__":
    unittest.main()
