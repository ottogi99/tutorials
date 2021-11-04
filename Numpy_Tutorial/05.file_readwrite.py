# f = open("C:/Repo/Python/tutorials/Numpy_Tutorial/readme.txt", encoding='cp949')
f = open("C:/Repo/Python/tutorials/Numpy_Tutorial/readme.txt", encoding='UTF8')
data = f.read()
f.close()

print(data)
