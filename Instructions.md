# 🏗️ PortalBekleyenPy - Proje Künyesi

## 📋 İçindekiler
- [Projenin Tanımı](#projenin-tanımı)
- [Proje Fazları](#proje-fazları)
- [Mevcut Durum (Sorun)](#mevcut-durum-sorun)
- [Projenin Amacı](#projenin-amacı)
- [İşleyiş Süreci](#işleyiş-süreci-algoritma)
- [Dosya Yapısı](#dosya-yapısı)
- [Kullanım](#kullanım)
- [Teknoloji Yığını](#teknoloji-yığını)

---

## 🎯 Projenin Tanımı

**PortalBekleyenPy**, yetkili servis süreçlerinde kullanılan ve ham haliyle analiz edilmeye uygun olmayan "Bekleyen İşler" Excel dökümünü; Python programlama dili kullanılarak temizleyen, düzenleyen ve analize hazır hale getiren bir **veri otomasyon projesidir**.

---

## 🚀 Proje Fazları

| Faz | Açıklama | Durum |
|-----|----------|-------|
| **Faz 1: Core Script** | Ham veriyi işleyen temel Python algoritmaları | ✅ Tamamlandı |
| **Faz 2: Web Arayüzü** | Streamlit tabanlı kullanıcı arayüzü | ✅ Tamamlandı |
| **Faz 3: Veritabanı** | PostgreSQL entegrasyonu (Gelecek Vizyonu) | 🔜 Planlandı |

### Faz 2: Web Arayüzü - Tamamlanan Özellikler

| Özellik | Açıklama | Durum |
|---------|----------|-------|
| Streamlit Arayüzü | Modern, responsive web arayüzü | ✅ |
| Dosya Yükleme | Sürükle-bırak ile Excel yükleme | ✅ |
| Otomatik Temizleme | 5 adımlı veri temizleme | ✅ |
| İnteraktif Tablo | Sıralama, kaydırma destekli görüntüleme | ✅ |
| Excel İndirme | .xlsx formatında indirme | ✅ |
| CSV İndirme | .csv formatında indirme | ✅ |
| Desktop Kısayolu | Mac Automator uygulaması | ✅ |
| Cloud Deployment | Streamlit Cloud online erişim | ✅ |

---

## ⚠️ Mevcut Durum (Sorun)

Servis portalından indirilen `Bekleyenler.xlsx` dosyası, bilgisayar algoritmaları için değil, **insan gözü için tasarlanmıştır**. Bu durum şu sorunları yaratmaktadır:

| Sorun | Açıklama |
|-------|----------|
| 🔀 **Hiyerarşik Dağınıklık** | Veriler "Durum" başlıkları altında gruplanmış ancak satırlarda bu bilgi tekrar edilmemiştir (Merge mantığı). |
| 🏗️ **Yapısal Bozukluk** | Sütun başlıkları ilk satırda değil, sayfanın ortalarında yer almaktadır. |
| 🔊 **Gürültülü Veri** | Analiz için gereksiz olan ara toplam satırları ve boşluklar gerçek veriyi maskelemektedir. |

---

## 🎯 Projenin Amacı

Bu projenin temel amacı **veri restorasyonudur**. Dağınık ve işlenmesi zor olan ham veriyi, Python'un güçlü kütüphanesi **Pandas** kullanarak standart, sorgulanabilir ve raporlanabilir bir veri tablosuna (DataFrame) dönüştürmektir.

### Kazanımlar:
- ✅ Servisteki iş yükü anlık olarak ölçülebilir
- ✅ Hangi teknisyenin üzerinde kaç iş olduğu tek tıkla görülebilir
- ✅ Manuel Excel işlemleriyle vakit kaybetmek yerine, süreç tamamen otomatikleştirilir

---

## ⚙️ İşleyiş Süreci (Algoritma)

PortalBekleyenPy, veriyi işlerken şu **5 adımlı mimari süreci** izler:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. GİRİŞ   │ -> │  2. DOLGU   │ -> │ 3. AYIKLAMA │ -> │ 4. TİP DÖN. │ -> │  5. ÇIKTI   │
│ (Ingestion) │    │(Forward Fill)│   │ (Filtering) │    │  (Casting)  │    │  (Export)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Adım Detayları:

| # | Adım | İşlem |
|---|------|-------|
| 1 | **Giriş (Ingestion)** | Dosya, ilk 2 satırdaki gereksiz veriler atlanarak okunur. |
| 2 | **Dolgu (Forward Fill)** | Excel'deki boş bırakılan "Durum" hücreleri, bir üstteki grup başlığı referans alınarak doldurulur. Böylece her işin hangi statüde olduğu satır bazında tanımlanır. |
| 3 | **Ayıklama (Filtering)** | Sadece gerçek iş kayıtlarını (Fiş Numarası olanlar) tutmak için, ara başlıklar ve özet satırları elenir. |
| 4 | **Tip Dönüşümü (Casting)** | Sayısal veriler (Fiş No, Gün vb.) ondalıklı sayı formatından kurtarılıp tam sayıya çevrilir. |
| 5 | **Çıktı (Export)** | Temizlenmiş ve yapılandırılmış veri, `Bekleyenler_Temiz.xlsx` adıyla analize hazır bir şekilde dışarı aktarılır. |

---

## 📁 Dosya Yapısı

```
PortalBekleyenPy/
├── venv/                     # Python sanal ortam
├── .git/                     # Git versiyon kontrol
├── Instructions.md           # Bu dosya - Proje dokümantasyonu
├── roadmap.md                # Yol haritası
├── requirements.txt          # Bağımlılıklar (streamlit, pandas, openpyxl)
├── Bekleyenler.xlsx          # Girdi: Ham portal verisi
├── Bekleyenler_Temiz.xlsx    # Çıktı: Temizlenmiş veri
├── kesfet.py                 # Veri keşif scripti
├── app.py                    # Streamlit web uygulaması
└── PortalBekleyenlerPy.app   # Mac desktop uygulaması (Automator)
```

---

## 🚀 Kullanım

### Yöntem 1: Desktop Uygulaması (En Kolay)

Mac'te masaüstündeki **PortalBekleyenlerPy** uygulamasına çift tıkla.
Tarayıcı otomatik açılır.

---

### Yöntem 2: Online Erişim (Streamlit Cloud)

Tarayıcıdan doğrudan erişim:
```
https://portalbeklenenpy.streamlit.app
```

> Not: GitHub reposundaki güncel kodu kullanır.

---

### Yöntem 3: Terminal ile Çalıştırma

```bash
cd /Users/sultan/Desktop/y/014_/PortalBekleyenPy
source venv/bin/activate
streamlit run app.py
```

#### Uygulama Akışı (Workflow)

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   1. INPUT      │ -> │   2. PROCESS    │ -> │   3. OUTPUT     │
│  Dosya Yükle    │    │  Pandas Motoru  │    │ Tablo + İndirme │
│ (Sürükle-Bırak) │    │ Temizle & Dönüş │    │    Butonu       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

1. **Input (Girdi):** Kullanıcı, tarayıcı arayüzünden ham `Bekleyenler.xlsx` dosyasını sürükleyip bırakır.
2. **Process (İşlem):** Streamlit dosyayı belleğe alır, Pandas motoru temizlik işlemlerini yapar.
3. **Output (Çıktı):** İşlenen veri ekranda interaktif tablo olarak gösterilir + indirme butonu sunulur.

---

## 🛠️ Teknoloji Yığını

| Teknoloji | Kullanım Amacı | Faz |
|-----------|----------------|-----|
| Python 3.x | Ana programlama dili | 1, 2 |
| Pandas | Veri manipülasyonu ve analizi | 1, 2 |
| OpenPyXL | Excel dosya okuma/yazma | 1, 2 |
| **Streamlit** | Web arayüzü (GUI) | 2 |
| PostgreSQL | Veritabanı (Gelecek Vizyonu) | 3 |

### Neden Streamlit?

- **Python-Native:** HTML/CSS/JS bilgisine ihtiyaç duymadan, %100 Python ile frontend oluşturulur.
- **Hızlı Prototipleme:** Veri odaklı uygulamalar için özel tasarlanmıştır (DataFrame'leri tablo olarak gösterme, grafik çizme vb. yerleşiktir).
- **Etkileşim:** Anlık veri filtreleme ve manipülasyon imkanı sağlar.

---

## 📊 Proje Durumu

### Genel İlerleme

```
[■■■■■■■■■□] %90 Tamamlandı
```

| Faz | Durum | İlerleme |
|-----|-------|----------|
| Faz 1: Core Script | ✅ Tamamlandı | ████████████ 100% |
| Faz 2: Web Arayüzü | ✅ Tamamlandı | ████████████ 100% |
| Faz 3: Veritabanı | 🔜 Planlandı | ░░░░░░░░░░░░ 0% |

### Uygulama Özellikleri

| Özellik | Durum |
|---------|-------|
| 📤 Dosya Yükleme (Sürükle-Bırak) | ✅ |
| 🔄 Otomatik Veri Temizleme | ✅ |
| 📊 İnteraktif Tablo Görünümü | ✅ |
| 📥 Excel İndirme (.xlsx) | ✅ |
| 📥 CSV İndirme (.csv) | ✅ |
| 🖥️ Desktop Kısayolu (Mac) | ✅ |
| ☁️ Online Erişim (Streamlit Cloud) | ✅ |

---

## 📊 Beklenen Sonuç

Temizlenmiş veri tablosu şu özelliklere sahip olacaktır:

- ✅ Her satır tek bir iş kaydını temsil eder
- ✅ "Durum" sütunu her satırda dolu olacak
- ✅ Ara başlık ve özet satırları olmayacak
- ✅ Sayısal değerler doğru formatta olacak
- ✅ Doğrudan pivot tablo, filtreleme ve raporlama için hazır

---

## 🔗 Bağlantılar

| Kaynak | URL |
|--------|-----|
| GitHub Repo | https://github.com/KULLANICI_ADIN/PortalBekleyenPy |
| Streamlit Cloud | https://portalbeklenenpy.streamlit.app |

---

*Bu proje, manuel Excel işlemlerini ortadan kaldırarak servis verimliliğini artırmayı hedeflemektedir.* 🎯

*Son Güncelleme: 13 Ocak 2026* 📅
