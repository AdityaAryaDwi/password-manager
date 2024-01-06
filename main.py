from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_fun():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list=[random.choice(letters) for n in range(random.randint(8,10))]
    password_list+=[random.choice(symbols) for n in range(random.randint(2,4))]
    password_list+=[random.choice(numbers) for n in range(random.randint(2,4))]

    # password_list=[]
    # for char in range(nr_letters):
    #  password_list += random.choice(letters)

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    #password = ""
    # for char in password_list:
    #   password += char
    password="".join(password_list)
    pass_input.insert(END,password)
    pyperclip.copy(password)

#print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    web_temp=web_input.get().lower()
    user_temp=user_input.get()
    pass_temp=pass_input.get()
    data_dict={
        web_temp : {
            "email/userid" : user_temp,
            "password" : pass_temp
        }
    }

    if len(web_temp)==0 or len(user_temp)==0 or len(pass_temp)<6:
        messagebox.showwarning(title="Oops",message="Please don't leave any empty fields")
    else:    
        is_okay=messagebox.askokcancel(title=web_temp,message=f"Username : {user_temp}\nPassword : {pass_temp}\nDo you want to proceed")
        if is_okay:

            # with open("password_data.txt","a") as fl:
            #     fl.write(f"{web_temp}    |    {user_temp}    |    {pass_temp} \n")
            
            try:
                with open("password_data.json","r") as new_json:
                    temp_dict=json.load(new_json)
                    temp_dict.update(data_dict)
            except FileNotFoundError:
                with open("password_data.json","w") as new_jsonn:
                    json.dump(data_dict,new_jsonn,indent=4)
            else:
                with open("password_data.json","w") as n_json:
                    json.dump(temp_dict,n_json,indent=4)
            finally:
                web_input.delete(0,END)
                pass_input.delete(0,END)
def find_password():
    website=web_input.get().lower()
    try:
        with open("password_data.json","r") as data:
            temp_dict=json.load(data)
            temp_id=temp_dict[website]["email/userid"]
            temp_pass=temp_dict[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title=website,message="No data file found")
    except KeyError:
        messagebox.showerror(title=website,message="No details for the website exists")
    else:
        messagebox.showinfo(title=website,message=f"Email : {temp_id}\nPassword : {temp_pass}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=20)
canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)
web_label=Label(text="Website:")
web_label.grid(row=1,column=0)
user_label=Label(text="Email/Username:")
user_label.grid(row=2,column=0)
pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)
web_input=Entry(width=35)
web_input.grid(row=1,column=1,columnspan=2)
web_input.focus()
user_input=Entry(width=35)
user_input.insert(END,"userid@gmail.com")
user_input.grid(row=2,column=1,columnspan=2)
pass_input=Entry(width=35)
pass_input.grid(row=3,column=1,columnspan=2)
generate_pass=Button(text="Generate Password",highlightthickness=0,command=generate_fun)
generate_pass.grid(row=4,column=3)
add_pass=Button(text="Add",width=30,highlightthickness=0,command=save_to_file)
add_pass.grid(row=4,column=1,columnspan=2)
search_pass=Button(text="Search",highlightthickness=0,width=15,command=find_password)
search_pass.grid(row=1,column=3)

window.mainloop()