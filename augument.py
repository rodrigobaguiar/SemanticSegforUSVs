from matplotlib import pyplot as plt
import albumentations as A
import cv2
import os

image_folder = "D:/Mestrado/Augmented_Dataset/image/"
mask_folder = "D:/Mestrado/Augmented_Dataset/mask/"

aug_image_folder = "D:/Mestrado/Augmented_Dataset/augumented/image/"
aug_mask_folder = "D:/Mestrado/Augmented_Dataset/augumented/mask/"

p1 = 1.0
p2 = 0.5
p3 = 0.8

transform = A.Compose([
    A.MultiplicativeNoise(multiplier=[0.5, 1.0], elementwise=True, p = 0.1),
    A.ImageCompression(quality_lower=19, quality_upper=20, p = 0.2),    
    A.ChannelShuffle(p = 0.2),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p = 0.5),
], p = 1.0)


count = 0
for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    mask_name = filename.split('.')[0] + 'm.png'
    mask_path = os.path.join(mask_folder, mask_name)    
    
    if os.path.isfile(image_path) and os.path.isfile(mask_path):
        image = cv2.imread(image_path)        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
        mask = cv2.imread(mask_path)

        transformed = transform(image=image, mask=mask)
        transformed_image = transformed['image']
        transformed_mask = transformed['mask']

        img = cv2.imwrite(aug_image_folder + "aug_" + str(count) + ".jpg" , transformed_image) 
        img = cv2.imwrite(aug_mask_folder + "aug_" + str(count) + ".png", transformed_mask) 
        count = count + 1




