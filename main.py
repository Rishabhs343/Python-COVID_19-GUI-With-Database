from tkinter import *
from tkinter import messagebox, Menu
import requests
import json
import sqlite3

COVID = Tk()
COVID.title("Covid-19 INDIA LIVE")
photo = PhotoImage(file = "new.png")
COVID.iconphoto(False, photo)

con = sqlite3.connect('covid_19.db')
cursorObj = con.cursor()
cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS COVID(id INTEGER PRIMARY KEY, States TEXT NOT NULL, Cases INTEGER, Recovered INTEGER,Deaths INTEGER)")
con.commit()


def reset(nt=0):
    for cell in COVID.winfo_children():
        cell.destroy()

    app_nav()
    app_header()
    if nt == 1:
        my_portfolio()


def prev(num):
    global i
    if (num - 20) >= 0:
        con = sqlite3.connect('covid_19.db')
        cursorObj = con.cursor()

        count = 0
        rows = 1
        if (num - 10) % 10 == 0:
            i = num - 20 + 1
        else:
            k = (num - 10) % 10
            if (num + k - 10) % 10 == 0:
                i = num + k - 20 + 1
            else:
                if (num - k - 10) % 10 == 0:
                    i = num - k - 10 + 1

        for r in range(i, i + 11):
            if r <= 35:
                api_cln = cursorObj.execute("SELECT id,States,Cases,Recovered,Deaths from COVID WHERE id=?", (r,))
                api_cln = list(api_cln)

                if count < 10:
                    ID = Label(COVID, text=api_cln[0][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                               relief="groove",
                               padx="2", pady="2")
                    ID.grid(row=rows, column=0, sticky=N + S + E + W)

                    STATES = Label(COVID, text=api_cln[0][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                                   relief="groove", padx="2", pady="2")
                    STATES.grid(row=rows, column=1, sticky=N + S + E + W)

                    CASES = Label(COVID, text=api_cln[0][2], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                                  relief="groove", padx="2", pady="2")
                    CASES.grid(row=rows, column=2, sticky=N + S + E + W)

                    RECOVERED = Label(COVID, text=api_cln[0][3], bg="#F3F4F6", fg="black", font="Lato 12",
                                      borderwidth=2,
                                      relief="groove", padx="2", pady="2")
                    RECOVERED.grid(row=rows, column=3, sticky=N + S + E + W)

                    DEATHS = Label(COVID, text=api_cln[0][4], bg="#F3F4F6", fg="black", font="Lato 12",
                                   borderwidth=2,
                                   relief="groove", padx="2", pady="2")
                    DEATHS.grid(row=rows, column=4, sticky=N + S + E + W)
                    count += 1
                    rows += 1
                else:
                    break
            else:
                break

        api = ""
        i += 9
        refresh = Button(COVID, text="Refresh", bg="#142E54", fg="white", command=lambda: reset(1), font="Lato 12",
                         borderwidth=2,
                         relief="groove", padx="2", pady="2")
        refresh.grid(row=rows + 1, column=2, sticky=N + S + E + W)
        if i >= 35:
            next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                          borderwidth=2,
                          relief="groove", padx="2", pady="2", state=DISABLED)
            next.grid(row=rows + 1, column=4, sticky=N + S + E + W)

        else:
            next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                          borderwidth=2,
                          relief="groove", padx="2", pady="2")
            next.grid(row=rows + 1, column=4, sticky=N + S + E + W)
        if i <= 10:
            pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                         borderwidth=2,
                         relief="groove", padx="2", pady="2", state=DISABLED)
            pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)
        else:
            pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                         borderwidth=2,
                         relief="groove", padx="2", pady="2")
            pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)

def nxt(num):
    reset()
    con = sqlite3.connect('covid_19.db')
    cursorObj = con.cursor()

    count = 0
    rows = 1

    i = num+1

    for r in range(i, i + 11):
        if r<=35:
            api_cln = cursorObj.execute("SELECT id,States,Cases,Recovered,Deaths from COVID WHERE id=?", (r,))
            api_cln = list(api_cln)

            if count < 10:
                ID = Label(COVID, text=api_cln[0][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                           relief="groove",
                           padx="2", pady="2")
                ID.grid(row=rows, column=0, sticky=N + S + E + W)

                STATES = Label(COVID, text=api_cln[0][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                               relief="groove", padx="2", pady="2")
                STATES.grid(row=rows, column=1, sticky=N + S + E + W)

                CASES = Label(COVID, text=api_cln[0][2], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                              relief="groove", padx="2", pady="2")
                CASES.grid(row=rows, column=2, sticky=N + S + E + W)

                RECOVERED = Label(COVID, text=api_cln[0][3], bg="#F3F4F6", fg="black", font="Lato 12",
                                  borderwidth=2,
                                  relief="groove", padx="2", pady="2")
                RECOVERED.grid(row=rows, column=3, sticky=N + S + E + W)

                DEATHS = Label(COVID, text=api_cln[0][4], bg="#F3F4F6", fg="black", font="Lato 12",
                               borderwidth=2,
                               relief="groove", padx="2", pady="2")
                DEATHS.grid(row=rows, column=4, sticky=N + S + E + W)
                count += 1
                rows += 1
            else:
                break
        else:
            break

    api = ""
    i+=9
    refresh = Button(COVID, text="Refresh", bg="#142E54", fg="white", command=lambda: reset(1), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2")
    refresh.grid(row=rows + 1, column=2, sticky=N + S + E + W)
    if i >= 35:
        next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                      borderwidth=2,
                      relief="groove", padx="2", pady="2", state=DISABLED)
        next.grid(row=rows + 1, column=4, sticky=N + S + E + W)

    else:
        next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                      borderwidth=2,
                      relief="groove", padx="2", pady="2")
        next.grid(row=rows + 1, column=4, sticky=N + S + E + W)
    if i <= 10:
        pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2", state=DISABLED)
        pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)
    else:
        pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2")
        pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)


