import numpy as np
import cv2
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-src", type=os.path.abspath,help="source directory containing images to be resized")
parser.add_argument("-dst", type=os.path.abspath, help="destination directory to store resized images.")
parser.add_argument("-size", type=int, help="size of scaling factor.")
args=parser.parse_args()


def makedir():
    try:
        temp = args.dst
        os.mkdir(temp)
        print(f"a new directory named {temp} has been created.")
    except:
        print(f"your files will be saved in {temp}.")


def resize():
    makedir()
    db = args.src
    resized = args.dst
    os.chdir(db)
    for img in os.listdir():
        # removes spaces in file names since that gives opencv problems
        r = img.replace(" ", "")
        if r != img:
            os.rename(img, r)
        try:
            temp = cv2.imread(img)
            assert (
                img is not None
            ), "file could not be read, check with os.path.exists()"
            res = cv2.resize(temp, None, fx=args.size, fy=args.size, interpolation=cv2.INTER_CUBIC)
            os.chdir(resized)
            cv2.imwrite(str(img), res)
            print(img + f"has been resized in {resized}")
            os.chdir(db)
        except:
            print(f"{img}could not be resized")


if args.src:
    resize()


