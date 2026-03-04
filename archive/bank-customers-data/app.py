import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Modeli ve Scaler'ı yükle
@st.cache_resource
def load_assets():
    model = joblib.load('banka_svm_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_assets()

st.title("🏦 Bankacı Muhammed - Tahmin Paneli")

# Arayüz girişleri
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Yaş", 18, 95, 30)
    balance = st.number_input("Bakiye ($)", -5000, 100000, 2000)
with col2:
    duration = st.number_input("Konuşma Süresi (Saniye)", 0, 5000, 150)
    campaign = st.number_input("Kampanya Temas Sayısı", 1, 50, 1)

if st.button("Müşteriyi Analiz Et"):
    # 43 sütunluk boş veri seti (Eğitimdeki formatımız)
    data = np.zeros(42)
    data[0], data[1], data[3] = age, balance, duration

    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        st.success("🎯 BU MÜŞTERİ MEVDUAT AÇABİLİR!")
    else:
        st.error("😔 Mevduat açma ihtimali düşük görünüyor.")
