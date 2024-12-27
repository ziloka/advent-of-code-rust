import pathlib
import time
import os
import glob

try:
    from aocd.models import Puzzle
except ImportError:
    print(f"Run `pip install advent-of-code-data` to autodownload input files")
    raise SystemExit()

def download(year, day):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

    output_folder = (pathlib.Path(__file__).parent / "input" / f"year{year}")
    output_folder.mkdir(parents=True, exist_ok=True)
    output_path = output_folder / f"day{str(day).zfill(2)}.txt"
    output_path.write_text(puzzle.input_data, newline="\n")

if __name__ == "__main__":
    for x in glob.glob('src/year*/day*.rs'):
        path = x.split(os.sep)
        year = int(path[-2].split("year")[1])
        day = int(path[-1].split("day")[1][:-3])
        download(year, day)
        print(f"Downloaded input for year {year} day {day}")
        time.sleep(1)

print("downloaded all inputs for repository")
