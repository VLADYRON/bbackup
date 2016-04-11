from System.IO import TextReader

class PythonFileReader(TextReader):
    def __init__(self, f):
        self.f = f
    def Read(self, buffer, index, count):
        chars = self.f.read(count).ToCharArray()
        chars.CopyTo(buffer, index)
        return len(chars)
