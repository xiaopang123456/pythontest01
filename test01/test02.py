# import random
# team=['a','b','c','d','e']
# for index,item in enumerate(team):
#     print(index+1,item)
# name=['小胖','比比东','唐三','小舞','胡列娜','小奥','荣荣']
# print(len(name))
# print(type(name))
# name.append("唐昊")
# print(name)
# name.insert(8,"阿蓝")
# print(name)
# name=['小胖','比比东','唐三','小舞','胡列娜','小奥','荣荣']
# name01=['a','b','c']
# name.extend(name01)
# print(name)
# print(name.extend(name01))
# list=['十年生死两茫茫','不思量']
# list[1]='自难忘'
# print(list)
# name=['小胖','比比东','唐三','小舞','胡列娜','小奥','荣荣']
# del name[-1]
# print(name)
# name=['1','2','3','4','3','4']
# count=[1,33,45,66,77,88]
# total=sum(count,1000)
# print(total)
# count=name.count('3')
# count=name.index('3')
# print(count)
# grade=[23,55,67,899,389,345,678]
# grade.sort()
# print(grade)
# grade.sort(reverse=True)
# print(grade)
# list=[]
# print(type(list))
# list01={}
# print(type(list01))
import random
# list=[]
# for i in range(10):
#     list.append(random.randint(1,100))
# print(list)
# tuple=tuple(range(2,21,2))
# del tuple
# print(tuple)
# tuple=('py','java','c','c++','c++','c#','unity','go')
# for index,tuple in enumerate(tuple):
#     if index%2==0:
#         print(tuple+"   ",end='')
#     else:
#         print(tuple+"\n")
# print(tuple)
# print(tuple[1:3])
# for i in tuple:
# tuple01=(1,2,3,4,5,6)
# tuple02=(7,)
# print(tuple01+tuple02)
# print(tuple01+tuple02)
# import random
# randomnumber=(random.randint(1,100) for i in range(10))
# print(tuple(randomnumber))
# for i in randomnumber:
#     print(i,end='')
# print(randomnumber.__next__())
# engenier01="我是小胖胖"
# engenier02="是的，你是"
# print(len(engenier01.encode("utf-8")))
# print(len(engenier01.encode('gbk')))
# print(engenier01+"\n"+engenier02)
# len="钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。"
# print(len.split("。"))
# len="@".join(len)
# print("@"+len)
list="春眠不@@觉@晓@c@处@处@闻@啼@鸟"
# print(list.count('@'))
# print(list.find("@"))
# print(list.find('*'))
# print(list.rfind("@"))
# print(list.index("@"))
# print(list.startswith("春"))
# print(list.endswith('@'))
# str1="WWWtttrrr"
# print(str1.lower())
# print(str1.upper())
# num=18
# if num>90:
#     print("我大于90")
# else:
#     print("我小于90")
# number=int(input("你送我几朵玫瑰？"))
# if number==1:
#     print("抠门")
# elif number==60:
#     print("666")
# elif number==108:
#     print("求婚")
# else:
#     print("不知道的朵数")
# proof=int(input("请输入每100毫升血液酒精的含量："))
# if proof<20:
#     print("可以开车")
# else:
#     if 80>=proof>20:
#         print("中度酒驾")
#     else:
#         print("严重酒驾")
# age=int(input("请输入您的年龄："))
# if age>=18 and age<=80:
#     print("可以考驾驶证")
# else:
#     print("不可以考驾驶证")