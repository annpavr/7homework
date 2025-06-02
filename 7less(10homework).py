import requests
import sqlite3
import time
import datetime

def make_db():
    con = sqlite3.connect("weath.db")
    con.execute("DROP TABLE IF EXISTS weather")
    con.execute("CREATE TABLE weather (d TEXT, t TEXT, temp TEXT)")
    con.commit()
    con.close()

def get_temp():
    try:
        r = requests.get("https://wttr.in/Cherkasy?format=%t", timeout=11)
        if r.status_code == 200:
            return r.text.strip()
    except:
        return None

def save(d, t, temp):
    con = sqlite3.connect("weath.db")
    con.execute("INSERT INTO weather (d, t, temp) VALUES (?, ?, ?)", (d, t, temp))
    con.commit()
    con.close()

def main():
    make_db()
    while True:
        n = datetime.datetime.now()
        d = n.strftime("%Y-%m-%d")
        t = n.strftime("%H:%M")
        temp = get_temp()

        if temp:
            save(d, t, temp)
            print("Дата:", d)
            print("Час:", t)
            print("Темп:", temp)
        else:
            print("Помилка")

        print("Оновлення через: 30 хв")
        time.sleep(1800)
main()
