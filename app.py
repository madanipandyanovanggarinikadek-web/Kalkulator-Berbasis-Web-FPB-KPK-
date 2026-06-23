import streamlit as st
import base64

# ======================
# BACKGROUND GALAXY
# ======================

page_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

.main{
background: rgba(0,0,0,0.5);
padding:20px;
border-radius:15px;
}

h1,h2,h3,p,label{
color:white !important;
}

.stButton>button{
background: linear-gradient(90deg,#8a2be2,#4b0082);
color:white;
border:none;
border-radius:10px;
height:50px;
font-size:18px;
font-weight:bold;
}

.result-box{
padding:15px;
border-radius:15px;
background:rgba(255,255,255,0.1);
backdrop-filter: blur(10px);
margin-top:15px;
}

.euclid-box{
padding:15px;
border-radius:15px;
background:rgba(0,0,0,0.4);
color:white;
margin-top:10px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ======================
# JUDUL
# ======================

st.markdown("""
<h1 style='text-align:center;'>
🌌 Kalkulator FPB & KPK
</h1>
<h3 style='text-align:center;'>
Menggunakan Algoritma Euclid
</h3>
""", unsafe_allow_html=True)

# ======================
# FUNGSI EUCLID
# ======================

def euclid_steps(a, b):
    langkah = []

    while b != 0:
        q = a // b
        r = a % b

        langkah.append(
            f"{a} = {b} × {q} + {r}"
        )

        a, b = b, r

    return a, langkah

# ======================
# INPUT
# ======================

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Masukkan Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Masukkan Bilangan Kedua",
        min_value=1,
        step=1
    )

# ======================
# PROSES
# ======================

if st.button("🚀 Hitung FPB & KPK"):

    fpb, langkah = euclid_steps(a, b)

    kpk = (a * b) // fpb

    st.markdown("""
    <div class='result-box'>
    <h2>📋 Langkah Algoritma Euclid</h2>
    </div>
    """, unsafe_allow_html=True)

    for i, l in enumerate(langkah, start=1):
        st.markdown(
            f"""
            <div class='euclid-box'>
            Langkah {i}: {l}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(f"✅ FPB = {fpb}")

    st.info(f"✨ KPK = {kpk}")

    st.markdown(f"""
    <div class='result-box'>
    <h3>Perhitungan KPK</h3>

    KPK = (a × b) / FPB

    = ({a} × {b}) / {fpb}

    = {kpk}
    </div>
    """, unsafe_allow_html=True)

# ======================
# FOOTER
# ======================

st.markdown("""
<br><br>
<center>
<p style='color:white'>
🌠 Dibuat untuk Proyek Teori Bilangan
</p>
</center>
""", unsafe_allow_html=True)
