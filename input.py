# https://github.com/gahjelle/template-aoc-python/blob/77ee24e6b80ea99c2a47bdf53d1c46887150db59/src/download_input.py

"""Download input for one Advent of Code puzzle if possible

Uses https://pypi.org/project/advent-of-code-data/ if it's available.
Otherwise, does nothing.
"""

# Standard library imports
import pathlib
import time
import os
import glob

# Third party imports
try:
    from aocd.models import Puzzle
except ImportError:
    print(f"Run `pip install advent-of-code-data` to autodownload input files")
    raise SystemExit()

def download(year, day):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

     # Download input
    output_folder = (pathlib.Path(__file__).parent / "input" / f"year{year}")
    output_folder.mkdir(parents=True, exist_ok=True)
    output_path = output_folder / f"day{str(day).zfill(2)}.txt"
    output_path.write_text(puzzle.input_data)

if __name__ == "__main__":
    for x in glob.glob('src/year*/day*.rs'):
        path = x.split(os.sep)
        year = int(path[-2].split("year")[1])
        day = int(path[-1].split("day")[1][:-3])
        download(year, day)
        print(f"Downloaded input for year {year} day {day}")
        time.sleep(1)

print("downloaded all inputs for repository")
