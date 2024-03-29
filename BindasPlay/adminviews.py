from django.shortcuts import render
from django.contrib import messages
from random import randrange
import pyrebase
import datetime
from django.contrib.auth import authenticate
from authentication.views import checkUserCredentials
from calendar import weekday
from collections import  OrderedDict
import random


Config2 = {
  "apiKey": "AIzaSyBE8thS3U1OK6ALzc5bPBe1P_KprxYHVKw",
  "authDomain": "bindasplay-cb08d.firebaseapp.com",
  "databaseURL": "https://bindasplay-cb08d-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-cb08d",
  "storageBucket": "bindasplay-cb08d.appspot.com",
  "messagingSenderId": "374562043128",
  "appId": "1:374562043128:web:b3e70f1c0256afe407b70d",
  "measurementId": "G-67NLCESH35"
}


Config = {
  "apiKey": "AIzaSyBuypl8nEeB0NbRdu3Nt2_6h3gYVPZvcHE",
  "authDomain": "bindasplay-43d58.firebaseapp.com",
  "databaseURL":"https://bindasplay-43d58-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-43d58",
  "storageBucket": "bindasplay-43d58.appspot.com",
  "messagingSenderId": "566594345888",
  "appId": "1:566594345888:web:7cb38cbcfeca0d22d622c5",
  "measurementId": "G-T3LLGYGPT2"
}

Config3 = {
  "apiKey": "AIzaSyDxFBqlyY2_eNGJRNyya4F0lS8vR4ArCrM",
  "authDomain": "milan-71cf2.firebaseapp.com",
  "databaseURL":"https://milan-71cf2-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "milan-71cf2",
  "storageBucket": "milan-71cf2.appspot.com",
  "messagingSenderId": "908285293971",
  "appId": "1:908285293971:web:cbf52f52b75f5afc846466"
}


firebase1 = pyrebase.initialize_app(Config2)
auth = firebase1.auth()
db1 = firebase1.database()


firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()

firebase2=pyrebase.initialize_app(Config3)
auth=firebase2.auth()
db2=firebase2.database()
 

def ATypeSubmit1(request):
    try:

        # print(username)
        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn1=="automatic"):
        #     row={"b1":"manual"}
        #     db.child('btn1').set(row)

        # elif(btn1=="manual"):
        #     row={"b1":"automatic"}
        #     db.child('btn1').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]

        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('data1').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('data1').child(t_date).child(t).set(row)

                # d1 = db.child('btn1').child('b1').get()
                # b1=d1.val()
            
        return render(request,"adminbindas.html")
        # return render(request,"dasboard.html",{"btn1":b1,"btn2":btn2,"btn3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminbindas.html")


def ATypeSubmit2(request):
    try:

        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn2=="automatic"):
        #     row={"b2":"manual"}
        #     db.child('btn2').set(row)

        # elif(btn2=="manual"):
        #     row={"b2":"automatic"}
        #     db.child('btn2').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('data2').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('data2').child(t_date).child(t).set(row)

            # d2 = db.child('btn2').child('b2').get()
            # b2=d2.val()
        return render(request,"adminbindas.html")
        # return render(request,"dasboard.html",{"btn1":btn1,"btn2":b2,"btn3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminbindas.html")

def ATypeSubmit3(request):
    try:

        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn3=="automatic"):
        #     row={"b3":"manual"}
        #     db.child('btn3').set(row)

        # elif(btn3=="manual"):
        #     row={"b3":"automatic"}
        #     db.child('btn3').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('data3').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('data3').child(t_date).child(t).set(row)
            
            # d3 = db.child('btn3').child('b3').get()
            # b3=d3.val()
            
        return render(request,"adminbindas.html")
        # return render(request,"dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":b3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminbindas.html")

def ATypeSubmitKalyan1(request):
    try:
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        
        # if(bt1=="automatic"):
        #     row={"b1":"manual"}
        #     db.child('kBtn1').set(row)

        # elif(bt1=="manual"):
        #     row={"b1":"automatic"}
        #     db.child('kBtn1').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('kalyandata1').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('kalyandata1').child(t_date).child(t).set(row)

            # dat1= db.child('kBtn1').child('b1').get()
            # btn1=dat1.val()
            
        return render(request,"adminkalyan.html")
        # return render(request,"kalyandasboard.html",{"b1":btn1,"b2":bt2,"b3":bt3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminkalyan.html")


