# PUNYA KELOMPOK 5
# 32180050 - RIVALTINO ARRON
# 32180051 - ANDREANTO S.L.
# 32180079 - RANDINESIA
# 32180137 - STEVEN

import cv2

def main():
    # training data untuk menentukan mata
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    '''
    # baca image
    img = cv2.imread('4.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''

    cap = cv2.VideoCapture(0)

    while 1:
        # mencari muka
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        '''
        eyes = []
        '''

        # mencari mata dalam muka
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        '''
        # Segmented Image of Eyes
        if eyes == []:
            imgError = cv2.imread('ERROR_IMG.jpg')
            cv2.imshow('ERROR', imgError)

            print('BISA JADI ORIENTASI GAMBAR KURANG BAGUS, JADI MATA TIDAK TERDETEKSI')
        else:
            cv2.imshow('img', img)
            # Show Segmented Object
            for x in range(eyes.shape[0]):
                a = roi_gray[eyes[x][1]:eyes[x][1] + eyes[x][3], eyes[x][0]:eyes[x][0] + eyes[x][2]]
                cv2.imshow('eye ' + str(x) , a)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()