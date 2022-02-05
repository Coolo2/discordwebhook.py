import ntpath
import io

class File():
    def __init__(self, path : str = None, fp : io.IOBase = None, name : str = None):

        self.path = path
        self.name = name or ntpath.basename(self.path)
        self.fp = fp

    def open(self):
        if not self.fp:
            self.fp = open(self.path, "rb")

        return self.fp
    
    def close(self):
        self.fp.close()
