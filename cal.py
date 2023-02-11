import tkinter

calculation = ""

def add_to_calculation(symbol):
   global calculation
   calculation += str(symbol)
   txt_result.delete(1.0,"end")
   txt_result.insert(1.0,calculation)

def evaluate_calculation():
  global calculation
  try:
      calculation = str(eval(calculation))
      txt_result.delete(1.0,"end")
      txt_result.insert(1.0, calculation)
  except:
      clear_field()
      txt_result.insert(1.0,"Error...")

def clear_field():
    global calculation
    calculation = ""
    txt_result.delete(1.0,"end")

cal_window = tkinter.Tk()
cal_window.geometry("400x280")
cal_window.title("GUI CALCULATOR")
cal_window.config(bg="black")
cal_window.resizable(False,False)

txt_result = tkinter.Text(cal_window, height=2, width=27,
                          font=("Open Sans",20),bg="white",fg="black")
txt_result.grid(columnspan=6)

button1 = tkinter.Button(cal_window, text="1", command=lambda: add_to_calculation(1),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button1.grid(row=2,column=1)

button2 = tkinter.Button(cal_window, text="2", command=lambda: add_to_calculation(2),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button2.grid(row=2,column=2)

button3 = tkinter.Button(cal_window, text="3", command=lambda: add_to_calculation(3),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button3.grid(row=2,column=3)

button4 = tkinter.Button(cal_window, text="4", command=lambda: add_to_calculation(4),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button4.grid(row=3,column=1)

button5 = tkinter.Button(cal_window, text="5", command=lambda: add_to_calculation(5),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button5.grid(row=3,column=2)

button6 = tkinter.Button(cal_window, text="6", command=lambda: add_to_calculation(6),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button6.grid(row=3,column=3)

button7 = tkinter.Button(cal_window, text="7", command=lambda: add_to_calculation(7),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button7.grid(row=4,column=1)

button8 = tkinter.Button(cal_window, text="8", command=lambda: add_to_calculation(8),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button8.grid(row=4,column=2)

button9 = tkinter.Button(cal_window, text="9", command=lambda: add_to_calculation(9),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button9.grid(row=4,column=3)

button0 = tkinter.Button(cal_window, text="0", command=lambda: add_to_calculation(0),
                         width=6,font=("Open Sans",16),bg="black",fg="white")
button0.grid(row=5,column=2)

button_plus = tkinter.Button(cal_window, text="+", command=lambda: add_to_calculation("+"),
                                       width=6,font=("Open Sans",16),bg="orange",fg="black")
                                    
button_plus.grid(row=2,column=4)

button_dot = tkinter.Button(cal_window, text=".", command=lambda: add_to_calculation("."),
                              width=6,font=("Open Sans",16),bg="orange",fg="black")
button_dot.grid(row=6,column=2)


button_minus = tkinter.Button(cal_window, text="-", command=lambda: add_to_calculation("-"),
                              width=6,font=("Open Sans",16),bg="orange",fg="black")
button_minus.grid(row=3,column=4)

button_multiplication = tkinter.Button(cal_window, text="*", command=lambda: add_to_calculation("*"),
                                       width=6,font=("Open Sans",16),bg="orange",fg="black")
button_multiplication.grid(row=4,column=4)

button_division = tkinter.Button(cal_window, text="/", command=lambda: add_to_calculation("/"),
                                 width=6,font=("Open Sans",16),bg="orange",fg="black")
button_division.grid(row=5,column=4)

button_openpar = tkinter.Button(cal_window, text="(", command=lambda: add_to_calculation("("),
                                width=6,font=("Open Sans",16),bg="orange",fg="black")
button_openpar.grid(row=5,column=1)

button_closepar = tkinter.Button(cal_window, text=")", command=lambda: add_to_calculation(")"),
                                 width=6,font=("Open Sans",16),bg="orange",fg="black")
button_closepar.grid(row=5,column=3)

button_equals = tkinter.Button(cal_window, text="=", command=evaluate_calculation,
                               width=10,font=("Open Sans",16),bg="orange",fg="black")
button_equals.grid(row=6,column=3,columnspan=2)

button_clear = tkinter.Button(cal_window, text="C", command=clear_field,
                              width=8,font=("Open Sans",16),bg="orange",fg="black")
button_clear.grid(row=6,column=1,columnspan=1)

cal_window.mainloop()