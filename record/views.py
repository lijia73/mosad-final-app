from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from account.models import User
from django.http import QueryDict
import json
import uuid
import time
# Create your views here.

def jsonMSG(state = 'fail', msg = 'no msg', data = []):
    response = {'state':state, 'msg':msg, 'data':data}
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def jsonMSGnoData(state = 'fail', msg = 'no msg'):
    response = {'state':state, 'msg':msg}
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def record(request):
    # 要在登录状态下
    if 'login_id' not in request.session:
        return jsonMSGnoData(msg = 'no login')

    # 只允许POST方法
    if request.method != 'POST':
        return jsonMSGnoData(msg = 'wrong method')
    
    # 已经登录, 所以拿取用户信息
    from_username = request.session['login_id']

    dataunicode = request.body.decode('utf-8')
    data = json.loads(dataunicode)

    try:
        Record.objects.create(
            RecordID = str(uuid.uuid4()).replace('-', '')[:24],
            Type = data['type'],
            Time = data['time'],

            Ownusername = from_username,
            Amount = data['amount'],
            Comment = data['comment'],
            Class = bool(data['class'])
        )
    except Exception as e:
        return jsonMSGnoData(msg = 'db error when add record')

    return jsonMSGnoData(state = 'success', msg = 'add record successfully')
    


def all(request):
    # 要在登录状态下
    if 'login_id' not in request.session:
        return jsonMSG(msg = 'no login')

    # 已经登录, 所以拿取用户信息
    from_username = request.session['login_id']

    # 只允许GET方法
    if request.method != 'GET':
        return jsonMSG(msg = 'wrong method')

    try:
        data = []
        for i in Record.objects.filter(Ownusername = from_username):
            data.append({
                'id': i.RecordID,
                'type': i.Type,
                'time' :i.Time,
                'amount':int(i.Amount),
                'comment':i.Comment,
                'class':i.Class
                })
    except Exception as e:
        return jsonMSGnoData(msg = 'db error when get record')
    return jsonMSG('success','get all record successfully',data)   

    

def detail(request, record_id):
    try:
        record = Record.objects.get(RecordID=record_id)
    except Exception as e:
        return jsonMSG(msg = 'db error')    
    # 要在登录状态下
    if 'login_id' not in request.session:
        return jsonMSG(msg = 'no login')

    # 已经登录, 所以拿取用户信息
    from_username = request.session['login_id']
 
    if request.method == 'GET':
        if from_username != record.Ownusername : 
            return jsonMSG(msg = 'not the owner')        
        data = []
        data.append({
            'id': record.RecordID,
            'type': record.Type,
            'time' :record.Time,
            'amount':record.Amount,
            'comment':record.Comment,
            'class':record.Class
            })
        return jsonMSG('success','get record detail successfully', data)
    
    if request.method == 'DELETE':
        if from_username != record.Ownusername : 
            return jsonMSGnoData(msg = 'not the owner')
        try:
            record.delete()
        except Exception as e:
            return jsonMSG(msg = 'db error')   
        return jsonMSGnoData(state = 'success', msg = 'delete record successfully')           

def allwithtime(request):
    # 要在登录状态下
    if 'login_id' not in request.session:
        return jsonMSG(msg = 'no login')

    # 已经登录, 所以拿取用户信息
    from_username = request.session['login_id']

    # 只允许GET方法
    if request.method != 'GET':
        return jsonMSG(msg = 'wrong method')

    begin=request.GET.get('begin','')
    end=request.GET.get('end','')

    try:
        data = []
        for i in Record.objects.filter(Ownusername = from_username):
            data.append({
                'id': i.RecordID,
                'type': i.Type,
                'time' :i.Time,
                'amount':int(i.Amount),
                'comment':i.Comment,
                'class':i.Class
                })
    except Exception as e:
        return jsonMSGnoData(msg = 'db error when get record')

    datanew = []
    for i in data:
        if i['time']>=begin and i['time']<=end :
            datanew.append(i)


    return jsonMSG('success','get all record with time successfully',datanew)     
        
 
