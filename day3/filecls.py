import logging as log
import uuid
import re
import collections as c
log.basicConfig(filename="std.log", format='%(name)s %(message)s')

class Filecls:
    def __init__(self):
            self.logobj = log.getLogger()

    def fread(self):
        f=open('input.txt', 'r+')
        return f

    def getwords(self,f):
        try:
            words = list(f.read().split())
            # self.logobj.setLevel(log.INFO)
            self.logobj.warning("words: {0}".format(words))
            return words
        except Exception as e:
            print(e)

    def getrepeatstr(self, li):
        try:
            str_count = c.Counter(li)
            maxstr = list(str_count.keys())[0]
            self.logobj.warning("repeted string :{0}".format(maxstr))
            return maxstr
        except Exception as e:
            print(e)

    def getpalincount(self, li):
        try:
            pal = []
            c_to, c_ing = 0, 0
            for i in li:
                if i == i[::-1]:
                    pal.append(i)
                if i.startswith('To'):
                    c_to += 1
                if i.endswith('ing'):
                    c_ing += 1
            self.logobj.warning("palindromes :{0}\n count of To:{1}\n count of ing:{2}".format(pal, c_to, c_ing))
            return pal, c_ing, c_to
        except Exception as e:
            print(e)

    def unifileops(self, li):
        try:
            li1 = []
            for i in range(len(li)):
                li1.extend(re.split('a|e|i|o|u|A|E|I|O|U', li[i]))
                li1 = ' '.join(li1).split()
            for i in range(len(li1)):
                if (i + 1) % 5 == 0:
                    li1[i] = li1[i].upper()
            self.logobj.warning("new list :{0}".format(li1))
            filen = str(uuid.uuid4())
            filen += '.txt'
            f = open(filen, 'w')
            f.write("-".join(li1))
            return li1

        except Exception as e:
            print(e)


class Results(Filecls):
    def printres(self):
        f=self.fread()
        li = self.getwords(f)
        print(li, '\n', self.getrepeatstr(li))
        print(self.getpalincount(li))
        print(self.unifileops(li))

if __name__ == "__main__":
    obj = Results()
    obj.printres()










