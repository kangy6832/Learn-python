import os
dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, "致橡树.txt")

# file = open(file_path, 'a', encoding='utf-8')
# file.write("\n 写的真好")
# file.close()

# file = open(file_path, 'r', encoding='utf-8')
# print(file.read())
# file.close()

# file = open(file_path, 'r', encoding='utf-8')
# for line in file :
#     print(line, end='')
# file.close()

# file = open(file_path, 'r', encoding='utf-8')
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
# file.close()

# file = None
# try:
#     file = open('致橡树.txt', 'r', encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')
# finally:
#     if file:
#         file.close()


try:
    with open('guido.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')






