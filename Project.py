from Tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("IQ Test")
global img
# Exit Program button
exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
exitprogram.grid(row=1, column=1)
levels = []
global correctAns
correctAns = 0

# Test types and beginning tests
def beginMiniTest():
    global totalQs
    totalQs = 5
    intro.grid_forget()
    minitest.grid_forget()
    fulltest.grid_forget()
    exitprogram.grid_forget()
    loadQ1()
    pass

def beginFullTest():
    global totalQs
    totalQs = 10
    intro.grid_forget()
    minitest.grid_forget()
    fulltest.grid_forget()
    exitprogram.grid_forget()
    loadQ1()
    pass
# All intro widgets
intro = Label(root, text="Welcome to your IQ test\nPlease select your test",
              bd=1, relief="solid", font="Times 32", width=21, height=2,
              anchor=N)

intro.grid(row=0, column=0, columnspan=3)

minitest = Button(root, text="Mini-test(5 questions)", height=2, 
                  bg='grey', command=beginMiniTest)
fulltest = Button(root, text="Full-test(10 questions)", height=2, 
                  bg='grey', command=beginFullTest)

minitest.grid(row=1, column=0)
fulltest.grid(row=1, column=2)

# Q1 widgets
def loadQ1():
    Q1 = Label(root, text="What is the next number in the series:", bd = 1,
           relief="solid", font="Times 20", width=29, height=1, anchor=N)
    Q1pattern = Label(root, text="7, 10, 16, 28, 52, ___", bd = 1,
                  font="Times 20", width=21, height=1)
    Q1.grid(row=0, column=0)
    
    Q1pattern.grid(row=1, column=0)
    r = IntVar()
    b1 = Radiobutton(root, text="88", variable=r, value=1)
    b1.grid(row=2, column=0)
    b2 = Radiobutton(root, text="100", variable=r, value=2, anchor=W)
    b2.grid(row=3, column=0)
    b3 = Radiobutton(root, text="66", variable=r, value=3, anchor=W)
    b3.grid(row=4, column=0)
    b4 = Radiobutton(root, text="76", variable=r, value=4, anchor=W)
    b4.grid(row=5, column=0)
    submit = Button(root, text="Submit", height=2, width=12, bg='grey',
                    command=lambda: submitQ1())
    submit.grid(row=6, column = 0)
    exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
    exitprogram.grid(row=7, column=0)
    def submitQ1():
        global correctAns
        if(r.get() == 2):
            correctAns += 1
        Q1.grid_forget()
        Q1pattern.grid_forget()
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        b4.grid_forget()
        submit.grid_forget()
        exitprogram.grid_forget()
        loadQ2()
        pass

def loadQ2():
    global correctAns
    Q2photo = PhotoImage(file="images/Q2.gif")
    img = Q2photo
    Q2label = Label(root, image=img)
    Q2label.grid(row=0, column=0, columnspan=2)
    Q2 = Label(root, text="Which figure belongs in the empty spot?", bd = 1,
           relief="solid", font="Times 20", width=29, height=1, anchor=N)
    Q2.grid(row=1, column=0, columnspan=2)
    r = IntVar()
    b1 = Radiobutton(root, text="1", variable=r, value=1)
    b1.grid(row=2, column=0)
    b2 = Radiobutton(root, text="2", variable=r, value=2, anchor=W)
    b2.grid(row=3, column=0)
    b3 = Radiobutton(root, text="3", variable=r, value=3, anchor=W)
    b3.grid(row=4, column=0)
    b4 = Radiobutton(root, text="4", variable=r, value=4, anchor=W)
    b4.grid(row=5, column=0)
    b5 = Radiobutton(root, text="5", variable=r, value=5)
    b5.grid(row=2, column=1)
    b6 = Radiobutton(root, text="6", variable=r, value=6, anchor=W)
    b6.grid(row=3, column=1)
    b7 = Radiobutton(root, text="7", variable=r, value=7, anchor=W)
    b7.grid(row=4, column=1)
    b8 = Radiobutton(root, text="8", variable=r, value=8, anchor=W)
    b8.grid(row=5, column=1)
    submit = Button(root, text="Submit", height=2, width=12, bg='grey',
                    command=lambda: submitQ2())
    submit.grid(row=6, column = 0, columnspan=2)
    exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
    exitprogram.grid(row=7, column=0, columnspan=2)
    
    def submitQ2():
        global correctAns
        if(r.get() == 3):
            correctAns += 1
        Q2.grid_forget()
        Q2label.grid_forget()
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        b4.grid_forget()
        b5.grid_forget()
        b6.grid_forget()
        b7.grid_forget()
        b8.grid_forget()
        submit.grid_forget()
        exitprogram.grid_forget()
        loadQ3()
        pass
    
