

from __future__ import division
import sys
import rows, Syms, Nums

UNKNOWN = "?"

class Table:
    def __init__(self, csvFile):
        self.csv = rows.csv(csvFile)
        self.cols = []
        self.rows = []
        self.headers = []

    def addRow(self):
        ##add the headers
        self.headers = self.csv.next()
        self.rows.append(self.csv.next())
        ##check the datatype of the first row
        i = 0
        for value in self.rows[0]:
            if isinstance(value, int) or isinstance(value, float):
                self.cols.append(Nums.Num(i))
                # print i
                self.cols[i].add(value)
            else:
                self.cols.append(Syms.Sym(i))
                # print i
                self.cols[i].add(value)
            i += 1
        ##add the following rows
        for nextRow in self.csv:
            self.rows.append(nextRow)
            i = 0
            for value in nextRow:
                self.cols[i].add(value)
                i += 1

    def printFormat(self):
        i = 0
        for col in self.cols:
            print '{:15s}'.format(self.headers[i]) + col.show()
            i += 1
            
    def distance(self,r1,r2,f=2):
        d,n = 0, 10**-32
        for col in self.cols:
            if col is not self.cols[len(self.cols)-1]:
                x, y  = r1[col.pos], r2[col.pos]
                if x is UNKNOWN and y is UNKNOWN:
                    continue
                if x is UNKNOWN: x=col.my.furthest(y)
                if y is UNKNOWN: y=col.my.furthest(x)
                n    += 1
                inc   = col.dist(x,y)**f
                d    += inc
        return (d**(1/f)) / (n**(1/f))

    def closestAndFurthest(self, rowToCheck, data):
        closest_dist = 2
        furthest_dist = 0
        closest_row = None
        furthest_row = None
        for row in data:
            if row is not rowToCheck:
                dist = self.distance(row, rowToCheck)
                if closest_dist > dist:
                    closest_dist = dist
                    closest_row = row
                if furthest_dist < dist:
                    furthest_dist = dist
                    furthest_row = row
        
        #print str(rowToCheck) + '\nClosest Row is: ' + str(closest_row) + '\nFurthest Row is: ' + str(furthest_row)
        return closest_row, furthest_row
if __name__ == '__main__':
    file = 'weather.csv'
    table = Table(file)
    table.addRow()
    print table.distance(table.rows[1],table.rows[2])
