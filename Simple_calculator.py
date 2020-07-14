from tkinter import *
from datetime import datetime
import math


def on_enter_equal(e):
    button_equal['background'] = "#66ccff"


def on_leave_equal(e):
    button_equal['background'] = "#99ddff"


def on_enter_c(e):
    button_c['background'] = "#ffc2b3"


def on_leave_c(e):
    button_c['background'] = "#e6e6e6"


window = Tk()

window.title("Calculator")  # "window" is the name of the calculator window
window.geometry("470x570")
window.configure(bg="#bfbfbf")
window.resizable(False, False)
e1 = Entry(window, width=50, borderwidth=0)
e2 = Entry(window, width=50, borderwidth=0)

e1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e2.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

e = e1.get()

window.columnconfigure(0, pad=3)
window.columnconfigure(1, pad=3)
window.columnconfigure(2, pad=3)
window.columnconfigure(3, pad=3)
window.columnconfigure(4, pad=3)
window.columnconfigure(5, pad=3)
window.columnconfigure(6, pad=3)
window.columnconfigure(7, pad=3)

window.rowconfigure(0, pad=3)
window.rowconfigure(1, pad=3)
window.rowconfigure(2, pad=3)
window.rowconfigure(3, pad=3)
window.rowconfigure(4, pad=3)
window.rowconfigure(5, pad=3)
window.rowconfigure(6, pad=3)
window.rowconfigure(7, pad=3)
window.rowconfigure(8, pad=3)
window.rowconfigure(9, pad=3)


def button_click(number):  # recieving button click and displaying
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current) + str(number))

    e2.delete(0, END)


def button_c():  # clear button
    e2.delete(0, END)
    e1.delete(0, END)


def button_equal():  # Calculation
    try:
        calculation = e1.get().replace("x", "*").replace("÷", "/")
        answer = eval(calculation)
        e2.delete(0, END)
        e2.insert(0, answer)


    except Exception:
        e2.delete(0, END)
        e2.insert(0, "ERROR : Refer Help Button")


def button_ce():  # clear entry
    a = len(e1.get().rstrip())
    e1.delete(a - 1)


def button_root():  # root unction
    try:
        number_int = int(e1.get())
        number_str = e1.get()
        root = math.pow(number_int, 0.5)
        root_str = str(round(root, 2))
        e2.delete(0, END)
        e2.insert(0, "√" + number_str + " = " + root_str)

    except Exception:
        e2.delete(0, END)
        e2.insert(0, "ERROR : Refer Help Button")


# ============================================================================================================
# date calculator

def calculate_date1():
    root = Tk()
    root.title("Date Calculator")
    root.geometry("390x350")
    root.resizable(False, False)

    txt_from_date = Entry(root)
    txt_from_date.place(relx=0.5, rely=0.1)

    txt_to_date = Entry(root)
    txt_to_date.place(relx=0.5, rely=0.2)

    txt_total = Entry(root)
    txt_total.place(relx=0.5, rely=0.3)

    def calculate_date():
        try:
            d1 = txt_from_date.get()
            d2 = txt_to_date.get()

            t1 = datetime.strptime(d1, "%d/%m/%Y")
            t2 = datetime.strptime(d2, "%d/%m/%Y")

            txt_total.delete(0, END)
            txt_total.insert(0, abs((t1 - t2).days))

        except Exception:
            txt_total.delete(0, END)
            txt_total.insert(0, "ERROR : Refer Help ")

    def reset():
        txt_from_date.delete(0, END)
        txt_to_date.delete(0, END)
        txt_total.delete(0, END)

    #    lbl_title = Label(root, text="Date calculator")
    #    lbl_title.place(relx=0.1,rely=0.1)

    lbl_from_date = Label(root, text="From Date")
    lbl_from_date.place(relx=0.1, rely=0.1)

    lbl_to_date = Label(root, text="To Date")
    lbl_to_date.place(relx=0.1, rely=0.2)

    lbl_total = Label(root, text="Calculated Date")
    lbl_total.place(relx=0.1, rely=0.3)

    btn_total = Button(root, text="Calculate", command=calculate_date)
    btn_total.place(relx=0.5, rely=0.5)

    btn_reset = Button(root, text="Reset", command=reset)
    btn_reset.place(relx=0.2, rely=0.5)