def loadQ3():
    Q3 = Label(root, text="Which conclusion can you draw with absolute certainty?",
               bd = 1, relief="solid", font="Times 20", width=42, height=1, anchor=N)
    Q3statement = Label(root, text="None of the runners is a teacher.",
                         bd = 1, font="Times 20", width=25, height=1)
    Q3statement2 = Label(root, text="All of the attendees are runners.",
                         bd = 1, font="Times 20", width=25, height=1)
    Q3.grid(row=0, column=0)
    Q3statement.grid(row=1, column=0)
    Q3statement2.grid(row=2, column=0)
    r = IntVar()
    b1 = Radiobutton(root, text="some attendees are teachers", variable=r, value=1)
    b1.grid(row=3, column=0)
    b2 = Radiobutton(root, text="no runners are attendees", variable=r, value=2, anchor=W)
    b2.grid(row=4, column=0)
    b3 = Radiobutton(root, text="teachers are not attendees", variable=r, value=3, anchor=W)
    b3.grid(row=5, column=0)
    b4 = Radiobutton(root, text="all runners are teachers", variable=r, value=4, anchor=W)
    b4.grid(row=6, column=0)
    submit = Button(root, text="Submit", height=2, width=12, bg='grey',
                    command=lambda: submitQ3())
    submit.grid(row=7, column = 0)
    exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
    exitprogram.grid(row=8, column=0)
    def submitQ3():
        global correctAns
        if(r.get() == 3):
            correctAns += 1
        Q3.grid_forget()
        Q3statement.grid_forget()
        Q3statement2.grid_forget()
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        b4.grid_forget()
        submit.grid_forget()
        exitprogram.grid_forget()
        loadQ4()
        pass

def loadQ4():
    Q4photo = PhotoImage(file="images/Q4.gif")
    img = Q4photo
    Q4label = Label(root, image=img)
    Q4label.grid(row=0, column=0)
    Q4 = Label(root, text="Which 3 choices are needed to create the figure on the left?",
               bd = 1, relief="solid", font="Times 20", width=50, height=1, anchor=N)
    Q4.grid(row=1, column=0)
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    e = IntVar()
    Q4statement = Label(root, text="Only tiles of the same color may overlap",
               bd = 1, font="Times 20", width=50, height=1, anchor=N)
    Q4statement.grid(row=2, column=0)
    b1 = Checkbutton(root, text="A", variable=a)
    b1.grid(row=3, column=0)
    b2 = Checkbutton(root, text="B", variable=b)
    b2.grid(row=4, column=0)
    b3 = Checkbutton(root, text="C", variable=c)
    b3.grid(row=5, column=0)
    b4 = Checkbutton(root, text="D", variable=d)
    b4.grid(row=6, column=0)
    b5 = Checkbutton(root, text="E", variable=e)
    b5.grid(row=7, column=0)
    submit = Button(root, text="Submit", height=2, width=12, bg='grey',
                    command=lambda: submitQ4())
    submit.grid(row=8, column = 0)
    exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
    exitprogram.grid(row=9, column=0)
    def submitQ4():
        global correctAns
        if(e.get() == 0 and a.get() == 0):
            if(b.get() == 1 and c.get() == 1):
                if(d.get() == 1):
                    correctAns +=1
        Q4.grid_forget()
        Q4label.grid_forget()
        Q4statement.grid_forget()
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        b4.grid_forget()
        b5.grid_forget()
        submit.grid_forget()
        exitprogram.grid_forget()
        loadQ5()
        pass
def loadQ5():
    Q5 = Label(root, text="What is the missing number in the series:", bd = 1,
           relief="solid", font="Times 20", width=32, height=1, anchor=N)
    Q5pattern = Label(root, text="3, 9, 81, 15, 21, 71, __, 33, 61", bd = 1,
                  font="Times 20", width=24, height=1)
    Q5.grid(row=0, column=0)
    
    Q5pattern.grid(row=1, column=0)
    r = IntVar()
    b1 = Radiobutton(root, text="56", variable=r, value=1)
    b1.grid(row=2, column=0)
    b2 = Radiobutton(root, text="22", variable=r, value=2, anchor=W)
    b2.grid(row=3, column=0)
    b3 = Radiobutton(root, text="27", variable=r, value=3, anchor=W)
    b3.grid(row=4, column=0)
    b4 = Radiobutton(root, text="25", variable=r, value=4, anchor=W)
    b4.grid(row=5, column=0)
    submit = Button(root, text="Submit", height=2, width=12, bg='grey',
                    command=lambda: submitQ5())
    submit.grid(row=6, column = 0)
    exitprogram = Button(root, text="Exit Program", height=2, width=12,
                     bg='red', command=root.quit)
    exitprogram.grid(row=7, column=0)
    def submitQ5():
        global correctAns
        global totalQs
        if(r.get() == 3):
            correctAns += 1
        Q5.grid_forget()
        Q5pattern.grid_forget()
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        b4.grid_forget()
        submit.grid_forget()
        exitprogram.grid_forget()
        if(totalQs == 5):
            loadResults()
        else:
            loadQ6()
def loadResults():
    global totalQs
    global correctAns
    score = float(correctAns) / totalQs * 200
    result = Label(root, text="Congratulations your score is \n {}".format(score),
              bd=1, relief="solid", font="Times 32", bg ="grey", width=25, height=2,
              anchor=N)

    result.grid(row=0, column=0)
    answers = Label(root, text="You got {}/{} questions correct".format(correctAns, totalQs),
                    bd=1, font="Times 32", width=25, height=1)
    answers.grid(row=1, column=0)

    stats = Label(root, text="Average score = 100 | Perfect score = 200", bd=1,
                  font="Times 32", width=30, height=1)
    stats.grid(row=2, column=0)
    
def loadQ6():
    print "nah"
    pass
root.mainloop()
