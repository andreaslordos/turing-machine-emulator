# turing-machine-emulator
A Turing Machine emulator. Allows you to write programs for a virtual Turing Machine and see the outcome.

# What is a Turing Machine?
A Turing Machine is a theoritical computer devised by Alan Turing in the 1930s. It uses an infinitely long 'tape' which is split up into an infinite number of cells as it's memory. The cells contain either 1s or 0s. There is a "head" which can change its position to read any cell to find out what it contains, and write over a cell to change what it contains. The Turing Machine has different "states", which change depending on what is read.

# Example Code

> / * STARTING_POSITION = 4

> / * NAME = ADDING MACHINE

> / * STARTING_STATE = 1

> S1 R0, 1L
> S1 R1, 4R S=2
> S1 RH, 4R W0 1L W0 1L W0 1L W0 H

> S2 R0, W1 5L S=1
> S2 R1, W0 5L S=3
> S2 RH, 4R W0 1L W0 1L W0 1L W0 H

> S3 R0, W0 4R S=2
> S3 R1, 1L
> S3 RH, 4R W0 1L W0 1L W0 1L W0 H

Note: ignore the slashes on lines 1-3, they're only there due to GitHub's formatting rules.

This is a program that takes a standard tape with the format of H x x x x x x x x H, where the "x"s are 1s or 0s. H stands for "HALT", and act as markers for the end of the tape. It then adds the two 4 bit binary numbers together, and leaves the result on the right side of the tape. 

# How to code with the Turing Machine

The first few lines of code should contain the starting position of the tape (so which cell to start on), name and starting state of your program. It is important to put an asterisk before these lines to ensure the compiler does not try to translate them into code. For example,

> / * STARTING_POSITION = x

Will set the starting position on the tape equal to x

After that, all lines follow a similar format:

> Sx Ry, {commands}
Where x is the state the Turing Machine is currently on, and y is the bit the Turing Machine is currently reading

You can issue the following commands:

* xL: moves the read/write "head" x spaces to the left
* yR: moves the read/write "head" y spaces to the right
* Wz: writes z, which can be either a 1, 0 or H, on the current cell the head is on
* S=q: sets the state of the machine equal to q
* H: halts the program and outputs the tape


