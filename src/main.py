import cv2
import os
import traceback
import time


class SerchPharmaceuticals:
    def __init__(self):
        self.image_dir = os.path.join(
            os.path.dirname(
                __name__
            ),
            '..',
            'images'
        )
        self.winname = 'serch pharmaceuticals'
        self.init_time = None
        self.push_time = None
    
    def mouse_cb(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.push_time = time.time()
    
    def show_selector(self):
        try:
            img_src = os.path.join(
                self.image_dir,
                '01.jpg'
            )
            img = cv2.imread(img_src)

            self.init_time = time.time()
            self.push_time = False
            while not self.push_time:
                cv2.imshow(self.winname, img)
                cv2.setMouseCallback(self.winname, self.mouse_cb)
                cv2.waitKey(1)
            
            interval = self.push_time - self.init_time
            interval = f"{int(interval // 60):02}:{int(interval % 60):02}:{int((interval % 1) * 1000):02}"

        except cv2.error as e:
            traceback.print_exc()
            #raise FileNotFoundError(f'Not found file: {os.path.abspath(img_src)}')
    
    def devel_mouse_cb(self, event, x, y, flags, param):
        if self.fp is None or self.ep is None:
            self.img_c = self.img.copy()
        if self.fp and self.ep is None:
            cv2.rectangle(self.img_c, self.fp, (x,y), (0, 255, 0), 2)
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.fp is None:
                self.fp = (x, y)
                print(self.fp)
            else:
                self.ep = (x, y)
                print(self.ep)
                cv2.rectangle(self.img_c, self.fp, self.ep, (0, 255, 0), 2)
    
    def devel_selector(self):
        try:
            img_src = os.path.join(
                self.image_dir,
                '01.jpg'
            )
            self.img = cv2.imread(img_src)
            self.img_c = self.img.copy()

            self.fp = None
            self.ep = None
            while not self.push_time:
                cv2.imshow(self.winname, self.img_c)
                cv2.setMouseCallback(self.winname, self.devel_mouse_cb)
                cv2.waitKey(1)

        except cv2.error as e:
            traceback.print_exc()

def main():
    serch_pharmaceuticals = SerchPharmaceuticals()
    #serch_pharmaceuticals.show_selector()
    serch_pharmaceuticals.devel_selector()

if __name__ == "__main__":
    main()