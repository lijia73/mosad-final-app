# API 设计文档

## 状态说明

|       状态        |                   说明                   |     应用API      |
| :---------------: | :--------------------------------------: | :--------------: |
|      success      |               表明成功返回               |     所有API      |
|       fail        |    表明请求失败，详细信息在msg中给出     |     所有API      |

## API概览
- 用户Account
  - 用户注册 POST /account/register
  - 用户登录 POST /account/login
  - 获取用户登录信息 GET /account/login
  - 退出登录 DELETE /account/logout
  - 更新登录用户信息 PUT /account/info/{attr:string}
  - 获取登录用户信息 GET /account/info
  - 获取预算 GET /account/budget
  - 更新预算 POST /account/budget
- 记录Record
  - 上传记账记录 POST /record/
  - 获取指定记账记录 GET /record/detail/{record_id:string}
  - 删除指定记账记录 DELETE /record/detail/{record_id:string}
  - 获取全部记账记录 GET /record/all
  - 获取全部指定时间段内的记账记录 GET /record/allwithtime
## Account
### 用户注册

```
POST /account/register
```

#### Request

| 参数名      | 类型   | 描述          |   位置  |
| ----------- | ------ | ------------- |---------|
| username    | string | 用户名        |   body  |
| password    | string | 密码          |   body  |

* 参数使用表单形式提交

##### Example

```json
{
	"username": "lijia",
	"password": "123456"
}
```

#### Response

> Status: 200 OK
>
> Location: /account/register

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 | 
|  msg   | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
	"state": "success",
  "msg": "register successfully"
}
```

### 用户登录

```
POST /account/login
```

#### Request

| 参数名      | 类型   | 描述          |   位置  |
| ----------- | ------ | ------------- |---------|
| username    | string | 用户名        |   body  |
| password    | string | 密码          |   body  |

* 参数使用表单形式提交

##### Example

```json
{
	"username": "lijia",
	"password": "123456"
}
```

#### Response

> Status: 200 OK
>
> Location: /account/login

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: | 
| state  | string | 状态 |
|  msg   | string | 消息 | 

* 参数使用json形式解析

##### Example
```json
{
	"state": "success",
  "msg":"login successfully"
}
```

### 获取用户登录信息

```
GET /account/login
```


#### Response

> Status: 200 OK
>
> Location: /account/login

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: | 
| state  | string | 状态 |
|  msg   | string | 消息 | 

* 参数使用json形式解析

##### Example
```json
{
	"state": "success",
  "msg":"already login"
}
```

### 退出登录

```
DELETE /account/logout
```

#### Response

> Status: 200 OK
>
> Location: /account/logout

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: | 
| state  | string | 状态 |
|  msg   | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
	"state": "success",
  "msg":"logout successfully"
}
```


### 更新登录用户信息

```
PUT /account/info/{attr:string}
```
* attr (Available values) : Password, Gender, Region, Nickname

#### Request

| 参数名      | 类型   | 描述          |   位置  |
| ----------- | ------ | ------------- |---------|
| value       | string | 更新值        |   body  |


* 参数使用json形式提交

##### Example

```json
{
	"value": "lijianew"
}
```

#### Response

> Status: 200 OK
>
> Location: /account/info/Nickname

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg  | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "change successfully",
}
```


### 获取登录用户信息

```
GET /account/info
```

#### Response

> Status: 200 OK
>
> Location: /account/info
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |
|  data  | dictionary | 用户信息 |


* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "success",
    "data": {
        "Username": "lijia",
        "Gender": "male",
        "Region": "earth",
        "Nickname": "fresh",
        "Avatar": ""
    }
}
```

### 获取预算
```
GET /account/budget
```

#### Response

> Status: 200 OK
>
> Location: /account/budget

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg  | string | 消息 |
|  data  | integer | 预算值 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "change budget successfully",
    "data":3000,
}
```

### 更新预算
```
POST /account/budget
```

#### Request

| 参数名      | 类型   | 描述          |   位置  |
| ----------- | ------ | ------------- |---------|
| value       | integer| 更新值        |   body  |


* 参数使用json形式提交

##### Example

```json
{
	"value": 1000
}
```

#### Response

> Status: 200 OK
>
> Location: /account/budget

| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg  | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "change budget successfully",
}
```

## Record
### 上传记账记录

```
POST /record/
```

#### Request

| 参数名      | 类型   | 描述          |   位置  |
| ----------- | ------ | ------------- |---------|
| type        | string | 类型          |   body  |
| time        | string | unix时间戳    |   body  |
| amount      | integer| 金额          |   body  |
| comment     | string | 备注          |   body  |


* 参数使用json形式提交

##### Example

```json
{
    "type":"早餐",
    "time":"1608148248000",
    "amount":30,
    "comment":"breakfast",
    "class":0
}
```

#### Response

> Status: 200 OK
>
> Location: /record/
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "add record successfully"
}
```

### 获取指定记账记录

```
GET /record/detail/{record_id:string}
```

#### Response

> Status: 200 OK
>
> Location: /record/detail/b467329bda274f05a2dd03e6
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |
|  data  | array  | 记录数据 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "get record detail successfully",
    "data": [
        {
            "id": "144092c227074b0aac6ebc98",
            "type": "早餐",
            "time": "1608148248000",
            "amount": 30,
            "comment": "breakfast",
            "class": true
        }
    ]
}
```


### 删除指定记账记录

```
DELETE /record/detail/{record_id:string}
```

#### Response

> Status: 200 OK
>
> Location: /record/detail/b467329bda274f05a2dd03e6
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "delete record successfully"
}
```

### 获取全部记账记录

```
GET /record/all
```


#### Response

> Status: 200 OK
>
> Location: /record/all
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |
|  data  | array  | 记录数据 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "get all record successfully",
    "data": [
        {
            "id": "144092c227074b0aac6ebc98",
            "type": "早餐",
            "time": "1608148248000",
            "amount": 30,
            "comment": "breakfast",
            "class": true
        }
    ]
}
```

### 获取全部指定时间段内的记账记录

```
GET /record/allwithtime
```


#### Parameters

| 字段     | 类型   | 描述   |
| -------- | ------ | ------ |
| begin    | number | 开始时间 |
| end      | number | 结束时间 |

#### Response

> Status: 200 OK
>
> Location: /record/allwithtime?begin=1608148248000&end=1609163672000
> 
| 参数名 |  类型  | 描述 |
| :----: | :----: | :--: |
| state  | string | 状态 |
|  msg   | string | 消息 |
|  data  | array  | 记录数据 |

* 参数使用json形式解析

##### Example
```json
{
    "state": "success",
    "msg": "get all record with time successfully",
    "data": [
        {
            "id": "144092c227074b0aac6ebc98",
            "type": "早餐",
            "time": "1608148248000",
            "amount": 30,
            "comment": "breakfast",
            "class": true
        }
    ]
}
```

## Model
```
User{
    UserID	integer 主键：用户id
    Username    string  用户名
    Password	string  密码
    Phone	string  手机号
    Email	string  邮箱
    Nickname	string  昵称
    Avatar	string 头像 
    Description	string 描述
}
Record{
    RecordID    string 主键：记录id，24位16进制数
    Type    string  类型
    Time    string  发布时间（Unix时间戳）
    Ownusername string 发布者
    Amount  integer 金额
    Comment string  备注
    Class   bool  支出/收入
}

```
