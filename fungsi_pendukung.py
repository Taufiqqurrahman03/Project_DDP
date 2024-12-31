import base64
import streamlit as st

def ubah_file_ke_base64(lokasi_file):
    """Mengubah file gambar menjadi format base64"""
    with open(lokasi_file, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

def tambah_latar_belakang(lokasi_file):
    """Menambahkan gambar latar belakang ke aplikasi Streamlit"""
    base64_str = ubah_file_ke_base64(lokasi_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )