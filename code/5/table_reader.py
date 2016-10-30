# simple csv reader
# copyright (c) 2016 Tim Menzies http://menzies.us
# all rights reserved, BSD 2-clause license
from __future__ import division, print_function
import sys, string, re, math, Nums, Syms, random, argparse

sys.dont_write_bytecode = True

UNKNOWN = "?"

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


    def distance(self, row1, row2, f=2):
        d,n,inc = 0, 10**-32,0
        for i in range(0,self.cols.__len__()-1):
            x,y = row1[i], row2[i]
            if x is UNKNOWN and y is UNKNOWN:
                continue
            if x is UNKNOWN:
                x= x.furthest(y)
            if y is UNKNOWN:
                y= y.furthest(x)
            n    += 1
            inc  = random.randint(1,10) #dist(x,y)**f
            d    += inc
        return (d**(1/f)) / (n**(1/f))

def options(before, after, *lst):
  parser = argparse.ArgumentParser(epilog=after, description = before,
              formatter_class = argparse.RawDescriptionHelpFormatter)
  for key, rest in lst:
    parser.add_argument(key,**rest)
  return parser.parse_args()

THE = options(*help())

def nb( train=THE.train,test=THE.test): return learn(nb1, train,test)

def learn(what, train, test):
  print(train,test)
  for actual, predicted in what(train, test):
    print(actual, predicted)

#from https://github.com/txt/ase16/blob/master/src/ase.py
def arff2rows(file):
  tbl   = Table()
  seen  = lambda x,y: re.match('^[ \t]*'+x,y,re.IGNORECASE)
  data,div  = False," "
  words = []
  with open(file) as fs: # cant use 'rows' since i have to flip commans
    for line in fs:
      line = re.sub(r'([\n\r]|#.*)', "", line)
      row  = map(lambda z:z.strip(), line.split(div))
      if row != []:
        if   seen("@relation", row[0]) : tbl.relation = row[1]
        if   seen("@attribute", row[0]): words += [row[1]]
        elif data and len(row) > 1     :
          yield tbl,tbl(row)
        elif seen("@data", row[0])     :
          data,div=True,","
          words[-1] = "=" + words[-1]
          tbl(words)

def arff2table(file):
    for tbl,_ in arff2rows(file): pass
    return tbl

def like(row, all, klasses):
  guess, best, nh, k = None, -1*10**32, len(klasses), THE.nbk
  for this,tbl in klasses.items():
    guess = guess or this
    like  = prior = (len(tbl._rows)  + k) / (all + k * nh)
    for col in tbl.decs:
      if col.my:
        x = row[col.pos]
        if x != UNKNOWN:
          like *= col.my.like( x, prior) # mult together all the likes
    if like > best:
      guess,best = this,like
  return guess

def knn(train=THE.train,test=THE.test): return learn(knn1,train,test)

def knn1(train,test):
  tbl = arff2table(train)
  k   = tbl.klass[0].pos
  for _,r1 in arff2rows(test):
    r2 = tbl.closest(r1)
    yield r1[k],r2[k]

def nb1(train,test):
  klasses = {}
  for all,(tbl1,row) in enumerate(arff2rows(train)):
    k = tbl1.isa(row)
    if not k in klasses:
      klasses[k] = tbl1.clone()
    klasses[k](row)
  for tbl2,row in arff2rows(test):
    yield tbl2.isa(row), like(row,all,klasses)


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
        for r in range (0,table.rows.__len__()-2):
            print(table.distance(table.rows[r], table.rows[r+1]))
