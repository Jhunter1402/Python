class Reader:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        self.file = open(self.filename, "r")
        return self

    def __next__(self):
        lines = self.file.readline()
        if lines:
            return lines.strip()
        else:
            self.file.close()
            raise StopIteration


data = Reader("data.txt")
for line in data:
    print(line)
