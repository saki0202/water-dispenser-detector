import cv2

# DroidCam の URL（スマホのIPに置き換える）
url = "http://172.20.10.2:4747/video"
cap = cv2.VideoCapture(url)

# カスケードファイルのパス（顔認識）
pictPath = r"C:\Users\sakis\2025_CV\water-dispenser-detector\data\cascade_output\cascade.xml"
face_cascade = cv2.CascadeClassifier(pictPath)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # 顔を検出（他の物体検出用 cascade でも可）
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 検出した顔に枠を描画
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                      (255, 0, 0), 2)  # 青い枠

    # 画面右下に検出数を表示
    cv2.rectangle(frame, (frame.shape[1]-160, frame.shape[0]-25),
                  (frame.shape[1], frame.shape[0]), (0, 255, 255), -1)
    cv2.putText(frame, f"Dispenser: {len(faces)}",
                (frame.shape[1]-155, frame.shape[0]-7),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

    # 表示
    cv2.imshow("DroidCam dispender Detection", frame)

    if cv2.waitKey(1) == 27:  # ESCで終了
        break

cap.release()
cv2.destroyAllWindows()