from puzzles.day1_tasks import task1

import os
import sys
from pathlib import Path

file = Path(__file__).resolve()
puzzles_inputs = os.sep.join([str(file.parents[1]), "puzzles_inputs"])
utils = os.sep.join([str(file.parents[1]), "utils"])
sys.path.append(str(puzzles_inputs))
sys.path.append(str(utils))

if __name__ == "__main__":
    task1()

