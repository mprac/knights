from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # if A were a knight, then that sentence would have to be true
    Implication(AKnight,And(AKnight,AKnave)),
    # A cannot be both a knight and a knave
    Not(And(AKnight, AKnave)),
    # we know that each character is either a knight or a knave, but not both
    Or(AKnight,AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # If A were a Knight then the sentence would have to be true
    Implication(AKnight, And(AKnave, BKnave)),
    # A and B cannot be both a knave
    Not(And(AKnave,BKnave)),
    # We know that A is either a knave or a knight and B is either a Knave or a Knight
    Or(And(AKnave,BKnight),And(BKnave,AKnight)) 
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If A were a Knight then the sentence is true
    Implication(AKnight, And(AKnight,BKnight)),
    # we know A and B cannot be of the same kind
    Not(And(AKnight,BKnight)),
    # if B were a knight we know that the sentence is true
    Implication(BKnight, Not(And(BKnight,AKnight))),
    # We know that A is either a knave or a knight and B is either a Knave or a Knight
    Or(And(AKnight,BKnave),And(BKnight,AKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # If A were a Knight then the sentence is true.
    Implication(AKnight, Or(AKnight,AKnave)),
    # If A were a knave then that sentence would be false, but it is true becuase A is either or. 
    Implication(AKnave, Not(Or(AKnight,AKnave))),
    # If B were a Knight then A said he is knave
    Implication(BKnight, Implication(AKnight, AKnave)),
    # If B were a knight then C is a knave
    Implication(BKnight, CKnave),
    # If C were a knight then the sentence is true
    Implication(CKnight, AKnight),
    # If C were a Knave then the sentence would be false
    Implication(CKnave, Not(AKnight)),
    # We know that each character is either a knight or a knave
    And(Or(AKnight,AKnave), Or(BKnight,BKnave), Or(CKnight,CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
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
