import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np
import sqlite3
import webbrowser
conn=sqlite3.connect('database.sqlite')
cur=conn.cursor()

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
abc=1
while abc>0:
    sucess,img=cap.read()
    for barcode in pyzbar.decode(img):
        mydata=barcode.data.decode()

        cur.execute('''Select LINK from PRODUCT where Code=?''',(mydata,) )
        n=cur.fetchone()
        if n==None:
            print("not Found")

        else:
            link=product


    cv2.imshow("Result:",img)
    key=cv2.waitKey(1)
    ab=abc-1
