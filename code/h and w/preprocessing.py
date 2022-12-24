import numpy as np
import cv2
import os
import shutil
# resize_factor = 2
def create_patches(image, dim_patch, stride, resize_factor, folder_in, folder_gt, idx_image):
    h, w = image.shape
    for i in range(0, h - dim_patch + 1, stride):
        for j in range(0, w - dim_patch + 1, stride):
            idx_image += 1
            gt_patch = image[i: i + dim_patch, j: j + dim_patch]
            if np.random.random(1) < 0.5:
                dim = (int(gt_patch.shape[1]/resize_factor), int(gt_patch.shape[0]/resize_factor))
                in_patch = cv2.resize(src = cv2.GaussianBlur(gt_patch, (3,3), 0), \
                    dsize = dim, interpolation=cv2.INTER_AREA)
            else:
                dim = (int(gt_patch.shape[1]/resize_factor), int(gt_patch.shape[0]/resize_factor))
                in_patch = cv2.resize(src = gt_patch, \
                    dsize = dim, interpolation=cv2.INTER_AREA)
            
            # if np.sum(in_patch) == 0:
            #     continue
            
            cv2.imwrite(folder_gt + "/" + str(idx_image) + ".png", gt_patch)
            cv2.imwrite(folder_in + "/" + str(idx_image) + ".png", in_patch)
    
    return idx_image

def resize_train(dim_patch, stride, resize_factor):
    
    location_name = '/home/aditya/Documents/UMCP PMRO/Sem 3/ENPM809K/Project/Datasets/png_data0/'
    for subject in sorted(os.listdir(location_name)):
        if subject[0] != '.':
            foldername = location_name + subject + '/'
            # print(foldername)
            
            # # current working directory
            # path = os.getcwd()
            # print("Current Directory:", path)
            # # parent directory
            # parent = os.path.join(os.path.join(path, os.pardir), os.pardir)
            # print(os.path.abspath(parent))
            folder_in = foldername + 'input_train_' + str(dim_patch) + '_' + str(resize_factor)
            folder_gt = foldername + 'gt_train_' + str(dim_patch) + '_' + str(resize_factor)
            
            if os.path.exists(folder_in):
                shutil.rmtree(folder_in)
            os.makedirs(folder_in)

            if os.path.exists(folder_gt):
                shutil.rmtree(folder_gt)
            os.makedirs(folder_gt)

            idx_image = 0
            for img_name in sorted(os.listdir(foldername)):
                if img_name[0] != '.' and img_name[-4:] == '.png':
                    print(img_name)
                    
                    img = cv2.imread(os.path.join(foldername, img_name), cv2.IMREAD_GRAYSCALE)
                    
                    idx_image = create_patches(img, dim_patch, stride, resize_factor, folder_in, folder_gt, idx_image)
            #         cv2.imshow('image', img)
            #         cv2.waitKey(10)
            # cv2.destroyAllWindows()

    return
dim_patch = 64
stride = 64
resize_factor = 2 # Was 4 in the original code
resize_train(dim_patch, stride, resize_factor)