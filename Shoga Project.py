import customtkinter as CTk
import datetime
import webbrowser
import requests

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    return f"Shoga - It's {current_time}"

def get_current_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A(%d), %B(%m) %Y")
    return f"Shoga - It's {current_date}"

def get_site_name(command_str):
    part = command_str.split(" ")
    junt = ""
    for i in part:
        if i == "open":
            continue
        junt = junt + i
    return junt

def open_site():
    user_input = get_site_name(user_input_entry.get())
    url = "https://www.{}.com/".format(user_input)
    try:
        response = requests.head(url)
        if response.status_code == 200:
            webbrowser.open(url)
            return 'Ok ^^'
    except:
        pass

def open_gpt():
    url = "https://chat.openai.com/"
    webbrowser.open(url)
    return 'Ok ^^'


def help():
    command = """\"time" = Shows time
\"Date\" = Shows what day is today
\"Exit\" = End the chat
\"Open (site name)\" = Open site"""
    return command

def get_bot_response(user_input):
    if "time" in user_input.lower():
        return get_current_time()
    elif "date" in user_input.lower():
        return get_current_date()
    elif ("--help" in user_input.lower()) or ("what can you do?" in user_input.lower()):
        return help()
    elif ("open chatgpt" in user_input.lower()) or ("open chat gpt" in user_input.lower()) or ("open gpt" in user_input.lower()):
        return open_gpt()
    elif "open" in user_input.lower():
        user_input = get_site_name(user_input)
        return open_site()
    elif "exit" in user_input.lower():
        return 'Bye ^^'
    else:
        return "I don't know if I can do that, please type \"--help\" to see the commands"



def initial(event):
    chat_display.insert(CTk.END, f"Shoga - Hej, how can I help you?\n")
    chat_display.configure(state=CTk.DISABLED)


def send_message(event=None):
    user_input = user_input_entry.get()
    chat_display.configure(state=CTk.NORMAL)  
    chat_display.insert(CTk.END, f"You - {user_input}\n")
    
    response = get_bot_response(user_input)
    chat_display.insert(CTk.END, f"Shoga - {response}\n")
    chat_display.configure(state=CTk.DISABLED)  
    user_input_entry.delete(0, CTk.END)  

    if "exit" in user_input.lower():
        chat_display.configure(state=CTk.DISABLED)
        user_input_entry.configure(state=CTk.DISABLED)
        send_button.configure(state=CTk.DISABLED)
        root.after(1200, root.destroy)

root = CTk.CTk()
root.title("Shoga - Chatbot")
CTk.set_appearance_mode("dark")
root.geometry('600x435')
root.resizable(True, True)
root.minsize(width = 400, height = 435)

chat_display =CTk.CTkTextbox(root, wrap=CTk.WORD, state=CTk.NORMAL) 
chat_display.pack(fill=CTk.BOTH, expand=True)
chat_display.bind('<Motion>', initial)           

user_input_entry = CTk.CTkEntry(root)
user_input_entry.pack(fill=CTk.X, pady=1)
user_input_entry.bind('<Motion>', initial)  
user_input_entry.bind("<Return>", send_message)  

send_button = CTk.CTkButton(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
