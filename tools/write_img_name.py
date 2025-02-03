import os

# 今いるディレクトリを取得
current_dir = os.getcwd()

# 対象フォルダのパス
folder_path = current_dir + '/data/object_images/connector_2/peg'

# フォルダ内のファイル名をリスト化
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]

# A.txtファイルに書き込み
with open('./data/BSDS/ImageSets/test.txt', 'w') as f:
    for image_file in image_files:
        # 対応する.matファイルの名前を作成
        mat_file = image_file.replace('.png', '.mat')
        # ファイル名を書き込む
        f.write(f"{image_file} {mat_file}\n")