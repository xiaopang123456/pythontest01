# sales=int(input("请输入商品的销量:"))
# if sales<10 or sales>100:
#     print("关注该商品")
# data=None
# print(data)
# if data is not None:
#     print("true")
# else:
#     print("false")
# a=range(101)
# result=0
# for i in a:
#     result +=i
# print(result)
# for i in range(1,5):
#     print(i)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j)+"="+str(i*j)+"\t",end='')
#     print('')
# for num in range(1,100):
#     print(num)
#     if num%3==2 and num%5==3 and num%7==2:
#         print("这个数是："+str(num))
#         break
# key=['xiao','pang','da','en']
# value=['小','胖','大','嗯']
# zip1=zip(key,value)
# word=dict(zip1)
# print(word)
# print(word.get('xiao2','没有'))
# print(word['xiao'] if 'xiao' in word else "我的zidianmeiy1")
# word=dict.fromkeys(key)
# print(word)
# sing={'xiao':'小','pang':'胖'}
# # for key in sing.keys():
# #     print(key)
# for value in sing.values():
#     print(value)
# word={'xiao':'小','pang':'胖','chi':'吃','fan':'饭','le':'了'}
# word['da']='大'
# word['da']='大da'
# print(word)
# math=['1','2','3','4','5']
# english=['a','b','c','d','e']
# dict1={i:j for i,j in zip(math,english)}
# print(dict1)
from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
# driver.maximize_window()

time.sleep(5)
driver.find_element_by_id("cart_num").click()
# driver.quit()
