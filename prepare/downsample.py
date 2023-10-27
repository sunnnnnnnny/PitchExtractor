import os
import shutil
from glob import glob

wav_44k_path_list = glob("/data8/master_dataset_model_zhangyuqiang/aishell3_44k/*/wav/*/*wav")
wav_24k_dir = "/data8/master_dataset_model_zhangyuqiang/aishell3_24k_without_normal"
if not os.path.exists(wav_24k_dir):
    os.makedirs(wav_24k_dir)


def sample(wav_path):
    wav_path_split = wav_path.split("/")
    speaker, filename = wav_path_split[-2], wav_path_split[-1]
    speaker_dir = os.path.join(wav_24k_dir, speaker)
    if not os.path.exists(speaker_dir):
        os.makedirs(speaker_dir)
    tgt_path = os.path.join(speaker_dir, filename)
    src_txt_path = wav_path.replace(".wav", ".txt")
    tgt_txt_path = os.path.join(speaker_dir, src_txt_path.split("/")[-1])
    if not os.path.exists(tgt_txt_path) and os.path.exists(src_txt_path):
        shutil.copyfile(src_txt_path, tgt_txt_path)
    cmd = "ffmpeg -i {} -ar 24000 -ac 1 {}".format(wav_path, tgt_path)
    
    if not os.path.exists(tgt_path):
        os.system(cmd)

    return


if __name__ == "__main__":
    import multiprocessing as mul

    pools = mul.Pool(os.cpu_count())
    print(len(wav_44k_path_list))
    pools.map(sample, wav_44k_path_list)
