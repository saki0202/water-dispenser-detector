import cv2

# Haar cascade 分類器のパス（あとで学習したXMLをここに置く）
cascade_path = "classifier/cascade.xml"
cascade = cv2.CascadeClassifier(cascade_path)

# カメラ起動（0 は通常ノートPC内蔵カメラ）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが起動できません")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレーム取得失敗")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Haar分類器で物体検出
    objects = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Water Dispenser Detection", frame)

    # ESCキーで終了
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
