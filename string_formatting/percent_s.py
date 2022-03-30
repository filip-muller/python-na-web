"""Pokud se ve stringu vyuzije %s, lze nasledne pomoci znaku % za
stringe nahradit %s urcitou hodnotou. Lze vyuzivat i %d a %f pro
decimal a float hodnoty, pro jednoduchost ale staci %s
"""

x = 12
s = "x je: %s" % x
print(s)
# output: x je 12

s = "13 + 4 je %s" % (13 + 4)
print(s)
# output: 13 + 4 je 17

def otoc(s: str):
    # vrati string pozpatku
    return s[-1::-1]

s = "auto pozpatku je: %s" % otoc("auto")
print(s)
# output: auto pozpatku je: otua


# pri pouziti vice %s je potreba hodnoty vlozit jako tuple
s = "%s + 13 = %s" % (x, x + 13)
print(s)
# output: 12 + 13 = 25
