# # import time
# #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.select import Select
# #
# # driver=webdriver.Chrome()
# # driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=14833530754385053164&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20462&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=Cj0KCQjwk7ugBhDIARIsAGuvgPbeQd6RTim8jkleex-XjW7lp8EAmY4r6ZfqjbtcvdrXe6HRDFzmbYYaAuVoEALw_wcB")
# #
# # links= driver.find_element(By.TAG_NAME,'a')
# # print(links.text)
# # # print(len(links))
# # # # print(len(dropdn.options))
# # # for link in links:
# #     print(link.text)
# from _cffi_backend import string
#
# # alist=[1,2,3,4,5,6,7,8,9,10]
# #
# # num=int(input('Enter the number'))
# # count=0
# #
# # for element in alist:
# #     if element==num:
# #
# #
# #         print()
# str='https://www.google.com/maps/place/Vishwakarma+Institute+of+Technology/@18.4636219,73.866015,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2ea950f616219:0x321bdae2cea9f064!8m2!3d18.4636219!4d73.8682037!16zL20vMDU5MjU0'
# #
# # # new_str=list(str)
# #
# # for element in range(72,92):
# #     print()


# # class Homepage:
# #
# #     def getdata(self):
# #         a='123'
# #
# #
# #
# #
# # class Page(Homepage):
#
# #get the index of given number
# # items=[1,2,3,4,5,6,7,8,9,10]
# # a=int(input('Enter the num'))
# #
# # for index in range(len(items)+1):
# #     if index==a:
# #         print(f'Index of {a} is :{index-1}')
#
# #get altitude and latitude from the string
#
# strg='https://www.google.com/maps/place/Vishwakarma+Institute+of+Technology/@18.4636219,73.866015,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2ea950f616219:0x321bdae2cea9f064!8m2!3d18.4636219!4d73.8682037!16zL20vMDU5MjU0'
#
# new_str=strg.split('/')
# # altitude=new_str[6]
# # print(altitude)
# # print(f'Altitude is: {altitude[1:10]}')
# # print(f'Latitude is:{altitude[12:21]}')
#
# print(new_str)
# # print(new_str[5])
# clg=new_str[5]
# clgname=clg.split('+')
# print(clgname)
# print(clgname)



import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import cv2
import uuid
import os
from model import U2NET
from torch.autograd import Variable
from skimage import io, transform
from PIL import Image
# Get The Current Directory
currentDir = os.path.dirname(__file__)
# Functions:
# Save Results
def save_output(image_name, output_name, pred, d_dir, type):
    predict = pred
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy()
    im = Image.fromarray(predict_np*255).convert('RGB')
    image = io.imread(image_name)
    imo = im.resize((image.shape[1], image.shape[0]))
    pb_np = np.array(imo)
    if type == 'image':
        # Make and apply mask
        mask = pb_np[:, :, 0]
        mask = np.expand_dims(mask, axis=2)
        imo = np.concatenate((image, mask), axis=2)
        imo = Image.fromarray(imo, 'RGBA')
    imo.save(d_dir+output_name)
# Remove Background From Image (Generate Mask, and Final Results)
def removeBg(imagePath):
    inputs_dir = os.path.join(currentDir, 'static/inputs/')
    results_dir = os.path.join(currentDir, 'static/results/')
    masks_dir = os.path.join(currentDir, 'static/masks/')
    # convert string of image data to uint8
    with open(imagePath, "rb") as image:
        f = image.read()
        img = bytearray(f)
    nparr = np.frombuffer(img, np.uint8)
    if len(nparr) == 0:
        return '---Empty image---'
    # decode image
    try:
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except:
        # build a response dict to send back to client
        return "---Empty image---"
    # save image to inputs
    unique_filename = str(uuid.uuid4())
    cv2.imwrite(inputs_dir+unique_filename+'.jpg', img)
    # processing
    image = transform.resize(img, (320, 320), mode='constant')
    tmpImg = np.zeros((image.shape[0], image.shape[1], 3))
    tmpImg[:, :, 0] = (image[:, :, 0]-0.485)/0.229
    tmpImg[:, :, 1] = (image[:, :, 1]-0.456)/0.224
    tmpImg[:, :, 2] = (image[:, :, 2]-0.406)/0.225
    tmpImg = tmpImg.transpose((2, 0, 1))
    tmpImg = np.expand_dims(tmpImg, 0)
    image = torch.from_numpy(tmpImg)
    image = image.type(torch.FloatTensor)
    image = Variable(image)
    d1, d2, d3, d4, d5, d6, d7 = net(image)
    pred = d1[:, 0, :, :]
    ma = torch.max(pred)
    mi = torch.min(pred)
    dn = (pred-mi)/(ma-mi)
    pred = dn
    save_output(inputs_dir+unique_filename+'.jpg', unique_filename +
                '.png', pred, results_dir, 'image')
    save_output(inputs_dir+unique_filename+'.jpg', unique_filename +
                '.png', pred, masks_dir, 'mask')
    return "---Success---"
# ------- Load Trained Model --------
print("---Loading Model---")
model_name = 'u2net'
model_dir = os.path.join(currentDir, 'saved_models',
                         model_name, model_name + '.pth')
net = U2NET(3, 1)
if torch.cuda.is_available():
    net.load_state_dict(torch.load(model_dir))
    net.cuda()
else:
    net.load_state_dict(torch.load(model_dir, map_location='cpu'))
# ------- Load Trained Model --------
print("---Removing Background...")
# ------- Call The removeBg Function --------
imgPath = "Image_File_Path"  # Change this to your image path
print(removeBg(imgPath))
#end