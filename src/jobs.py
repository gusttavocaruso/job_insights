from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_as_dict = csv.DictReader(file)
        return list(file_as_dict)


if __name__ == '__main__':
    print(read('jobs.csv'))
