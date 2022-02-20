#Importing Tkinter
import datetime
from tkinter import *




#Saving Values Function
def save_Values():
    Save_Start_Date=StartDate_Entry.get()
    Save_End_Date=EndDate_Entry.get()




#Creating Window
screen=Tk()
screen.geometry("500x500")
screen.title("Project Resource Calculator")

#Adding Widgets

#Adding Headers
Heading= Label(screen, text='Please Enter the Details below to generate Amount',fg="black",width='70',height='3')
Heading.place(x=3,y=2)

#Adding Entrylabels
Project_Name= Label(screen, text='Project Name',fg="black",width='10',height='3')
Project_Name.place(x=10,y=80)

Start_Date= Label(screen, text='Date of Commencement',fg="black",width='19',height='3')
Start_Date.place(x=3,y=160)

Finish_Date= Label(screen, text='Date of Completion',fg="black",width='15',height='3')
Finish_Date.place(x=3,y=240)

#Creating Entry Widgets

# Creating Text Variables
Projectname=StringVar
Startdate=datetime.date
Enddate=datetime.date

#Creating Entry Widet & Their Positions
Project_Name_Entry=Entry(textvariable=Projectname,width=50)
Project_Name_Entry.place(x=160,y=99)

StartDate_Entry= Entry(textvariable=Startdate,width=50)
StartDate_Entry.place(x=160,y=179)

EndDate_Entry= Entry(textvariable=Enddate,width=50)
EndDate_Entry.place(x=160,y=259)

#Creating Execute Button Widget
Execute_Button=Button(text='Calculate Amount Due',command=save_Values, fg="black",width='20')
Execute_Button.place(x=190,y=310)










screen.mainloop()




