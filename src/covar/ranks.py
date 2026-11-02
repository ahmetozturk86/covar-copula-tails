import pandas as pd


def to_ranks(x):
    return x.rank() / (len(x) + 1)


if __name__ == "__main__":
    example = pd.Series([0.8, -3.2, 0.1, 2.5, -0.5],
                        index=["Mon", "Tue", "Wed", "Thu", "Fri"])
    print(to_ranks(example))
