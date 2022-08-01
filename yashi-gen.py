import argparse
import pandas as pd
import random
import copy

FILE_NAME = "yashi"


def write_csv(filename, yashi_grid):
    yashi_grid.to_csv(filename, index=False)


def generate_yashi_grid(size):
    yashi_grid = {"vertex": [], "row": [], "column": []}

    existing_tiles = []

    for _ in range(size):
        existing_tiles.append([False] * size)

    for v in range(random.randint(size * 2, size * 4)):
        row = None
        column = None
        while row == None or existing_tiles[row][column]:
            row = random.randint(0, size - 1)
            column = random.randint(0, size - 1)

        yashi_grid["vertex"].append(v)
        yashi_grid["row"].append(row)
        yashi_grid["column"].append(column)

        existing_tiles[row][column] = True

    return pd.DataFrame(yashi_grid)


def init_args():
    parser = argparse.ArgumentParser()

    def check_positive(v):
        v = int(v)
        if v <= 0:
            raise argparse.ArgumentTypeError(f"{v} is an invalid positive int value")
        return v

    parser.add_argument("--directory", type=str, required=True)

    parser.add_argument(
        "--size",
        type=check_positive,
        required=True,
    )

    return parser


def main():
    args = init_args().parse_args()

    yashi_grid = generate_yashi_grid(args.size)
    filename = f"{args.directory}/{FILE_NAME}-{args.size}.csv"
    write_csv(filename, yashi_grid)

    print(f"Just written {filename}")


if __name__ == "__main__":
    main()
