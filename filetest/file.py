import os


class File:

    def __init__(self):
        file = open('d://test.txt', 'w')
        file.write('My first python file.\n')

        file.close()

    def writeFile(self):
        file = open('d://test.txt', 'a')
        file.write('This is the second line.\n')

    def readFile(self):
        file = open('d://test.txt')

        print(file.read())
        file.close()


    def lineReadFile(self):
        file = open('d://test.txt')

        print(file.readline())
        file.close()

    def clearFile(self):
        file = open('d://test.txt', 'w')
        file.close()


if __name__ == '__main__':
    f = File()
    f.writeFile()

    f.readFile()

    print('')

    f.lineReadFile()
    f.lineReadFile()