#    lbl_reference=Label(root,text="(dd/mm/yyyy)")
#    lbl_reference.place(relx=0.2,rely=0.2)

# ===========================================================================================================
# circle

def circle_calc1():
    circle = Tk()
    circle.title("circle Calculator")
    circle.geometry("390x350")
    circle.resizable(False, False)

    ce1 = Entry(circle)
    ce1.place(relx=0.6, rely=0.2)

    ce2 = Entry(circle)
    ce2.place(relx=0.6, rely=0.4)

    ce3 = Entry(circle)
    ce3.place(relx=0.6, rely=0.6)

    def cylinder_reset():
        ce1.delete(0, END)
        ce2.delete(0, END)
        ce3.delete(0, END)

    def circle_calc():
        try:
            ce = float(ce1.get())
            perimeter = abs(2 * 22 / 7 * ce)
            area = abs(22 / 7 * ce * ce)
            perimeter_str = str(round(perimeter, 2))
            area_str = str(round(area, 2))

            ce2.delete(0, END)
            ce3.delete(0, END)
            ce2.insert(0, perimeter_str + " cm")
            ce3.insert(0, area_str + " cm²")

        except Exception:
            ce2.delete(0, END)
            ce3.delete(0, END)
            ce2.insert(0, "ERROR : Refer Help ")
            ce3.insert(0, "ERROR : Refer Help ")

    lbl_radius = Label(circle, text="Enter your radius")
    lbl_radius.place(relx=0.1, rely=0.2)

    lbl_perimeter = Label(circle, text="Perimeter of the Circle")
    lbl_perimeter.place(relx=0.1, rely=0.4)

    lbl_area = Label(circle, text="Area of the Circle")
    lbl_area.place(relx=0.1, rely=0.6)

    btn_calculate = Button(circle, text="Calculate", command=circle_calc, width=10, bg="#cccccc", )
    btn_calculate.place(relx=0.6, rely=0.7)

    btn_reset = Button(circle, text="Reset", command=cylinder_reset, width=10, bg="#cccccc", )
    btn_reset.place(relx=0.1, rely=0.7)


# ==================================================================================================================
# cylinder calculator
def cylinder_calc1():
    cylinder = Tk()
    cylinder.title("Cylinder")
    cylinder.geometry("390x350")
    cylinder.resizable(False, False)

    ce1 = Entry(cylinder)
    ce1.place(relx=0.6, rely=0.1)

    ce2 = Entry(cylinder)
    ce2.place(relx=0.6, rely=0.2)

    ce3 = Entry(cylinder)
    ce3.place(relx=0.6, rely=0.4)

    ce4 = Entry(cylinder)
    ce4.place(relx=0.6, rely=0.6)

    ce5 = Entry(cylinder)
    ce5.place(relx=0.6, rely=0.8)

    def cylinder_reset():
        ce1.delete(0, END)
        ce2.delete(0, END)
        ce3.delete(0, END)
        ce4.delete(0, END)
        ce5.delete(0, END)

    def cylinder_calc():
        try:
            cr = float(ce1.get())
            ch = float(ce2.get())
            csa = abs(2 * 22 / 7 * cr * ch)
            tsa = abs(2 * 22 / 7 * cr * (cr + ch))
            vol = abs(22 / 7 * cr * cr * ch)

            csa_str = str(round(csa, 2))
            tsa_str = str(round(tsa, 2))
            vol_str = str(round(vol, 2))

            ce3.delete(0, END)
            ce4.delete(0, END)
            ce5.delete(0, END)
            ce3.insert(0, csa_str + " cm²")
            ce4.insert(0, tsa_str + " cm²")
            ce5.insert(0, vol_str + " cm³")


        except Exception:
            ce3.delete(0, END)
            ce4.delete(0, END)
            ce5.delete(0, END)

            ce3.insert(0, "ERROR : Refer Help ")
            ce4.insert(0, "ERROR : Refer Help ")
            ce5.insert(0, "ERROR : Refer Help ")

    lbl_height = Label(cylinder, text="Enter your Radius")
    lbl_height.place(relx=0.1, rely=0.1)

    lbl_radius = Label(cylinder, text="Enter your Height")
    lbl_radius.place(relx=0.1, rely=0.2)

    lbl_csa = Label(cylinder, text="Curved surface area of Cylinder")
    lbl_csa.place(relx=0.1, rely=0.4)

    lbl_tsa = Label(cylinder, text="Total surface area of Cylinder")
    lbl_tsa.place(relx=0.1, rely=0.6)

    lbl_vol = Label(cylinder, text="Volume of Cylinder")
    lbl_vol.place(relx=0.1, rely=0.8)

    btn_reset = Button(cylinder, text="Reset", width=10, bg="#cccccc", command=cylinder_reset)
    btn_reset.place(relx=0.1, rely=0.9)

    btn_calculate = Button(cylinder, text="Calculate", width=10, bg="#cccccc", command=cylinder_calc)
    btn_calculate.place(relx=0.6, rely=0.9)


