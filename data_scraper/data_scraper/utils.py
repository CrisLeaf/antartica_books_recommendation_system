def replace_iso(string):
    string = string.replace("\u00e0", "a")
    string = string.replace("\u00e1", "a")
    string = string.replace("\u00e2", "a")
    string = string.replace("\u00e3", "a")
    string = string.replace("\u00e4", "a")
    string = string.replace("\u00e5", "a")
    string = string.replace("\u00e8", "e")
    string = string.replace("\u00e9", "e")
    string = string.replace("\u00ea", "e")
    string = string.replace("\u00eb", "e")
    string = string.replace("\u00ec", "i")
    string = string.replace("\u00ed", "i")
    string = string.replace("\u00ee", "i")
    string = string.replace("\u00ef", "i")
    string = string.replace("\u00f2", "o")
    string = string.replace("\u00f3", "o")
    string = string.replace("\u00f4", "o")
    string = string.replace("\u00f5", "o")
    string = string.replace("\u00f6", "o")
    string = string.replace("\u00f9", "u")
    string = string.replace("\u00fa", "u")
    string = string.replace("\u00fb", "u")
    string = string.replace("\u00fc", "u")
    string = string.replace("\u00a0", " ")
    string = string.replace("\u00bf", "")
    string = string.replace("&amp;", "&")
    string = string.replace("\u00b0", "")
    string = string.replace("\u00ba", "")
    string = string.replace("\u00aa", "")
    string = string.replace("\u00a1", "")
    string = string.replace("\u00e7", "c")
    string = string.replace("\u2013", "-")
    string = string.replace("\u00f1", "n")
    string = string.replace("\u2026", "...")
    string = string.replace("\u00ae", "")
    string = string.replace("\u201d", "")
    string = string.replace("\u201c", "")
    string = string.replace("\u00ab", "'")
    string = string.replace("\u00bb", "'")
    string = string.replace("\u00b4", "'")
    string = string.replace("\u00b7", "'")
    string = string.replace("\u00ad", "")
    string = string.replace("\u2022", "")
    string = string.replace("\u2019", "'")
    string = string.replace("\u2018", "'")
    string = string.replace("\u2014", " ")
    string = string.replace("a\u00b3", "o")
    string = string.replace("\u0153", "oe")
    string = string.replace("\u00e6", "ae")
    string = string.replace("a\u00b1o", "n")
    return string

def remove_spaces(string):
    string = string.replace("\n\r", " ")
    string = string.replace("\r\n", " ")
    string = string.replace("\n", " ")
    string = string.replace("\t", " ")
    string = string.replace("\r", " ").strip()
    return string

def replace_uper(string):
    return string.lower()

def clean_price(value):
    value = value.replace("$", "")
    value = value.replace(",", "")
    value = value.replace(".", "").strip()
    return int(value)

def clean_discount(string):
    string = string.replace("%", "")
    return float(string)

def clean_text(string):
    for character in string:
        if character not in "abcdefghijklmnopqrstuvwxyz ":
            string = string.replace(str(character), " ")
    return " ".join(string.split())