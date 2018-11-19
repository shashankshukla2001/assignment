import sys
import os
import tempfile
from collapser import collapse
class CatArrow:
    def __init__(self):
        self.TempInputFp = tempfile.NamedTemporaryFile(delete=False)
    def makefempfile(self):

        for line in sys.stdin:
            line=line.rstrip()
            if (line!=''):
                self.TempInputFp.write(line+'\n')
        self.TempInputFp.seek(0)
        self.TempInputFp.close()

    def write_out(self):
        self.makefempfile()
        InputFile=self.TempInputFp.name
        PlussMinus = collapse(InputFile)
        PlussMinus.read_lines()
        return self.TempInputFp

    def __del__(self):
        self.TempInputFp.close()
        os.unlink(self.TempInputFp.name)

def main():
    ForCmd=CatArrow()
    ForCmd.write_out()


if __name__ == '__main__':
    main()
