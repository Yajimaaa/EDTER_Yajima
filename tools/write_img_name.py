import os

# 対象フォルダのパス
folder_path = '/gs/fs/tga-openv/masaruy/general_insertion/object_images/3d_printed_3/hole'

# フォルダ内のファイル名をリスト化
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]

# A.txtファイルに書き込み
with open('./data/NYUD/ImageSets/image-test.txt', 'w') as f:
    for image_file in image_files:
        # 対応する.matファイルの名前を作成
        mat_file = image_file.replace('.png', '.mat')
        # ファイル名を書き込む
        f.write(f"{image_file} {mat_file}\n")