def ATypeSubmitKalyan2(request):
    try:
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        # if(bt2=="automatic"):
        #     row={"b2":"manual"}
        #     db.child('kBtn2').set(row)

        # elif(bt2=="manual"):
        #     row={"b2":"automatic"}
        #     db.child('kBtn2').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute


        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('kalyandata2').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('kalyandata2').child(t_date).child(t).set(row)

            # d2= db.child('kBtn2').child('b2').get()
            # btn2=d2.val()
            
        return render(request,"adminkalyan.html")
        # return render(request,"kalyandasboard.html",{"b1":bt1,"b2":btn2,"b3":bt3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminkalyan.html")


def ATypeSubmitKalyan3(request):
    try:
        
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        # if(bt3=="automatic"):
        #     row={"b3":"manual"}
        #     db.child('kBtn3').set(row)

        # elif(bt3=="manual"):
        #     row={"b3":"automatic"}
        #     db.child('kBtn3').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('kalyandata3').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('kalyandata3').child(t_date).child(t).set(row)

            # d3= db.child('kBtn3').child('b3').get()
            # btn3=d3.val()
            
        return render(request,"adminkalyan.html")
        # return render(request,"kalyandasboard.html",{"b1":bt1,"b2":bt2,"b3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"adminkalyan.html")

