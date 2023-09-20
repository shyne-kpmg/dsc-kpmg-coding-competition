import argparse
import os
import re
import sys

def main(arguments):

    #argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('team_name', help="The team name you have chosen")
    args = parser.parse_args(arguments)

    #get user entered team name
    team_name = args.team_name
    
    dir = "solutions"
    pattern = re.compile("team_(.+)_question_(\d+).py")
    for file in os.listdir(dir):
        if bool(pattern.fullmatch(file)):
            new_name = re.sub(pattern, r'team_' + team_name + r'_question_\2.py', file)
            old_path = os.path.join(dir, file)
            new_path = os.path.join(dir, new_name)
            os.rename(old_path, new_path)
  
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
