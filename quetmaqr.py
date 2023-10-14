import cv2 as cv
from pyzbar.pyzbar import decode

# Mở camera
cap = cv.VideoCapture(0)
while True:
    # Đọc frame từ camera
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx=0.6, fy=0.6)
    barcodes = decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(barcode_data)


        # Hiển thị thông tin về mã vạch hoặc mã QR code
        cv.putText(frame, f'Type: {barcode_type}', (barcode.rect.left, barcode.rect.top - 10),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv.putText(frame, f'Data: {barcode_data}', (barcode.rect.left, barcode.rect.top + 20),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị frame
    cv.imshow('Barcode Scanner', frame)

    if cv.waitKey(1) & 0xFF == 27:  # Bấm ESC để thoát
        break

# Giải phóng camera và đóng cửa sổ hiển thị
cap.release()
cv.destroyAllWindows()
