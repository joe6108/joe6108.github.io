import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖片
image = cv2.imread("./img/capo/block_capo.jpg")

# 檢查圖片是否成功讀取
if image is None:
    print("無法載入圖片，請檢查路徑是否正確！")
    exit()

# 縮小顯示圖片（不影響原始計算）
scale_percent = 50  # 顯示縮放比例（例如 50%）
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height))

# 讓使用者選擇前景區域（在縮小版的圖片上選擇）
rect = cv2.selectROI("請選擇前景", resized_image, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("請選擇前景")

# **將選擇的範圍還原為原始解析度**
rect = (
    int(rect[0] * 100 / scale_percent),  # x
    int(rect[1] * 100 / scale_percent),  # y
    int(rect[2] * 100 / scale_percent),  # w
    int(rect[3] * 100 / scale_percent)   # h
)

# 建立 GrabCut 需要的 mask
mask = np.zeros(image.shape[:2], np.uint8)

# 建立背景與前景模型
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 使用 GrabCut 進行去背
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 轉換 Mask（0,2 是背景，1,3 是前景）
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

# 取得前景
result = image * mask2[:, :, np.newaxis]

# 設定新的背景顏色
bg_color = (176, 237, 204)  # 你想要的背景顏色（BGR）
background = np.full_like(image, bg_color, dtype=np.uint8)

# 替換背景顏色
final_image = np.where(result == 0, background, result)

# 顯示結果
plt.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# 儲存結果
cv2.imwrite("output.jpg", final_image)
