# name=['a','b','c','d','e']
# print('列表一：',name)
# print(type(name))
# set1=set(name)
# print(type(set1))
# print('集合：',set1)
# mr=set(['a','b','c','d','e'])
# mr.add('xiaopang')
# print(mr)
# mr.remove('xiaopang')
# print(mr)
# if '零基础学py' in mr:mr.remove('零基础学py')
# print(mr)
# mr.pop()
# print(mr)
# mr.clear()
# print(mr)
# py=set(['小胖','思齐','小博','邱爽','东东'])
# c=set(['明杰','Mery','小胖'])
# print('并集：',py & c)
# print('交集：',py | c)
# print('差集：',py - c)
# def filterchar(string):
#     '''功能：过滤字符串
#     string:要过滤的字符串
#     '''
#     import re
#     pattern=r'(黑客)|(抓包)|(监听)'
#     sub=re.sub(pattern,"@_@",string)
#     print(sub)
#
# def empty():
#     pass
# about='我是一名黑客'
# filterchar(about)
# def coffee(*coffeename):
#     print("小胖喜欢的咖啡有：")
#     for item in coffeename:
#         print(item)
# coffeename=["小胖",'小胖001']
# coffee(*coffeename)