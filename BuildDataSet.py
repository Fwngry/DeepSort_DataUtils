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
LABEL_DICT={'0_0': 0, '0_1': 1, '0_2': 2, '0_3': 3, '0_4': 4, '0_5': 5, '0_6': 6, '1_0': 7, '1_1': 8, '1_2': 9, '1_3': 10, '1_4': 11, '1_5': 12, '2_0': 13, '2_1': 14, '2_2': 15, '3_0': 16, '3_1': 17, '3_3': 18, '3_4': 19, '3_5': 20, '3_6': 21, '3_7': 22, '3_8': 23, '3_9': 24, '4_0': 25, '4_1': 26, '4_2': 27, '5_0': 28, '5_1': 29, '5_2': 30}
# mkdir

def Cropimg_SaveCSV(read_json,read_img,save_img_dir,save_csv,img_num):
# read_img=""
# img=cv2.imread(read_img)
    img = cv2.imread(read_img, 0)
    img = cv2.equalizeHist(img)
    with open(read_json, 'r') as json_f:
        data = json.load(json_f)
        # print(data['shapes'])
        for idx,shapes in enumerate(data['shapes']):
            save_img=save_img_dir + "/" + format(img_num, '08d') +".png" 
            # print(save_img)
            # print(idx,shapes['label'],shapes['points'][0][0],shapes['points'][1][0],shapes['points'][0][1],shapes['points'][1][1])
            X_left=int(shapes['points'][0][0])
            Y_left=int(shapes['points'][0][1])
            X_Right=int(shapes['points'][1][0])
            Y_Right=int(shapes['points'][1][1])
            # print(X_left,X_Right,Y_left,Y_Right)
            tem_img=img[Y_left:Y_Right,X_left:X_Right]
            #plt.imshow(tem_img)
            #plt.show()
            cv2.imwrite(save_img, tem_img)
            label=get_label(read_img,shapes['label'])
            row=[save_img,label]
            with open(save_csv,'a+',newline='')as csv_f: # a+是追加
                wf = csv.writer(csv_f)
                wf.writerow(row)
            img_num+=1
    return img_num
# print(data['shapes'][1]['label'])
def get_label(read_img,label):
    p1 = re.compile(r'[q](.*?)[/]', re.S) #最小匹配
    label_key=re.findall(p1, read_img)[0] + '_' + label
    return LABEL_DICT[label_key]
    # print(label_dict)

def main():
    # always using relative path in this .py

    idx_file = open(idx_path)
    img_num=0           
    with open(save_csv,'w',newline='')as f:
        f_csv = csv.DictWriter(f,headers) # csv_file+head，create csv object
        f_csv.writeheader() 
    for line in idx_file: # read txt line by line
        read_json = line.strip() # the json_dir
        read_img = read_json[:read_json.rfind(".")] + ".png" # change surffix (form .json to .png) as the read img path
        # save_img = save_img_dir + "/" + format(i, '08d') +".png" 
        # 原始路径 save_img_str = output_img_dir + line[line.rfind("/"):line.rfind(".")]+".png" 
        img_num=Cropimg_SaveCSV(read_json,read_img,save_img_dir,save_csv,img_num) # 循环+值传递
        
        '''
        print(save_img_str)
        img = cv2.imread(read_img_str, 0)
        equ = cv2.equalizeHist(img)
        cv2.imwrite(save_img_str, equ)
        i+=1
        '''
        # print(line, end = '')
    idx_file.close()


if __name__ == '__main__':
    main()
