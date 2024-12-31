import streamlit as st

# st.title("Helo Masbro")
# st.write("Apa Kabar")
# st.image("Lazis.png", caption="ini gambar")

# Sidebar directory
dasboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama":[dasboard],
        "Transaksi":[nabung]
    }

)
if"total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()