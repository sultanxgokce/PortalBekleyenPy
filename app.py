import streamlit as st
import pandas as pd

# Temizleme fonksiyonları
def clean_data(df):
    """
    5 adımlı temizleme:
    1. İlk 2 satırı atla (header'ı düzelt)
    2. Gereksiz sütunları sil
    3. Durum sütununu doldur (ffill)
    4. Özet satırlarını sil
    5. Veri tiplerini düzelt
    """
    
    # 1. İlk 2 satırı atla, 3. satırı header yap
    df = pd.read_excel(df, skiprows=2)
    
    # 2. Gereksiz sütunları sil
    df = df.drop(columns=['Adet'], errors='ignore')
    unnamed_cols = [col for col in df.columns if 'Unnamed' in str(col)]
    df = df.drop(columns=unnamed_cols, errors='ignore')
    
    # 3. Durum sütununu doldur
    df['Durum'] = df['Durum'].ffill()
    
    # 4. Özet satırlarını sil (Fiş No olanları tut)
    df = df[df['Fiş No'].notna()]
    
    # 5. Veri tiplerini düzelt
    df['Fiş No'] = df['Fiş No'].astype(int)
    df['Başvuru No'] = df['Başvuru No'].astype(int)
    df['Gün'] = df['Gün'].astype(int)
    
    return df

# Sayfa Ayarları
st.set_page_config(
    page_title="PortalBekleyenPy",
    page_icon="📊",
    layout="wide"
)

# Başlık
st.title("PortalBekleyenPy")
st.subheader("Bekleyen İşler Veri Temizleme Aracı")

# Açıklama
st.markdown("""
Bu uygulama, servis portalından indirilen **Bekleyenler.xlsx** dosyasını 
otomatik olarak temizler ve analize hazır hale getirir.
""")

# Ayırıcı çizgi
st.divider()


st.subheader("1) Dosya Yükle")
uploaded = st.file_uploader("Bekleyenler.xlsx dosyasını seçin", type=["xlsx"])

if uploaded:
    st.success("Dosya yüklendi, temizleniyor...")
    try:
        # Ham veriyi göster
        df_raw = pd.read_excel(uploaded, header=None)
        with st.expander("📋 Ham Veri (ilk 20 satır)"):
            st.dataframe(df_raw.head(20))
        
        # Temizlenmiş veriyi göster
        df_clean = clean_data(uploaded)
        st.success(f"✅ Temizleme tamamlandı! ({len(df_clean)} satır)")
        st.write("📊 Temizlenmiş Veri:")
        st.dataframe(df_clean)
        
                # İndirme butonu
        st.divider()
        st.subheader("2) Temiz Dosyayı İndir")
        
        # Excel'e çevir
        from io import BytesIO
        buffer = BytesIO()
        df_clean.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)
        
        st.download_button(
            label="📥 Bekleyenler_Temiz.xlsx İndir",
            data=buffer,
            file_name="Bekleyenler_Temiz.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # CSV olarak indir
        csv_data = df_clean.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📥 Bekleyenler_Temiz.csv İndir",
            data=csv_data,
            file_name="Bekleyenler_Temiz.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Hata: {e}")
        