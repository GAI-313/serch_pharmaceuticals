# -*- coding: utf-8 -*-
import cv2
import os
import traceback
import time

import random

from load_yaml import LoadYaml

import tkinter as tk
from tkinter import messagebox

RATE = 2        # 選択回数
VAL_MIN = 1     # 開始番号
VAL_MAX = 13    # 終了番号


class PopUp:
    def __init__(self, text):
        self.root = tk.Tk()

        window_width = 300
        window_height = 100

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = int((screen_width - window_width) / 2)
        position_y = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        button = tk.Button(self.root, text=text, command=self.quit)
        button.pack()

        self.root.mainloop()

    def quit(self):
        self.root.destroy()


class SerchPharmaceuticals():
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
            if x >= self.target_area[0][0] and x <= self.target_area[1][0] and y >= self.target_area[0][1] and y <= self.target_area[1][1]:
                self.push_time = time.time()
            else:
                print(f"Clicked different pose: {[x, y]}")
    
    def show_selector(self, image: str, data_info: dict, target: str):
        try:
            img_src = os.path.join(
                self.image_dir,
                f'{image}.jpg'
            )
            img = cv2.imread(img_src)

            self.init_time = time.time()
            self.push_time = False
            self.target_area = data_info[target]
            #print(self.target_area)
            print(f"target name: {target}")
            popup = PopUp(target)
            while not self.push_time:
                cv2.imshow(self.winname, img)
                cv2.setMouseCallback(self.winname, self.mouse_cb)
                cv2.waitKey(1)
            
            interval = self.push_time - self.init_time
            interval = f"{int(interval // 60):02}:{int(interval % 60):02}:{int((interval % 1) * 1000):02}"

            print(f"clicked interval: {interval}")
            cv2.destroyAllWindows()
            return interval

        except cv2.error as e:
            traceback.print_exc()
    
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
    
    def devel_selector(self, image: str):
        try:
            img_src = os.path.join(
                self.image_dir,
                f'{image}.jpg'
            )
            self.img = cv2.imread(img_src)
            self.img_c = self.img.copy()

            self.fp = None
            self.ep = None
            while not self.push_time:
                cv2.imshow(self.winname, self.img_c)
                cv2.setMouseCallback(self.winname, self.devel_mouse_cb)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    print("----------")
                    self.fp = None

        except cv2.error as e:
            traceback.print_exc()

def devel():
    serch_pharmaceuticals = SerchPharmaceuticals()
    serch_pharmaceuticals.devel_selector("image_14")

def main():
    try:
        serch_pharmaceuticals = SerchPharmaceuticals()
        load_yaml = LoadYaml()
        data_info = load_yaml.data

        j = VAL_MIN
        c = 1

        for image_info in data_info:
            if VAL_MAX < j:
                break
            selected_target = []
            print("Page Update")

            if c == j:
                for i in range(RATE):
                    target_list = data_info[image_info]
                    target = random.choice(list([item for item in target_list if item not in selected_target]))
                    selected_target.append(target)
                    
                    serch_pharmaceuticals.show_selector(image_info,
                                                        data_info[image_info],
                                                        target
                                                        )
                    i += 1
                j += 1
            c += 1
    except KeyboardInterrupt:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    #devel()