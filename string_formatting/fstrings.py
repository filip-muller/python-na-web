"""Pro vyuziti fstring je potreba pred string napsat f, nasledne lze
ve stringu uvnitr slozenych zavorek vyhodnocovat jakykoli Python kod
"""

x = 12
s = f"x je: {x}"
print(s)
# output: x je 12

s = f"13 + 4 je {13 + 4}"
print(s)
# output: 13 + 4 je 17


# uvnitr slozenych zavorek lze volat funkce, metody, cokoliv
def otoc(s: str):
    # vrati string pozpatku
    return s[-1::-1]

s = f"auto pozpatku je: {otoc('auto')}"
print(s)
# output: auto pozpatku je: otua


# lze pouzivat i vice zavorek v jednom stringu
s = f"{x} + 13 = {x + 13}"
print(s)
# output: 12 + 13 = 25