# =======================================================================================================
# square calculator
def square_calc1():
    square = Tk()
    square.title("square")
    square.geometry("390x350")
    square.resizable(False, False)

    ce1 = Entry(square)
    ce1.place(relx=0.6, rely=0.1)

    ce2 = Entry(square)
    ce2.place(relx=0.6, rely=0.2)

    ce3 = Entry(square)
    ce3.place(relx=0.6, rely=0.4)

    ce4 = Entry(square)
    ce4.place(relx=0.6, rely=0.6)

    ce5 = Entry(square)
    ce5.place(relx=0.6, rely=0.8)

    def square_reset():
        ce1.delete(0, END)
        ce2.delete(0, END)
        ce3.delete(0, END)
        ce4.delete(0, END)
        ce5.delete(0, END)

    def square_calc():
        try:
            cl = float(ce1.get())
            cb = float(ce2.get())
            perimeter = abs(2 * (cl + cb))
            area = abs(cl * cb)
            diagonal = math.pow(((cl * cl) + (cb * cb)), 0.5)

            perimeter_str = str(round(perimeter, 2))
            area_str = str(round(area, 2))
            diagonal_str = str(round(diagonal, 2))

            ce3.delete(0, END)
            ce4.delete(0, END)
            ce5.delete(0, END)

            ce3.insert(0, perimeter_str + " cm")
            ce4.insert(0, area_str + " cm²")
            ce5.insert(0, diagonal_str + " cm")


        except Exception:
            ce3.delete(0, END)
            ce4.delete(0, END)
            ce5.delete(0, END)

            ce3.insert(0, "ERROR : Refer Help ")
            ce4.insert(0, "ERROR : Refer Help ")
            ce5.insert(0, "ERROR : Refer Help ")

    lbl_length = Label(square, text="Enter your Length (in cm)")
    lbl_length.place(relx=0.1, rely=0.1)

    lbl_breadth = Label(square, text="Enter your Breadth (in cm)")
    lbl_breadth.place(relx=0.1, rely=0.2)

    lbl_perimeter = Label(square, text="Perimeter of Square")
    lbl_perimeter.place(relx=0.1, rely=0.4)

    lbl_area = Label(square, text="Area of Square")
    lbl_area.place(relx=0.1, rely=0.6)

    lbl_area = Label(square, text="Diagonal of Square")
    lbl_area.place(relx=0.1, rely=0.8)

    btn_calculate = Button(square, text="Calculate", width=10, bg="#cccccc", command=square_calc)
    btn_calculate.place(relx=0.6, rely=0.9)

    btn_reset = Button(square, text="Reset", width=10, bg="#cccccc", command=square_reset)
    btn_reset.place(relx=0.1, rely=0.9)


