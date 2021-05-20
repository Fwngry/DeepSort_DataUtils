# import argparse
import json
import os
import cv2
import csv
import matplotlib.pyplot as plt
import re
'''
parser = argparse.ArgumentParser(description="build the dataset for classifing")
parser.add_argument("opt", default='build', type=str)
args = parser.parse_args()
opt = args.opt
'''

idx_path = "txt.txt"
output_dir = "dataset"

save_img_dir = os.path.join(output_dir,"img")
save_csv=os.path.join(output_dir,"label.csv")
headers = ['imgpath','label']
# mkdir

def Cropimg_SaveCSV(read_json,read_img,save_img_dir,save_csv,img_num,list_key):
# read_img=""
# img=cv2.imread(read_img)

    with open(read_json, 'r') as json_f:
        data = json.load(json_f)
        # print(data['shapes'])
         
        for idx,shapes in enumerate(data['shapes']):
            # print(save_img)
            # print(idx,shapes['label'],shapes['points'][0][0],shapes['points'][1][0],shapes['points'][0][1],shapes['points'][1][1])
            if shapes['label']=="4545":
                print(read_img)
            label_dict=get_label(read_img,shapes['label'])
            if label_dict not in list_key:
                list_key.append(label_dict)
            img_num+=1
    return img_num
# print(data['shapes'][1]['label'])

def get_label(read_img,label):
    p1 = re.compile(r'[q](.*?)[/]', re.S) #最小匹配
    label_dict=re.findall(p1, read_img)[0] + '_' + label
    return label_dict

def buildDict(list_key):
    Dict={}
    for idx,key_str in enumerate(list_key):
        Dict[key_str]=idx
    return Dict

def main():
    # always using relative path in this .py

    idx_file = open(idx_path)
    img_num=0    
    list_key=[]       
    for line in idx_file: # read txt line by line
        read_json = line.strip() # the json_dir
        read_img = read_json[:read_json.rfind(".")] + ".png" # change surffix (form .json to .png) as the read img path
        # save_img = save_img_dir + "/" + format(i, '08d') +".png" 
        # 原始路径 save_img_str = output_img_dir + line[line.rfind("/"):line.rfind(".")]+".png" 
        img_num=Cropimg_SaveCSV(read_json,read_img,save_img_dir,save_csv,img_num,list_key) # 循环+值传递
        '''
        print(save_img_str)
        img = cv2.imread(read_img_str, 0)
        equ = cv2.equalizeHist(img)
        cv2.imwrite(save_img_str, equ)
        i+=1
        '''
        # print(line, end = '')

    print(buildDict(list_key))
    idx_file.close()


if __name__ == '__main__':
    main()
