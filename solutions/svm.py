from abc import abstractmethod
from itertools import product

Program = list[int]

class Instruction:
    def __init__(self, data: list[int]):
        self.data = data
    @abstractmethod
    def evaluate(self) -> int:
        pass

class Sum(Instruction):
    def evaluate(self) -> int:
        return sum(self.data)

class Product(Instruction):
    def evaluate(self) -> int:
        prod = 1
        for n in self.data:
            prod *= n
        return prod


def parse(program: Program) -> list[Instruction]:
    if program == []:
        return 0
    if program[0] % 2 != 0:
        raise ValueError("Invalid Program")

    instructions: list[Instruction] = []
    iptr = 0

    # Start of loop invariant: The iptr indexes into the program at an even
    # number.
    while iptr < len(program):
        inumber = program[iptr]
        idata: list[int] = []
        iptr += 1
        while iptr < len(program) and program[iptr] % 2 == 1:
            idata.append(program[iptr])
            iptr += 1

        if inumber == 2:
            instructions.append(Sum(idata))
        elif inumber == 4:
            instructions.append(Product(idata))
        else:
            raise ValueError(f"Unknown instruction {inumber}")

    return instructions


def svm(program: Program) -> int:
    instructions = parse(program)
    return sum(instruction.evaluate() for instruction in instructions)


if __name__ == "__main__":
    print(svm([2, 1, 1, 1]))
    print(svm([4, 1, 3, 5]))
    print(svm([2, 5, 1, 5, 1]))
    print(svm([2, 1, 1, 1, 4, 1, 3, 5, 2, 5, 1, 5, 1]))