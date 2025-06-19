📁 腳本一覽 / Script Overview

這個資料夾中的 Python 腳本分為兩類：資料準備與即時偵測。
The Python scripts in this repository are categorized into data preparation and real-time detection.


🔧 資料準備 / Data Preparation
| 檔案名稱                         | 說明（繁體中文）                                   | Description (English)                                                               |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------- |
| `convert_xml_to_info_dat.py` | 將 Pascal VOC 格式的 XML 轉換為 `info.dat` 檔（舊格式） | Converts Pascal VOC XML files into `info.dat` (legacy format)                       |
| `generate_info_from_xml.py`  | 將標註 XML 轉換為 OpenCV 用的 `info.lst` 格式        | Converts annotated XML files into `info.lst` for OpenCV training                    |
| `opencv_createsamples.py`    | 處理新的 XML 標註，產生對應的 `info.lst`               | Generates `info.lst` from new XMLs for positive samples                             |
| `validate_and_fix_info.py`   | 驗證 `info.lst` 中的座標是否超出圖片範圍並進行修正            | Validates and corrects bounding boxes in `info.lst` if they exceed image boundaries |
| `positive_resized.py`        | 將正樣本圖片的長邊縮放為 1024px 並儲存至新資料夾               | Resizes positive images to 1024px on the longer side and saves them                 |


🎥 即時偵測展示 / Real-Time Detection Demos
| 檔案名稱                                     | 說明（繁體中文）                         | Description (English)                                                             |
| ---------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- |
| `main.py`                                | 使用 DroidCam 影像進行給水機 cascade 偵測展示 | Runs dispenser detection on DroidCam video using custom cascade                   |
| `realtime_face_detection_droidcam.py`    | 使用手機相機即時偵測人臉（OpenCV 內建分類器）       | Real-time face detection using smartphone camera and OpenCV's pre-trained cascade |
| `realtime_dispenser_detection_webcam.py` | 使用筆電內建鏡頭執行給水機即時偵測                | Real-time dispenser detection using webcam and custom-trained cascade             |
| `tempCodeRunnerFile.py`                  | 對單張靜態圖片執行物體偵測的測試程式               | Test script for running object detection on a static image (`IMG_5758.jpg`)       |
