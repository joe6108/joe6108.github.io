import cv2
import numpy as np

# 定義回調函數（處理滑鼠點擊）
def get_rgb(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 滑鼠左鍵點擊
        pixel_color = image[y, x]  # 讀取點擊位置的顏色 (B, G, R)
        pixel_color = (int(pixel_color[2]), int(pixel_color[1]), int(pixel_color[0]))  # 轉為 (R, G, B)
        
        print(f"座標 ({x}, {y}) 的 RGB 顏色: {pixel_color}")
        
        # 標記點擊的位置
        cv2.circle(display_image, (x, y), 5, (0, 255, 0), -1)  # 畫一個綠色小圓點
        cv2.imshow("點擊圖片獲取 RGB", display_image)  # 更新畫面

# 讀取圖片
image_path = "./img/capo/capo.jpg"  # 改成你的圖片檔案路徑
image = cv2.imread(image_path)  # 讀取圖片（BGR 格式）

if image is None:
    print("無法載入圖片，請檢查路徑是否正確！")
    exit()

display_image = image.copy()  # 建立副本以顯示標記
cv2.imshow("點擊圖片獲取 RGB", display_image)  # 顯示圖片
cv2.setMouseCallback("點擊圖片獲取 RGB", get_rgb)  # 綁定滑鼠事件

cv2.waitKey(0)  # 等待鍵盤輸入
cv2.destroyAllWindows()  # 關閉視窗