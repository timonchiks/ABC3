import objective
import procedural

#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    #def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    def shaker_sort(cont: list):
        swapped = True
        start = 0
        end = len(cont) - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if cont[i][3] < cont[i + 1][3]:
                    cont[i], cont[i + 1] = cont[i + 1], cont[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if cont[i][3] < cont[i + 1][3]:
                    cont[i], cont[i + 1] = cont[i + 1], cont[i]
                    swapped = True
            start += 1

