import csv
from statistics import mode
from statistics import mean
from statistics import stdev


from Abalone import Abalone


class AbaloneData:

    def __init__(self, file):
        self.ab = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.ab.append(Abalone(row))

    def getSexInfo(self):
        sex = [a.attributes["sex"] for a in self.ab]
        dom = mode(sex)
        return 'Dominant: ' + dom + \
               ' Occurrences: ' + sex.count(dom).__str__() + \
               ' Frequency ' + (sex.count(dom) / sex.__len__()).__str__()

    def getMean(self, key):
        arr = [a.attributes[key] for a in self.ab]
        result = mean(arr)
        return result.__str__()

    def getStdev(self,key):
        arr = [a.attributes[key] for a in self.ab]
        result = stdev(arr)
        return result.__str__()



