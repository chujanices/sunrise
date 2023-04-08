import os
import cv2

path = "Images"
images = []

#201-110 -- sunrise
#110-201 -- sunset

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape  
size = (width, height)                  # <--- tupil 
print(size)
out = cv2.VideoWriter("sunrise.mp4", cv2.VideoWriter.fourcc(*'DIVX'), 30, size)

for i in range (count-1, 0, -1): # i is all images
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("it's done!!")

out.destroyAllWindows()