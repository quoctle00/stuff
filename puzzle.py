from lib2to3.pgen2.token import AT
from logic import *

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."
Asaysone = And(ATruthoraptor, ALieosaurus)

knowledge0 = And(
    Not(Biconditional(ATruthoraptor, ALieosaurus)),
    Or(Biconditional(ATruthoraptor, Asaysone),
       Biconditional(ALieosaurus, Not(Asaysone)))
)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.
Asaystwo = And(ALieosaurus, BLieosaurus)

knowledge1 = And(
    Not(Biconditional(ALieosaurus, ATruthoraptor)),
    Not(Biconditional(BLieosaurus, BTruthoraptor)),
    Or(Biconditional(ATruthoraptor, Asaystwo)),
    Biconditional(ALieosaurus, Not(Asaystwo))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

Asaysthree = Or(And(ALieosaurus, BLieosaurus),
                And(ATruthoraptor, BTruthoraptor))
Bsaysthree = Or(And(ALieosaurus, BTruthoraptor),
                And(ATruthoraptor, BLieosaurus))
knowledge2 = And(
    Not(Biconditional(ALieosaurus, ATruthoraptor)),
    Not(Biconditional(BLieosaurus, BTruthoraptor)),
    Or(Biconditional(ATruthoraptor, Asaysthree),
       Biconditional(ALieosaurus, Not(Asaysthree))),
    Or(Biconditional(BTruthoraptor, Bsaysthree),
       Biconditional(BLieosaurus, Not(Bsaysthree)))
)

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'."
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."

Asaysfour = Or(ATruthoraptor, ALieosaurus)
Bsaysfour = Or(Biconditional(ATruthoraptor, ALieosaurus),
               Biconditional(ALieosaurus, Not(ALieosaurus)))
Bsaysfive = CLieosaurus
Csaysfive = ATruthoraptor
knowledge3 = And(
    Not(Biconditional(ALieosaurus, ATruthoraptor)),
    Not(Biconditional(BLieosaurus, BTruthoraptor)),
    Not(Biconditional(CLieosaurus, CTruthoraptor)),
    Or(Biconditional(ATruthoraptor, Asaysfour),
       Biconditional(ALieosaurus, Not(Asaysfour))),
    Or(Biconditional(BTruthoraptor, Bsaysfour),
       Biconditional(BLieosaurus, Not(Bsaysfour))),
    Or(Biconditional(BTruthoraptor, Bsaysfive),
       Biconditional(BLieosaurus, Not(Bsaysfive))),
    Or(Biconditional(CTruthoraptor, Csaysfive),
       Biconditional(CLieosaurus, Not(Csaysfive)))
)


def main():
    symbols = [ATruthoraptor, ALieosaurus, BTruthoraptor,
               BLieosaurus, CTruthoraptor, CLieosaurus]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
