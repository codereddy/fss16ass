# using code of older homework to read in data file
from __future__ import division, print_function
import sys, re, random, Syms, Nums

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


# select 500 random rows with class label not_recom & 500 with priority
def get50500(t1, out):
    selectedRows = []  # to avoid multiple same rows
    class_labels = ['not_recom', 'priority', 'spec_prior']
    label = class_labels[0]
    while (out.rows.__len__() < 500):
        randIndex = random.randint(0, t1.rows.__len__() - 1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[1]
    while (out.rows.__len__() < 1000):
        randIndex = random.randint(0, t1.rows.__len__() - 1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[0]
    while (out.rows.__len__() < 1100):
        randIndex = random.randint(0, t1.rows.__len__() - 1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[1]
    while (out.rows.__len__() < 1400):
        randIndex = random.randint(0, t1.rows.__len__() - 1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)

    label = class_labels[2]
    while (out.rows.__len__() < 1700):
        randIndex = random.randint(0, t1.rows.__len__() - 1)
        random_row = t1.rows[randIndex]
        if ((random_row[8] == label) & (not selectedRows.__contains__(random_row))):
            out.rows.append(random_row)
            selectedRows.append(randIndex)


def getEras(table, eras, section):
    selectedRows = []

    result = Table()
    result.__init__()

    if (section < 10):
        for _ in xrange(100):
            while (result.rows.__len__() < 100):
                randIndex = random.randint(0, 1000 - 1)  # of first 1000
                random_row = table.rows[randIndex]
                if (not selectedRows.__contains__(random_row)):
                    result.rows.append(random_row)
                    selectedRows.append(randIndex)
    else:
        for _ in xrange(100):
            while (result.rows.__len__() < 100):
                randIndex = random.randint(0, table.rows.__len__() - 1)  # of first 1000
                random_row = table.rows[randIndex]
                if (not selectedRows.__contains__(random_row)):
                    result.rows.append(random_row)
                    selectedRows.append(randIndex)
    # return result
    for i in range(0, result.rows.__len__(), 1):
        eras.rows.append(result.rows[i])


# class variable in column 8
def separateByClass(training):
    separated = {}
    for i in range(training.rows.__len__()):
        vector = training.rows[i]
        if vector[8] not in separated:
            separated[vector[8]] = []
        separated[vector[8]].append(vector)
    return separated


class Table:
    def __init__(self):
        self.rows = []
        self.cols = [Syms.Sym(), Syms.Sym(), Syms.Sym(), Nums.Num(), Syms.Sym(), Syms.Sym(), Syms.Sym(), Syms.Sym(),
                     Syms.Sym()]


class Main:
    table = Table()
    table.__init__()

    if __name__ == '__main__':
        print("reading data")
        for row in csv('nursery_m.data'):
            table.rows.append(row)
            for i in range(0, 9, 1):
                table.cols[i].add(row[i])

        table_out = Table()
        table_out.__init__()

        get50500(table, table_out)
        print("create eras")
        eras = Table()
        eras.__init__()
        era_test = Table()
        era_test.__init__()
        print("incremental bayes")
        for erasCount in range(0, 18, 1):
            getEras(table_out, eras, erasCount)
            train = eras
            test = getEras(table_out, era_test, erasCount + 1)

        print("done")