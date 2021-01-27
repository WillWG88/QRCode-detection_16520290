import cv2  # library opencv
import numpy as np 
from pyzbar.pyzbar import decode # library python untuk menscan QR code

image=cv2.imread('kartustudimahasiswa.png') 

for code in decode(image):
    print(code.data)
    print(code.type)
    info=code.data.decode('utf-8')
    print('data di dalam qr code : ' + info)
    
