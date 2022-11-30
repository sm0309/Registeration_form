import tkinter as tk
root=tk.Tk()
label_0=tk.Label(root,text='Name',width=25)
label_0=tk.Entry(root,text='Name',width=25)
label_0.place(x=100,y=150)

label_1=tk.Label(root,text='Course',width=25)
label_1=tk.Entry(root,text='Course',width=25)
label_1.place(x=100,y=150)

label_2=tk.Label(root,text='Semester',width=25)
label_2=tk.Entry(root,text='Semseter',width=25)
label_2.place(x=100,y=150)

label_3=tk.Label(root,text='Form No.',width=25)
label_3=tk.Entry(root,text='Form no.',width=25)
label_3.place(x=100,y=150)

label_4=tk.Label(root,text='Contact NO.',width=25)
label_4=tk.Entry(root,text='Contact No.',width=25)
label_4.place(x=100,y=150)

label_5=tk.Label(root,text='Email id',width=25)
label_5=tk.Entry(root,text='Email Id',width=25)
label_5.place(x=100,y=150)

label_6=tk.Label(root,text='Address',width=25)
label_6=tk.Entry(root,text='Address',width=25)
label_6.place(x=100,y=150)
btn=tk.Button(root,text='submit',width=25)
btn.pack()
root.title("Registeration Form")
root.grid()
root.mainloop()


