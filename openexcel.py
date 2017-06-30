#-encoding:utf8-
#-author:william-
#-email:william.sv@icloud.com-
import os
import sys
import chardet

class Oel():

    def __init__(self, path):
        self.path = path

    def file_char(self):
        file = self.file_or_dir()
        if type(file) == str:
            with open(file, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
                if encoding == None:
                    print('无法识别此文件的字符编码，请转为csv文件后重试！')
                    sys.exit(1)
                else:
                    return encoding
        else:
            print('输入的不是一个文件')
            sys.exit(1)

    def file_or_dir(self):
        listdirs = []
        if os.path.isfile(self.path) or os.path.isdir(self.path):
            if os.path.isdir(self.path):
                listdir = os.listdir(self.path)
                if '.DS_Store' in listdir:
                    listdir.remove('.DS_Store')
                for list in listdir:
                    listdirs.append(os.path.abspath(list))
                return listdirs
            else:
                return os.path.abspath(self.path)
        else:
            print('文件或目录不存在')

    def results(self):
        list = []
        file = self.file_or_dir()
        if type(file) == list:
            print('这是一个目录')
            sys.exit(1)
        elif type(file) == str:
            try:
                with open(file, 'rb') as f:
                    char = self.file_char()
                    lines = f.readlines()
                    for line in lines:
                        line = line.decode(char)
                        if '\t' in line:
                            line = line.replace('\t', ',')
                        if '\r\n' in line:
                            line = line.rsplit('\r\n')
                            line = line[:-1]
                        list.append(line)
                return list
            except Exception as e:
                print(e)
        else:
            print('文件读取错误，请稍后重试')
