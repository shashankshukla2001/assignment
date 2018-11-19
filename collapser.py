import re
from filewriter import writer


class collapse:
    def __init__(self,InputFile,OutPutFile=None):
        self.IndentLevel=-1
        self.CountLevel=[0]
        counter_re='^(\*+)'
        indentl_re='^(\.+)'
        self.OutPutFile=OutPutFile
        self.input = open(InputFile, "rt")
        self.CounterRe=re.compile(counter_re)
        self.IndentRe=re.compile(indentl_re)

    def get_count_level(self, TextLine):
        Counter=self.has_counter(TextLine)

        if (Counter==None):
            return None

        #print(Counter)
        Level=Counter.count('*')
        Level=Level-1

        CounterLength=len(self.CountLevel)-1
        if (CounterLength<Level):
            self.CountLevel.append(1)
            #print(self.CountLevel)
            return self.CountLevel

        self.CountLevel[Level]=self.CountLevel[Level]+1
        self.CountLevel=self.CountLevel[:Level+1]
        #print(self.CountLevel)
        return self.CountLevel

    def get_indent_level(self,TextLine):
        Indent = self.has_indent_level(TextLine)
        IndentDict={}
        if (Indent == None):
            IndentDict['IndentLevel']=self.IndentLevel
            IndentDict['IndentHigher']=None
            return IndentDict

        self.IndentLevel = Indent.count('.')
        #print(Indent)
        #print(self.IndentLevel)
        IndentHigher=self.is_indent_higher()
        #print(IndentHigher)
        IndentDict['IndentLevel'] = self.IndentLevel
        IndentDict['IndentHigher'] = IndentHigher
        return IndentDict

    def is_indent_higher(self):
        CurrentLine=self.input.tell()
        TextLine=self.input.readline()
        Indent = self.has_indent_level(TextLine)

        while (Indent==None):
            TextLine = self.input.readline()
            Indent = self.has_indent_level(TextLine)
            if (TextLine==''):
                self.input.seek(CurrentLine)
                return False


        IndentCount=Indent.count('.')
        self.input.seek(CurrentLine)
        if (IndentCount>self.IndentLevel):
            return True
        return False

    def has_counter(self,TextLine):
        stars=self.CounterRe.match(TextLine)
        if (stars==None):
            return None
        return stars.group(0)

    def has_indent_level(self,TextLine):
        Indent = self.IndentRe.match(TextLine)
        if (Indent == None):
            return None
        return Indent.group(0)

    def get_text_line(self,TextLine):
        TextLine=self.IndentRe.sub('',TextLine)
        TextLine=self.CounterRe.sub('',TextLine)
        return TextLine
    def is_line_blank(self,TextLine):

        TextLine=TextLine.strip()
        if(TextLine==''):
            return True
        return False
    def read_lines(self):

        DataDict={}
        TextLine=self.input.readline()

        OutFileWriter=writer(self.OutPutFile)
        while(TextLine!=''):
            #print('_____________________________________')
            #print(TextLine)
            Blank=self.is_line_blank(TextLine)
            if (Blank==True):
                TextLine = self.input.readline()
                continue
            DataDict['CounterList']=self.get_count_level(TextLine)

            IndentDict=self.get_indent_level(TextLine)
            DataDict.update(IndentDict)


            DataDict['Line']=self.get_text_line(TextLine)
            #print(DataDict)

            OutFileWriter.make_line(DataDict)
            TextLine = self.input.readline()




    def __del__(self):
        self.input.close()


def main():
    InputFile="input.txt"
    OutPutFile='output2.txt'
    PlussMinus=collapse(InputFile,OutPutFile)
    PlussMinus.read_lines()

if __name__ == '__main__':
    main()
