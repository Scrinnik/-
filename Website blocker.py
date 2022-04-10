from tkinter import*
from tkinter import messagebox
import time
from datetime import datetime


hosts = r'C:\Windows\System32\drivers\etc\hosts'
# hosts = '/etc/hosts'
redirect_url = '127.0.0.1'

root = Tk()
root.geometry("300x300")
root.title("Блокировщик сайтов")

starttime_text = StringVar()
starttime = Label(text="Введите время начала работы программы: ")  
starttime.grid(column=0, row=0)
message = Entry(textvariable = starttime_text)
message.grid(column = 0, row = 2)


finishtime_text = StringVar()
finishtime = Label(text="Введите время окончания работы программы: ")
finishtime.grid(column=0, row=4)
message = Entry(textvariable = finishtime_text)
message.grid(column=0, row=6)

blocked_sites_text = StringVar()
blocked_sites = Label(text = "Введите url сайтов через запятую: ")
blocked_sites.grid(column=0, row=8)
message = Entry(textvariable = blocked_sites_text)
message.grid(column=0, row=10)
print(blocked_sites_text.get())


def startApp():
    start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(starttime_text.get()))
    finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(finishtime_text.get()))
    print(blocked_sites_text.get())
    while True:
        if start_time_text < datetime.now() < finish_time_text:
            print('Доступ ограничен!')
            
            with open(hosts, 'r+') as file:
                src = file.read()
                
                for site in blocked_sites:
                    if site in src:
                        pass
                    else:
                        file.write(f'{redirect_url} {site}\n')
        else:
            with open(hosts, 'r+') as file:
                src = file.readlines()
                file.seek(0)
                
                for line in src:
                    if not any(site in line for site in blocked_sites):
                        file.write(line)
                file.truncate()
            print('Доступ открыт!')
            
        time.sleep(5)

btn = Button(root, text="Запуск программы", command=startApp)
btn.grid(column = 0, row = 12)



root.mainloop()
