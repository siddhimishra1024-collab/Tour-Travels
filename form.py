from tkinter import *
root=Tk()
root.geometry("440x440")
def getval():
    print("Submitted")

L1=Label( root , text="Welcome To Tours&Travels", fg="purple" , font="Helvetica 15 bold" , borderwidth=6, padx=15 ,pady=30)
L1.grid(row=0 , column=3)

Name=Label(root , text="Name", borderwidth=4 , padx=5 , pady=5 , font="SUNKEN 10 italic"  , fg="black")
phone =Label(root,text="Phone Number", borderwidth=4 , padx=5 , pady=5 , font="SUNKEN 10 italic" , fg="black")
gender=Label(root, text="Gender", borderwidth=4 , padx=5 , pady=5 , font="SUNKEN 10 italic" ,  fg="black")
emergencynumber=Label(root , text="Emergency Contact", borderwidth=4 , padx=5 , pady=5 , font="SUNKEN 10 italic" ,  fg="black")
paymentmode=Label(root , text="Payment Mode", borderwidth=4 , padx=5 , pady=5 , font="SUNKEN 10 italic"  , fg="black")

Name.grid(row= 1,column=2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
emergencynumber.grid(row=4 , column=2)
paymentmode.grid(row=5 , column=2)
# where user can write 
# Entry area 
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emervalue=StringVar()
payvalue=StringVar()
FoodServiceValue=IntVar()

name_entry=Entry(root , textvariable=namevalue)
phone_entry=Entry(root , textvariable=phonevalue)
gender_entry=Entry(root , textvariable=gendervalue)
emer_entry=Entry(root , textvariable=emervalue)
pay_entry=Entry(root , textvariable=payvalue)

name_entry.grid(row=1 ,column=3)
phone_entry.grid(row=2 , column=3)
gender_entry.grid(row=3 , column=3)
emer_entry.grid(row=4 , column=3)
pay_entry.grid(row=5 , column=3)

Button(text="Submit Form" , command=getval).grid(row=7 , column=3)
Food_service=Checkbutton(text="Want to Prebook Meal ?")
Variable=FoodServiceValue
Food_service.grid(row=6 , column = 3)






root.mainloop()