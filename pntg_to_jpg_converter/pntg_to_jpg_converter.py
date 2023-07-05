import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
pntg_folder = askdirectory(title='Select folder with PNTG images:')
jpg_folder = askdirectory(title='Select folder to save converted JPG images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the PNTG folder
for file_name in os.listdir(pntg_folder):
    if file_name.endswith('.pntg'):
        # open PNTG image and convert to JPG
        pntg_file_path = os.path.join(pntg_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        pntg_image = Image.open(pntg_file_path)

        # save JPG image with maximum quality
        pntg_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All PNTG images in {pntg_folder} converted to JPG and saved in {jpg_folder}.')

#softy_plug