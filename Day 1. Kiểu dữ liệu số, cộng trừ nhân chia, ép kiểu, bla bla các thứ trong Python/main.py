""" x = 2 # có 1 biến x có giá trị là 2

print(type(x)) # output: dạng `int` nghĩa là 'integer' hay còn gọi là số nguyên

 """
# =================================================================

""" x = 2.0

print(type(x)) # output: số thực
 """

#============================================================

# phép cộng, trừ, nhân giống nhau nhak

# cộng: +
# trừ: -
# nhân: *

""" a = 6
b = 9
 """
# print('{1} + {0} = {2} thích làm chơi vầy nè {4}'.format(b, a, a + b, 5, 'Tui là Hồng'))

""" c = a + b # int + int = int

print(type(c))


c = 2.0 + 3
print(type(c)) """

# int + int = int
# float + int (float) = float


#============================================================


# phép chia mặc dù int / int nhưng kết quả sẽ ra float nhak
""" a = 6
b = 3

c = a / b

print(c)

print(type(a))
print(type(b))
print(type(c)) """


#============================================================

# int chia int mà vẫn ra int thì sài này nhak mấy đứa
""" a = 7
b = 3
c = int(a / b)

print(c)
print(type(c))
 """


# int(x) gọi là ép kiểu dữ liệu


a = 2

print(a)
print(type(a))

a = float(a)
print('------')

print(a)
print(type(a))


#============================================================
# int / float = float

""" a = 6
b = 9.0

print(a/b) """


# float / int = float

# print(6.9696969/1)

# => phép chia nhak, luôn ra số thực đó


# sao sao thì đừng lấy chia cho số 0 dùm con, lỗi ZeroDevisionError
# print(1/0)