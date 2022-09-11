
from xml.etree.ElementTree import tostring
from django.shortcuts import render
import datetime

import pyrebase


Config={
    "apiKey": "AIzaSyCPxYzRtwgkbRTC2sYbflSCWR1OJw-CLNc",
    "authDomain": "bindasplay-91539.firebaseapp.com",
    "databaseURL": "https://bindasplay-43d58-default-rtdb.firebaseio.com",
    'projectId': "bindasplay-43d58",
    'storageBucket': "bindasplay-91539.appspot.com",
    "messagingSenderId": "848155187545",
    "appId": "1:848155187545:web:7c9beefecba1479c5a1448",
    "measurementId": "G-QYR2NPPB22"
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()

def Userview(request):
    try:
        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
    
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]
        data = db.child('Notifications').child(curr).get().val()
        if(data):
            row = data['notification']
        return render(request,"Userinterface.html", {"row":row})
    except Exception as e:
        print("error:",e)
        return render(request,"Userinterface.html")


def displayResult(request):
    try:
        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
        
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]
        data = db.child('data').child(curr).get()
        data_list=[]
        rows=[]
        for x in data.each():
            data_list.append(x.val())
            
            for row in data_list:
                d = row.values()
                y=list(d)
            rows.append(y)
      
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute
        

        res=[]
        for row in rows:
           
            l = row[3].split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            if(h < hour):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
            elif(h==hour and m<=min):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
        return render(request,"displayresult.html",{'rows':res}) 
    except Exception as e:
        print('err:  ',e)
        return render(request,"displayresult.html")



def saveResult(request):
    try:
        time=request.GET['time']
        number1=request.GET['number1']
        number2=request.GET['number2']
        number3=request.GET['number3']
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]


        row = {"time":time,"num1":number1,"num2":number2,"num3":number3}
        db.child('data').child(curr).child(time).set(row)
        
        return render(request,"dasboard.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"dasboard.html", {'status': False})


def SearchByDate(request):
    try:
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]

        date = request.GET['date'] 
        curr=date[2:] 

        curr_str = str(curr)

        c_list = curr_str.split("-")
        t_list = t_date.split("-")

        t_y = int(t_list[0])
        t_m = int(t_list[1])
        t_d = int(t_list[2])

        c_y = int(c_list[0])
        c_m = int(c_list[1])
        c_d = int(c_list[2])
        
        data = db.child('data').child(curr).get()
        data_list=[]
        rows=[]
        for x in data.each():
            data_list.append(x.val())
            
            for row in data_list:
                d = row.values()
                y=list(d)
            rows.append(y)
      
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute
        

        res=[]

        if (c_m<=t_m and c_y<=t_y):

            if(c_d <t_d):
                for row in rows:
            
                    l = row[3].split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    
                    if(h==12):
                        Ho = str(h)
                        Mi = str(m)
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    elif(h>12):
                        h=h-12
                        Ho = str(h)
                        Mi = str(m)
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    else:
                        Ho = str(h)
                        Mi = str(m)
                        t=Ho+":"+Mi+"am"
                        row[3] = t
                    res.append(row)

            elif (c_d==t_d):
                for row in rows:
                
                    l = row[3].split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    if(h == hour and m<=min):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)
                    elif(h<hour):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)

        return render(request,"resultbydate.html",{'rows':res}) 
    except Exception as e:
        print('errooooor:',e)
        return render(request,'resultbydate.html')

def SearchAll(request):
    try:
        date = request.GET['date']
        curr=date[2:]
        
        data = db.child('data').child(curr).get()
        data_list=[]
        rows=[]
        for x in data.each():
            data_list.append(x.val())
            
            for row in data_list:
                d = row.values()
                y=list(d)
            rows.append(y)

        res=[]
        for row in rows:
           
            l = row[3].split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            
            if(h==12):
                Ho = str(h)
                Mi = str(m)
                t=Ho+":"+Mi+"pm"
                row[3] = t
            elif(h>12):
                h=h-12
                Ho = str(h)
                Mi = str(m)
                t=Ho+":"+Mi+"pm"
                row[3] = t
            else:
                Ho = str(h)
                Mi = str(m)
                t=Ho+":"+Mi+"am"
                row[3] = t
            res.append(row)

        return render(request,"editresult.html",{'rows':res}) 
    except Exception as e:
        print('erreeee:  ',e)
        return render(request,'editresult.html')


def Notification(request):
    return render(request,"Notifications.html")

def AddNotification(request):
    try:
        notification=request.GET['notification']
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]


        row = {"notification":notification}
        db.child('Notifications').child(curr).set(row)
        
        return render(request,"Notifications.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"Notifications.html", {'status': False})