
import sys
import cv2
import numpy as np

error_msg1 = "python image_resize.py --input_file=image.jpg -w=256 -h=256"

def tidl_image_resize(input_file, w, h, output_file):

    img = cv2.imread(input_file)

    resize_img = cv2.resize(img, (w, h), 0, 0, cv2.INTER_AREA);

    cv2.imwrite(output_file, resize_img)

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if(len(args) < 3):
        print("Example Usage:")
        print(error_msg1)

    else:
        output_file = ""
        input_file = ""
    
        for arg in args:
            opt, value = arg.split("=")
        
            if(opt == "--input_file"):
                input_file = value
            if(opt == "-w"):
                w = int(value,10)
            if(opt == "-h"):
                h = int(value,10)
            if(opt == "--output_file"):
                output_file = value
    
        if output_file == "":
            name, ext = input_file.split(".")
            output_file = name + "_" + str(w) + "x" + str(h) + ".png"

        print("Resizing image " + input_file)
        tidl_image_resize(input_file, w, h, output_file)
        print("Done!")
        
