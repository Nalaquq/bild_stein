import numpy as np
import cv2
import os


home = os.getcwd()
db = "/home/nalkuq/bild_stein/db"
resized = "/home/nalkuq/bild_stein/resized"


def makedir():
    try:
        temp = "resized"
        os.mkdir(temp)
        print(f"a new directory named {temp} has been created.")
    except:
        print(f"your files will be saved in {temp}.")


def resize():
    makedir()
    db = "/home/nalkuq/bild_stein/db"
    resized = "/home/nalkuq/bild_stein/resized"
    os.chdir(db)
    for img in os.listdir(db):
        # removes spaces in file names since that gives opencv problems
        r = img.replace(" ", "")
        if r != img:
            os.rename(img, r)
        try:
            temp = cv2.imread(img)
            assert (
                img is not None
            ), "file could not be read, check with os.path.exists()"
            res = cv2.resize(temp, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
            os.chdir(resized)
            cv2.imwrite(str(img), res)
            print(img + f"has been resized in {resized}")
            os.chdir(db)
        except:
            print(f"{img}could not be resized")


resize()


