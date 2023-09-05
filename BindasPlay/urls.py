"""BindasPlay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import userview
from .import auto
from .import kalyanViews
from . import adminviews
from . import milanviews
from . import userdataview

urlpatterns = [
    #homepage
    path('',userview.Userview),
    path('usersData/',userdataview.userData),
    
    #bindas
    path('displayresult/',userview.displayResult),
    path('saveresult/',userview.saveResult),
    path('searchAll/',userview.SearchAll),
    path('search/',userview.SearchByDate),
    path('',include('authentication.urls')),
    path('notification/',userview.Notification),
    path('addNotification/',userview.AddNotification),
    path('typeSubmit1/',auto.TypeSubmit1),
    path('typeSubmit2/',auto.TypeSubmit2),
    path('typeSubmit3/',auto.TypeSubmit3),

    #kalyan
    path('displayresultkalyan/',kalyanViews.displayResultKalyan),
    path('saveresultkalyan/',kalyanViews.saveResultKalyan),
    path('searchAllkalyan/',kalyanViews.SearchAllKalyan),
    path('searchkalyan/',kalyanViews.SearchByDateKalyan),
    path('typeSubmitkalyan1/',auto.TypeSubmitKalyan1),
    path('typeSubmitkalyan2/',auto.TypeSubmitKalyan2),
    path('typeSubmitkalyan3/',auto.TypeSubmitKalyan3),  

    #Milan
    path('saveresultmilan1/',milanviews.MilanSubmit),
    path('automilansaveresult/',milanviews.AutoMilanSubmit),
    path('holidaymilan/',milanviews.Holidaysubmit),
    path('panelresult/',milanviews.displayMilanPanelResult),
    path('jodiresult/',milanviews.displayMilanJodiresult),
    path('saveresultmilan2/',milanviews.Milan2Submit),
    path('automilan2saveresult/',milanviews.AutoMilan2Submit),
    path('holidaymilan2/',milanviews.Holiday2submit),
    path('panel2result/',milanviews.displayMilanPanel2Result),
    path('jodi2result/',milanviews.displayMilanJodi2result),


    #adminworks
        #bindas
    path('atypeSubmit1/',adminviews.ATypeSubmit1),
    path('atypeSubmit2/',adminviews.ATypeSubmit2),
    path('atypeSubmit3/',adminviews.ATypeSubmit3),
    path('asaveresult/',adminviews.AsaveResult),

        #kalyan
    path('atypeSubmitkalyan1/',adminviews.ATypeSubmitKalyan1),
    path('atypeSubmitkalyan2/',adminviews.ATypeSubmitKalyan2),
    path('atypeSubmitkalyan3/',adminviews.ATypeSubmitKalyan3),
    path('asaveresultkalyan/',adminviews.AsaveResultKalyan),

        #milan
    path('amilansaveresult/',adminviews.AMilanSubmit),
    path('aautomilansaveresult/',adminviews.AautoMilanSubmit),
    path('aholiday/',adminviews.Aholidaysubmit),
    path('amilan2saveresult/',adminviews.AMilan2Submit),
    path('aautomilan2saveresult/',adminviews.AautoMilan2Submit),
    path('aholiday2/',adminviews.Aholiday2submit),
    path('game1name/',adminviews.Gname),
    path('game2name/',adminviews.G2name),
    path('previousdateData/',adminviews.PreviousDatapage),
    path('savePreviousdata/',adminviews.AddPreviousdata),
]
