import time
import picamera
import cv2

titulo = 'Ventana 1'
ruta = 'pines.png'

imagen = cv2.imread(ruta,1)
cv2.namedWindow(titulo,cv2.WINDOW_NORMAL)

with picamera.PiCamera() as picam:
    picam.start_preview()
    cv2.imshow(titulo,imagen)

    
    while(True):
        if (cv2.waitKey(1) == ord(' ')):
            picam.stop_preview()
            break


cv2.destroyAllWindows()