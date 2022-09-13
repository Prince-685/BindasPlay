from calendar import weekday
from django.shortcuts import render
from random import randrange
import pyrebase
import datetime




Config={
    'apiKey': "AIzaSyBuypl8nEeB0NbRdu3Nt2_6h3gYVPZvcHE",
    'authDomain': "bindasplay-43d58.firebaseapp.com",
    'databaseURL': "https://bindasplay-43d58-default-rtdb.firebaseio.com",
    'projectId': "bindasplay-43d58",
    'storageBucket': "bindasplay-43d58.appspot.com",
    'messagingSenderId': "566594345888",
    'appId': "1:566594345888:web:7cb38cbcfeca0d22d622c5",
    'measurementId': "G-T3LLGYGPT2"
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()


def TypeSubmit1(request):
    try:
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
            
        return render(request,"dasboard.html")
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")


def TypeSubmit2(request):
    try:
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
        return render(request,"dasboard.html")
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")

def TypeSubmit3(request):
    try:
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
        return render(request,"dasboard.html")
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")

    

