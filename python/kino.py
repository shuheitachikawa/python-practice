# for i in range(5):
#   if i == 3:
#     continue
#   print(i)

# for i in range(3):
#   for j in range(3):
#     for k in range(3):
#       print(i,j,k, sep="--")

# def say_hello(num1, num2):
#   return (num1 + num2)

# print(say_hello(1,3))

# def calc_ave(num1, num2, num3):
#   return (num1+num2+num3)/3

# print(calc_ave(9,4,2))


# class Student:

#   def __init__(self, name):
#     self.name = name

#   def avg(self,num1,num2):
#     print((num1 + num2) /2)

# a001 = Student("太刀川")
# a001.avg(3,4)


# print(a001.name)

# a002 = Student("さつぇt")
# print(a002.name)

class Student:
  def __init__(self, name):
    self.name = name
  
  def calcAvg(self, date):
    sum = 0
    for num in date:
      sum += num
    return sum / len(date)

  def judge(self, avg):
    if avg >= 60:
      return "合格"
    else:
      return "不合格"

a001 = Student("太刀川")
date = [90, 60, 30, 90]
avg = a001.calcAvg(date)
result = a001.judge(avg)

print(a001.name + " " + result)