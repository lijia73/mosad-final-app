from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import QueryDict
import json

# Create your views here.


def register(request):
    response = {'state':'fail', 'msg':'no msg'}

    # if 'login_id' in request.session:
    #     response['msg'] = 'already login'
    #     return HttpResponse(json.dumps(response), content_type = 'application/json')

    if request.method != 'POST':
        response['msg'] = 'wrong method'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 获取参数
    try:
        t_username = request.POST['username']
        t_password = request.POST['password']
    except Exception as e:
        response['msg'] = 'bad req'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 数据库操作
    try:
        t_user = User.objects.filter(Username = t_username)
    except Exception as e:
        response['msg'] = 'db error'
    else:
        if t_user.count() == 0:
            User.objects.create(
                Username = t_username,
                Password = t_password
            )
            response['state'] = 'success'
            response['msg'] = 'register successfully'
        else:
            response['msg'] = 'repeat username'

    return HttpResponse(json.dumps(response), content_type = 'application/json')

def logout(request):
    if request.method == "GET":
         return HttpResponse("article")

    response = {'state':'fail', 'msg':'no msg'}
    # 只允许通过 DELETE 方法退出登录
    if request.method != 'DELETE':
        response['msg'] = 'wrong method'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    try:
        del request.session['login_id']
    except KeyError:
        response['msg'] = 'no login'
    else:
        response['state'] = 'success'
        response['msg'] = 'logout successfully'

    return HttpResponse(json.dumps(response), content_type = 'application/json')


def login(request):
    response = {'state':'fail', 'msg':'no msg'}

    if request.method != 'POST':
        if 'login_id' in request.session:
            response['state'] = 'success'
            response['msg'] = 'already login'
        else:
            response['msg'] = 'no login'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 获取参数
    try:
        t_username = request.POST['username']
        t_password = request.POST['password']
    except Exception as e:
        response['msg'] = 'POST parameter error'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 数据库操作
    try:
        t_user = User.objects.filter(Username = t_username, Password = t_password)
    except Exception as e:
        response['msg'] = 'db error'
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        if t_user.count() <= 0:
            response['msg'] = 'username or password error'
        else:
            response['state'] = 'success'
            response['msg'] = 'login successfully'
            request.session['login_id'] = t_username

    return HttpResponse(json.dumps(response), content_type = 'application/json')


def info(request):
    response = {'state':'fail', 'msg':'no msg'}

    # 要在登录状态下
    if 'login_id' not in request.session:
        response['msg'] = 'no login'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 已经登录, 所以拿取用户信息
    t_username = request.session['login_id']

    if request.method != 'GET':
        response['msg'] = 'wrong method'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 这里进入GET方法
    # 数据库操作
    try:
        t_user = User.objects.filter(Username = t_username)
    except Exception as e:
        response['msg'] = 'db error'
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        if t_user.count() == 1:
            # temp = model_to_dict(t_user[0])
            t_user = t_user[0]
            temp = {}
            temp['Username'] = t_user.Username
            temp['Gender'] = t_user.Gender
            temp['Region'] = t_user.Region
            temp['Nickname'] = t_user.Nickname
            temp['Avatar'] = t_user.Avatar
            
            response = {'state':'success', 'msg':'success', "data":temp}
        else:
            response['msg'] = 'no data'

    return HttpResponse(json.dumps(response), content_type = 'application/json')

def changeInfo(request, t_attr):

    response = {'state':'fail', 'msg':'no msg'}
    
    # 要在登录状态下
    if 'login_id' not in request.session:
        response['msg'] = 'no login'
        return HttpResponse(json.dumps(response), content_type = 'application/json')


    if request.method != 'PUT':
        response['msg'] = 'wrong method'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 已经登录, 所以拿取用户信息
    t_username = request.session['login_id']

    # print(request.body)
    dataunicode = request.body.decode('utf-8')
    data = json.loads(dataunicode)

    # 获取参数
    try:
        t_value = data['value']
    except Exception as e:
        response['msg'] = 'bad req'
        return HttpResponse(json.dumps(response), content_type = 'application/json')

    # 数据库操作
    try:
        t_user = User.objects.filter(Username = t_username)
    except Exception as e:
        response['msg'] = 'db error'
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        if t_user.count() <= 0:
            response['msg'] = 'no such user'
            return HttpResponse(json.dumps(response), content_type = 'application/json')
        else:
            t_user = t_user[0]
            if t_attr == 'Password':
                t_user.Password = t_value
                t_user.save()
            elif t_attr == 'Gender':
                t_user.Gender = t_value
                t_user.save()
            elif t_attr == 'Region':
                t_user.Region = t_value
                t_user.save()
            elif t_attr == 'Nickname':
                t_user.Nickname = t_value
                t_user.save()
            
    response['msg'] = 'change successfully'
    response['state'] = 'success'
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def jsonMSGnoData(state = 'fail', msg = 'no msg'):
    response = {'state':state, 'msg':msg}
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def jsonMSG(state = 'fail', msg = 'no msg', data = 0):
    response = {'state':state, 'msg':msg, 'data':data}
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def budget(request):

    if request.method == 'POST':  
        # 要在登录状态下
        if 'login_id' not in request.session:
            return jsonMSGnoData(msg = 'no login')

        # 已经登录, 所以拿取用户信息
        t_username = request.session['login_id']
        dataunicode = request.body.decode('utf-8')
        data = json.loads(dataunicode)  

        # 获取参数
        try:
            t_value = data['value']
        except Exception as e:
            return jsonMSGnoData(msg = 'bad req')   
        
        # 数据库操作
        try:
            t_user = User.objects.get(Username = t_username)
            t_user.Budget=int(t_value)
            t_user.save()
        except Exception as e:
            return jsonMSGnoData(msg = 'db error')     

        return jsonMSG('success','change budget successfully')
    if request.method == 'GET': 
        # 要在登录状态下
        if 'login_id' not in request.session:
            return jsonMSG(msg = 'no login')

        # 已经登录, 所以拿取用户信息
        t_username = request.session['login_id'] 
         # 数据库操作
        try:
            t_user = User.objects.get(Username = t_username)
            budget = t_user.Budget
        except Exception as e:
            return jsonMSG(msg = 'db error')     

        return jsonMSG('success','change budget successfully',budget)
  