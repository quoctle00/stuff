from logic import *

colors = ["red", "blue", "green", "purple"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.
for color in colors:
    for position in range(4):
        for pos in range(4):
            if position != pos:
                knowledge.add(
                    Implication(Symbol(f"{color}{position}"), Not(Symbol(f"{color}{pos}")))
                )


# Only one color per position.
for posi in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{posi}"), Not(Symbol(f"{c2}{posi}")))
                )

# First Guess
knowledge.add(symbols[0])
knowledge.add(symbols[5])

# Second Guess
knowledge.add(Not(symbols[1]))
knowledge.add(Not(symbols[4]))
knowledge.add(Not(symbols[10]))
knowledge.add(Not(symbols[15]))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
