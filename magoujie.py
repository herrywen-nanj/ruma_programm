#!/usr/bin/python
# - * - coding: utf-8 - * -
def magoujieprogram():
 name = raw_input("请输入你需要辱骂的人: ")
 sigoujie = raw_input("是否需要进行辱骂？: (y/n)")
 while True:
  if sigoujie == 'y':
   print '你真明智,' + name + '就是一泡屎唉'
  elif sigoujie == 'n':
   print '你是煞笔吧，竟然不辱骂他,' +  '辱骂' + name + '是对他最好的尊重'
  else:
   break
magoujieprogram()
while 1:
 if  'y' or 'n' not in list(sigoujie):
  print '你输入的有问题，请重新输入姓名和是否需要辱骂(y/n)'
  magoujieprogram()
  
#print '你输入的有错误，请重新输入'
#print '该程序已结束'
#if sigoujie == 'y':
# while True:
#  print '劳资把小狗杰骂死，他就是一泡屎唉'
#elif sigoujie == 'n':
# print '你竟然不骂陈杰，你就是不尊重陈杰'
#else:
# print '你输入的不是(y/n),请重新输入'
