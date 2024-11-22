#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("0 arguments.")
    else:
        print(f"{len(arguments)} argument{'s' if len(arguments) > 1 else ''}:")

        for index, arg in enumerate(arguments, start=1):
            print(f"{index}: {arg}")
