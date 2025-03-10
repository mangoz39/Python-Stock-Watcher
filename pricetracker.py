import requests
import time
import sqlite3
from bs4 import BeautifulSoup


def get_details(stock):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/102.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    changes = soup.findAll('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'})
    change_price = changes[0].find('span').text
    change_quote = changes[1].find('span').text
    return float(price.text), change_price, change_quote


def get_price(stock):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/102.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    return float(price.text)


def search_price(lis):
    res = []
    for i in range(len(lis)):
        p, cp, cq = get_details(lis[i])
        res.append(str(p))
        res.append(str(cp))
        res.append(str(cq))

    return res


def total_val(lisa: list, lisb: list):
    res = []
    for i in range(len(lisa)):
        p = get_price(lisa[i])
        res.append(float(p) * float(lisb[i]))

    return res


def get_gap(stock):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                               AppleWebKit/537.36 (KHTML, like Gecko) \
                               Chrome/102.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    changes = soup.findAll('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'})
    change_price = changes[0].find('span').text
    return change_price


def search_gap(lis: list, lisa: list):
    res = []
    for i in range(len(lis)):
        cp = get_gap(lis[i])
        res.append(float(cp) * float(lisa[i]))

    return res


def getdate():
    return time.strftime("%a, %Y-%m-%d  %H:%M:%S", time.localtime())


def get_time():
    return time.strftime("%H:%M:%S", time.localtime())


def sell(stock: str, price, qty):
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    pz = str(cur.execute(f"select avgPrice from Position WHERE IX = '{stock}'").fetchone())
    pz = pz.replace('(', '')
    pz = pz.replace(',', '')
    pz = pz.replace('\'', '')
    pz = pz.replace(')', '')
    pz = float(pz)
    qt = str(cur.execute(f"select amount from Position WHERE IX = '{stock}'").fetchone())
    qt = qt.replace('(', '')
    qt = qt.replace(',', '')
    qt = qt.replace('\'', '')
    qt = qt.replace(')', '')
    qt = float(qt)
    cur.execute(f"update Position SET amount = {qt - qty}, avgPrice = {pz - (qty * price)} WHERE IX = '{stock}';")
    conn.commit()
    conn.close()
    return


def ord(stock: str, price: float, qty: float):
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    pz = str(cur.execute(f"select avgPrice from Position WHERE IX = '{stock}'").fetchone())
    if pz == "None":
        cur.execute(f"Insert into Position Values('{stock}', {qty}, {price * qty})")
        conn.commit()
        conn.close()
        return
    pz = pz.replace('(', '')
    pz = pz.replace(',', '')
    pz = pz.replace('\'', '')
    pz = pz.replace(')', '')
    pz = float(pz)
    qt = str(cur.execute(f"select amount from Position WHERE IX = '{stock}'").fetchone())
    qt = qt.replace('(', '')
    qt = qt.replace(',', '')
    qt = qt.replace('\'', '')
    qt = qt.replace(')', '')
    qt = float(qt)
    cur.execute(f"update Position SET amount = {qt + qty}, avgPrice = {pz + (qty * price)} WHERE IX = '{stock}';")
    conn.commit()
    conn.close()
    return


def ser(stock):
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    qt = str(cur.execute(f"select amount from Position WHERE IX = '{stock}'").fetchone())
    qt = qt.replace('(', '')
    qt = qt.replace(',', '')
    qt = qt.replace('\'', '')
    qt = qt.replace(')', '')
    return qt


def get_ticker():
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    sr = cur.execute("select Ticker from WatchList").fetchall()
    res = []
    for i in sr:
        a = str(i)
        a = a.replace(',', '')
        a = a.replace('(', '')
        a = a.replace(')', '')
        res.append(a)
    conn.commit()
    conn.close()
    return res


def get_pos_ticker():
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    sr = cur.execute("select IX from Position").fetchall()
    resp = []
    for i in sr:
        a = str(i)
        a = a.replace(',', '')
        a = a.replace('(', '')
        a = a.replace(')', '')
        resp.append(a)
    conn.commit()
    conn.close()
    return resp


def changetik(old, new):
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    cur.execute(f"update WatchList Set Ticker = '{new}' WHERE Ticker = '{old}';")
    conn.commit()
    conn.close()


def get_pos_qty():
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    sr = cur.execute("select amount from Position").fetchall()
    resa = []
    for i in sr:
        a = str(i)
        a = a.replace(',', '')
        a = a.replace('(', '')
        a = a.replace(')', '')
        resa.append(float(a))
    conn.commit()
    conn.close()
    return resa


def get_pos_price():
    conn = sqlite3.connect('midterm.db')
    cur = conn.cursor()
    sr = cur.execute("select avgPrice from Position").fetchall()
    resb = []
    for i in sr:
        a = str(i)
        a = a.replace(',', '')
        a = a.replace('(', '')
        a = a.replace(')', '')
        resb.append(float(a))
    conn.commit()
    conn.close()
    return resb

"""
aapl = yf.download('AAPL', period='1d', interval='1d')

# print(type(aapl), '\n')
# print(str(aapl).split(' '))
# print(aapl)
all = []
for x in aapl.iloc(0):
    temp = {}
    for k, v in x.items():
        temp[k] = v
    all.append(temp)
print(all)
"""
