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
  return render(request, "dice3.html", {"persons": persons})