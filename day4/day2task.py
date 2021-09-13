'''classes and objects'''
import logging
import uuid
import re
import collections as c
class Filecls:
    '''parent class'''
    def fread(self):
        '''reading file'''
        file_new = open('input.txt', 'r+')
        return file_new
        # with open('input.txt', 'r+') as file_new:
        #     return file_new

    def getwords(self,file_new):
        '''get file content'''
        try:
            words = list(file_new.read().split())
            logging.warning("words: {0}".format(words))#pylint: disable=logging-format-interpolation
            return words
        except FileNotFoundError as error:
            print(error)
        else:
            print("error in getting words")

    def getrepeatstr(self, list_arg):
        '''repeted string'''
        try:
            str_count = c.Counter(list_arg)
            maxstr = list(sorted(str_count.items(),key=lambda x:x[1], reverse=True))[0][0]
            logging.warning("repeted string :%s",maxstr)
            return maxstr
        except (TypeError, ValueError) as error:
            print(error)
        else:
            print("error in repeated string")

    def prefixcount(self, list_arg):
        '''prefix count'''
        c_to = 0
        for i in list_arg:
            if i.startswith('To'):
                c_to += 1
        logging.info("prefix to count :%d",c_to)
        return c_to

    def suffixcount(self, list_arg):
        '''suffix count'''
        c_ing = 0
        for i in list_arg:
            if i.endswith('ing'):
                c_ing += 1
        logging.warning("suffix ing count %d",c_ing)
        return c_ing

    def getpalindrome(self, list_arg):
        '''palindromes'''
        pal = []
        for i in list_arg:
            if i == i[::-1] and len(i)>1:
                pal.append(i)
        logging.warning(pal)
        return list(set(pal))

    def unifileops(self, list_arg):
        '''returning file and writing list '''
        try:
            li1 = []
            for i in range(len(list_arg)):
                li1.extend(re.split('a|e|i|o|u|A|E|I|O|U', list_arg[i]))
                li1 = ' '.join(li1).split()
            for i in range(len(li1)):
                if (i + 1) % 5 == 0:
                    li1[i] = li1[i].upper()
            logging.warning(li1)
            filen = str(uuid.uuid4())
            filen += '.txt'
            with open("filen",'w') as fnew:
                fnew.write("-".join(li1))
            return li1
        except ValueError as error:
            logging.error(error)
        else:
            logging.warning("error in writing comtent to unique file")
class Results(Filecls):
    '''print all results'''
    def printres(self):
        """results method"""
        file_new=self.fread()
        list_eg = self.getwords(file_new)
        print(list_eg)
        print(self.getrepeatstr(list_eg))
        print(self.prefixcount(list_eg))
        print(self.suffixcount(list_eg))
        print(self.getpalindrome(list_eg))
        print(self.unifileops(list_eg))

if __name__ == "__main__":
    logging.basicConfig(filename="std.log", format='%(name)s %(message)s')
    logobj = logging.getLogger()
    logobj.setLevel(logging.DEBUG)
    logging.info("executing...")
    obj = Results()
    obj.printres()
