# 📥 Pasang & Kembali — OrangeFox

[← Panduan OrangeFox](README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](pasang.en.md)

---

## Unduh

Buka **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)** → rilis bertanda **`ofox-v…`** (bukan `v…`, itu TWRP). Versi firmware di judulnya harus **sama** dengan HyperOS-mu (*Setelan → Tentang ponsel*).

| File | Guna |
|---|---|
| **`PAKET-OrangeFox-rothko-<versi>.zip`** | Paket lengkap: bisa di-flash di recovery **atau** diekstrak untuk PC |
| `OrangeFox-rothko-<versi>.img` | Image OrangeFox saja (untuk **Pasang Image**) |
| `STOK-vendor_boot-<versi>.img` | Bawaan Xiaomi — **menghapus** recovery kustom |

Isi paket:

| File | Guna |
|---|---|
| `1-PASANG-ORANGEFOX.bat` | Pasang OrangeFox lewat PC (FASTBOOT) |
| `2-KEMBALIKAN-STOK.bat` | Kembali ke stok, tanpa recovery kustom |
| `3-KEMBALI-KE-TWRP.bat` | Pasang lagi TWRP versi terbaru lewat PC (FASTBOOT) |
| `OrangeFox-…img` · `TWRP-…img` · `STOK-…img` | Ketiga image di atas, dicek sha256 oleh `.bat` |
| `PANDUAN-ORANGEFOX.html` | Panduan lengkap langkah demi langkah, bisa dibuka offline dan di-print |
| `BACA-SAYA.txt` | Ringkasan cara pakai + SHA256 |

---

## Pasang OrangeFox

### Dari TWRP (tanpa PC — paling mudah)

1. Salin **`PAKET-OrangeFox-rothko-<versi>.zip`** ke HP. **Tidak perlu diekstrak.**
2. [Masuk TWRP](../masuk-twrp.md) → **Install** → pilih zip itu → geser.
3. Tunggu tulisan **Berhasil** → **Reboot → Recovery**.

Zip mengecek HP & file, menulis OrangeFox ke `vendor_boot`, lalu memeriksa ulang. Kalau tidak cocok, **tidak ada yang ditulis**.

### Lewat PC (FASTBOOT)

1. Ekstrak paket ke folder **platform-tools**.
2. Matikan HP → tahan **Power + Volume Bawah** sampai **FASTBOOT** → sambungkan kabel.
3. Klik dua kali **`1-PASANG-ORANGEFOX.bat`** → ikuti petunjuk.

### Pertama kali masuk

- Masuk OrangeFox sama seperti TWRP: dari HP mati, tahan **Power + Volume Atas**.
- OrangeFox meminta **pola** → masukkan pola layar kuncimu. Data, foto dan Download akan terbuka.
- Coba layar sentuh, lalu **Pilihan → Mulai ulang → System** untuk memastikan Android menyala normal.

## Update OrangeFox

Sama seperti memasang: flash zip paket versi baru di OrangeFox (**Berkas** → ketuk zip → **Pasang Zip**), atau `1-PASANG-ORANGEFOX.bat` dari PC.

## Kembali ke TWRP

| Dari | Cara |
|---|---|
| **OrangeFox** | **Berkas** → ketuk zip paket TWRP (`PAKET-TWRP-…zip`, v1.4+) → **Pasang Zip** → geser |
| **OrangeFox** (image) | **Berkas** → ketuk `TWRP-rothko-….img` → **Pasang Image** → pilih **`vendor_boot`** → geser |
| **PC** | HP di FASTBOOT → **`3-KEMBALI-KE-TWRP.bat`** |

> ⚠️ Di OrangeFox, **"Muat" artinya *Mount***, bukan Install. Memasang file selalu lewat **Berkas** (ketuk file-nya).

## Kembali ke stok (tanpa recovery kustom)

HP di FASTBOOT → **`2-KEMBALIKAN-STOK.bat`**. Atau di OrangeFox: **Berkas** → `STOK-vendor_boot-….img` → **Pasang Image** → **`vendor_boot`**.

## ⚠️ Penting

- File **`STOK-…`** menghapus recovery kustom. Jangan tertukar dengan `OrangeFox-…` atau `TWRP-…`.
- **Jangan reset pabrik** dari recovery — memicu FRP ([Reset & FRP](../reset-dan-frp.md)).
- HP terus masuk recovery dan tidak keluar? Tahan **Power + Volume Bawah** sampai FASTBOOT, lalu jalankan `.bat` dari PC.
- Data di HP **tidak dihapus** oleh semua cara di halaman ini.
