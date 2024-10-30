# The Stupid Virtual Machine

PuPPy consultancy finally has a client! They have instructed us to implement an
SVM (which, upon insisting, we are told means Stupid Vitual Machine). The SVM's
job is to process lists of numbers and produce a final number, the instructions
for this processing strike you as bizzare, but you're getting paid, so you may
as well try to do it correctly.

## Initial Brief

The SVM processes the list of numbers from left to right, and you've been told
that the leftmost number in the list is always *even*. The idea is that the even
numbers in the list are *instructions* and the odd numbers in the list are
*data*, so evens instruct the SVM on what to do with the odd numbers. When you
encounter an even number, all the following odd numbers (from left to right)
are processed acording to that even number, up until you encounter another even
number, which indicates a new mode of processing for the following odd numbers,
and so on until you reach the end of the list.

Here's a diagram of a list, where the even numbers are indicated along with the
following associated odd numbers:

    [2, 1, 1, 1, 4, 1, 3, 5, 2, 5, 1, 5, 1]
     |--------|  |--------|  |-----------|

As of now, there are two instructions requested from the client:

  - The `2` instruction indicates that the following odd numbers should be
  *summed*, the result of the instruction is the sum of the associated odds.
  - The `4` instruction indicates that the following odd numbers should be
  *multiplied*, the result of the instruction is the product of the associated
  odds.

Helpfully, your clients have supplied some simple examples:

    [2, 1, 1, 1] -> 1 + 1 + 1 = 3
    [4, 1, 3, 5] -> 1 * 3 * 5 = 15
    [2, 5, 1, 5, 1] -> 5 + 1 + 5 + 1 = 12

When put alltogether in the same list, we'd get back three numbers:

    [2, 1, 1, 1, 4, 1, 3, 5, 2, 5, 1, 5, 1]
    -> 3, 15, 12

The final client direction is that these final numbers should be *summed* to get
the ultimate result:

    [2, 1, 1, 1, 4, 1, 3, 5, 2, 5, 1, 5, 1]
    -> 3 + 15 + 12 = 30

Your job, programmer, is to implement the SVM and deliver it to the client. You
should deliver your work as a python function:

```python
def svm(program: list[int]) -> int:
    # Let's go!
```

## Follow Up Brief
You've made the first delivery of the SVM to your client, and they are pleased with your work!

They've discovered they need to implement an additional instruction:

  - The `6` instruction indicates that the following odd numbers sould be
  *alternating summed*. The result of the instruction is the alternating sum of
  the following odds.

An example will hopefully clarify what they want here:

    [6, 1, 1, 1] -> 1 - 1 + 1 = 1
    [6, 1, 3, 5] -> 1 - 3 + 5 = 3
    [6, 5, 1, 5, 1] -> 5 - 1 + 5 - 1 = 8

And an example involving multiple instructions:

    [2, 1, 1, 1, 4, 1, 3, 5, 6, 5, 1, 5, 1]
    -> 3 + 15 + 8 = 26

Add the alternating sum instruction to your SVM implementation. Reflect on how
difficult this was and how to make it easier to add new instructions in the
future.