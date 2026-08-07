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
    return render(request, "hello3.html", locals())