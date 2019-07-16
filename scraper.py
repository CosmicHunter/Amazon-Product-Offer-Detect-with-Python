import requests    # what this does is we can access some URL and pull some information
from bs4 import BeautifulSoup
import smtplib
import  time  # to run the script again and again

URL = 'https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_1_sspa?keywords=iphone+xR&qid=1562761357&s=gateway&sr=8-1-spons&psc=1'
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

# headers basically gives us some information about our browser so we have header as
# a dictionary
# Now we will make requests to the page
def chkPrice():
        page = requests.get(URL,headers = header)


        # this basically gets all the data from the website
        # Now what Beautiful Soup does for us is we can parse the data and pull out
        # individual data from it
        # Now we will create another variable calles soup and pass contents of the
        # page to BeautifulSoup()


        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id="productTitle").get_text()
        # this is how productTitle is spelled on the source of amazon webpage
        # data has a lot of white spaces so we can remove them
        print(title.strip())  # .strip to remove white spaces

        # Now what we are interested is in price

        price = soup.find(id="priceblock_ourprice").get_text()

        # note that the id mentioned should be as it is as it is on the webpage
        # source code

        converted_price = price[2:8]
        print(converted_price)

        # as we can see there is a comma so we need to remove it
        priceNumber = float(converted_price.replace(',', ''))

        # c = converted_price[0:2]
        # d = converted_price[3:6]
        # converted_price = c+d


        if priceNumber < 55000 :
            send_mail()


# Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending
# e-mail and routing e-mail between mail servers.
# Python provides smtplib module, which defines an SMTP client session
# object that can be used to send mail to any Internet machine with an
# SMTP or ESMTP listener daemon


def send_mail():
    server =    smtplib.SMTP('smtp.gmail.com',587) #587 is the connection number
    server.ehlo()

    # ehlo-Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol
    # (ESMTP) command sent by an email server to identify itself when
    # connecting to another email server to start the process of sending an
    # email. It is followed with the sending email server's domain name.
    # The EHLO command tells the receiving server it supports extensions
    #compatible with ESMTP.


    server.starttls()   # this basically encrypts our connection
    server.ehlo()
    server.login('manavvallecha311998@gmail.com','dzbhdallolmuyczh')

    subject = 'Hey, The Price of your requested product fell down'
    body = 'Check the amazon link : https://www.amazon.in/Apple-iPhone-XR-128GB-Coral/dp/B07JHQCYWR?tag=googinkenshoo-21&ascsubtag=_k_CjwKCAjwx_boBRA9EiwA4kIELjxNQyAsTbZBpYRKFrYvz0UgQEaaBu848BvMnKIm29Leipm27y5etxoCNgcQAvD_BwE_k_&gclid=CjwKCAjwx_boBRA9EiwA4kIELjxNQyAsTbZBpYRKFrYvz0UgQEaaBu848BvMnKIm29Leipm27y5etxoCNgcQAvD_BwE&th=1'
    mail = f'Subject:{subject}\n\n{body}'


    server.sendmail('manavvallecha311998@gmail.com','manav31vallecha@gmail.com',mail)

    print('Email Sent')

    server.quit() # to close the connection

while True:
   chkPrice()
   time.sleep(86400)   # to  run the script once every day
