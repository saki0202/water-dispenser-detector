import os
import cv2

input_lst = "data/final_positive/info.lst"
output_lst = "data/final_positive/info_cleaned.lst"
base_path = "data/final_positive"

fixed_lines = []

with open(input_lst, "r") as f:
    for line in f:
        parts = line.strip().split()
        img_path = os.path.join(base_path, os.path.basename(parts[0]))
        if not os.path.exists(img_path):
            print(f"Not found: {img_path}")
            continue
        img = cv2.imread(img_path)
        if img is None:
            print(f"Unreadable: {img_path}")
            continue
        h, w = img.shape[:2]
        x, y, bw, bh = map(int, parts[2:])
        if x + bw <= w and y + bh <= h:
            fixed_lines.append(line.strip())
        else:
            print(f"Invalid bbox: {img_path} ({x+bw}>{w} or {y+bh}>{h})")

# 書き出し
with open(output_lst, "w") as f:
    for line in fixed_lines:
        f.write(line + "\n")

print(f"✅ 修正完了: valid entries = {len(fixed_lines)} 行")