def AsaveResult(request):
    try:

        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
        
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]

        time1=request.GET['time']
        number1=request.GET['number1']
        number2=request.GET['number2']
        number3=request.GET['number3']
        if(len(number1)==1):
            number1 = "0"+number1
        if(len(number2)==1):
            number2 = "0"+number2
        if(len(number3)==1):
            number3 = "0"+number3

        curr_hour = time1[0:2]
        curr_min = time1[3:]
        h = int(curr_hour)
        m = int(curr_min)
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        min= time.minute

        if(hour < h):
            if(number1):
                if(weekday!=6):
                    row={"num1":number1}
                    db.child('data1').child(curr).child(time1).set(row)
            if(number2):
                if(weekday!=6):
                    row={"num2":number2}
                    db.child('data2').child(curr).child(time1).set(row)
            if(number3):
                if(weekday!=6):
                    row={"num3":number3}
                    db.child('data3').child(curr).child(time1).set(row)
        elif( hour==h):
            if min<m :
                if(number1):
                    if(weekday!=6):
                        row={"num1":number1}
                        db.child('data1').child(curr).child(time1).set(row)
                if(number2):
                    if(weekday!=6):
                        row={"num2":number2}
                        db.child('data2').child(curr).child(time1).set(row)
                if(number3):
                    if(weekday!=6):
                        row={"num3":number3}
                        db.child('data3').child(curr).child(time1).set(row)
        
        return render(request,"adminbindas.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"adminbindas.html", {'status': False})

def AsaveResultKalyan(request):

    try:

        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
        
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]

        time2=request.GET['kalyantime']
        number1=request.GET['kalyannumber1']
        number2=request.GET['kalyannumber2']
        number3=request.GET['kalyannumber3']
        if(len(number1)==1):
            number1 = "0"+number1
        if(len(number2)==1):
            number2 = "0"+number2
        if(len(number3)==1):
            number3 = "0"+number3

        curr_hour = time2[0:2]
        curr_min = time2[3:]
        h = int(curr_hour) 
        m = int(curr_min)
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        
        if(hour < h):
            if(number1):
                if(weekday!=6):
                    row={"num1":number1}
                    db.child('kalyandata1').child(curr).child(time2).set(row)
            if(number2):
                if(weekday!=6):
                    row={"num2":number2}
                    db.child('kalyandata2').child(curr).child(time2).set(row)
            if(number3):
                if(weekday!=6):
                    row={"num3":number3}
                    db.child('kalyandata3').child(curr).child(time2).set(row)
        
        return render(request,"adminkalyan.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"adminkalyan.html", {'status': False})

def AMilanSubmit(request):
    try:
        slot=request.GET['type']
        firstnum=request.GET['firstNum']
        secondnum=request.GET['secondNum']
        thirdnum=request.GET['thirdNum']
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")

        
        a=str(firstnum)+str(secondnum)+str(thirdnum)
        if slot=='open':
            row={'number':a}
            db2.child('Game1').child(d).child('open').set(row)
            b=int(firstnum)+int(secondnum)+int(thirdnum)
            b=b%10
            rrr={'number':b}
            db2.child('Game1').child(d).child('center').set(rrr)
        if slot=='close':
                    row={'number':a}
                    db2.child('Game1').child(d).child('close').set(row)
                    b=int(firstnum)+int(secondnum)+int(thirdnum)
                    b=b%10
                    mid=db2.child('Game1').child(d).child('center').get()
                    ordered_dict = mid.val()
                    value = ordered_dict['number']
                    if value==0:res='0'+str(b)
                    else:res=value*10+b
                    res=str(res)
                    rrr={'number':res}
                    db2.child('Game1').child(d).child('center').update(rrr)


        messages.success(request, 'Data is Saved Successfully')
        return render(request,"PanelDashboard.html",{'status':True})

    except Exception as e:
        print("errr:::",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard.html", {'status': False})
    
def AautoMilanSubmit(request):
    try:
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')

        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        first_index = random.randint(0, 8)
        second_index = random.randint(first_index , 9)
        third_index = random.randint(second_index , 9)
        
        firstnum = values[first_index]
        secondnum = values[second_index]
        thirdnum = values[third_index]
        a=str(firstnum)+str(secondnum)+str(thirdnum)
        
        row={'number':a}
        db2.child('Game1').child(d).child('open').set(row)
        b=int(firstnum)+int(secondnum)+int(thirdnum)
        b=b%10
        rrr={'number':b}
        db2.child('Game1').child(d).child('center').set(rrr)

        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        first_i = random.randint(0, 8)
        second_i = random.randint(first_i , 9)
        third_i = random.randint(second_i , 9)
        
        firstNum = value[first_i]
        secondNum = value[second_i]
        thirdNum = value[third_i]
        b=str(firstNum)+str(secondNum)+str(thirdNum)
        row={'number':b}
        db2.child('Game1').child(d).child('close').set(row)
        c=int(firstNum)+int(secondNum)+int(thirdNum)
        c=c%10
        mid=db2.child('Game1').child(d).child('center').get()
        ordered_dict = mid.val()
        value = ordered_dict['number']
        if value==0:res='0'+str(c)
        else:res=value*10+c
        res=str(res)
        rrr={'number':res}
        db2.child('Game1').child(d).child('center').update(rrr)

        messages.success(request, 'Data is Saved Successfully')
        return render(request,"PanelDashboard.html")
    
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard.html")

def Aholidaysubmit(request):
    try:
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        row={'number':'***'}
        db2.child('Game1').child(d).child('open').set(row)
        row={'number':'***'}
        db2.child('Game1').child(d).child('close').set(row)
        rrr={'number':'**'}
        db2.child('Game1').child(d).child('center').set(rrr)

        messages.success(request, 'Today is Holiday Successfully Set')
        return render(request,"PanelDashboard.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard.html")

def AMilan2Submit(request):
    try:
        slot=request.GET['type']
        firstnum=request.GET['firstNum']
        secondnum=request.GET['secondNum']
        thirdnum=request.GET['thirdNum']
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")
        if day=='Sunday':
            messages.error(request, 'Oops Today is Sunday ')
            return render(request,"PanelDashboard2.html", {'status': False})

        a=str(firstnum)+str(secondnum)+str(thirdnum)
        if slot=='open':
            row={'number':a}
            db2.child('Game2').child(d).child('open').set(row)
            b=int(firstnum)+int(secondnum)+int(thirdnum)
            b=b%10
            rrr={'number':b}
            db2.child('Game2').child(d).child('center').set(rrr)
        if slot=='close':
                    row={'number':a}
                    db2.child('Game2').child(d).child('close').set(row)
                    b=int(firstnum)+int(secondnum)+int(thirdnum)
                    b=b%10
                    mid=db2.child('Game2').child(d).child('center').get()
                    ordered_dict = mid.val()
                    value = ordered_dict['number']
                    if value==0:res='0'+b
                    else:res=value*10+str(b)
                    res=str(res)
                    rrr={'number':res}
                    db2.child('Game2').child(d).child('center').update(rrr)

        messages.success(request, 'Data is Saved Successfully')
        return render(request,"PanelDashboard2.html",{'status':True})

    except Exception as e:
        print("errr:::",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard2.html", {'status': False})

def AautoMilan2Submit(request):
    try:
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")
        
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        first_index = random.randint(0, 8)
        second_index = random.randint(first_index , 9)
        third_index = random.randint(second_index , 9)
        
        firstnum = values[first_index]
        secondnum = values[second_index]
        thirdnum = values[third_index]
        a=str(firstnum)+str(secondnum)+str(thirdnum)
        
        if day=='Sunday':
            messages.error(request, 'Oops Today is Sunday ')
            return render(request,"PanelDashboard2.html", {'status': False})

        row={'number':a}
        db2.child('Game2').child(d).child('open').set(row)
        b=int(firstnum)+int(secondnum)+int(thirdnum)
        b=b%10
        rrr={'number':b}
        db2.child('Game2').child(d).child('center').set(rrr)

        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        first_i = random.randint(0, 8)
        second_i = random.randint(first_i , 9)
        third_i = random.randint(second_i , 9)
        
        firstNum = value[first_i]
        secondNum = value[second_i]
        thirdNum = value[third_i]
        b=str(firstNum)+str(secondNum)+str(thirdNum)
        row={'number':b}
        db2.child('Game2').child(d).child('close').set(row)
        c=int(firstNum)+int(secondNum)+int(thirdNum)
        c=c%10
        mid=db2.child('Game2').child(d).child('center').get()
        ordered_dict = mid.val()
        value = ordered_dict['number']
        if value==0:res='0'+str(c)
        else:res=value*10+c
        res=str(res)
        rrr={'number':res}
        db2.child('Game2').child(d).child('center').update(rrr)

        messages.success(request, 'Data is Saved Successfully')
        return render(request,"PanelDashboard2.html")
    
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard2.html")

def Aholiday2submit(request):
    try:
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        row={'number':'***'}
        db2.child('Game2').child(d).child('open').set(row)
        row={'number':'***'}
        db2.child('Game2').child(d).child('close').set(row)
        rrr={'number':'**'}
        db2.child('Game2').child(d).child('center').set(rrr)

        messages.success(request, 'Today is Holiday Successfully Set')
        return render(request,"PanelDashboard2.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"PanelDashboard2.html")


def Gname(request):
    try:
        gname=request.GET['gameName']
        if(gname):
            row={'G1':gname}
            db2.child('Gname').child('G1').set(row)
        messages.success(request, 'Game Name Successfully Set')
        return render(request,'PanelDashboard.html')
    except Exception as e:
        print('eeeeeee::',e)
        messages.error(request, 'An error occurred Game Name is not Saved')
        return render(request,'PanelDashboard.html')

def G2name(request):
    try:
        gname=request.GET['GameName']
        if(gname):
            row={'G2':gname}
            db2.child('Gname').child('G2').set(row)
        messages.success(request, 'Game Name Successfully Set')
        return render(request,'PanelDashboard2.html')
    except Exception as e:
        print('eeeeeee::',e)
        messages.error(request, 'An error occurred Game Name is not Saved')
        return render(request,'PanelDashboard2.html')

def PreviousDatapage(request):
    return render(request,'PreviousDate.html')

def AddPreviousdata(request):
    try:
        gname=request.GET['gameName']
        date=request.GET['date']
        slot=request.GET['type']
        n1=request.GET['firstNum']
        n2=request.GET['secondNum']
        n3=request.GET['thirdNum']
        date=date[2:]

        a=str(n1)+str(n2)+str(n3)
        if slot=='open':
            row={'number':a}
            db2.child(gname).child(date).child('open').set(row)
            b=int(n1)+int(n2)+int(n3)
            b=b%10
            rrr={'number':b}
            db2.child(gname).child(date).child('center').set(rrr)
        if slot=='close':
                    row={'number':a}
                    db2.child(gname).child(date).child('close').set(row)
                    b=int(n1)+int(n2)+int(n3)
                    b=b%10
                    mid=db2.child(gname).child(date).child('center').get()
                    ordered_dict = mid.val()
                    value = ordered_dict['number']
                    if value==0:res='0'+str(b)
                    else:res=value*10+b
                    res=str(res)
                    rrr={'number':res}
                    db2.child(gname).child(date).child('center').update(rrr)
        messages.success(request, 'Data is Saved Successfully')
        return render(request,'PreviousDate.html')

    except Exception as e:
        print('error: ',e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,'PreviousDate.html')

    
