from threading import Thread
import cv2

class WebcamStream:

    def __init__(self):
        # initialize the video camera stream and read the first frame
        # from the stream
        print("init")
        # self.stream = cv2.VideoCapture('https://192.168.137.166:8080/video')
        #self.stream = cv2.VideoCapture('https://10.100.20.230:8080/video')
        #self.stream = cv2.VideoCapture('https://192.168.1.105:8080/video')
        # self.stream = cv2.VideoCapture('https://192.168.1.101:8080/video')
        # self.stream = cv2.VideoCapture('https://192.168.1.68:8080/video')
        # self.stream = cv2.VideoCapture('https://10.100.30.246:8080/video')
        # self.stream = cv2.VideoCapture('https://10.100.30.128:8080/video')
        # self.stream = cv2.VideoCapture('https://10.100.31.86:8080/video')
        self.stream = cv2.VideoCapture('https://10.100.31.86:8080/video')



        (self.grabbed, self.frame) = self.stream.read()


        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        print("start thread")
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        print("read")
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return  #just return
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True