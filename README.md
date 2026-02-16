Projeler
1. Sağlık Sigortası Maliyet Tahmini (Polynomial Regression)
Lineer modellerin verideki non-lineer (doğrusal olmayan) ilişkileri yakalayamadığı durumlarda, modele karesel özellikler ekleyerek karmaşıklığı yönettik.
   - Model Mimarisi: Scikit-Learn PolynomialFeatures (Degree 2).
   - Performans Metrikleri: R² Skoru: %86.7, MAE: 2783$.
   - Kritik Çıkarım: Sigara kullanımı ile BMI (Vücut Kitle Endeksi) arasındaki korelasyonun, sigorta primleri üzerinde ivmeli (exponential) bir artışa neden olduğu saptanmıştır.

2. Hava Durumu Sıcaklık Tahmini (KNN Regressor)
Zaman serisi tabanlı hava durumu verilerinde, benzer hava koşullarının benzer sıcaklık sonuçları doğuracağı hipoteziyle K-Nearest Neighbors algoritması kullanılmıştır.
   - Model Mimarisi: KNeighborsRegressor (n_neighbors=5).
   - Ön İşleme (Preprocessing): StandardScaler ile özellik ölçeklendirme ve pd.to_numeric ile veri tipleme optimizasyonu yapılmıştır.
   - Performans Metrikleri: R² Skoru: %94.8, MAE: 1.30°C.
   - Kritik Çıkarım: Özellikle nem (H) ve maksimum sıcaklık (TM) değişkenlerinin, ortalama sıcaklık üzerinde en yüksek açıklayıcı güce (high feature importance) sahip olduğu gözlemlenmiştir.

💻 3. Bilgisayar Fiyat Tahminleme (Computer Price Prediction)
Bu proje, donanım özelliklerine göre bilgisayar fiyatlarını tahmin etmek amacıyla geliştirilmiştir.

   -Kullanılan Yöntemler: Keşifçi Veri Analizi (EDA), Veri Temizleme (Data Cleaning), Özellik Mühendisliği (Feature Engineering).

   -Amaç: Donanım bileşenlerinin fiyat üzerindeki etkisini analiz etmek ve regresyon modelleri ile fiyat öngörüsünde bulunmak.

📊 4. Algoritma Karşılaştırmalı Fiyat Tahmini (Multi-Model Regression)
Aynı veri seti üzerinde farklı makine öğrenmesi algoritmalarının performanslarını karşılaştırdığım kapsamlı bir çalışmadır.

Kullanılan Algoritmalar:

   -Linear Regression: Değişkenler arası doğrusal ilişki analizi.

   -Polynomial Regression: Doğrusal olmayan karmaşık ilişkilerin modellenmesi.

   -K-Nearest Neighbors (KNN): Benzerlik tabanlı tahminleme.

   -Naive Bayes: Olasılıksal modelleme yaklaşımları.

Teknik Detay: Modellerin hata payları (RMSE, R2 Score) üzerinden performans kıyaslaması yapılarak en iyi sonuç veren algoritma belirlenmiştir.

📧 5. Spam Filtreleme Sistemi (Spam or Not Classifier)
Doğal Dil İşleme (NLP) tekniklerini kullanarak metin verilerini sınıflandıran bir projedir.

   -Kullanılan Teknoloji: NLP (Natural Language Processing).

   -Özellik: Gelen mesajların metin içeriklerini analiz ederek "Spam" veya "Ham" (güvenli) olarak sınıflandırılmasını sağlar.

   -Kapsam: Veri ön işleme, tokenization ve metin sınıflandırma algoritmaları üzerine odaklanılmıştır.

Kullanılan Teknolojiler
   - Diller: Python 
   - Veri Görselleştirme: Matplotlib, Seaborn
   - Makine Öğrenmesi: Scikit-learn
   - Versiyon Kontrol: Git & GitHub
