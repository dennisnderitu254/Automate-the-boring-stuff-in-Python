#! python3

# Chapter 16 Practice Random Chore Assignment Emailer
# Randomly assigns a list of chores to a list of email addresses
# and emails the chore assignment to the corresponding email address.

import random
import smtplib


def emailChores(rchore, remail):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('myemail@address.com', 'mySecretPassword')
    body = 'Subject: Your Chore\n\nYour weekly assigned chore is: %s' % rchore
    print('Sending chore email to ' + remail + '...')
    smtpObj.sendmail('myemail@address.com', remail, body)
    smtpObj.quit()

chores = ['dishes', 'bathroom', 'vaccum', 'trash']
emails = ['someone@emailaddress.com', 'someone@emailaddress.com'\
          'someone@emailaddress.com', 'someone@emailaddress.com']

for i in range(0, len(emails)):
    randomChore = random.choice(chores)
    emailChores(randomChore, emails[i])
    chores.remove(randomChore)
