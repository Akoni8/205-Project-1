"""
Project 1
Akoni Morrison
9/7/2016
"""
from PIL import Image
from statistics import median
print("Hello")
#Opening and loading pictures
pic1=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/1.png")
pic1.load()
pic2=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/2.png")
pic2.load()
pic3=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/3.png")
pic3.load()
pic4=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/4.png")
pic4.load()
pic5=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/5.png")
pic5.load()
pic6=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/6.png")
pic6.load()
pic7=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/7.png")
pic7.load()
pic8=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/8.png")
pic8.load()
pic9=Image.open("C:/Users/akoni/Desktop/Akoni's school/CST 205/Project 1 Images/9.png")
pic9.load()

#Picture width/height
pictureWidth=495
pictureHeight=557
theImages=[pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9]
new_image=Image.new("RGB",(pictureWidth,pictureHeight))
new_imagePixelAccess=new_image.load()
for x in range(0, pictureWidth):
    for y in range(0, pictureHeight):
        redPixelList=[]
        greenPixelList=[]
        bluePixelList=[]
        for myImage in theImages:
            
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)  
        medianRed=int(median(redPixelList))
        medianGreen=int(median(greenPixelList))
        medianBlue=int(median(bluePixelList))
    
        new_imagePixelAccess[x,y]= (medianRed,medianGreen,medianBlue)

new_image.show()
# Do our median calculations
# Clear our red, green, blue value lists
# Put the red, green blue values for the pixel for the output image
