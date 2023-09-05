from calendar import weekday
from django.shortcuts import render
from random import randrange
import pyrebase
import datetime
from datetime import datetime as dt
from authentication.views import checkUserCredentials
from django.contrib import messages
import random


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


def MilanSubmit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        slot=request.GET['type']
        firstnum=request.GET['firstNum']
        secondnum=request.GET['secondNum']
        thirdnum=request.GET['thirdNum']
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        
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
                    if value==0: 
                        res='0'+str(b)
                    else:res=value*10+b
                    res=str(res)
                    rrr={'number':res}
                    db2.child('Game1').child(d).child('center').update(rrr)
        messages.success(request, 'Data is Saved Successfully')
        return render(request,"Userpaneldashboard.html",{'status':True})
    except Exception as e:
        print("errr:::",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpaneldasboard.html", {'status': False})


def AutoMilanSubmit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')

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

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        
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
        if value==0: 
            res='0'+str(c)
        else:res=value*10+c
        res=str(res)
        rrr={'number':res}
        db2.child('Game1').child(d).child('center').update(rrr)

        messages.success(request, 'Data is Saved Successfully')
        return render(request,"Userpaneldashboard.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpaneldashboard.html")

def Holidaysubmit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')

        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")

        row={'number':'***'}
        db2.child('Game1').child(d).child('open').set(row)
        row={'number':'***'}
        db2.child('Game1').child(d).child('close').set(row)
        rrr={'number':'**'}
        db2.child('Game1').child(d).child('center').set(rrr)

        messages.success(request, 'Today is Holiday Successfully Set')
        return render(request,"Userpaneldashboard.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpaneldashboard.html")
    

def displayMilanPanelResult(request):
    try:
        g1=db2.child('Gname').child('G1').child('G1').get().val()
        gname=[g1]

        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        today = datetime.date.today()
        d = today.strftime('%y-%m-%d')

        day=today.strftime("%A")
        x=db2.child('Game1').get()
        date=[]
        slot=[]
        for a in x.each():
             y=a.key()
             date.append(y)
             s=db2.child('Game1').child(y).get()
             arr=[]
             for b in s.each():
                  
                  d=b.key()
                  f=db2.child('Game1').child(y).child(d).get()
                  l=f.val()
                  value=l['number']
                  arr.append(value)
             slot.append(arr)
        res=[]
        for i in range(len(date)):
            date_obj = dt.strptime(date[i], "%y-%m-%d").date()

            day = date_obj.strftime("%A")
            curr=''
            if day=='Monday':
                days_until_next_sunday = 6  # If today is Sunday, move to the next Sunday
                next_sunday = date_obj + datetime.timedelta(days=days_until_next_sunday)
                curr=date[i] +' '+'to'+' '+str(next_sunday)
                res.append(curr)
            
            today = datetime.date.today()
            d = today.strftime('%y-%m-%d')
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute

            time_min = hour * 60 + min

            if int(d[:2]) > int(date[i][:2]):
                res.append(slot[i][0])
                res.append(slot[i][1])
                res.append(slot[i][2])
            elif int(d[:2]) == int(date[i][:2]):
                if int(d[3:5]) > int(date[i][3:5]):
                    res.append(slot[i][0])
                    res.append(slot[i][1])
                    res.append(slot[i][2])
                elif int(d[3:5]) == int(date[i][3:5]):
                    if int(d[6:]) > int(date[i][6:]):
                        res.append(slot[i][0])
                        res.append(slot[i][1])
                        res.append(slot[i][2])
                    elif int(d[6:]) == int(date[i][6:]):
                        if time_min >= 810:
                            res.append(slot[i][0][0])
                            res.append(" ")
                            res.append(slot[i][2])
                        if time_min >= 930:
                            res[len(res)-3] = slot[i][0]
                            res[len(res)-2] = slot[i][1]
        
        result = []
        current_sublist = []

        for item in res:
            if isinstance(item, str) and ('to' in item):
                if current_sublist:
                    result.append(current_sublist)
                current_sublist = [item]
            else:
                current_sublist.append(item)

        if current_sublist:
            result.append(current_sublist)
        
        return render(request,'Panel.html',{'rows':result,"listRed":listRed,'gname':gname})
             
    except Exception as e:
        print('err::-',e)
        return render(request,'Userinterface.html')


def displayMilanJodiresult(request):
    try:
        g1=db2.child('Gname').child('G1').child('G1').get().val()
        gname=[g1]

        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        date=[]
        val=[]
        data=db2.child("Game1").get()
        for x in data.each():
            x=x.key()
            date.append(x)
            y=db2.child("Game1").child(x).child('center').get()
            ordered_dict = y.val()
            value = ordered_dict['number']
            val.append(value)
        
        res=[]
        for i in range(len(date)):
            date_obj = dt.strptime(date[i], "%y-%m-%d").date()

            day = date_obj.strftime("%A")
            curr=''
            if day=='Monday':
                days_until_next_sunday = 6  # If today is Sunday, move to the next Sunday
                next_sunday = date_obj + datetime.timedelta(days=days_until_next_sunday)
                curr=date[i] +' '+'to'+' '+str(next_sunday)
                res.append(curr)

            today = datetime.date.today()
            d = today.strftime('%y-%m-%d')
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute

            time_min = hour * 60 + min

            if int(d[:2]) > int(date[i][:2]):
                res.append(val[i])
            elif int(d[:2]) == int(date[i][:2]):
                if int(d[3:5]) > int(date[i][3:5]):
                    res.append(val[i])
                elif int(d[3:5]) == int(date[i][3:5]):
                    if int(d[6:]) > int(date[i][6:]):
                       res.append(val[i])
                    elif int(d[6:]) == int(date[i][6:]):
                        if time_min >= 810:
                            res.append(val[i][0])
                        if time_min >= 930:
                            res[len(res)-1] = val[i]
        
        result = []
        current_sublist = []

        for item in res:
            if isinstance(item, str) and ('to' in item):
                if current_sublist:
                    result.append(current_sublist)
                current_sublist = [item]
            else:
                current_sublist.append(item)

        if current_sublist:
            result.append(current_sublist)

        return render(request,'Jodi.html',{'rows':result,"listRed":listRed,'gname':gname})


    except Exception as e:
        print('errr__:',e)
        return render(request,'Userinterface.html')


def Milan2Submit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        slot=request.GET['type']
        firstnum=request.GET['firstNum']
        secondnum=request.GET['secondNum']
        thirdnum=request.GET['thirdNum']
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        
        a=str(firstnum)+str(secondnum)+str(thirdnum)
        if day=='Sunday':
            messages.error(request, 'Oops Today is Sunday')
            return render(request,'Userpanel2dashboard.html')
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
                    if value==0: 
                        res='0'+str(b)
                    else:res=value*10+b
                    res=str(res)
                    rrr={'number':res}
                    db2.child('Game2').child(d).child('center').update(rrr)
        messages.success(request, 'Data is Saved Successfully')
        return render(request,"Userpanel2dashboard.html",{'status':True})

    except Exception as e:
        print("errr:::",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpanel2dashboard.html", {'status': False})

def AutoMilan2Submit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
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

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        
        if day=='Sunday':
            messages.error(request, 'Oops Today is Sunday!!!')
            return render(request,'Userpanel2dashboard.html')

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
        if value==0: 
            res='0'+str(c)
        else:res=value*10+c
        res=str(res)
        rrr={'number':res}
        db2.child('Game2').child(d).child('center').update(rrr)


        messages.success(request, 'Data is Saved Successfully')
        return render(request,"Userpanel2dashboard.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpanel2dashboard.html")

def Holiday2submit(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")

        row={'number':'***'}
        db2.child('Game2').child(d).child('open').set(row)
        row={'number':'***'}
        db2.child('Game2').child(d).child('close').set(row)
        rrr={'number':'**'}
        db2.child('Game2').child(d).child('center').set(rrr)

        messages.success(request, 'Today is Holiday Successfully Set')
        return render(request,"Userpanel2dashboard.html")
    except Exception as e:
        print("error:",e)
        messages.error(request, 'An error occurred Data is not Saved')
        return render(request,"Userpanel2dashboard.html")
    
def displayMilanPanel2Result(request):
    try:
        g2=db2.child('Gname').child('G2').child('G2').get().val()
        gname=[g2]

        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        today = datetime.date.today()
        d= today.strftime('%y-%m-%d')
        day=today.strftime("%A")
        x=db2.child('Game2').get()
        date=[]
        slot=[]
        for a in x.each():
             y=a.key()
             date.append(y)
             s=db2.child('Game2').child(y).get()
             arr=[]
             for b in s.each():
                  
                  d=b.key()
                  f=db2.child('Game2').child(y).child(d).get()
                  l=f.val()
                  value=l['number']
                  arr.append(value)
             slot.append(arr)
        res=[]
        for i in range(len(date)):
            date_obj = dt.strptime(date[i], "%y-%m-%d").date()

            day = date_obj.strftime("%A")
            curr=''
            if day=='Monday':
                days_until_next_sat = 5  # If today is Sunday, move to the next Sunday
                next_sat = date_obj + datetime.timedelta(days=days_until_next_sat)
                curr=date[i] +' '+'to'+' '+str(next_sat)
                res.append(curr)
            
            today = datetime.date.today()
            d = today.strftime('%y-%m-%d')
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute

            time_min = hour * 60 + min

            if int(d[:2]) > int(date[i][:2]):
                res.append(slot[i][0])
                res.append(slot[i][1])
                res.append(slot[i][2])
            elif int(d[:2]) == int(date[i][:2]):
                if int(d[3:5]) > int(date[i][3:5]):
                    res.append(slot[i][0])
                    res.append(slot[i][1])
                    res.append(slot[i][2])
                elif int(d[3:5]) == int(date[i][3:5]):
                    if int(d[6:]) > int(date[i][6:]):
                        res.append(slot[i][0])
                        res.append(slot[i][1])
                        res.append(slot[i][2])
                    elif int(d[6:]) == int(date[i][6:]):
                        if time_min >= 1230:
                            res.append(slot[i][0][0])
                            res.append(" ")
                            res.append(slot[i][2])
                        if time_min >= 1350:
                            res[len(res)-3] = slot[i][0]
                            res[len(res)-2] = slot[i][1]

        
        result = []
        current_sublist = []

        for item in res:
            if isinstance(item, str) and ('to' in item):
                if current_sublist:
                    result.append(current_sublist)
                current_sublist = [item]
            else:
                current_sublist.append(item)

        if current_sublist:
            result.append(current_sublist)
        
        return render(request,'Panel2.html',{'rows':result,"listRed":listRed,'gname':gname})
             
    except Exception as e:
        print('err::-',e)
        return render(request,'Userinterface.html')


def displayMilanJodi2result(request):
    try:
        g2=db2.child('Gname').child('G2').child('G2').get().val()
        gname=[g2]

        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        date=[]
        val=[]
        data=db2.child("Game2").get()
        for x in data.each():
            x=x.key()
            date.append(x)
            y=db2.child("Game2").child(x).child('center').get()
            ordered_dict = y.val()
            value = ordered_dict['number']
            val.append(value)
        
        res=[]
        for i in range(len(date)):
            date_obj = dt.strptime(date[i], "%y-%m-%d").date()

            day = date_obj.strftime("%A")
            curr=''
            if day=='Monday':
                days_until_next_sat = 5  # If today is Sunday, move to the next Sunday
                next_sat = date_obj + datetime.timedelta(days=days_until_next_sat)
                curr=date[i] +' '+'to'+' '+str(next_sat)
                res.append(curr)
            
            today = datetime.date.today()
            d = today.strftime('%y-%m-%d')
            now = datetime.datetime.now()
            time = now.time()
            hour = time.hour
            min= time.minute

            time_min = hour * 60 + min

            if int(d[:2]) > int(date[i][:2]):
                res.append(val[i])
            elif int(d[:2]) == int(date[i][:2]):
                if int(d[3:5]) > int(date[i][3:5]):
                    res.append(val[i])
                elif int(d[3:5]) == int(date[i][3:5]):
                    if int(d[6:]) > int(date[i][6:]):
                       res.append(val[i])
                    elif int(d[6:]) == int(date[i][6:]):
                        if time_min >= 1230:
                            res.append(val[i][0])
                        if time_min >= 1350:
                            res[len(res)-1] = val[i]
        
        result = []
        current_sublist = []

        for item in res:
            if isinstance(item, str) and ('to' in item):
                if current_sublist:
                    result.append(current_sublist)
                current_sublist = [item]
            else:
                current_sublist.append(item)

        if current_sublist:
            result.append(current_sublist)

        return render(request,'Jodi2.html',{'rows':result,"listRed":listRed,'gname':gname})


    except Exception as e:
        print('errr__:',e)
        return render(request,'Userinterface.html')
