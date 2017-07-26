# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2017 Luzzi Valerio
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
# Name:        strings.py
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     27/12/2012
# -------------------------------------------------------------------------------
import binascii
import hashlib
import re


def lower(text):
    """
    lower
    """
    if isstring(text):
        return text.lower()
    elif isarray(text):
        return [lower(item) for item in text]
    return ""


def upper(text):
    """
    upper
    """
    if isstring(text):
        return text.upper()
    elif isarray(text):
        return [upper(item) for item in text]
    return ""


def padr(text, n, c):
    """
    padr - right pad of text with character c
    """
    text = str(text)
    return text + str(c) * (n - len(text))


def padl(text, n, c):
    """
    left pad of text with character c
    """
    text = str(text)
    return str(c) * (n - len(text)) + text


def ltrim(text, toremove):
    """
    ltrim - left trim
    """
    toremove = toremove[0]
    if isstring(text):
        return text.lstrip(toremove)
    elif isarray(text):
        return [ltrim(item, toremove) for item in text if len(item) > 0]
    return text


def chrtran(text, tosearch, toreplace):
    """
    chrtran
    """
    for j in range(0, len(tosearch)):
        c = toreplace[j] if j in range(0, len(toreplace)) else ""
        text = text.replace(tosearch[j], c)
    return text


def sformat(text, args):
    """
    sformat
    """
    for key in args:
        text = text.replace("{%s}" % key, "%s" % (args[key]))
    return text


def startswith(text, elenco, casesensitive=True):
    """
    startswith - Returns True if the text starts with one of ...
    """
    for item in listify(elenco, ","):
        if casesensitive:
            if text.startswith(item):
                return True
        else:
            if text.lower().startswith(item.lower()):
                return True
    return False


def endswith(text, elenco, casesensitive=True):
    """
    endswith - Returns True if the text ends with one of ...
    """

    for item in listify(elenco, ","):
        if casesensitive:
            if text.endswith(item):
                return True
        else:
            if text.lower().endswith(item.lower()):
                return True
    return False


def leftpart(text, sep):
    """
    leftpart
    """
    if isstring(text):
        arr = text.split(sep, 1)
        if len(arr) >= 1:
            return arr[0]
    elif isarray(text):
        return [leftpart(item, sep) for item in text]


def rightpart(text, sep):
    """
    rightpart
    """
    if isstring(text):
        arr = text.split(sep, 1)
        if len(arr) > 1:
            return arr[1]
    elif isarray(text):
        return [rightpart(item, sep) for item in text]
    return ""


def textin(text, prefix, postfix, casesensitive=True):
    """
    textin - return text between prefix and suffix excluded
    """
    if casesensitive:
        g = re.search(r'(?<=' + prefix + ')(.*?)(?=' + postfix + ')', text)
    else:
        g = re.search(r'(?<=' + prefix + ')(.*?)(?=' + postfix + ')', text, re.IGNORECASE)

    return g.group() if g else ""


def textbetween(text, prefix, postfix, casesensitive=True):
    """
    textin - return text between prefix and suffix excluded
    """
    if casesensitive:
        g = re.search(r'' + prefix + '(.*?)' + postfix, text)
    else:
        g = re.search(r'' + prefix + '(.*?)' + postfix, text, re.IGNORECASE)

    return g.group() if g else ""


def normalizestring(text):
    """
    normalizestring
    """
    return re.sub(r'\s+', ' ', text);


def wrap(text, leftc, rightc=False):
    """
    wrap
    """
    if isstring(text):
        rightc = leftc if not rightc else rightc
        return leftc + text + rightc
    elif isarray(text):
        return [wrap(item, leftc, rightc) for item in text]


def unwrap(text, leftc, rightc=False):
    """
    unwrap
    """
    if isstring(text):
        rightc = leftc if not rightc else rightc
        start = len(leftc)
        end = len(rightc)
        while text.startswith(leftc) and text.endswith(rightc):
            text = text[start:-end]
        return text
    elif isarray(text):
        return [unwrap(item, leftc, rightc) for item in text]


def split(text, sep=" ", glue="'", removeEmpty=False):
    """
    split - a variant of split with glue characters
    """
    res = []
    word = ""
    dontsplit = False
    for j in range(0, len(text)):
        c = text[j]
        if c in glue:
            dontsplit = not dontsplit
        if c in sep and not dontsplit:
            res.append(word)
            word = ""
        else:
            word += c

    if not removeEmpty or len(word.strip()) > 0:
        res.append(word)

    return res


def density(text, chars=None):
    """
    density
    Returns the list of char ordered by density
    """
    dic = {}
    chars = set(text) & set(chars) if chars else set(text)
    for c in text:
        if c in chars:
            dic[c] = 1 if not dic.has_key(c) else dic[c] + 1
    dic = (sorted(dic.items(), key=lambda x: x[1], reverse=True))
    dic = [key for (key, value) in dic]
    return dic


def listify(text, sep=",", glue="\""):
    """
    listify -  make a list from string
    """
    if text is None:
        return []
    elif isstring(text):
        if not sep:
            sep = density(text, ",;|: \t\n\r")
            sep = sep[0] if sep else ","
        return split(text, sep, glue, removeEmpty=True)
    elif isarray(text):
        return text
    return [text]


def isstring(var):
    """
    isstring - Returns True if the variable is a string
    """
    return isinstance(var, (str, unicode))


def isarray(var):
    """
    isarray - Returns True if the variable is a list
    """
    return isinstance(var, (list, tuple))


def isnumeric(text):
    """
    isnumeric - a simple implementation
    (TODO: numbers with exponent)
    """
    text = text.strip()
    dot = False
    for i in range(0, len(text)):
        c = text[i]
        if i == 0 and c in "+-":
            continue
        if c == "." and not dot:
            dot = True
            continue
        if not c.isdigit():
            return False
    return True


def val(text):
    """
    val - parse the text value
    """
    if text is None:
        return None
    elif isinstance(text, int):
        return text
    elif isinstance(text, float):
        return text
    # Se e' una stringa e c'e' possibilita' che sia un numero
    elif isstring(text):

        if text == "":
            return 0

        match = re.match("[-+]?(\d+(\.\d*)|\.\d+)([eE][-+]?\d+)?", text)
        if match:
            return float(match.group())
        match = re.match("[-+]?\d+", text)
        if match:
            return int(match.group())

        return None
    # Se e' una lista applico val a ogni singolo elemento
    elif isarray(text):
        return [val(item) for item in text]

    return None


def md5text(text):
    """
    md5text - Returns the md5 of the text
    """
    ##print  md5.new(text).hexdigest()
    hash = hashlib.md5()
    hash.update(text)
    return hash.hexdigest()


def crc32text(text):
    """
    crc32text - Returns the crc2
    """
    return binascii.crc32(text) & 0xffffffff


if __name__ == '__main__':
    print textin("hello <h1>world  are</h1> you<h1>how</h1>", "<h1>", "</h1>")
    print textbetween("hello <h1>world  are</h1> you<h1>how</h1>", "<h1>", "</h1>")
    print normalizestring("hello     world    SELECT  hello from   table;")
