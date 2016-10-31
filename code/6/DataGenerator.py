#using code of older homework to read in data file
from __future__ import division, print_function
import sys, string, re, math, Syms, Nums, random

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

#select 500 random rows with class label not_recom & 500 with priority
def get50500(t1, out):
    selectedRows = []   #to avoid multiple same rows
    class_labels = ['not_recom', 'priority', 'spec_prior']
    label = class_labels[0]
    while (out.rows.__len__() < 500):
        randIndex = random.randint(0,t1.rows.__len__()-1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[1]
    while (out.rows.__len__() < 1000):
        randIndex = random.randint(0,t1.rows.__len__()-1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[0]
    while (out.rows.__len__() < 1100):
        randIndex = random.randint(0,t1.rows.__len__()-1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[1]
    while (out.rows.__len__() < 1400):
        randIndex = random.randint(0,t1.rows.__len__()-1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[2]
    while (out.rows.__len__() < 1700):
        randIndex = random.randint(0,t1.rows.__len__()-1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)


class Table:
    def __init__(self):
        self.rows = []
        self.cols = [Syms.Sym(),Syms.Sym(),Syms.Sym(), Nums.Num(), Syms.Sym(),Syms.Sym(),Syms.Sym(),Syms.Sym(),Syms.Sym()]  # summary objects, one per column




class Main:
    table = Table()
    table.__init__()

    if __name__ == '__main__':
        for row in csv('nursery_m.data'):
            table.rows.append(row)
            for i in range(0, 9, 1):
                table.cols[i].add(row[i])
            print(row)

        table_out = Table()
        table_out.__init__()
        get50500(table, table_out)
