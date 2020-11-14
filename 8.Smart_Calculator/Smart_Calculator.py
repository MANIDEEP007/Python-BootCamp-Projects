from tkinter import *

#Addition
def add(a,b):
    return a+b

#Subtraction
def sub(a,b):
    return a-b

#Multiplication
def mul(a,b):
    return a*b

#Division
def div(a,b):
    return a/b

#Modulus
def mod(a,b):
    return a%b

#LCM
def lcm(a,b):
    l = a if a>b else b
    while l <= a*b:
        if l % a == 0 and l % b == 0:
            return l
        else:
            l += 1
#HCF
def hcf(a,b):
    h = a if a<b else b
    while h >= 1:
        if a % h ==0 and b % h==0:
            return h
        else:
            h = h - 1

#Extract Numbers
def extract_num(text):
    num = []
    #Get Numbers
    for word in text.strip().split():
        try:
            num.append(float(word))
        except ValueError:
            pass
    return num

#Calculate
def calculate():
    #Get Text from Entry box
    text = text_ent.get()
    for word in text.split():
        if word.upper() in operations.keys():
            try:
                num = extract_num(text)
                res = operations[word.upper()](num[0],num[1])
                list_box.delete(0,END)
                list_box.insert(END,res)
            except:
                list_box.delete(0,END)
                list_box.insert(END,"Something Went Wrong1. Please try Again")
            finally:
                break
        elif word.upper() not in operations.keys():
            list_box.delete(0,END)
            list_box.insert(END,"Something Went Wrong. Please try Again")

#Operations dictionary
operations = {
    'ADD':add,
    'ADDITION':add,
    'SUM':add,
    "PLUS":add,
    'SUB':sub,
    'DIFFERENCE':sub,
    'MINUS':sub,
    'SUBTRACT':sub,
    'LCM':lcm,
    'HCF':hcf,
    'MULTIPLICATION':mul,
    'PRODUCT':mul,
    'MULTIPLY':mul,
    'DIVISION':div,
    'DIV':div,
    'MOD':mod,
    'REMAINDER':mod,
    'MODULUS':mod,
    }
#Create Window Object
win = Tk()
#Set Size of Window
win.geometry("500x500")
#Set Background color for Window
win.configure(bg="lightskyblue")
#Set Title for Window
win.title("Smart Calculator")

#Create Label
l1 = Label(
           win,
           text="I am a Smart Calculator",
           width=20,
           padx=3,
           )
l1.place(x=150,y=10)

#Create Label2
l2 = Label(
           win,
           text="My Name is Pugger",
           padx=3,
           )
l2.place(x=180,y=40)

#Create Label3
l3 = Label(
           win,
           text="How can I help you?",
           padx=3,
           )
l3.place(x=176,y=130)

#Variable to Get Text entered by User
text_var = StringVar()

#Entry Box
text_ent = Entry(
    win,
    width=30,
    textvariable=text_var
    )
text_ent.place(x=140,y=160)

#Add Button
btn = Button(
    win,
    text="Just This!!",
    command=calculate,
    )
btn.place(x=210,y=200)

#List Box for Output
list_box = Listbox(
    win,
    width=40,
    height=3
    )
list_box.place(x=140,y=230)
