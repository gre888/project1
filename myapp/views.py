from django.shortcuts import render
from django.http import HttpResponse



def sayhello(request):
    return HttpResponse("<b>Hello World 40!!!!!</b>")

def hello1(request,username):
    print(username)
    return HttpResponse(f"<b>Hello {username}!!!!!</b>")

from datetime import datetime
def hello2(request,username):
    print(f"username: {username}")
    now = datetime.now() #產生現在時間
    print(f"now: {now}") #列印現在時間
    # return HttpResponse("Hello2")
    return render(request, "hello2.html", locals())
  
def hello3(request,username):
    print(f"username: {username}")
    now = datetime.now() #產生現在時間
    print(f"now: {now}") #列印現在時間
    
    #return HttpResponse("Hello3")
    #return render(request, "hello3.html", locals())
    return render(request, "hello3_2.html", locals())
  
def hello4(request, username1, username2):
    print(username1)
    print(username2)
    return HttpResponse("Hello "+ username1 + " "+username2)
  
import random
def dice1(request):
    no1=random.randint(1,6)
    no2=random.randint(1,6)
    no3=random.randint(1,6)
    print(f"no1: {no1}, no2: {no2}, no3: {no3}")
    # return HttpResponse("Hello dice1")
    # return render(request, "dice1.html", locals())
    return render(request, "dice1.html", {"no1": no1, "no2": no2, "no3": no3})
def dice2(request):
  student = {'id':1234, "name": "John", 'sex': 'M'}
  fruits=['apple', 'banana', 'orange']
  print(student,fruits)
  return render(request, "dice2.html", {"student": student, "fruits": fruits})

def dice3(request):
  person1={'name':'Amy','phone':'049-1234567','age':'20'}
  person2={'name':'Jack','phone':'02-4455666','age':'25'}
  person3={'name':'Nacy','phone':'04-9876543','age':'17'}
  persons=[person1, person2, person3]
  print(persons)
  persons=[] #模擬無資料情況
  return render(request, "dice3.html", {"persons": persons})

def get1(request):
    # name=request.GET.get["name"]
    # city=request.GET.get["city"]
    #basic -07.py
    #透過get()方法取得GET請求的參數值
    name=request.GET.get("name", None) #若沒有name參數，則回傳None
    city=request.GET.get("city", None)
    print(f"name: {name}, city: {city}")  
    # return HttpResponse("Hello get")
    return render(request, "get1.html", locals())

def get2(request):
  try:
    name=request.GET["name"] #利用try except來捕捉例外，若沒有name參數，則會產生KeyError例外
    city=request.GET["city"]
    status=True
    print(f"name: {name}, city: {city}")
  except:
    status=False
    print(f'status: {status}')
    # return HttpResponse("請輸入完整的姓名和城市")
  return render(request, "get2.html", locals())


def get3(request, mode):
  print(f"mode: {mode}")
  # return HttpResponse(f"Hello get3, mode: {mode}")
  if mode == "save":
    username=request.GET.get("username") #檢查GET請求中是否有username參數，若有則取得其值，若沒有則回傳None
    password=request.GET.get("password")
    print(f"username: {username}, passwd: {password}")
    # return HttpResponse("表單已送出")
    return render(request, "get3_response.html", locals())
  elif mode == "load":
    return render(request, "get3.html", locals())
  
  
def post1(request):
  if request.method == "POST":
    # return HttpResponse("表單已送出")
    username=request.POST.get("username", None).strip() #去除前後空白
    password=request.POST.get("password", None).strip()
    print(f"username: {username}, passwd: {password}")
    # username=request.POST['username'] #前端已經擋了 所以不用get也可以擋
    # password=request.POST['password'] 

    if username == 'admin' and password == '1234':
      # return HttpResponse("登入成功")
      status=True
    else:
      # return HttpResponse("登入失敗")
      status=False
    return render(request, "post1_response.html", locals())
  else:
    return render(request, "post1.html", locals())
  
def post2(request):
  if request.method == "POST":
    items=request.POST.getlist('items') #取得多選checkbox的值，回傳為list
    print(items)
    return render(request, "post2_response.html", locals())
  else:
    return render(request, "post2.html", locals())










  