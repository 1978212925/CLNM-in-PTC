import os
import pandas as pd
PC_name_list = os.listdir('../../dataset/cropped/primary_cohort')
test0_name_list = os.listdir('../../dataset/cropped/internal_test_cohort')
test1_name_list = os.listdir('../../dataset/cropped/external_test_cohort1')

all_name_list = PC_name_list + test0_name_list + test1_name_list
print(len(all_name_list))
fat_root_path = 'cropped_img'
fat_mask_root_path = 'cropped_mask'
fat_name_list = os.listdir(fat_root_path)
fat_name_list2 = os.listdir(fat_mask_root_path)
print(len(fat_name_list), len(fat_name_list2))
all_name_list = [int(ids.replace('.jpg', '')) for ids in all_name_list]
