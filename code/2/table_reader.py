# simple csv reader
# copyright (c) 2016 Tim Menzies http://menzies.us
# all rights reserved, BSD 2-clause license
from __future__ import division, print_function
import sys, string, re, math, Nums, Syms

sys.dont_write_bytecode = True


def rows(file, prep=None,
         whitespace='[\n\r\t]',
         comments='#.*',
         sep=","
):
    """
    Walk down comma seperated values,
    skipping bad white space and blank lines
    """
    doomed = re.compile('(' + whitespace + '|' + comments + ')')
    with open(file) as fs:
        for line in fs:
            line = re.sub(doomed, "", line)
            if line:
                row = map(lambda z: z.strip(), line.split(sep))
                if len(row) > 0:
                    yield prep(row) if prep else row


def csv(file):
    """
    Convert rows of strings to ints,floats, or strings
    as appropriate
    """

    def atoms(lst):
        return map(atom, lst)

    def atom(x):
        try:
            return int(x)
        except:
            try:
                return float(x)
            except ValueError:
                return x

    for row in rows(file, prep=atoms):
        yield row


class Table:
    def __init__(self):
        self.rows = []
        self.cols = [Syms.Sym(), Nums.Num(), Nums.Num(), Syms.Sym(), Nums.Num()]  # summary objects, one per column


class Main:
    table = Table()
    table.__init__()

    if __name__ == '__main__':
        n = 0;
        for row in csv('weather.csv'):
            table.rows.append(row)
            if n > 0:                   #do not consider headline
                for i in range(0, 5, 1):
                    table.cols[i].add(row[i])
            n += 1
            print(row)
        print("----")
        for col in table.cols:
            print(col.show())
            print("\t")