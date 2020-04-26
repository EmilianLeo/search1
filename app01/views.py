# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

import pymysql
from app01 import models
from django.http import HttpResponse
from app01.models import wx01
# Create your views here.


def vlan(x,y,z):
    x=int(x)
    y=int(y)
    print(z.split('.'))
    z=z.split('.')

    for num in range(x,y+1):

        a = print('interface vlanif %d' % (num))
        b = print('ip address %s.%s.%s.%s 255.255.255.0' % (z[0],z[1],z[2],z[3]))

        z[2]=int(z[2])+1
        return render(a)





        # return HttpResponse(str('interface vlanif %d' % (num)))
        # return HttpResponse('ip address %s.%s.%s.%s 255.255.255.0' % (z[0],z[1],z[2],z[3]))





        # print('ip address %s 255.255.255.0 ' % (z))








def login(request):
    print(request.method)
    if request.method=="GET":
        return render(request,"vlan.html")
    else:
        print(request.GET)
        print(request.POST)

        first=request.POST.get("first")
        final=request.POST.get("final")
        Ip_addr = request.POST.get("Ip_addr")
        vlan(first,final,Ip_addr)

        # final=request.POST.get("final")
        # final=list(map(int,final))

        Ip_addr=request.POST.get("Ip_addr")
        file=request.POST.get("file")
        # user=request.POST.get("user")
        # pwd=request.POST.get("pwd")


        #
        # for i in range(first,final):
        #     print('interface vlanif i')


        # if user=='liye' and pwd=='123':
        #     return HttpResponse("登陆成功")
        # else:
        #     return HttpResponse("shibaasasai")
    # if request.method=='POST':
    #     # username = request.POST.get('username')   ###获取前台提交的用户
    #     # password = request.POST.get('password')   ###获取前台提交的密码
    #     # user_list=models.User.objects.filter(username=username,password=password).first()
    #     # print(user_list)
    #     # if user_list:
    #     #     return HttpResponse('登陆成功')
    #     return render(request,'login.html')

# 数据库操作
def hj(request):
    response = ""
    response1 = ""

    list = wx01.objects.all()
    response2 = wx01.objects.filter(id=1)
    response3 = wx01.objects.get(id=1)
    wx01.objects.order_by("id")
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "/p")




# def testdb(request):
#     test1 = Test(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")