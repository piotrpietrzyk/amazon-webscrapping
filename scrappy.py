import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/dp/B07LGCK683/' \
      'ref=sr_1_2?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=tecnica+zero+g&qid=1578862266&sr=8-2'

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()
    converted_price = int(price[0:3])
    print(converted_price)

    if converted_price < 700:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('youremail@gmail.com', 'password')

    subject = 'price fell down'
    body = f'check the amazon link: {URL}'
    msg = f"Subject: {subject, body}"

    server.sendmail('email@email.com', msg)

    print('email has been send')

    server.quit()


check_price()

