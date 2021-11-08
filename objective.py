#----------------------------------------------

import random
from enum import Enum
import string

class Inheritance(Enum):
    nothing = 0
    single = 1
    multiple = 2
    interface = 3


class Objective:
    def __init__(self):
        self.popularity = 0.0
        self.year = 0
        self.inheritance = Inheritance(0).name
        self.name = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум четыре непрочитанных значения в массиве
        if i > len(strArray) - 4:
            return 0
        self.popularity = float(strArray[i + 2])
        self.year = int(strArray[i + 1])
        self.inheritance = Inheritance(int(strArray[i + 3])).name
        self.name = strArray[i]
        i += 4
        return i

    def Random(self):
        self.year = random.randint(1900, 2022)
        self.popularity = random.randint(0,10000)/100.0
        self.name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,50)))
        self.inheritance = Inheritance(random.randint(0,3)).name

    def Print(self):
        print("Objective:", self.name, " popularity = ", self.popularity, " year = ", self.year, " inheritance = ", self.inheritance, " Function = ", self.Function())
        pass

    def Write(self, ostream):
        ostream.write("Objective:{} popularity = {}  year = {}, inheritance = {}, Function = {}".format(self.name, self.popularity, self.year, self.inheritance,  self.Function()))
        pass

    def Function(self):
        return float(self.year / len(self.name))
        pass
