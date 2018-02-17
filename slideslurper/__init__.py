import os, errno, sys
from shutil import rmtree

import cv2
import numpy as np
from tqdm import tqdm
from fpdf import FPDF
# can probably get rid of this, but no time so far
from PIL import Image

def makePdf(pdfFileName, listPages, dir):
    # make a pdf from the slides
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(pdfFileName + ".pdf", "F")


def setUp(directory):
    """create the .frames folder"""
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def cleanUp(directory):
    """deletes all files saved in the frames folder"""
    if os.path.isdir(directory):
        rmtree(directory)
    else:
        print("error -> temporary %s was not found" % directory)

# helper functions
def mse(image1, image2):
    """index of difference betweeen two frames"""
    return np.linalg.norm(image1 - image2)

def toGrayscale(arr):
    """remove color from an image"""
    if len(arr.shape) == 3:
        return np.average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def getUniqueFrames(videoPath, directory):
    """goes over the video, saves different frames and puts them in the frame folder"""
    videoStream = cv2.VideoCapture(videoPath)
    frameCount = int(videoStream.get(cv2.CAP_PROP_FRAME_COUNT))

    imageList = []

    success1, image1 = videoStream.read()
    grayImage1 = toGrayscale(image1)

    # cv2.imwrite("short-frames/frame%d.jpg" % 1, image1)
    # imageList.append("frame1")

    success = True
    slide = 0
    progressBar = tqdm(total=frameCount, desc="parsing video (%d frames)" % frameCount, unit="frames")

    while success:
        success2, image2 = videoStream.read()
        success = success1 & success2

        if success:
            grayImage2 = toGrayscale(image2)
            error = mse(grayImage1, grayImage2)

            threshold = 3000
            if error >= threshold:
                cv2.imwrite("%s/slide%d.jpg" % (directory ,(slide + 1)), image2)
                imageList.append("slide%d" % (slide+1))
                slide += 1

        image1, grayImage1 = (image2, grayImage2)
        progressBar.update(1)

    progressBar.close()
    return imageList

def validArgs(argc, argv):
    """check that we have two arguments, and that the video one points to a valid video file"""
    if argc != 3:
        print("usage: slurp <lecture_video.mp4> <name_for_output_pdf>")
        print("e.g python slide_slurper.py lecture.mp4 lecture-out #=> will output a pdf called lecture-out.pdf")
        return False

    if not os.path.isfile(argv[1]):
        print("video file not found. make sure you include the extension (eg .mp4)")
        return False

    return True

def main():
    if not validArgs(len(sys.argv), sys.argv):
        sys.exit()

    videoFilePath, outputPdfName = (sys.argv[1], sys.argv[2])

    # hardcoded configuration
    tmpDir = ".frames"

    setUp(tmpDir)
    imageList = getUniqueFrames(videoFilePath, tmpDir)

    print("building pdf...")
    makePdf(outputPdfName, imageList, tmpDir)

    print("cleaning up...")
    cleanUp(tmpDir)

    print("done! %d slides slurped and assembled in %s.pdf" % (len(imageList), outputPdfName))

if __name__ == '__main__':
    main()
