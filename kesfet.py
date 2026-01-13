#%%
import pandas as pd

#%%
# 1. OKUMA: İlk 2 satırı atla, 3. satır başlık olsun
df = pd.read_excel("Bekleyenler.xlsx", skiprows=2)

print("📊 Sütun isimleri:")
print(df.columns.tolist())
print(f"\n📊 Boyut: {len(df)} satır, {len(df.columns)} sütun")

# İlk 10 satırı göster
df.head(10)

#%%
# 2. ADET sütununu sil (gereksiz)
df = df.drop(columns=['Adet'])

# 3. Unnamed sütunlarını sil
unnamed_cols = [col for col in df.columns if 'Unnamed' in str(col)]
df = df.drop(columns=unnamed_cols)

print(f"🗑️ Silinen sütunlar: Adet, {unnamed_cols}")
print(f"📊 Kalan sütunlar: {df.columns.tolist()}")
# %%
df.head(10)
# %%
# 4. FORWARD FILL: Durum sütunundaki NaN'ları doldur
print("🔍 Doldurmadan ÖNCE - Durum sütunu:")
print(df['Durum'].head(15).tolist())

# ffill = forward fill (yukarıdaki değerle doldur)
df['Durum'] = df['Durum'].ffill()
print("\n✅ Doldurduktan SONRA - Durum sütunu:")
print(df['Durum'].head(15).tolist())

# %%
df.head(10)
# %%
# 5. ÖZET SATIRLARINI SİL: Sadece Fiş No olanları tut
print(f"🔍 Silmeden önce: {len(df)} satır")

# Fiş No boş olmayanları tut
df = df[df['Fiş No'].notna()]

print(f"✅ Sildikten sonra: {len(df)} satır")

# Kontrol
df.head(10)
# %%
# 6. VERİ TİPLERİNİ DÜZELT
# Fiş No ve Başvuru No'yu tam sayıya çevir
df['Fiş No'] = df['Fiş No'].astype(int)
df['Başvuru No'] = df['Başvuru No'].astype(int)

# Gün sütununu da tam sayıya çevir (varsa)
df['Gün'] = df['Gün'].astype(int)

print("✅ Veri tipleri düzeltildi!")
print(df.dtypes)
# %%
df.head(10)
# %%
# %%
# 7. TEMİZ DOSYAYI KAYDET
df.to_excel("Bekleyenler_Temiz.xlsx", index=False)

print(f"✅ Temiz dosya kaydedildi!")
print(f"📊 Toplam: {len(df)} satır, {len(df.columns)} sütun")
print(f"📁 Dosya: Bekleyenler_Temiz.xlsx")
# %%
