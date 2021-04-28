#library that allows you to take image from user
import argparse
import cv2
import pandas

showing_image = True
clicked = False

#function that gets the r,g,b balue when clicked
def get_rgb_pixel(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
      
#function that takes rgb values and returns the closest match to the csv file
def get_color_name(r, g, b):
    smallest = 100000
    for row in range(len(csv)):
        r_value_row = int(csv.loc[row, "R"])
        g_value_row = int(csv.loc[row, "G"])
        b_value_row = int(csv.loc[row, "B"])
        diff = abs(r - r_value_row) + abs(g - g_value_row)+ abs(b - b_value_row)  
        if (diff <= smallest):
            smallest = diff
            color_name = csv.loc[row, "color name"]
    return color_name



#get the image in terminal
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument('-i', '--imagepath', required=True, help="path to image")
#arg_parse.add_argument('-csv', '--csvpath', required=True, help="path to csv file for colors")

parser = arg_parse.parse_args()
#csv_path = parser.csvpath
#load the image with opencv
img = cv2.imread(parser.imagepath)



#read the csv file with pandas
csv_color_columns = ["color", "color name", "hex value", "R", "G", "B"]
csv = pandas.read_csv("colors.csv", names=csv_color_columns, header=None)

cv2.namedWindow('img')
cv2.setMouseCallback('img', get_rgb_pixel)

while (showing_image):
    cv2.imshow('img', img)
    if (clicked):
        print("color clicked is " + get_color_name(r,g,b))
        print("R: " + str(r) + " G: " + str(g) + " B: " + str(b))
        clicked = False
    #closes with esc key
    if cv2.waitKey(20) & 0xFF ==27:
        showing_image = False
        
cv2.destroyAllWindows()  
    
