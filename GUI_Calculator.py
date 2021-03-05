from tkinter import *

root = Tk()
root.title('Calculator')
entry_box = Entry(root, width=40, borderwidth=8, fg='blue')
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    #entry_box.delete(0, END)
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current) + str(number))

    
def button_clear():
    entry_box.delete(0, END)


def button_add():
    first_number = entry_box.get()
    global first_num
    global button
    button ='add'
    first_num = int(first_number)
    entry_box.delete(0, END)


def button_subt():
    first_number = entry_box.get()
    global first_num
    global button
    button ='sub'
    first_num = int(first_number)
    entry_box.delete(0, END)


def button_mult():
    first_number = entry_box.get()
    global first_num
    global button
    button ='mul'
    first_num = int(first_number)
    entry_box.delete(0, END) 


def button_divi():
    first_number = entry_box.get()
    global first_num
    global button
    button ='div'
    first_num = int(first_number)
    entry_box.delete(0, END)


def button_equal():
    second_number = entry_box.get()
    entry_box.delete(0, END)
    #answer = first_num + int(second_number)
    if button=='add':
        entry_box.insert(0, first_num + int(second_number))
    elif button == 'sub':
        entry_box.insert(0, first_num - int(second_number))
    elif button == 'mul':
        entry_box.insert(0, first_num * int(second_number))
    elif button == 'div':
        entry_box.insert(0, first_num / int(second_number))


# defining the button
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_sum = Button(root, text='+', padx=40, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=88, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=80, pady=20, command=button_clear)

button_sub = Button(root, text='-', padx=40, pady=20, command=button_subt)
button_mul = Button(root, text='*', padx=40, pady=20, command=button_mult)
button_div = Button(root, text='/', padx=40, pady=20, command=button_divi)

# displaying the button
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_sum.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=4, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()