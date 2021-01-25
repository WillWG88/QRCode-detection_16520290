import cv2  # library opencv
import numpy as np 
from pyzbar.pyzbar import decode # library python untuk menscan QR code

gambar=cv2.imread('kartustudimahasiswa.png') 

for barcode in decode(gambar):
    print(barcode.data)
    print(barcode.type)
    info=barcode.data.decode('utf-8')
    print('data di dalam qr code : ' + info)
    
