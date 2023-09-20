import os
import re
import sys
import argparse
import importlib
import _thread, threading
import time

from examples import examples
from func_timeout import func_timeout

def print_colour(text, C):
    CEND = '\033[0m'
    print(C + text + CEND)

def green_print(text):
    print_colour(text, '\33[32m')

def red_print(text):
    print_colour(text, '\033[91m')
    
def values_match(out, output):
    if type(out) is float and type(output) is float:
        diff = out - output
        condition = (diff < 1e-9) or (diff > -1e-9)
        return condition
    else:
        condition = (out == output)
        return condition
    
def main(arguments):

    #argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('question', help="The question to test")
    args = parser.parse_args(arguments)

    #get user entered question
    q = args.question

    try:
        pattern = re.compile("team_(.+)_question_" + q + ".py")
        filename = None
        for file in os.listdir("solutions"):
            if bool(pattern.fullmatch(file)):
                filename = file[:-3]
        question = importlib.import_module(f'solutions.{filename}')
        sol = question.Solution
    except Exception as exc:
        print("Solution not found or import failed. Make sure you have a file at solutions/team_{team_name}_question_{q}.py with a function called 'Solution'.")
        print(repr(exc))
        return

    print(f'Testing question {q}')
    for i, (input,output) in examples[q].items():

        try:
            if type(input) is tuple:
                out = func_timeout(30,sol,args=(input))
            else:
                out = func_timeout(30,sol,args=([input]))
        except Exception as exc:
            out = repr(exc)

        if not values_match(out, output):
            red_print(f'  Test {i}: FAIL')
            print(f'    Input: {input}')
            print(f'    Expected output: {output}')
            print(f'    Received output: {out}')
            print('\n')

        else:
            green_print(f'  Test {i}: PASS')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))