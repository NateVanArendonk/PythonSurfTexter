'''See the below template for the correct format for contacting your phone via email
Please Note This template is taken from reference below, not created by NV
*****************************************************************
Alltel	                        [10-digit phone number]@message.alltel.com
                Example: 1234567890@message.alltel.com
AT&T (formerly Cingular)        [10-digit phone number]@txt.att.net
                                [10-digit phone number]@mms.att.net (MMS)
                                [10-digit phone number]@cingularme.com
                Example: 1234567890@txt.att.net
Boost Mobile	                [10-digit phone number]@myboostmobile.com
                Example: 1234567890@myboostmobile.com
Nextel (now Sprint Nextel)	[10-digit telephone number]@messaging.nextel.com
                Example: 1234567890@messaging.nextel.com
Sprint PCS (now Sprint Nextel)	[10-digit phone number]@messaging.sprintpcs.com
                                [10-digit phone number]@pm.sprint.com (MMS)
                Example: 1234567890@messaging.sprintpcs.com
T-Mobile	                [10-digit phone number]@tmomail.net
                Example: 1234567890@tmomail.net
US Cellular	                [10-digit phone number]@email.uscc.net (SMS)
                                [10-digit phone number]@mms.uscc.net (MMS)
                Example: 1234567890@email.uscc.net
Verizon	                        [10-digit phone number]@vtext.com
                                [10-digit phone number]@vzwpix.com (MMS)
                Example: 1234567890@vtext.com
Virgin Mobile USA	        [10-digit phone number]@vmobl.com
                Example: 1234567890@vmobl.com
*****************************************************************'''

#References: https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# https://www.reddit.com/r/Python/comments/186fr0/use_python_to_send_a_text_message/


import smtplib


# set username equal to your email address
username = 'nate.vanaren@gmail.com'
# set the name of the email to text from
email = 'nate.vanaren@gmail.com'
# set the cell number from the above info to your cell phone
cell = cell #
# set the password for the email
password = # pw is first name and hs bb #

def sendWeatherText(morningStatement):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)

        server.sendmail(email, cell, morningStatement)
        print("Email successfully sent")
        server.quit()

    except:
        print("Error: mail not sent")


def sendSurfText(surfStatement):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)

        server.sendmail(email, cell, surfStatement)
        print("Surf statement successfully sent")
        server.quit()

    except:
        print("Error: mail not sent")
