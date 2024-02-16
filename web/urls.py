from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('package/',views.package,name='package'),
    path('blog/',views.blog,name='blog'),
    path('branch/',views.blog,name='brancg'),
    path('gallery/',views.gallery,name='gallery'),
    path('executive-package/',views.executive_package,name='executive-package'),
    path('ayush-general/',views.ayush_general,name='ayush-general'),
    path('ayush-silver/',views.ayush_silver,name='ayush-silver'),
    path('ayush-gold/',views.ayush_gold,name='ayush-gold'),
    path('cardiac/',views.cardiac,name='cardiac'),
    path('lab-chambakkara/',views.lab_chambakkara,name='lab-chamakkara'),
    path('lab-vadakkekotta/',views.lab_vadakkekotta,name='lab-vadakkekotta'),
    path('lab-kolencherry/',views.lab_kolenchery,name='lab-kolencherry'),
    path('lab-thrippunithura/',views.lab_thrippunithura,name='lab-thrippunithura'),
    path('moleculor/',views.molecular,name='moleculor'),
    path('radiology/',views.radiology,name='radiology'),
    path('test/',views.test,name='test'),
    path('contact-us/',views.contact,name='contact-us'),
    path('appointment/',views.appointment,name='appointment'),
    path('dept/',views.dept,name='dept'),
    # path('index/',views.register,name='register')
]