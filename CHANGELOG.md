# 📝 Catatan Rilis

[← Kembali ke README](README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](CHANGELOG.en.md)

Versi teratas = versi terbaru di [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases).

## v1.8 — 4 Nov 2026

### ✨ Baru
- **Untuk HyperOS OS3.0.302.0.WNNIDXM** (update 4 Nov 2026). Modul kernel (kernel `6.1.157`) dan blob keamanan diambil dari ROM resmi 302. Firmware ini terbukti sama dengan yang dipasang di HP owner: md5 paket yang diunduh HP cocok, dan sha256 `boot` di slot baru HP sama dengan hasil ekstraksi.
- **v1.7 tetap untuk OS3.0.301.0.WNNIDXM.** Jangan memasang v1.8 di 301, atau v1.7 di 302.

## v1.7 — 3 Nov 2026

### 🔧 Perbaikan
- Tulisan merah `E:String resource 'rothko_…' not found` saat TWRP dibuka sudah hilang. Teks peringatan kuning dari v1.6 kini juga ada di bahasa dasar (English) yang dimuat TWRP sebelum bahasa Indonesia. Isi dan letak peringatannya tidak berubah.

Diuji owner di HP (3 Nov 2026): di v1.6 peringatan kuning tampil di layar Pulihkan; di v1.7 tulisan merah saat TWRP dibuka sudah tidak muncul.

## v1.6 — 3 Nov 2026

### ✨ Baru
- **Peringatan kuning di layar Pulihkan:** geseran di layar ini **memulihkan** backup dan menimpa Data (foto dan Download tetap aman). Untuk menghapus backup, ketuk **Hapus Cadangan**.
- **Peringatan kuning saat menghapus backup:** geseran hanya menghapus backup itu; data di HP tidak berubah.
- Daftar partisi di layar Pulihkan sedikit lebih pendek supaya peringatan muat.

## v1.5 — 30 Okt 2026

### 🔧 Perbaikan
- **Restore Data di Android 16** tidak lagi gagal dengan `extractTarFork() ... 255` di folder `/data/user/0/…`. Sebelumnya wipe sebelum restore ikut menghapus `/data/data` yang sedang dipakai Android, sehingga data aplikasi tidak bisa dikembalikan.
- **Backup Data lebih kecil dan cepat**: data aplikasi tidak lagi tersimpan dua kali.

## v1.4 — 29 Okt 2026

### ✨ Baru
- **Zip paket bisa langsung di-flash di TWRP** (Install → zip → geser). Tak perlu ekstrak dan tak perlu memilih partisi. Zip mengecek HP & file, menulis TWRP ke `vendor_boot`, lalu memeriksa ulang. Kalau tidak cocok, tidak ada yang ditulis.

### 🔧 Perbaikan
- Tidak ada lagi *Invalid zip file format* saat zip paket dipasang di TWRP (sebelumnya zip harus diekstrak, dan file `TWRP-` mudah tertukar dengan `STOK-`).

## v1.3 — 29 Okt 2026

### 🔧 Perbaikan
- Menu yang salah sasaran dihapus: **Install Recovery Ramdisk** (pilihan ke-6 di Install Image), **Flash Current TWRP**, dan **reflash TWRP otomatis setelah flash ROM**. Di HP ini TWRP tinggal di `vendor_boot`, tapi menu-menu itu menulis ke `boot` — berisiko bootloop.
- Install Image kini benar-benar hanya 5 pilihan: `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta`.

## v1.2 — 21 Okt 2026

### ✨ Baru
- Menu **Install Image** ringkas seperti Kernel Flasher: hanya `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta`. Sebelumnya 33 partisi, banyak yang berbahaya kalau salah pilih.
- Label partisi dipendekkan (mis. `vendor_boot`), di Install Image dan Backup.

### 🔧 Perbaikan
- **Baterai selalu 100%** di TWRP — sekarang tampil persentase asli.

## v1.1 — 20 Okt 2026

### ✨ Baru
- **Update TWRP tanpa FASTBOOT**: dari PC dengan `5-UPDATE-LEWAT-TWRP.bat` (HP cukup di TWRP), atau langsung di HP lewat Install Image.
- Kembali ke stok tanpa PC (Install Image + file STOK).
- `TWRP-rothko-….img` dan `STOK-vendor_boot-….img` tersedia terpisah di Releases — tak perlu ekstrak zip di HP.
- **Bukti keaslian**: paket dan image ditandatangani digital; info build di `/BUILD-INFO.txt`.

## v1.0 — 20 Okt 2026

Rilis pertama, untuk HyperOS OS3.0.301.0.WNNIDXM (Android 16).

### ✨ Baru
- Boot ke recovery (vendor_boot dua fragmen, seperti stok).
- Layar sentuh.
- Buka data dengan **pola** (Gatekeeper); ikut otomatis kalau pola diganti. Second Space (999) dikenali.
- Backup / restore, fastbootd, MTP.
- Paket siap pakai dengan skrip `.bat`: pasang, kembali ke stok, ambil log.
