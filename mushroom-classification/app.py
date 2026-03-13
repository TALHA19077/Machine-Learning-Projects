import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Veriyi yükle ve encode et
import os
BASE_DIR = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(BASE_DIR, "mushrooms.csv"))

with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)
columns = [i for i in df.columns if i != 'class']
encoders = {}
for col in columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

st.title("🍄 Mantar Tahmin Uygulaması")
st.write("Mantar özelliklerini seçin, model zehirli mi yenilebilir mi söylesin.")
user_input = {}
for col, le in encoders.items():
    user_input[col] = st.selectbox(col, le.classes_)
if st.button("Tahmin Et"):
    # Kullanıcı girdilerini encode et
    encoded_input = {}
    for col, value in user_input.items():
        encoded_input[col] = encoders[col].transform([value])[0]
    
    # DataFrame'e çevir
    input_df = pd.DataFrame([encoded_input])
    
    # Tahmin yap
    prediction = model.predict(input_df)[0]
    
    if prediction == 0:
        st.success("✅ Bu mantar YENİLEBİLİR!")
    else:
        st.error("☠️ Bu mantar ZEHİRLİ!")    