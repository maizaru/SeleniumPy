import tkinter,sys,clow

root = tkinter.Tk()
root.geometry('300x200')
root.title('tkTest')

label = tkinter.Label(text='指定URL')
label.place(x=30,y=20)
'''
label2 = tkinter.Label(text='DM内容2')
label2.place(x=30,y=40)
label3 = tkinter.Label(text='DM内容3')
label3.place(x=30,y=60)
'''
txt = tkinter.Entry(width=20)
txt.place(x=90,y=20)
'''
txt2 = tkinter.Entry(width=20)
txt2.place(x=90,y=40)
txt3 = tkinter.Entry(width=20)
txt3.place(x=90,y=60)

str_input = ["","",""]

fluctuation = 5

sVar = tkinter.IntVar(master=root,value=fluctuation,)

scale = tkinter.Scale(
    master=root,
    orient='horizontal',
    showvalue=True,
    variable=sVar,)
scale.place(x=90,y=80)
'''
def callback():
    '''
    str_input[0]=txt.get()
    str_input[1]=txt2.get()
    str_input[2]=txt3.get()
    '''
    clow.start(txt.get())
    clow.imagesClow()
    clow.textClow()
    #fluctuation = scale.get()
    #print(str_input)
    root.destroy()
    sys.exit()


btn = tkinter.Button(root,text='決定',command=callback)
btn.place(x=150,y=150)

#root.bind('<Return>',callback)
root.mainloop()