from tkinter import * 
from tkinter.ttk import *
import os
import time
import webbrowser


# DO NOT REDISTRIBUTE THIS PRODUCT!


def ok_error_command():
    Label1.destroy()
    Label2.destroy()
    ok_err.destroy()
    ct_error.destroy()
    virus_err.destroy()

    global Title_Var
    global Text_Var    
    Title_Var = StringVar()
    Text_Var = StringVar()
    
    Label(screen, text="").pack()
    Label(screen,text="").pack()
    Title_Label = Label(screen, text="Title of Window Error", font = ('Arial', 14))
    Title_Label.pack()

    Label(screen, text="").pack()
    
    Title_Entry = Entry(width=35, textvariable=Title_Var)
    Title_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()

    Text_Label = Label(screen, text="Text in Window Error", font = ('Arial', 14))
    Text_Label.pack()

    Label(screen, text="").pack()
    
    Text_Entry = Entry(width=100,textvariable=Text_Var)
    Text_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()
    global compile_btn
    compile_btn = Button(screen, width=50, text = 'Compile Your Error', command=compile_ok_error)
    compile_btn.pack(side = TOP)

def compile_ok_error():
    global Title
    Title = Title_Var.get()
    Text = Text_Var.get()
    error = open(f'Errors/{Title}.vbs', 'w')
    error.write(f"X=MsgBox(\"{Text}\",0+64,\"{Title}\")")
    error.close()
    
    Label(screen, text="").pack()
    compiling_label = Label(screen, text = "Compiling...")
    compiling_label.pack()
    Label(screen, text="").pack()

    progress = Progressbar(screen, orient = HORIZONTAL, length = 300, mode = 'determinate')
    progress.pack(pady = 10) 
    progress['value'] = 20
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    screen.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100
    
    compiling_label.destroy()
    Label(screen, text = "Finished Compiling, your error is in the Errors folder", font=('Arial', 12)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Preview Error", command=preview_ok_error).pack()
    compile_btn.destroy()
    Label(screen, text="").pack()
    Button(screen, text="Compile Another Error!", width=30, command=refresh).pack()
    Label(screen, text="").pack()
    Button(screen, text="By Just Another Coder!", width=25, command=subscribe).pack()
    
def preview_ok_error():
    os.system(f"Errors\{Title}.vbs")


def ct_error_command():
    Label1.destroy()
    Label2.destroy()
    ok_err.destroy()
    ct_error.destroy()
    virus_err.destroy()

    global Title1_Var
    global Text1_Var    
    Title1_Var = StringVar()
    Text1_Var = StringVar()
    
    Label(screen, text="").pack()
    Label(screen,text="").pack()
    Title1_Label = Label(screen, text="Title of Window Error", font = ('Arial', 14))
    Title1_Label.pack()

    Label(screen, text="").pack()
    
    Title1_Entry = Entry(width=35, textvariable=Title1_Var)
    Title1_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()

    Text1_Label = Label(screen, text="Text in Window Error", font = ('Arial', 14))
    Text1_Label.pack()

    Label(screen, text="").pack()
    
    Text1_Entry = Entry(width=100,textvariable=Text1_Var)
    Text1_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()
    global compile1_btn
    compile1_btn = Button(screen, width=50, text = 'Compile Your Error', command=compile_ct_error)
    compile1_btn.pack(side = TOP)    

def compile_ct_error():
    global Title1
    Title1 = Title1_Var.get()
    Text1 = Text1_Var.get()
    error1 = open(f'Errors/{Title1}.vbs', 'w')
    error1.write(f"X=MsgBox(\"{Text1}\",3+48,\"{Title1}\")")
    error1.close()
    
    Label(screen, text="").pack()
    compiling_label1 = Label(screen, text = "Compiling...")
    compiling_label1.pack()
    Label(screen, text="").pack()

    progress = Progressbar(screen, orient = HORIZONTAL, length = 300, mode = 'determinate')
    progress.pack(pady = 10) 
    progress['value'] = 20
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    screen.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100

    compiling_label1.destroy()
    Label(screen, text = "Finished Compiling, your error is in the Errors folder", font=('Arial', 12)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Preview Error", command=preview_ct_error).pack()
    compile1_btn.destroy()
    Label(screen, text="").pack()
    Button(screen, text="Compile Another Error!", width=30, command=refresh).pack()
    Label(screen, text="").pack()
    Button(screen, text="By Just Another Coder!", width=25, command=subscribe).pack()

def preview_ct_error():
    os.system(f"Errors\{Title1}.vbs")

def alert_error_command():
    Label1.destroy()
    Label2.destroy()
    ok_err.destroy()
    ct_error.destroy()
    virus_err.destroy()

    global Title2_Var
    global Text2_Var    
    Title2_Var = StringVar()
    Text2_Var = StringVar()
    
    Label(screen, text="").pack()
    Label(screen,text="").pack()
    Title2_Label = Label(screen, text="Title of Window Error", font = ('Arial', 14))
    Title2_Label.pack()

    Label(screen, text="").pack()
    
    Title2_Entry = Entry(width=35, textvariable=Title2_Var)
    Title2_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()

    Text2_Label = Label(screen, text="Text in Window Error", font = ('Arial', 14))
    Text2_Label.pack()

    Label(screen, text="").pack()
    
    Text2_Entry = Entry(width=100,textvariable=Text2_Var)
    Text2_Entry.pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()
    global compile2_btn
    compile2_btn = Button(screen, width=50, text = 'Compile Your Error', command=compile_alert_error)
    compile2_btn.pack(side = TOP)    

def compile_alert_error():
    global Title2
    Title2 = Title2_Var.get()
    Text2 = Text2_Var.get()
    error2 = open(f'Errors/{Title2}.vbs', 'w')
    error2.write(f"X=MsgBox(\"{Text2}\",3+16,\"{Title2}\")")
    error2.close()
    
    Label(screen, text="").pack()
    compiling_label2 = Label(screen, text = "Compiling...")
    compiling_label2.pack()
    Label(screen, text="").pack()

    progress = Progressbar(screen, orient = HORIZONTAL, length = 300, mode = 'determinate')
    progress.pack(pady = 10) 
    progress['value'] = 20
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    screen.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    screen.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100

    compiling_label2.destroy()
    Label(screen, text = "Finished Compiling, your error is in the Errors folder", font=('Arial', 12)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Preview Error", command=preview_alert_error).pack()
    compile2_btn.destroy()
    Label(screen, text="").pack()
    Button(screen, text="Compile Another Error!", width=30, command=refresh).pack()
    Label(screen, text="").pack()
    Button(screen, text="By Just Another Coder!", width=25, command=subscribe).pack()

def preview_alert_error():
    os.system(f"Errors\{Title2}.vbs")

def refresh():
    screen.destroy()
    main_screen()

def subscribe():
    webbrowser.open("https://www.youtube.com/channel/UChJdYcnvUGkUzl0rH4orcog")

def main_screen():
    global screen
    screen = Tk()
    screen.title("Error Simulator ~ By Just Another Coder")
    screen.geometry("800x700")
    screen.iconbitmap("assets/icon.ico")

    global Label1
    Label1 = Label(text = "Welcome to Error Simulator! Created by Just Another Coder", font = ('Arial', 14))
    Label1.pack()

    Label(text = "").pack()
    global Label2
    Label2 = Label(text = "Choose what type of error you want to simulate below by clicking on it:", font = ('Arial', 14))
    Label2.pack()

    Label(text = "").pack()
    global ok_err
    ok_error = PhotoImage(file = r"assets/ok_error.png")
    ok_err = Button(screen, text = 'Ok Error', image = ok_error, compound = BOTTOM, command=ok_error_command)
    ok_err.pack(side = TOP)

    Label(text = "").pack()
    global ct_error
    caution_error = PhotoImage(file = r"assets/caution_error.png")
    ct_error = Button(screen, text = 'Caution Error', image = caution_error, compound = BOTTOM, command=ct_error_command)
    ct_error.pack(side = TOP)

    Label(text = "").pack()
    global virus_err
    virus_error = PhotoImage(file = r"assets/virus_error.png")
    virus_err = Button(screen, text = 'Alert Error', image = virus_error, compound = BOTTOM, command=alert_error_command)
    virus_err.pack(side = TOP)

    screen.mainloop()

main_screen()












