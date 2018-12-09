from django.shortcuts import render
import json
import os


def index(request):
    PROJECT_ROOT = os.path.dirname(__file__)  #项目的绝对路径
    with open(PROJECT_ROOT + '/windABC.json','rb') as f:
        data = json.load(f)

    temp1 = list()
    for i in range(len(data['windHR'])):
        data2 = data['windHR'][i]
        temp1.append(data2["category"])
    content1 = []
    for i in temp1:
        if i not in content1:
            content1.append(i)

    temp2 = list()
    for i in range(len(data['windTech'])):
        data2 = data['windTech'][i]
        temp2.append(data2["category"])
    content2 = []
    for i in temp2:
        if i not in content2:
            content2.append(i)

    return render(request,'index.html',{'content1':content1,'content2':content2})


def detail(request,id):
    PROJECT_ROOT = os.path.dirname(__file__)  #项目的绝对路径
    with open(PROJECT_ROOT + '/windABC.json','rb') as f:
        data = json.load(f)

    dict = {}
    for key in data.keys():
        for i in range(len(data[key])):
            data2 = data[key][i]
            if data2["category"] == id:
                dict[data2['key']] = data2['value']
    tmp = []
    dict1 = {}
    for key,value in dict.items():
        for j in range(len(value)):
            tmp.append(value[j]['item'])
        dict1[key] = tmp
        tmp = []

    return render(request,'detail.html',{'dict':dict1,'id':id})


