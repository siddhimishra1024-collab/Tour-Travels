from tkinter import *
root=Tk()
root.geometry("540x440")
root.title("Travel Form")
def submit():
    print("Submitted")
    print(f"{n.get() , p.get() , a.get() , e.get() , pa.get() ,f.get()}")


with open ("records.txt" , "w")as f:
    pass
Label(root , text="Welcome to Jaguar Travels" , font="Helvetica 16 bold" ,fg="purple", padx=15 , pady=20).grid(row=0 , column =3)
Label(root , text="Name" , font="SUNKEN 10 italic" , padx=5, pady=5 , borderwidth=6, fg="green").grid(row=1 , column =2)
Label(root , text="Phone Number" , font="SUNKEN 10 italic" , padx=5, pady=5 , borderwidth=6, fg="green").grid(row=2 , column =2)
Label(root , text="Address" , font="SUNKEN 10 italic" , padx=5, pady=5 , borderwidth=6, fg="green").grid(row=3 , column =2)
Label(root , text="Emergency Contact" , font="SUNKEN 10 italic" , padx=5, pady=5 , borderwidth=6, fg="green").grid(row=4 , column =2)
Label(root , text="Payment Mode" , font="SUNKEN 10 italic" , padx=5, pady=5 , borderwidth=6 , fg="green").grid(row=5 , column =2)

n=StringVar()
p=StringVar()
a=StringVar()
e=StringVar()
pa=StringVar()
f=IntVar()
Entry(root , textvariable=n).grid(row=1 , column=3)
Entry(root , textvariable=p).grid(row=2 , column=3)
Entry(root , textvariable=a).grid(row=3 , column=3)
Entry(root , textvariable=e).grid(row=4 , column=3)
Entry(root , textvariable=pa).grid(row=5 , column=3)
Button(root , text="Press to Submit" , command =submit).grid(row=7 , column=3)
f_s=Checkbutton(text="Want to prebook meal" )
Variable=f
f_s.grid(row=6 , column=3)

root.mainloop()
   

# from tkinter import *
# root=Tk()
# root.geometry("540x440")
# root.title("Tours & Travels")
# def prints():
#     print("Submitted")

#     print(f"{n.get() ,g.get(), p.get(), a.get(), em.get(), alt.get(), foodservice.get()}")
#     with open("records.txt" , "w") as f:
#         pass
# Label(root, text="Welcome to Jaguar Tours & Travels" ,font ="Helvetica 16 bold" , pady=16 , padx=5 , borderwidth=6).grid(row=0 , column =3)
# Label(root , text="Name" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=1 , column =2)
# Label(root , text="Gender" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=2 , column =2)
# Label(root , text="Phone Number" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=3 , column =2)
# Label(root , text="Address" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=4 , column =2)
# Label(root , text="Email Address" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=5 , column =2)
# Label(root , text="Alt Number" ,font ="Helvetica 8 italic" , pady=12 , padx=5 , borderwidth=6).grid(row=6 , column =2)

# n=StringVar()
# g=StringVar()
# p=StringVar()
# a=StringVar()
# em=StringVar()
# alt=StringVar()
# foodservice=IntVar()

# Entry(root , textvariable=n ).grid(row=1 , column=3)
# Entry(root , textvariable=g ).grid(row=2 , column=3)
# Entry(root , textvariable=p ).grid(row=3 , column=3)
# Entry(root , textvariable=a ).grid(row=4 , column=3)
# Entry(root , textvariable=em ).grid(row=5 , column=3)
# Entry(root , textvariable=alt ).grid(row=6 , column=3)

# food_ser=Checkbutton(root , text="Want to prebook food delivery")
# Variable=foodservice
# # 1 for checked .....0 for not checked
# food_ser.grid(row=7 , column =3)

# Button(root , text="Press To Submit" , command=prints ).grid(row=8 , column=3) 

# root.mainloop()