# ================================================================================================================

# cube calculator

def cube_calc1():
    cube = Tk()
    cube.title("Cube Cuboid")
    cube.geometry("390x350")
    cube.resizable(False, False)

    ce1 = Entry(cube)
    ce1.place(relx=0.6, rely=0.1)

    ce2 = Entry(cube)
    ce2.place(relx=0.6, rely=0.2)

    ce3 = Entry(cube)
    ce3.place(relx=0.6, rely=0.3)

    ce4 = Entry(cube)
    ce4.place(relx=0.6, rely=0.5)

    ce5 = Entry(cube)
    ce5.place(relx=0.6, rely=0.6)

    ce6 = Entry(cube)
    ce6.place(relx=0.6, rely=0.7)

    ce7 = Entry(cube)
    ce7.place(relx=0.6, rely=0.8)

    def cube_reset():
        ce1.delete(0, END)
        ce2.delete(0, END)
        ce3.delete(0, END)
        ce4.delete(0, END)
        ce5.delete(0, END)
        ce6.delete(0, END)
        ce7.delete(0, END)

    def cube_calc():
        try:
            cl = float(ce1.get())
            cb = float(ce2.get())
            ch = float(ce3.get())

            tsa = abs(2 * ((cl * cb) + (cb * ch) + (ch * cl)))
            lsa = abs(2 * ch * (cl + cb))
            vol = abs(cl * cb * ch)
            diagonal = math.pow(((cl * cl) + (cb * cb) + (ch * ch)), 0.5)

            tsa_str = str(round(tsa, 2))
            lsa_str = str(round(lsa, 2))
            vol_str = str(round(vol, 2))
            diagonal_str = str(round(diagonal, 2))

            ce4.delete(0, END)
            ce5.delete(0, END)
            ce6.delete(0, END)
            ce7.delete(0, END)

            ce4.insert(0, tsa_str + " cm²")
            ce5.insert(0, lsa_str + " cm²")
            ce6.insert(0, vol_str + " cm³")
            ce7.insert(0, diagonal_str + " cm")


        except Exception:
            ce4.delete(0, END)
            ce5.delete(0, END)
            ce6.delete(0, END)
            ce7.delete(0, END)

            ce4.insert(0, "ERROR : Refer Help ")
            ce5.insert(0, "ERROR : Refer Help ")
            ce6.insert(0, "ERROR : Refer Help ")
            ce7.insert(0, "ERROR : Refer Help ")

    lbl_length = Label(cube, text="Enter your Length")
    lbl_length.place(relx=0.1, rely=0.1)

    lbl_breadth = Label(cube, text="Enter your Breadth")
    lbl_breadth.place(relx=0.1, rely=0.2)

    lbl_height = Label(cube, text="Enter your Height")
    lbl_height.place(relx=0.1, rely=0.3)

    lbl_height = Label(cube, text="Total surface area of Cube")
    lbl_height.place(relx=0.1, rely=0.5)

    lbl_csa = Label(cube, text="Lateral surface area of Cube")
    lbl_csa.place(relx=0.1, rely=0.6)

    lbl_tsa = Label(cube, text="Volume of Cube")
    lbl_tsa.place(relx=0.1, rely=0.7)

    lbl_vol = Label(cube, text="Main Diagonal")
    lbl_vol.place(relx=0.1, rely=0.8)

    btn_calculate = Button(cube, text="Reset", width=10, bg="#cccccc", command=cube_reset)
    btn_calculate.place(relx=0.1, rely=0.9)

    btn_reset = Button(cube, text="Calculate", width=10, bg="#cccccc", command=cube_calc)
    btn_reset.place(relx=0.6, rely=0.9)