def app_nav():
    def close_app():
        COVID.destroy()

    menu = Menu(COVID)
    file_item = Menu(menu, tearoff=0)
    file_item.add_command(label='Close App', command=close_app)
    file_item["bg"]="blue"
    menu.add_cascade(label="File", menu=file_item)
    COVID.config(menu=menu)


def my_portfolio():
    url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise"

    headers = {
        'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
        'x-rapidapi-key': "ce449b0e7dmshb15238af6f10230p16d7b1jsn59796b7a5b76"
    }
    response = requests.request("GET", url, headers=headers)
    api = json.loads(response.content)
    con = sqlite3.connect('covid_19.db')
    cursorObj = con.cursor()
    cursorObj.execute("DROP TABLE COVID")
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS COVID(id INTEGER PRIMARY KEY, States TEXT NOT NULL, Cases INTEGER, Recovered "
        "INTEGER,Deaths INTEGER)")

    for data in api:
        if data['id']!="":
            cursorObj.execute("INSERT INTO COVID (id,States,Cases,Recovered,Deaths) VALUES ( ?,?,?,?,?)",
                              (int(data['id']), str(data['name']), int(data['cases']), int(data['recovered']), int(data['deaths'])))
        else:
            break
    con.commit()
    count = 0
    rows = 1
    i = 1

    for r in range(i, i + 11):
        if r <= 35:
            api_cln = cursorObj.execute("SELECT id,States,Cases,Recovered,Deaths from COVID WHERE id=?", (r,))
            api_cln = list(api_cln)

            if count < 10:
                ID = Label(COVID, text=api_cln[0][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                           relief="groove",
                           padx="2", pady="2")
                ID.grid(row=rows, column=0, sticky=N + S + E + W)

                STATES = Label(COVID, text=api_cln[0][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                               relief="groove", padx="2", pady="2")
                STATES.grid(row=rows, column=1, sticky=N + S + E + W)

                CASES = Label(COVID, text=api_cln[0][2], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2,
                              relief="groove", padx="2", pady="2")
                CASES.grid(row=rows, column=2, sticky=N + S + E + W)

                RECOVERED = Label(COVID, text=api_cln[0][3], bg="#F3F4F6", fg="black", font="Lato 12",
                                  borderwidth=2,
                                  relief="groove", padx="2", pady="2")
                RECOVERED.grid(row=rows, column=3, sticky=N + S + E + W)

                DEATHS = Label(COVID, text=api_cln[0][4], bg="#F3F4F6", fg="black", font="Lato 12",
                               borderwidth=2,
                               relief="groove", padx="2", pady="2")
                DEATHS.grid(row=rows, column=4, sticky=N + S + E + W)
                count += 1
                rows += 1
            else:
                break
        else:
            break

    api = ""
    i += 9
    refresh = Button(COVID, text="Refresh", bg="#142E54", fg="white", command=lambda: reset(1), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2")
    refresh.grid(row=rows + 1, column=2, sticky=N + S + E + W)
    if i >= 35:
        next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                      borderwidth=2,
                      relief="groove", padx="2", pady="2", state=DISABLED)
        next.grid(row=rows + 1, column=4, sticky=N + S + E + W)

    else:
        next = Button(COVID, text="NEXT", bg="#142E54", fg="white", command=lambda: nxt(i), font="Lato 12",
                      borderwidth=2,
                      relief="groove", padx="2", pady="2")
        next.grid(row=rows + 1, column=4, sticky=N + S + E + W)
    if i <= 10:
        pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2", state=DISABLED)
        pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)
    else:
        pre = Button(COVID, text="PREVIOUS", bg="#142E54", fg="white", command=lambda: prev(i), font="Lato 12",
                     borderwidth=2,
                     relief="groove", padx="2", pady="2")
        pre.grid(row=rows + 1, column=0, sticky=N + S + E + W)


def app_header():
    ID = Label(COVID, text="ID", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2,
               relief="groove")
    ID.grid(row=0, column=0, sticky=N + S + E + W)

    STATES = Label(COVID, text="STATES", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                   borderwidth=2, relief="groove")
    STATES.grid(row=0, column=1, sticky=N + S + E + W)

    CASES = Label(COVID, text="CASES", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2,
                  relief="groove")
    CASES.grid(row=0, column=2, sticky=N + S + E + W)

    RECOVERED = Label(COVID, text="RECOVERED", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                      borderwidth=2, relief="groove")
    RECOVERED.grid(row=0, column=3, sticky=N + S + E + W)

    DEATHS = Label(COVID, text="DEATHS", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                   borderwidth=2, relief="groove")
    DEATHS.grid(row=0, column=4, sticky=N + S + E + W)


app_nav()
app_header()
my_portfolio()
COVID.mainloop()

cursorObj.close()
con.close()
