from calendar import weekday
from django.shortcuts import render
import datetime
from random import randrange
import pyrebase
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
from authentication.views import checkUserCredentials

# Config = {
#   "apiKey": "AIzaSyBE8thS3U1OK6ALzc5bPBe1P_KprxYHVKw",
#   "authDomain": "bindasplay-cb08d.firebaseapp.com",
#   "databaseURL": "https://bindasplay-cb08d-default-rtdb.firebaseio.com",
#   "projectId": "bindasplay-cb08d",
#   "storageBucket": "bindasplay-cb08d.appspot.com",
#   "messagingSenderId": "374562043128",
#   "appId": "1:374562043128:web:b3e70f1c0256afe407b70d",
#   "measurementId": "G-67NLCESH35"
# }

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
firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()

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

firebase1 = pyrebase.initialize_app(Config2)
authe1 = firebase1.auth()
db1 = firebase.database()

Config3 = {
  "apiKey": "AIzaSyDxFBqlyY2_eNGJRNyya4F0lS8vR4ArCrM",
  "authDomain": "milan-71cf2.firebaseapp.com",
  "databaseURL":"https://milan-71cf2-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "milan-71cf2",
  "storageBucket": "milan-71cf2.appspot.com",
  "messagingSenderId": "908285293971",
  "appId": "1:908285293971:web:cbf52f52b75f5afc846466"
}


firebase2=pyrebase.initialize_app(Config3)
auth=firebase2.auth()
db2=firebase2.database()


def Userview(request):
    try:
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        data = db.child('Notifications').get()
        data1=db2.child('Game1').child(d).child('open').child('number').get().val()
        data2=db2.child('Game1').child(d).child('center').child('number').get().val()
        data3=db2.child('Game1').child(d).child('close').child('number').get().val()
        d1=db2.child('Game2').child(d).child('open').child('number').get().val()
        d2=db2.child('Game2').child(d).child('center').child('number').get().val()
        d3=db2.child('Game2').child(d).child('close').child('number').get().val()
        g1=db2.child('Gname').child('G1').child('G1').get().val()
        g2=db2.child('Gname').child('G2').child('G2').get().val()
        result1=[]
        result2=[]
        if data1 and data2:
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute
            time_min = hour * 60 + min 
            if time_min>=810:
                r1=data1+'-'+data2[0]
                result1.append(r1)
                if time_min>=930 and data3:
                    r2=data1+'-'+data2+'-'+data3
                    result1[0]=r2
            else:result1.append('Coming Soon')
            
        else:
            result1.append('Coming Soon...')

        
        if d1 and d2:
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute
            time_min = hour * 60 + min 
            if time_min>=1230:
                r=d1+'-'+d2[0]
                result2.append(r)
                if d3 and time_min>=1350:
                    r=d1+'-'+d2+'-'+d3
                    result2[0]=r
                
            else:result2.append('Coming Soon...')

            
        else:
            result2.append('Coming Soon...')
        row=[]
        if(data):
            for x in data.each():
                row.append(x.val())

        row.append(g1)
        row.append(g2)
        

        return render(request,"Userinterface.html",{"row":row,'result1':result1,'result2':result2})
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

        
        data1 = db.child('data1').child(curr).get()
        data2 = db.child('data2').child(curr).get()
        data3 = db.child('data3').child(curr).get()
        
        
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        
        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)
        
        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)           
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute
        res=[]
        for row in new:
            x = row[3]
            l = x.split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            if(h < hour):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
            elif(h==hour and m<=min):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)

        return render(request,"displayresult.html",{"rows":res}) 
    except Exception as e:
        print('err:  ',e)
        return render(request,"displayresult.html")


def saveResult(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
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

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
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
        
        data1 = db.child('data1').child(curr).get()
        data2 = db.child('data2').child(curr).get()
        data3 = db.child('data3').child(curr).get()
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)

        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)           
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute
        

        res=[]
        if (c_y<t_y):
            for row in new:
                x=row[3]
                l = x.split(":")
                h_s = l[0]
                m_s = l[1]
                
                h = int(h_s)
                m = int(m_s)
                
                
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
        elif (c_m==t_m and c_y==t_y):

            if(c_d <t_d):
                for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    
                    if(h==12):
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    elif(h>12):
                        h=h-12
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    else:
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"am"
                        row[3] = t
                    res.append(row)
            elif (c_d==t_d):
                
                for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    h = int(h_s)
                    m = int(m_s)
                    
                    if(h == hour and m<=min):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)
                    elif(h<hour):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)

        elif (c_m<t_m and c_y==t_y):
            for row in new:
                x=row[3]
                l = x.split(":")
                h_s = l[0]
                m_s = l[1]
                
                h = int(h_s)
                m = int(m_s)
                
                
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
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
        
        data1 = db.child('data1').child(curr).get()
        data2 = db.child('data2').child(curr).get()
        data3 = db.child('data3').child(curr).get()
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)

        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)        

        res=[]
        for row in new:
           
            l = row[3].split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            
            if(h==12):
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"pm"
                row[3] = t
            elif(h>12):
                h=h-12
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"pm"
                row[3] = t
            else:
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"am"
                row[3] = t
            res.append(row)

        return render(request,"editresult.html",{'rows':res}) 
    except Exception as e:
        print('erreeee:  ',e)
        return render(request,'editresult.html')


def Notification(request):
    data = db.child('Notifications').get()
    rows=[]
    if(data):
        for x in data.each():
            rows.append(x.val())
        
        row = rows[0]
    return render(request,"Notifications.html",{"row":row})


def AddNotification(request):
    try:
        notification=request.GET['notification']
        
        row = {"notification":notification}
        db.child('Notifications').set(row)
        
        return render(request,"Notifications.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"Notifications.html", {'status': False})