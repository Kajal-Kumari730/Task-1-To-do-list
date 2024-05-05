from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def adding_tasks():  
    tasks_string = tasks_field.get()  
    if len(tasks_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(tasks_string)   
        the_cursor.execute('insert into tasks values (?)', (tasks_string ,))    
        lists_update()    
        tasks_field.deleting(0, 'end')  
    
def lists_update():    
    clear_lists()    
    for task in tasks:    
        tasks_listsbox.insert('end', task)  
  
def deleting_task():  
    try:  
        the_value = tasks_listsbox.get(tasks_listsbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            lists_update()   
            the_cursor.execute('deleting from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def deleting_all_tasks():  
    message_box = messagebox.askyesno('Deleting All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('deleting from tasks')   
        lists_update()  
   
def clear_lists():   
    tasks_listsbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
   
if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do Lists ")  
    guiWindow.geometry("665x400+550+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  
   
    the_connection = sql.connect('listsOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []  
        
    functions_frame = Frame(guiWindow, bg = "#8EE5EE") 
    
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    tasks_label = Label( functions_frame,text = "TO-DO-LIST \n Enter the Task Title:",  
        font = ("arial", "14", "bold"),  
        background = "#8EE5EE", 
        foreground="#FF6103"
    )    
    tasks_label.place(x = 20, y = 30)  
        
    tasks_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )    
    tasks_field.place(x = 180, y = 30)  
    
    add_button =Button(  
        functions_frame,  
        text = "Add",  
        width = 15,
        bg='#D4AC0D',font=("arial", "14", "bold"),
        command = adding_tasks,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Remove",  
        width = 15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command = deleting_task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text = "Delete All",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='#D4AC0D',
        command = deleting_all_tasks  
    )
    
    exit_button = Button(  
        functions_frame,  
        text = "Exit / Close",  
        width = 52,
        bg='#D4AC0D',  font=("arial", "14", "bold"),
        command = close  
    )    
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    del_all_button.place(x = 460, y = 80)  
    exit_button.place(x = 17, y = 330)  
    
    tasks_listsbox = Listbox(  
        functions_frame,  
        width = 70,  
        height = 9,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#FF8C00",  
        selectforeground="BLACK"
    )    
    tasks_listsbox.place(x = 17, y = 140)  
    
    retrieve_database()  
    lists_update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()
