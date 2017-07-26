# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2017 Luzzi Valerio
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
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
# Name:        exec
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     27/12/2012
# -------------------------------------------------------------------------------
"""apt install mpich"""

import datetime
import subprocess

from filesystem import *


def Exec(command, env={}, precond=[], postcond=[], remove=[], skipIfExists=False, nowait=False, verbose=False):
    """
    Exec
    """
    t1 = datetime.datetime.now()
    res = True

    if skipIfExists:
        # check post conditions
        for filename in postcond:
            if not os.path.isfile(filename):
                res = False
                break
        if res:
            t2 = datetime.datetime.now()
            if verbose:
                command = sformat(command, env)
                print "Post conditions already fulfilled for %s[...]!" % command[:12]
                print "Done in %ss." % ((t2 - t1).total_seconds())
            return res

    res = True
    # check pre conditions (file existence)
    for filename in listify(precond):
        if not os.path.isfile(filename):
            res = False
            break
    if verbose:
        print sformat(command, env)
    if res:

        if isWindows():
            command = sformat(command, env)
            args = command
        else:
            command = command.replace('"{', '{').replace('}"', '}')
            command = sformat(command, env)
            command = normalizestring(command)
            args = listify(command, " ", '"')
        if nowait:
            subprocess.Popen(args)
        else:
            subprocess.call(args, shell=False)
    # check post conditions
    for filename in listify(postcond):
        if verbose:
            print "Checking post conditions:%s" % filename
        if not os.path.isfile(filename):
            res = False
            break
    # remove temporary files
    for filename in listify(remove):
        if verbose:
            print "removing temp file:%s" % filename
        if os.path.isfile(filename):
            os.remove(filename)
    t2 = datetime.datetime.now()
    if verbose:
        print "Done in %ss." % ((t2 - t1).total_seconds())
    return res


def mpiexec(command, env={}, n=0, precond=[], postcond=[], remove=[], skipIfExists=False, verbose=False):
    """
    mpiexec
    """
    if n <= 0:
        n = os.environ["NUMBER_OF_PROCESSOR"] if os.environ.has_key("NUMBER_OF_PROCESSOR") else 1

    if isWindows():
        if Exec("mpiexec"):
            env["__mpiexe__"] = "mpiexec"
        elif os.environ.has_key("MSMPI_BIN"):
            env["__mpiexe__"] = os.environ["MSMPI_BIN"] + "\\mpiexec.exe"
        else:
            print "Warning: may be mpiexec is not installed!"
            n = 1

    env["__n__"] = n
    if n > 1:
        if isWindows():
            command = """"{__mpiexe__}" -n {__n__} """ + command
        else:
            command = """mpiexec -n {__n__} """ + command
    if Exec(command, env, precond, postcond, remove, skipIfExists, False, verbose):
        return postcond[0] if len(postcond) == 1 else tuple(postcond)
    return False


def Python(command, env={}, precond=[], postcond=[], remove=[], skipIfExists=False, verbose=False):
    """
    Python
    """
    return Exec("python " + command, env, precond, postcond, remove, skipIfExists, False, verbose)


if __name__ == '__main__':
    a = mpiexec("gdalinfo")
    print a, type(a)
