import logging
from django.shortcuts import render
import datetime
import random
import pyrebase
from random import randrange
from django.shortcuts import render
from django.contrib import messages


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


app = pyrebase.initialize_app(Config)
auth=app.auth()
db5=app.database()

firebase2=pyrebase.initialize_app(Config3)
authe=firebase2.auth()
db2=firebase2.database()

logger = logging.getLogger(__name__)


def GenerateRandomNumbers():
  values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  first_index = random.randint(0, 8)
  second_index = random.randint(first_index , 9)
  third_index = random.randint(second_index , 9)
  
  firstnum = values[first_index]
  secondnum = values[second_index]
  thirdnum = values[third_index]
  return firstnum,secondnum,thirdnum

def AutoSubmitMilanGame1Data():
      today = datetime.date.today()
      d= today.strftime('%y-%m-%d')
      firstnum,secondnum,thirdnum = GenerateRandomNumbers()
      a=str(firstnum)+str(secondnum)+str(thirdnum)
      row={'number':a}
      db2.child('Game1').child(d).child('open').set(row)
      
      center1 = int(firstnum)+int(secondnum)+int(thirdnum)
      center1 = center1 % 10
      center1 = str(center1)

      firstnum1,secondnum1,thirdnum1 = GenerateRandomNumbers()
      c=str(firstnum1)+str(secondnum1)+str(thirdnum1)
      row={'number':c}
      db2.child('Game1').child(d).child('close').set(row)
      center2 = int(firstnum1)+int(secondnum1)+int(thirdnum1)
      center2 = center2 % 10
      center2 = str(center2)
      res = center1 + center2
      rrr={'number': res}
      db2.child('Game1').child(d).child('center').set(rrr)


def AutoSubmitMilanGame2Data():
      today = datetime.date.today()
      d= today.strftime('%y-%m-%d')
      day=today.strftime("%A")

      if day != "Sunday":
        firstnum,secondnum,thirdnum = GenerateRandomNumbers()
        a=str(firstnum)+str(secondnum)+str(thirdnum)
        row={'number':a}
        db2.child('Game2').child(d).child('open').set(row)
        
        center1 = int(firstnum)+int(secondnum)+int(thirdnum)
        center1 = center1 % 10
        center1 = str(center1)

        firstnum1,secondnum1,thirdnum1 = GenerateRandomNumbers()
        c=str(firstnum1)+str(secondnum1)+str(thirdnum1)
        row={'number':c}
        db2.child('Game2').child(d).child('close').set(row)
        center2 = int(firstnum1)+int(secondnum1)+int(thirdnum1)
        center2 = center2 % 10
        center2 = str(center2)
        res = center1 + center2
        rrr={'number': res}
        db2.child('Game2').child(d).child('center').set(rrr)


def BindasAutomatic():
  today = datetime.date.today()
  d = today.strftime("%y-%m-%d")
        
  L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]

  now = datetime.datetime.now()

  day=today.strftime("%A")

  if day != "Sunday":
    for t in L:
      number = randrange(0,100)
      y = str(number)
      if(len(y)==1):
          y = "0"+y
      row={"num1":y}
      db5.child('data1').child(d).child(t).set(row)
    
    for t1 in L:
      number1 = randrange(0,100)
      y1 = str(number1)
      if(len(y1)==1):
          y1 = "0"+y1
      row1={"num2":y1}
      db5.child('data2').child(d).child(t1).set(row1)

    for t2 in L:
      number2 = randrange(0,100)
      y2 = str(number2)
      if(len(y2)==1):
          y2 = "0"+y2
      row2={"num3":y2}
      db5.child('data3').child(d).child(t2).set(row2)
  
def KalyanAutomatic():
  today = datetime.date.today()
  d = today.strftime("%y-%m-%d")
        
  L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]

  now = datetime.datetime.now()
  day=today.strftime("%A")

  if day != "Sunday":
    for t in L:
      number = randrange(0,100)
      y = str(number)
      if(len(y)==1):
          y = "0"+y
      row={"num1":y}
      db5.child('kalyandata1').child(d).child(t).set(row)

    for t1 in L:
      number1 = randrange(0,100)
      y1 = str(number1)
      if(len(y1)==1):
          y1 = "0"+y1
      row1={"num2":y1}
      db5.child('kalyandata2').child(d).child(t1).set(row1)
    
    for t2 in L:
      number2 = randrange(0,100)
      y2 = str(number2)
      if(len(y2)==1):
          y2 = "0"+y2
      row2={"num3":y2}
      db5.child('kalyandata3').child(d).child(t2).set(row2)