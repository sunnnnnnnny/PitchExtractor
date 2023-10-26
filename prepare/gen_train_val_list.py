import os
import random
from glob import glob
from sklearn.model_selection import train_test_split


random.seed(616)

# parameter dir
data_dir = "../Data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
wav_dir = "/data8/master_dataset_model_zhangyuqiang/aishell3_24k_without_normal"

# split speaker: %70 train %30 eval
all_speakers = []
all_speakers_tmp = glob("/data8/master_dataset_model_zhangyuqiang/aishell3_24k_without_normal/*")
print("all_speakers_tmp: ", len(all_speakers_tmp))
for tmp in all_speakers_tmp:
    speaker = tmp.split("/")[-1]
    all_speakers.append(speaker)

train_speakers, eval_speakers = train_test_split(all_speakers, test_size=0.3, random_state=616)


wav_path_list = glob(wav_dir + "/*/*wav")
train_lines, eval_lines = [], []
for wav_path in wav_path_list:
    speaker = wav_path.split("/")[-2]
    if speaker in train_speakers:
        line = wav_path + "|something|something\n"
        train_lines.append(line)
    else:
        line = wav_path + "|something|something\n"
        eval_lines.append(line)

with open(os.path.join(data_dir, "train_list_aishell3.txt"), "w") as train_log:
    for line in train_lines:
        train_log.write(line)

with open(os.path.join(data_dir, "eval_list_aishell3.txt"), "w") as eval_log:
    for line in eval_lines:
        eval_log.write(line)




# collect data



