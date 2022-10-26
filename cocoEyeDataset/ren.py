import os 
import cv2
arr = os.listdir("images/")
for aa in arr:
    # print(aa)
    brr = os.listdir("images/"+aa)
    for bb in brr:
        # print(bb)
        img = cv2.imread("images/"+aa+'/'+bb)
        ress = cv2.resize(img,(160,160))
        cv2.imwrite("images/"+aa+'/'+bb,ress)