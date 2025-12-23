import cv2

def test_camera():
    print("basit kamera testi baslatiliyor...")
    
    # Denenecek indeksler
    indexes = [0, 1, 2, 3]
    
    for idx in indexes:
        print(f"\n--- Index {idx} deneniyor ---")
        try:
            # Backend belirtmeden dene (Varsayılan)
            cap = cv2.VideoCapture(idx)
            
            if cap.isOpened():
                print(f"✅ Kamera {idx} AÇILDI (Backend: Default)")
                ret, frame = cap.read()
                if ret:
                    print(f"✅ Görüntü alındı! Boyut: {frame.shape}")
                    cv2.imshow(f"Test Kamera {idx}", frame)
                    print("Kapatmak için bir tuşa basın...")
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("❌ Kamera açıldı ama görüntü (frame) okunamadı.")
                cap.release()
            else:
                print(f"❌ Kamera {idx} açılamadı (isOpened=False).")
                
            # Backend ile dene (DSHOW - Windows için)
            print(f"--- Index {idx} (DSHOW) deneniyor ---")
            cap_dshow = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
            if cap_dshow.isOpened():
                print(f"✅ Kamera {idx} AÇILDI (Backend: DSHOW)")
                ret, frame = cap_dshow.read()
                if ret:
                    print(f"✅ Görüntü alındı! Boyut: {frame.shape}")
                    cap_dshow.release()
                else:
                    print("❌ Kamera açıldı ama görüntü okunamadı.")
                    cap_dshow.release()
            else:
                print(f"❌ Kamera {idx} (DSHOW) açılamadı.")
                
        except Exception as e:
            print(f"HATA: {e}")

    print("\nTest tamamlandı.")

if __name__ == "__main__":
    test_camera()
