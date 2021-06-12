from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

num_label=Label(root, text="Enter a number", font=("Courier",20))
label1=Label(root, font=("Courier",20))

num = Entry(root, font=("Courier",20))
result=Label(root, font=("Courier",20), text="Sum : ")
label_series = Label(root, text="Fibonacci Series:  ")

def Fibonacci():
    some = (num.get())
    some = int(some)
    nums = some
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    while (counter <= some):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
        result['text'] = "Sum : " + str(sum2)
        
def clear():
    label_series['text'] = "Fibbonaci Series: "
    result['text'] = "Sum : "
    num.delete(0, 'end')

btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)

clear = Button(root, text="Clear", command=clear)

btn.pack()
result.pack()
num.pack()
label_series.pack()
clear.pack()
root.mainloop()