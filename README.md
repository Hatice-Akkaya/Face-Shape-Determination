# 📸  Yüz Şekli Analizi MobileNetV2 Modeli ile

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Proje Özeti
Bu proje, insan yüz şekillerini **(Heart, Oblong, Oval, Round, Square)** otomatik olarak sınıflandırmak için derin öğrenme tabanlı bir model geliştirmeyi amaçlamaktadır. 

Model, **MobileNetV2** mimarisi kullanılarak transfer learning yöntemiyle eğitilmiş olup, hem statik fotoğraf dosyalarından hem de canlı kamera görüntüsünden yüksek doğrulukla yüz şekli tahmini yapabilmektedir.

---


## 🚀 Özellikler
* **Otomatik Yüz Tespiti:** OpenCV kullanarak görüntüdeki yüzü bulur ve kırpar.
* **Derin Öğrenme Modeli:** MobileNetV2 tabanlı güçlü bir sınıflandırma altyapısı.
* **Çoklu Tahmin Yöntemi:**
    * 📁 Dosyadan (JPG, PNG) tahmin.
    * 📹 Webcam üzerinden canlı tahmin.
* **Kullanıcı Arayüzü (GUI):** Dosya seçimi için Tkinter entegrasyonu.
* **Görselleştirme:** Tahmin edilen sınıfı ve eminlik (confidence) oranını görsel üzerinde gösterir.

---
## Dosyalar
[requirements.txt](https://github.com/user-attachments/files/24301168/requirements.txt)
[simple_camera_test.py](https://github.com/user-attachments/files/24301169/simple_camera_test.py)
[main.py](https://github.com/user-attachments/files/24301172/main.py)
[face.ipynb](https://github.com/user-attachments/files/24301173/face.ipynb)
[test_on_examples.py](https://github.com/user-attachments/files/24301174/test_on_examples.py)
[train_improved.py](https://github.com/user-attachments/files/24301186/train_improved.py)

## 📂 Klasör Yapısı

```text
faceshape_proje/
│
├── app.py/                  # Uygulama denemeleri
├── dataset/                 # Ham veri seti (5 sınıf)
├── dataset_cropped/         # İşlenmiş (kırpılmış) veri seti
├── efficientnetb0_notop.h5  # Alternatif model ağırlıkları
├── en_iyi_yuz_modeli.h5     # 🏆 Eğitilmiş ve kaydedilmiş ana model
├── face.ipynb               # Proje not defteri (Eğitim & Test)
├── live_inference_improved.py # 📹 Canlı kamera tahmin kodu
├── main.py                  # Ana giriş dosyası
├── simple_camera_test.py    # Basit kamera testi
├── test_on_examples.py      # 🖼️ Dosya üzerinden test kodu
├── train_improved.py        # 🏋️‍♂️ Model eğitim kodu
└── yuz_sekli_mobilenet.h5   # Yedek model dosyası
---




🧠 Teknik Detaylar
Ön İşleme (Preprocessing)
Yüzler OpenCV Haar Cascades veya DNN modülleri ile tespit edilir.

Tespit edilen yüzler kare şeklinde kırpılır ve 160x160 boyutuna getirilir.

preprocess_input fonksiyonu ile MobileNetV2 formatına normalize edilir.


---



Model Mimarisi
Base Model: MobileNetV2 (ImageNet ağırlıkları ile, son katman hariç).

Custom Layers: GlobalAveragePooling2D -> Dense (Softmax).



Eğitim: Class weights kullanılarak dengesiz veri seti yönetimi ve Data Augmentation (veri artırma) teknikleri uygulanmıştır.



📝 Notlar
Modelin en iyi performansı için yüzün net olduğu ve iyi ışık alan fotoğraflar tercih edilmelidir.

en_iyi_yuz_modeli.h5 dosyası proje dizininde bulunmalıdır.



⚖️ Lisans
Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.



📞 İletişim
Sorularınız veya önerileriniz için GitHub üzerinden iletişime geçebilirsiniz.
