class writer:
    def __init__(self,FileName):
        if (FileName!=None):
            self.OutFile = open(FileName, "wt")


    def make_line(self,DataDict):
        #print(DataDict)
        DataDict['Line']
        if (DataDict['CounterList']!=None):
            WriteLine=self.make_counter_line(DataDict)
        else:
            WriteLine=self.make_collapse_line(DataDict)

        self.write_line(WriteLine)

    def make_counter_line(self,DataDict):
        CounterList=[]
        for Counter in DataDict['CounterList']:
            Counter=str(Counter)
            CounterList.append(Counter)

        CounterText='.'.join(CounterList)
        WriteLine=CounterText+DataDict['Line']
        return WriteLine

    def make_collapse_line(self,DataDict):
        IndentText=' '
        IndentText=IndentText*DataDict['IndentLevel']
        WriteLine = DataDict['Line']
        if (DataDict['IndentHigher']==True):
            WriteLine='+'+WriteLine
        elif(DataDict['IndentHigher']==False):
            WriteLine = '-' + WriteLine
        WriteLine=IndentText+WriteLine
        return WriteLine


    def write_line(self,TextLine):
        if (hasattr(self, 'OutFile')):
            self.OutFile.write(TextLine)
        else:
            TextLine = TextLine.rstrip()
            print(TextLine)

    def __del__(self):
        if (hasattr(self, 'OutFile')):
            self.OutFile.close()