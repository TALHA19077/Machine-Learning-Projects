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


Kullanılan Teknolojiler
   - Diller: Python 
   - Veri Görselleştirme: Matplotlib, Seaborn
   - Makine Öğrenmesi: Scikit-learn
   - Versiyon Kontrol: Git & GitHub
