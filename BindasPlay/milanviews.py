from calendar import weekday
from django.shortcuts import render
from random import randrange
import pyrebase
import datetime
from datetime import datetime as dt, timedelta
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
        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        g1 = db2.child('Gname').child('G1').child('G1').get().val()
        gname = [g1]

        game_data = db2.child('Game1').get().val()
        if not game_data:
            return render(request, 'Userinterface.html')

        today = datetime.date.today()
        current_week_day = today.weekday()
        now = datetime.datetime.now()
        current_time = now.hour * 60 + now.minute  
        
        result = []  
        today_data = [] 

        for date_str, slots in sorted(game_data.items()):
            date_obj = datetime.datetime.strptime(date_str, "%y-%m-%d").date()
            start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=6)

            week_id = f"{start_of_week.strftime('%y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}"

            # Check if the current day is Monday before appending new week_id
            if date_obj.weekday() == 0:  # 0 is Monday
                if not any(week_id in sublist for sublist in result):
                    result.append([week_id])

            week_list = next(sublist for sublist in result if week_id in sublist)

            # Check if the current date is today
            if date_obj == today:
                if current_time >= 780:  # after 1pm
                    today_data = [week_id]
                    if current_time < 900:  # after 1pm and before 3pm
                        numbers = [val['number'] for slot, val in slots.items() if 'number' in val]
                        print(numbers)
                        if numbers:
                            today_data.append(numbers[0][0])
                            today_data.append("")
                            today_data.append(numbers[2])
                    else:  # after 3pm
                        today_data.extend(val['number'] for slot, val in slots.items() if 'number' in val)
            else:
                # Append all numbers from other dates
                week_list.extend(val['number'] for slot, val in slots.items() if 'number' in val)

        # Append today's data if it's available
        if today_data:
            result[-1].extend(today_data[1:])
                    
        return render(request, 'Panel.html', {'rows': result,"listRed": listRed,'gname': gname})

    except Exception as e:
        print('err::-', e)
        return render(request, 'Userinterface.html')


def displayMilanJodiresult(request):
    try:
        g1 = db2.child('Gname').child('G1').child('G1').get().val()
        gname = [g1]

        game_data = db2.child("Game1").get().val()

        result = []
        current_week = None
        current_week_data = []

        now = datetime.datetime.now()
        current_time = now.time()
        today_date = now.date().strftime('%y-%m-%d')

        for date_str, day_data in sorted(game_data.items()):
            date_obj = datetime.datetime.strptime(date_str, "%y-%m-%d").date()
            start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=6)

            week_range = f"{start_of_week.strftime('%y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}"
            
            if current_week != week_range:
                if current_week_data:
                    result.append(current_week_data)
                current_week = week_range
                current_week_data = [week_range]
            
            if date_str == today_date:
                # Skip today's data if the current time is before 1 PM
                if current_time < datetime.time(13, 0):
                    continue
                # Include only the first digit of today's data if the current time is between 1 PM and 3 PM
                elif datetime.time(13, 0) <= current_time < datetime.time(15, 0):
                    # Assuming 'number' is a string
                    current_week_data.append(day_data['center']['number'][0] + ' ')
                    continue

            # Include the full data for other days or if current time is past 3 PM
            if 'center' in day_data and 'number' in day_data['center']:
                current_week_data.append(day_data['center']['number'])

        if current_week_data and current_week_data not in result:
            result.append(current_week_data)


        context = {
            'rows': result,
            'listRed': ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "05", "50", "16", "61", "27", "72", "38", "83", "49", "94", "**"],
            'gname': gname
        }

        return render(request, 'Jodi.html', context)

    except Exception as e:
        print('errr__:', e)
        return render(request, 'Userinterface.html')
 


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
        listRed = ["00","11","22","33","44","55","66","77","88","99","05","50","16","61","27","72","38","83","49","94","**"]
        g1 = db2.child('Gname').child('G2').child('G2').get().val()
        gname = [g1]

        game_data = db2.child('Game2').get().val()
        if not game_data:
            return render(request, 'Userinterface.html')

        today = datetime.date.today()
        current_week_day = today.weekday()
        now = datetime.datetime.now()
        current_time = now.hour * 60 + now.minute  
        
        result = []  
        today_data = [] 

        for date_str, slots in sorted(game_data.items()):
            date_obj = datetime.datetime.strptime(date_str, "%y-%m-%d").date()
            start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=5)

            week_id = f"{start_of_week.strftime('%y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}"

            if date_obj.weekday() == 0:  # 0 is Monday
                if not any(week_id in sublist for sublist in result):
                    result.append([week_id])

            week_list = next(sublist for sublist in result if week_id in sublist)

            # Check if the current date is today
            if date_obj == today:
                if current_time >= 1200:  # after 8pm
                    today_data = [week_id]
                    if current_time < 1380:  # after 8pm and before 11pm
                        numbers = [val['number'] for slot, val in slots.items() if 'number' in val]
                        print(numbers)
                        if numbers:
                            today_data.append(numbers[0][0])
                            today_data.append("")
                            today_data.append(numbers[2])
                    else:  # after 11pm
                        today_data.extend(val['number'] for slot, val in slots.items() if 'number' in val)
            else:
                # Append all numbers from other dates
                week_list.extend(val['number'] for slot, val in slots.items() if 'number' in val)

        # Append today's data if it's available
        if today_data:
            # print(today_data)
            # if current_week_day == 0:
            #     date_obj = datetime.datetime.strptime(date_str, "%y-%m-%d").date()
            #     start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
            #     end_of_week = start_of_week + datetime.timedelta(days=5)

            #     week_id = f"{start_of_week.strftime('%y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}"
            #     # result.append[week_id]
            #     result[-1].extend(today_data[1:])
            # else:
            result[-1].extend(today_data[1:])
        return render(request, 'Panel2.html', {'rows': result,"listRed":listRed,'gname': gname})

    except Exception as e:
        print('err::-', e)
        return render(request, 'Userinterface.html')


def displayMilanJodi2result(request):
    try:
        g1 = db2.child('Gname').child('G2').child('G2').get().val()
        gname = [g1]

        game_data = db2.child("Game2").get().val()

        result = []
        current_week = None
        current_week_data = []

        now = datetime.datetime.now()
        current_time = now.time()
        today_date = now.date().strftime('%y-%m-%d')

        for date_str, day_data in sorted(game_data.items()):
            date_obj = datetime.datetime.strptime(date_str, "%y-%m-%d").date()
            start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=5)

            week_range = f"{start_of_week.strftime('%y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}"
            
            if current_week != week_range:
                if current_week_data:
                    result.append(current_week_data)
                current_week = week_range
                current_week_data = [week_range]
            
            if date_str == today_date:
                if current_time < datetime.time(20, 0):
                    continue
                elif datetime.time(20, 0) <= current_time < datetime.time(23, 0):
                    current_week_data.append(day_data['center']['number'][0] + ' ')
                    continue

            if 'center' in day_data and 'number' in day_data['center']:
                current_week_data.append(day_data['center']['number'])

        if current_week_data and current_week_data not in result:
            result.append(current_week_data)
        context = {
            'rows': result,
            'listRed': ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "05", "50", "16", "61", "27", "72", "38", "83", "49", "94", "**"],
            'gname': gname
        }

        return render(request, 'Jodi2.html', context)

    except Exception as e:
        print('errr__:', e)
        return render(request, 'Userinterface.html')
