import cv2
import time
import random
import dropbox
start_time=time.time()
def time_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print('snapshot taken!')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.At94xeRil_hdoNYgPMXTI9VsamC6stKyyGSLPkzzx2Td5c9NpVy2bgzkUl-W5n3tNpqY3V36-P-zxPh6y6DM-uRp9fwq5obXcb80d4J2vOds6tFgVwftxPgtu5PZqAYtYeswCNE'
    file = img_name
    file_from=file
    file_to='/newfolder1/'+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=time_snapshot()
            upload_file(name)

main()

