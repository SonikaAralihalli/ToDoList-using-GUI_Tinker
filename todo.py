from tkinter import *
window=Tk()
window.title("A")
window.minsize(width=500,height=340)
window.configure(bg="lightblue")
lable=Label(text="TO DO LIST",font=("Arial",25,"bold"))
lable.place(x=10,y=10)
lable.configure(bg="lightblue")
current_y = 90 
def Add():
    global current_y
    k = text_box.get("1.0", END).strip()
    if k:
        acheckbutton = Checkbutton(window,text=k, font=("Arial", 15, "bold"), bg="lightblue")
        acheckbutton.place(x=10,y=current_y)
        current_y += 30
        text_box.delete("1.0", END)
button=Button(window, text="Add", command=Add)
button.place(x=350,y=60)
text_box = Text(window, width=27, height=1, font=("Arial", 15))
text_box.place(x=10,y=60)

window.mainloop()