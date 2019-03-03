import tkinter as tk
from PIL import Image
from PIL import ImageTk

root =tk.Tk()
root.title("House Retailing")
root.configure(background="black")

cwgt=tk.Canvas(root)
cwgt.pack(expand=True, fill=tk.BOTH)
image1=ImageTk.PhotoImage(file="Property-Retailer.jpeg")
w,h=image1.width(),image1.height()
root.geometry('535x405')

cwgt.img=image1
cwgt.create_image(0, 0, anchor=tk.NW, image=image1)


class MyButton:
	def __init__(self, root):
		self.f = tk.Frame(root)
		self.f.propagate(0)
		self.f.pack()
		b1=tk.Button(root,text="T & C",bg="orange",fg="green", cursor='watch').place(x=100,y=10, width=100,height=30)
		b2=tk.Button(root,text="SEARCH",bg="orange",fg="green", cursor='watch',command=self.search).place(x=200,y=10, width=100, height=30)
		b3=tk.Button(root,text="REGISTER",bg="orange",fg="green", cursor='watch',command=self.register).place(x=300,y=10, width=100, height=30)
		b4= tk.Button(root, text="Exit", bg="orange", fg="BLACK",cursor='watch',command=exit).place(x=235,y=370, width=100, height=30)


	def search(self):
		self.f1 =tk.Frame(root)
		self.f1.propagate(0)
		self.f1.pack()
		window = tk.Toplevel(self.f1)
		window.configure(bg="black")
		window.geometry('535x405')

		
		self.f1.l1 = tk.Label(window, font=('arial ',30,'bold') ,text="Search Page:",fg="Steel Blue", bd=10 , anchor='w',bg="black",cursor='watch').grid(row=1,column=1)
		

		
		self.f1.Btn2= tk.Button(window, text="search", bg="orange", fg="BLACK",cursor='watch').place(x=272,y=65,width=100,height=25)
		self.f1.ent1 = tk.Entry(window,bg="gray",fg="orange").grid(row=2,column=1)		
		self.f1.Btn2= tk.Button(window, text="Exit", bg="orange", fg="BLACK",cursor='watch',command=quit).place(x=235,y=370, width=100, height=30)
		self.cwgt1=tk.Canvas(window)
		self.cwgt1.grid(row=6,column=1)
		self.image1=ImageTk.PhotoImage(file="a.jpeg")
		self.cwgt1.img=image1
		self.cwgt1.create_image(0, 0, anchor=tk.NW, image=self.image1)
		
		
		self.f1.l5 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Type of Home :",cursor='watch')
		self.f1.l6 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text=" Location : ",cursor='watch')
		self.f1.l7 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black"text="Money Range :",cursor='watch')
		self.f1.l5.grid(row=3,column=1)
		self.f1.l6.grid(row=4,column=1)
		self.f1.l7.grid(row=5,column=1)
		
	
	def register(self):
		self.f2 =tk.Frame(root)
		self.f2.propagate(0)
		self.f2.pack()
		window = tk.Toplevel(self.f2)
		window.configure(bg="black")
		self.f2.l1 = tk.Label(window, font=('arial ',30,'bold') ,text="Register Page:",fg="Steel Blue", bd=10 , anchor='w',bg="black",cursor='watch')
		self.f2.l2 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Name:",cursor='watch')
		self.f2.l3 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Address:",cursor='watch')
		self.f2.l4 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Mobile Number :",cursor='watch')
		self.f2.l5 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Type of Home :",cursor='watch')
		self.f2.l6 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text=" Location : ",cursor='watch')
		self.f2.l7 = tk.Label(window, font=('arial ',15,'bold') ,fg="orange",bg="black",text="Money Range :",cursor='watch')
		self.f2.ent1 = tk.Entry(window,bg="gray",fg="white")
		self.f2.ent2 = tk.Entry(window,bg="gray",fg="white")
		self.f2.ent3 = tk.Entry(window,bg="gray",fg="white")
		self.f2.ent4 = tk.Entry(window,bg="gray",fg="white")
		self.f2.ent5 = tk.Entry(window,bg="gray",fg="white")
		self.f2.ent6 = tk.Entry(window,bg="gray",fg="white")
		self.f2.Btn1= tk.Button(window, text="Confirm", bg="orange", fg="BLACK",cursor='watch').grid(row=10,column=3)
		self.f2.Btn2= tk.Button(window, text="Exit", bg="orange", fg="BLACK",cursor='watch',command=exit).grid(row=10,column=4)
		self.f2.l1.grid(row=1)
		self.f2.l2.grid(row=3)
		self.f2.l3.grid(row=4)
		self.f2.l4.grid(row=5)
		self.f2.l5.grid(row=6)
		self.f2.l6.grid(row=7)
		self.f2.l7.grid(row=8)
		self.f2.ent1.grid(row=3,column=2)
		self.f2.ent2.grid(row=4,column=2)
		self.f2.ent3.grid(row=5,column=2)
		self.f2.ent4.grid(row=6,column=2)
		self.f2.ent5.grid(row=7,column=2)
		self.f2.ent6.grid(row=8,column=2)

mb=MyButton(root) 
root.mainloop()
