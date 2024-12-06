import argparse
import os
import csv
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, help='path to the data', default="/content/mtunet_sea2/FSL_data/underwater_photo")
parser.add_argument('--split', type=str, help='path to the split folder', default="/content/mtunet_sea2/data/data_split/underwater_photo")
args = parser.parse_args()

def get_name(root, mode_folder=True):
    for root, dirs, file in os.walk(root):
        if mode_folder:
            return dirs
        else:
            return file

def make_csv(data, name):
    f_val = open(name + ".csv", "w", encoding="utf-8")
    csv_writer = csv.writer(f_val)
    csv_writer.writerow(["filename", "label"])
    for i in range(len(data)):
        csv_writer.writerow(data[i])
    f_val.close()

def move(cls, phase):
    shutil.copytree(os.path.join(data_root, "data", cls), os.path.join(save_root, "underwater_photo", phase, cls))  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**

def read_csv(name):
    with open(name, 'r') as f:
        split = [x.strip() for x in f.readlines() if x.strip() != '']
    return split

def get_split(cls, phase):
    record = []
    for cl in cls:
        name_imgs = get_name(os.path.join(data_root, "data", cl), mode_folder=False)
        for name in name_imgs:
            record.append([cl+"/"+name, cl])
        move(cl, phase)
    # make_csv(record, "data_split/underwater_photo/"+phase) 

if __name__ == '__main__':
    data_root = args.data
    save_root = args.split
    r_root = os.path.join(save_root, "underwater_photo")  
    os.makedirs(r_root, exist_ok=True)

    # **여기에서 새로운 데이터셋에 맞는 파일 경로를 수정**
    name_train = os.path.join(data_root, "splits", "underwater_photo", "train.txt")  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**
    name_val = os.path.join(data_root, "splits", "underwater_photo", "val.txt")  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**
    name_test = os.path.join(data_root, "splits", "underwater_photo", "test.txt")  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**

    train = read_csv(name_train)
    val = read_csv(name_val)
    test = read_csv(name_test)

    os.makedirs(os.path.join(save_root, "underwater_photo", "train"), exist_ok=True)  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**
    os.makedirs(os.path.join(save_root, "underwater_photo", "val"), exist_ok=True)  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**
    os.makedirs(os.path.join(save_root, "underwater_photo", "test"), exist_ok=True)  # **여기에서 "new_dataset"을 새로운 데이터셋 이름으로 수정**

    get_split(train, "train")
    get_split(val, "val")
    get_split(test, "test")