# ====================================================================================================
# help
def help():
    root = Tk()
    root.geometry("500x500")
    root.title("HELP")
    root.resizable(False, False)

    lbl = Label(root, text="Calculator - HELP\n\n\n"
                           "»  Avoid  unnecessary trailing OPERATORS after \nDigits/Numbers \n\n\n"

                           "»  Avoid  leading ZEROES (example :- 4 + 05 ) in Calculation \n Zeroes between and after numbers are allowed \n\n\n"

                           "»  root function only consider the input text field \n not output text field \n\n\n"

                           "»  In Date,Circle,Square Rectangle,Cube Cuboid, \nCylinder and Circle follow the correct format"
                           " specified\n\n\n "

                           "»  Use brackets CAREFULLY .\n If a bracket is opened , remember to close it\n\n\n"

                           "»  CE : Clear Entry - Clears single entry\n C : Clear - Clears all Entry")

    lbl.place(relx=0.1, rely=0.1)


# defines the buttons


button_1 = Button(window, text="1", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=42, pady=20, font=("verdana", 11), bg="#FFFFFF", borderwidth=0,
                  command=lambda: button_click(0))

button_date = Button(window, text="Date", padx=30, pady=23, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                     command=calculate_date1)
button_dot = Button(window, text=".", padx=44, pady=23, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                    command=lambda: button_click("."))
button_equal = Button(window, text="=", padx=40, pady=22, font=("verdana", 11), bg="#99ddff", borderwidth=0, height=5,
                      width=2,
                      command=button_equal)
button_add = Button(window, text="+", padx=41, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                    command=lambda: button_click(" + "))
button_minus = Button(window, text="-", padx=44, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                      command=lambda: button_click(" - "))
button_multiply = Button(window, text="x", padx=43, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                         command=lambda: button_click(" x "))
button_divide = Button(window, text="÷", padx=41, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                       command=lambda: button_click(" ÷ "))
button_modulus = Button(window, text="%", padx=39, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                        command=lambda: button_click(" % "))
button_c = Button(window, text=" C", padx=39, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                  command=button_c)
button_ce = Button(window, text="CE", padx=36, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                   command=button_ce)
button_open_bracket = Button(window, text="( ", padx=41, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                             command=lambda: button_click(" ( "))
button_close_bracket = Button(window, text=")", padx=43, pady=20, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                              command=lambda: button_click(" ) "))
button_root = Button(window, text="√x", padx=36, pady=23, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                     command=button_root)
button_square = Button(window, text="square \n rectangle ", padx=9, pady=14, font=("verdana", 11), bg="#e6e6e6",
                       borderwidth=0,
                       command=square_calc1)
button_circle = Button(window, text="circle", padx=28, pady=23, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                       command=circle_calc1)
button_cube = Button(window, text="cube\ncuboid", padx=23, pady=14, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                     command=cube_calc1)
button_cylinder = Button(window, text="Cylinder", padx=18, pady=23, font=("verdana", 11), bg="#e6e6e6", borderwidth=0,
                         command=cylinder_calc1)

button_help = Button(window, text="Help", command=help)

# =============================================================================================================

# displays the button

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=6, column=1)
button_date.grid(row=8, column=0)
button_dot.grid(row=8, column=1)
button_equal.grid(row=6, column=3, rowspan=3, padx=1, pady=1)
button_add.grid(row=5, column=3)
button_minus.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_modulus.grid(row=2, column=2)
button_c.grid(row=2, column=1)
button_ce.grid(row=2, column=0)
button_open_bracket.grid(row=6, column=0)
button_close_bracket.grid(row=6, column=2)
button_root.grid(row=8, column=2)
button_square.grid(row=9, column=0)
button_circle.grid(row=9, column=1)
button_cube.grid(row=9, column=2)
button_cylinder.grid(row=9, column=3)
button_help.grid(column=4, row=0)

button_equal.bind("<Enter>", on_enter_equal)
button_equal.bind("<Leave>", on_leave_equal)
button_c.bind("<Enter>", on_enter_c)
button_c.bind("<Leave>", on_leave_c)

window.mainloop()
