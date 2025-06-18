import os
import cv2

# 入力画像フォルダ（オリジナル画像）
input_dir = r'C:\Users\sakis\2025_CV\water-dispenser-detector\data\positive'
# 出力画像フォルダ（リサイズ済み画像）
output_dir = input_dir + '_resized'

# 出力フォルダがなければ作成
os.makedirs(output_dir, exist_ok=True)

# 各画像を読み込み＆リサイズ＆保存
for fname in os.listdir(input_dir):
    if fname.lower().endswith(('.jpg', '.png')):
        img_path = os.path.join(input_dir, fname)
        img = cv2.imread(img_path)
        if img is None:
            print(f"読み込み失敗: {fname}")
            continue
        h, w = img.shape[:2]
        scale = 1024 / max(h, w)  # 長辺を1024に
        resized = cv2.resize(img, (int(w * scale), int(h * scale)))
        save_path = os.path.join(output_dir, fname)
        cv2.imwrite(save_path, resized)
        print(f"保存済み: {save_path}")
