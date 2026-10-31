# 📘 Buku Manual OrangeFox — Xiaomi 14T Pro (rothko)

[← Panduan OrangeFox](README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](buku-manual.en.md)

Satu buku untuk semua hal tentang OrangeFox di HP ini: dari unduh sampai kembali ke stok. Baca dari atas kalau baru pertama kali; kalau sudah biasa, lompat lewat daftar isi.

> **Nama menu di buku ini** diambil dari kode sumber OrangeFox `fox_16.0` berbahasa Indonesia, jadi sama dengan yang tampil di layar. Beberapa label belum diterjemahkan OrangeFox dan tetap tampil dalam bahasa Inggris (mis. *Main*, *Additions*, *Partitions Management*) — buku ini menulisnya apa adanya.

**Tanda:** ✅ aman · ⚠️ hati-hati · ⛔ jangan dipakai di HP ini

---

## Daftar isi

1. [Kenalan dengan OrangeFox](#1-kenalan-dengan-orangefox)
2. [Persiapan](#2-persiapan)
3. [Unduh dan cek file](#3-unduh-dan-cek-file)
4. [Memasang OrangeFox](#4-memasang-orangefox)
5. [Masuk OrangeFox](#5-masuk-orangefox)
6. [Membuka data (pola)](#6-membuka-data-pola)
7. [Layar dan navigasi](#7-layar-dan-navigasi)
8. [Tab Berkas — file manager dan memasang file](#8-tab-berkas--file-manager-dan-memasang-file)
9. [Tab Cadangkan — backup dan restore](#9-tab-cadangkan--backup-dan-restore)
10. [Tab Bersihkan — wipe](#10-tab-bersihkan--wipe)
11. [Tab Pilihan — semua menu](#11-tab-pilihan--semua-menu)
12. [Modul KernelSU — mengatasi bootloop karena modul](#12-modul-kernelsu--mengatasi-bootloop-karena-modul)
13. [Kernel dan root](#13-kernel-dan-root)
14. [Pengaturan OrangeFox](#14-pengaturan-orangefox)
15. [Update HyperOS](#15-update-hyperos)
16. [Kembali ke TWRP atau stok](#16-kembali-ke-twrp-atau-stok)
17. [Reset pabrik dan FRP](#17-reset-pabrik-dan-frp)
18. [Masalah dan log](#18-masalah-dan-log)
19. [Daftar larangan](#19-daftar-larangan)
20. [Istilah](#20-istilah)

---

## 1. Kenalan dengan OrangeFox

OrangeFox adalah recovery turunan TWRP: tampilan modern, file manager lengkap, pengelola modul KernelSU, dan tema yang bisa diganti. Di repo ini OrangeFox dibangun dari **device tree yang sama** dengan TWRP, jadi layar sentuh, modul, dan dekripsinya sama.

| | |
|---|---|
| Basis | OrangeFox R12, `fox_16.0` (Android 16) |
| Firmware | HyperOS **OS3.0.301.0.WNNIDXM** |
| Tempat tinggal | partisi **`vendor_boot`**, sama seperti TWRP |
| Diuji owner di HP | boot, layar sentuh, dekripsi pola (ofox-v1.0) |

**Penting dipahami:**

- TWRP dan OrangeFox **tinggal di tempat yang sama**. Yang terpasang hanya satu; memasang yang satu otomatis menggantikan yang lain.
- `vendor_boot` di HP ini berisi dua bagian: bagian *platform* (modul dan berkas awal yang **juga dipakai Android saat boot normal**) dan bagian *recovery*. Karena itu image OrangeFox harus untuk versi HyperOS yang **sama persis**.
- Data, foto, dan aplikasi **tidak tersentuh** saat memasang, mengganti, atau melepas OrangeFox.

## 2. Persiapan

- [ ] Bootloader sudah **unlock**.
- [ ] Versi HyperOS (*Setelan → Tentang ponsel*) **sama** dengan versi di nama file paket.
- [ ] Baterai minimal **50%**.
- [ ] Data penting sudah dicadangkan (foto dan Download ke PC).
- [ ] **Tanpa PC:** TWRP atau OrangeFox sudah terpasang.
- [ ] **Lewat PC:** Windows, kabel USB yang bagus, folder **platform-tools** (berisi `adb.exe` dan `fastboot.exe`).

## 3. Unduh dan cek file

Unduh **hanya** dari **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)** → rilis bertanda **`ofox-v…`** (yang bertanda `v…` saja adalah TWRP). Jangan dari tab *Actions* — itu file uji yang hilang setelah 90 hari.

| File | Guna |
|---|---|
| **`PAKET-OrangeFox-rothko-<versi>.zip`** | Paket lengkap: bisa di-flash di recovery **atau** diekstrak untuk PC |
| `OrangeFox-rothko-<versi>.img` | Image OrangeFox saja |
| `STOK-vendor_boot-<versi>.img` | Bawaan Xiaomi — **menghapus** recovery kustom |

Isi paket: `1-PASANG-ORANGEFOX.bat`, `2-KEMBALIKAN-STOK.bat`, `3-KEMBALI-KE-TWRP.bat`, image OrangeFox, TWRP, dan STOK, `PANDUAN-ORANGEFOX.html` (panduan offline), `BACA-SAYA.txt` (berisi SHA256), dan `META-INF` (supaya zip bisa di-flash).

### Pastikan file utuh

Unduhan yang terputus menghasilkan zip rusak. ZArchiver menandainya dengan **"Kesalahan Data"**, dan image hasil ekstrak menjadi **lebih kecil dari 64 MB** — file seperti itu **jangan dipakai**.

**Cek di HP dengan Termux** (ganti folder sesuai tempat unduhan):

```sh
cd /sdcard/Download
ls -l PAKET-OrangeFox-*.zip
sha256sum PAKET-OrangeFox-*.zip
```

Ukuran dan SHA256 harus sama dengan yang tertulis di halaman rilis. Cara lain tanpa Termux: di OrangeFox, **Berkas** → tekan lama file → **Cheksum** → *Ketuk disini untuk menghitung*.

**Kalau mengekstrak:** ekstrak ke **folder baru** (ZArchiver: tekan lama zip → *Ekstrak ke ./nama-zip/*), lalu pastikan ketiga `.img` masing-masing **64,00 MB**. Zip yang terlihat di folder hasil ekstrak adalah zip sumbernya sendiri, bukan isi paket.

## 4. Memasang OrangeFox

### A. Dari TWRP (tanpa PC — paling mudah)

1. Salin **`PAKET-OrangeFox-rothko-<versi>.zip`** ke HP. **Tidak perlu diekstrak.**
2. [Masuk TWRP](../masuk-twrp.md) → **Install** → pilih zip → geser.
3. Tunggu tulisan **Berhasil** → **Reboot → Recovery**.

Zip mengecek bahwa HP-nya rothko dan file-nya utuh, menulis OrangeFox ke `vendor_boot`, lalu membaca ulang untuk memastikan. Kalau ada yang tidak cocok, **tidak ada yang ditulis**.

### B. Dari OrangeFox (update versi)

**Berkas** → ketuk zip paket versi baru → halaman **Pasang Zip** → **Gesek untuk Menginstal** → **Pilihan → Mulai ulang → Pemulihan**.

### C. Lewat PC (FASTBOOT)

1. Ekstrak paket ke folder **platform-tools**.
2. Matikan HP → tahan **Power + Volume Bawah** sampai muncul **FASTBOOT** → sambungkan kabel.
3. Klik dua kali **`1-PASANG-ORANGEFOX.bat`** → ikuti petunjuk sampai **BERHASIL**.

`.bat` mengecek SHA256 image sebelum menulis, dan hanya menulis ke `vendor_boot`.

### Setelah memasang

1. Masuk OrangeFox ([bab 5](#5-masuk-orangefox)), buka dengan pola ([bab 6](#6-membuka-data-pola)).
2. Coba layar sentuh dan buka **Berkas** — foto dan Download harus terlihat.
3. **Pilihan → Mulai ulang → Sistem** — pastikan Android menyala normal.

## 5. Masuk OrangeFox

### Dengan tombol (selalu bisa)

1. Matikan HP sampai benar-benar mati.
2. Tahan **Volume Atas + Power** bersamaan.
3. Saat logo Mi muncul, lepas **Power**, tahan terus **Volume Atas** sampai OrangeFox terbuka.

### Dari Android yang sudah root (Termux)

```sh
su -c 'reboot recovery'
```

> ⚠️ Pakai cara ini **hanya kalau OrangeFox yang terpasang sudah terbukti jalan**. `reboot recovery` meninggalkan tanda (*BCB*) di partisi `misc`; kalau recovery-nya rusak, HP akan terus kembali ke recovery yang rusak itu. Jalan keluarnya: tahan **Power ±15 detik** sampai mati → **Power + Volume Bawah** → FASTBOOT → `.bat` dari PC.

Keluar dari OrangeFox: **Pilihan → Mulai ulang → Sistem**.

## 6. Membuka data (pola)

Data HP terenkripsi. Saat OrangeFox terbuka, muncul **"Partisi Data dienkripsi"** dan permintaan pola.

- **Pengguna utama (0):** gambar **pola layar kunci** — **sekali, teliti**. Muncul *Mencoba Dekripsi*, lalu *Deskripsi sukses!*. Foto dan Download langsung terbuka.
- **Ruang Kedua / XSpace (999):** profil terpisah dengan sandinya sendiri. Kalau tidak dipakai, **tekan kembali** untuk melewati — data utama tetap terbuka.
- Sudah melewati permintaan pola dan ingin membuka nanti: **Pilihan → Lainnya → Dekripsi data** (atau **Dekripsi Pengguna** untuk user lain).

> ⚠️ **Pola gagal!** berulang kali bisa membuat kunci sementara. Jangan diulang terus — [ambil log](#18-masalah-dan-log).

Ganti pola di Android? OrangeFox otomatis memakai pola yang baru.

Di balik layar: HyperOS menyimpan kunci di chip **Weaver** yang tidak bisa dibaca recovery. OrangeFox di HP ini dipatch supaya cepat beralih ke pelindung **Gatekeeper** untuk pola yang sama — itulah yang membuat dekripsi tidak macet di *Mencoba Dekripsi* sejak ofox-v1.0. Detail: [Enkripsi & Pola](../enkripsi-dan-pola.md).

## 7. Layar dan navigasi

- **Bilah bawah: 4 tab** — **Berkas**, **Cadangkan**, **Bersihkan**, **Pilihan**.
- **Tombol navigasi** di paling bawah: kembali, beranda, dan menyembunyikan bilah. Tombol kembali juga membatalkan permintaan pola.
- **Ikon roda gigi** di pojok atas tab **Pilihan** = **Pengaturan** ([bab 14](#14-pengaturan-orangefox)).
- Semua tindakan berisiko meminta **geser** (*Gesek untuk Mengonfirmasi*) — selama belum digeser, belum ada yang terjadi.

## 8. Tab Berkas — file manager dan memasang file

Semua pemasangan **dimulai dari sini**. Di OrangeFox tidak ada menu "Install" terpisah — **ketuk file-nya**.

### Ketuk file

| File | Yang terbuka | Langkah |
|---|---|---|
| `.zip` | **Pasang Zip** | Cek **Opsi** (lihat di bawah) → **Gesek untuk Menginstal** |
| `.img` | **Pasang Image** | Di **Partisi**, pilih tujuannya → geser |
| teks (`.txt`, `.log`, `.sh`) | penampil teks | Untuk membaca saja |

**Partisi yang benar untuk `.img`:**

| File | Partisi |
|---|---|
| `OrangeFox-…img`, `TWRP-…img`, `STOK-vendor_boot-…img` | **`vendor_boot`** |
| kernel `boot.img` | `boot` |
| `init_boot` hasil patch root | `init_boot` |

> ⛔ Jangan pernah menulis recovery ke `boot` atau `init_boot`.
> ⛔ Di halaman **Pasang Image**, biarkan **Flash ke kedua slot** mati (bawaan) dan **jangan** tekan **Instal Ramdisk**.

**Opsi di halaman Pasang Zip:**

| Opsi | |
|---|---|
| **Tambahkan ke antrian** / **Lihat Antrian** | ✅ memasang beberapa zip berurutan (maks 10) |
| Mulai ulang setelah pemasangan selesai | ✅ boleh |
| Tanda Verifikasi ZIP | ✅ biarkan bawaan |
| Unmount Sistem / Vendor sebelum menginstal ZIP | ✅ biarkan bawaan |
| Flash Ulang OrangeFox setelah flashing ROM, Suntikkan OrangeFox setelah memasang, Nonaktifkan vbmeta AVB2.0, Tambah Magisk | ⛔ kalau muncul, biarkan **mati** |

### Tekan lama file atau folder

| Pilihan | |
|---|---|
| **Buka sebagai** → *File teks*, *ZIP yang dapat di-flash*, *Gambar yang dapat di-flash* | ✅ kalau OrangeFox tidak mengenali jenis file |
| **Salin**, **Pindah**, **Ubah Nama** | ✅ |
| **Hapus** | ⚠️ tidak bisa diurungkan |
| **Kompres** / **Buka paket arsip** | ✅ membuat atau membuka zip/tar |
| **Cheksum** | ✅ menghitung MD5/SHA — untuk mencocokkan SHA256 rilis |
| **Informasi** | ✅ ukuran, izin, tanggal |
| **Edit File di nano**, **Buka terminal disini** | ⚠️ untuk yang paham |
| **Atur Perizinan**, **Sembunyikan** | ⚠️ jangan ubah izin file sistem |

**Pilih banyak:** tekan lama satu file, ketuk file lain → **Urutan aksi** (*Salin*, *Pindah*, *Hapus*).
**Folder Favorit:** simpan folder yang sering dibuka (mis. `Download`, `Fox/BACKUPS`).

Lokasi penting: penyimpanan internal = `/sdcard` (sama dengan `/data/media/0`), backup OrangeFox = `Fox/BACKUPS`, log = `Fox/logs`.

## 9. Tab Cadangkan — backup dan restore

### Membuat backup

1. **Cadangkan** → **Cadangan Baru**.
2. **Nama**: biarkan *(Buat Otomatis)* atau ketik sendiri.
3. Centang **Partisi**. Paling penting: **`boot`**, **`init_boot`**, **`vendor_boot`**, dan **Data** kalau perlu.
4. Opsional: **Aktifkan Enkripsi** — hanya Data yang dienkripsi; **kata sandinya wajib diingat**, tanpa itu backup tidak bisa dipulihkan.
5. **Geser untuk mencadangkan** → tunggu **Pencadangan selesai**.

**Pilih Penyimpanan** menentukan tempat simpan (penyimpanan internal atau USB OTG). Hasilnya di `Fox/BACKUPS/<nomor-seri>/<nama>`. **Salin juga ke PC** — reset atau Format Data menghapus penyimpanan internal.

**Backup Cepat** memakai daftar partisi yang diatur di **Pengaturan → Cadangkan → Partisi cadangan cepat**.

### Memulihkan (restore)

1. **Cadangkan** → ketuk backup yang ada (urut menurut tanggal).
2. Di halaman **Kembalikan cadangan**, centang partisi yang mau dipulihkan → **Geser untuk Mengembalikan**.
3. Tunggu **Pemulihan selesai** → **Pilihan → Mulai ulang → Sistem**. Boot pertama setelah restore Data bisa lama.

Di halaman yang sama ada **Ganti nama cadangan** dan **Hapus cadangan**.

### Aturan backup Data

- Backup **Data** **tidak** berisi foto dan Download (penyimpanan internal). Salin itu ke PC terpisah.
- Restore Data **hanya ke versi HyperOS yang sama** dengan saat backup ([Update HyperOS](../update-hos.md)).
- **Jangan reset pabrik atau Bersihkan Data sebelum restore** — restore sudah mengosongkan Data sendiri. Reset dari recovery memicu FRP ([bab 17](#17-reset-pabrik-dan-frp)).
- Di Android 16, `/data/data` disambungkan ke `/data/user/0`. OrangeFox rilis ini memakai `OF_WORKAROUND_BACKUP_BUG`, jadi restore tidak gagal `extractTarFork() … 255` seperti TWRP lama.
- Setelah restore Data, aplikasi kembali seperti **tanggal backup**: aplikasi yang dipasang setelah backup hilang, dan modul root kadang perlu dipasang ulang ([Root & Kernel](../root-dan-kernel.md)).

## 10. Tab Bersihkan — wipe

| Pilihan | Akibat | |
|---|---|---|
| **Dalvik / ART Cache**, **Cache** | Cache dibuang, Android membangun ulang | ✅ |
| **Penyimpanan USB** | Mengosongkan flashdisk OTG | ⚠️ |
| **Data** | Sama dengan reset pabrik | ⛔ memicu FRP |
| **Metadata** | Kunci enkripsi hilang, data tidak bisa dibuka lagi | ⛔ |
| **Penyimpanan Internal** | Foto, Download, **file backup** terhapus | ⛔ |
| **Format Data** (minta ketik `yes`) | Semua aplikasi, foto, backup terhapus | ⛔ |

Tab **Bersihkan** langsung menampilkan daftar partisi bercentang dan tombol **Format Data** di atasnya. Cara membersihkan cache: centang **Dalvik / ART Cache** dan **Cache** saja → **Geser untuk Bersihkan**. Periksa ulang centangnya sebelum menggeser.

## 11. Tab Pilihan — semua menu

### Main

| Menu | Guna | |
|---|---|---|
| **Muat** (Mount & MTP) | Memasang/melepas partisi; **Aktifkan MTP** supaya HP terbaca di PC. **Bukan** untuk memasang file. | ✅ |
| **Partitions Management** → **Kelola Partisi** | Info tiap partisi, **Perbaiki FS**, **Ubah ukuran FS**, **Ganti FS** | ⚠️ hanya *Informasi partisi* yang aman untuk dicoba |
| **Partitions Management** → **Gabungkan Snapshot**, **Unmap Perangkat Super** | Untuk sisa update OTA yang belum selesai | ⚠️ hanya bila diminta saat troubleshooting |
| **ADB & Sideload** | Memasang zip dari PC: **Geser untuk Memulai Sideload**, lalu `adb sideload nama.zip` di PC | ✅ |
| **Mulai ulang** | **Sistem**, **Pemulihan**, **Bootloader**, **Fastboot**, **Matikan Perangkat** | ✅ — ⛔ **jangan Beralih slot** |

> **Perbaiki FS** gagal *device or resource busy*? Matikan MTP dulu di **Muat**.

### Additions

| Menu | Guna | |
|---|---|---|
| **Modul KernelSU** | Melihat, mematikan, menghapus modul ([bab 12](#12-modul-kernelsu--mengatasi-bootloop-karena-modul)) | ✅ |
| **Manajer Aplikasi** | Melihat dan menghapus aplikasi terpasang | ⚠️ jangan hapus aplikasi sistem |
| **Salin Log ke kartu SD** | Menyimpan log ke `Fox/logs` | ✅ |
| **Addon C++** (Fox Addons) | Lihat tabel di bawah | ⚠️ |
| **Lainnya** | Lihat tabel di bawah | ⚠️ |

**Addon C++:**

| Pilihan | |
|---|---|
| **Cadangkan Pengaturan OrangeFox**, **Setel ulang ke default** | ✅ hanya pengaturan OrangeFox |
| **Hapus kata sandi** | ✅ hanya kata sandi **OrangeFox** ([bab 14](#14-pengaturan-orangefox)), bukan pola HP |
| **Hapus semua skrip survival**, **Menghapus file OrangeFox** | ⚠️ tidak diperlukan di HP ini |
| **Remove FRP**, **Aktifkan dukungan init.d**, **Pasang** Magisk / KernelSU / KernelSU Next / SukiSU, AromaFM | ⛔ |

**Lainnya:**

| Pilihan | |
|---|---|
| **Dekripsi data**, **Dekripsi Pengguna** | ✅ membuka data kalau tadi dilewati |
| **Terminal** | ⚠️ baris perintah — hanya untuk perintah yang kamu pahami |
| **Perbaiki Konteks** | ⚠️ jarang diperlukan; OrangeFox sendiri memperingatkan bisa membuat HP tidak boot |
| **Suntikkan OrangeFox**, **Perbaiki Bootloop Pemulihan** | ⛔ |

## 12. Modul KernelSU — mengatasi bootloop karena modul

Android bootloop setelah memasang modul? Tidak perlu reset:

1. Masuk OrangeFox, buka dengan pola.
2. **Pilihan → Modul KernelSU** → tunggu daftar modul.
3. Ketuk modul yang dicurigai:
   - matikan **Aktif** — modul tidak dijalankan saat boot, atau
   - **Lewati mount** — modul jalan tanpa memasang file-filenya, atau
   - **Hapus modul mulai ulang selanjutnya** / **Hapus** — modul dibuang.
4. **Mulai ulang** → Android menyala tanpa modul itu.

Ragu modul yang mana? Matikan yang **terakhir dipasang**. Masih bootloop, matikan satu per satu. Tanpa menu ini (mis. di TWRP): **Berkas** → `/data/adb/modules/<modul>/` → buat file kosong bernama `disable`.

## 13. Kernel dan root

Sebelum apa pun: **Cadangkan** `boot` dan `init_boot` ([bab 9](#9-tab-cadangkan--backup-dan-restore)), salin ke PC.

| Tugas | Langkah |
|---|---|
| Pasang kernel (AnyKernel3 zip, mis. [Cogan-Kernel](https://github.com/cogan17/Cogan-Kernel)) | **Berkas** → ketuk zip → **Gesek untuk Menginstal** → **Mulai ulang → Sistem** |
| Pasang root hasil patch (`init_boot`) | Patch `init_boot.img` stok di aplikasi manager (KernelSU/Magisk) di Android → **Berkas** → ketuk hasilnya → **Pasang Image** → **`init_boot`** → geser |
| Kernel/root bermasalah | **Cadangkan** → backup tadi → **Kembalikan cadangan** → centang `boot`/`init_boot` → geser |
| Tanpa backup | **Pasang Image** `boot`/`init_boot` **stok** dari ROM yang sama dengan HyperOS-mu |

> ⛔ Jangan pakai **Pasang Magisk/KernelSU** dari menu OrangeFox — pasang root lewat aplikasi manager seperti di atas.
> Manager root harus cocok dengan varian kernel yang terpasang. Lengkapnya: [Root & Kernel](../root-dan-kernel.md).

## 14. Pengaturan OrangeFox

Buka lewat **ikon roda gigi** di tab **Pilihan**.

| Bagian | Isi | |
|---|---|---|
| **Umum** | Tampilkan file tersembunyi, Deteksi otomatis jenis file, **Mode pemulihan performa tinggi** (Performa tinggi / Seimbang / Hemat daya), Paksa pengisian cepat | ✅ |
| **Umum** — opsi flash ROM | Nonaktifkan vbmeta AVB2.0, Flash Ulang OrangeFox, Suntikkan OrangeFox | ⛔ biarkan mati |
| **OTA & ROM** | Dukungan OTA, Nonaktifkan DM-Verity, Nonaktifkan Enkripsi Paksa | ⛔ jangan diubah — untuk ROM kustom, bukan HyperOS stok |
| **Kustomisasi** | Tema (warna, aksen), font dan ukurannya, splash, bilah navigasi, status bar | ✅ |
| **Keamanan** | Mengunci OrangeFox dengan **Kode PIN**, **Setel kata sandi**, atau **Kunci gerakan** | ⚠️ tidak perlu di HP ini — lupa sandinya berarti terkunci dari recovery sendiri. Sudah terpasang? Lepas lewat **Addon C++ → Hapus kata sandi** |
| **Tampilan** | Kecerahan, batas waktu layar mati | ✅ |
| **Getaran** | Getaran tombol, papan ketik, aksi | ✅ |
| **Cadangkan** | Aktifkan Kompresi, Verifikasi Digest, Partisi cadangan cepat | ✅ |
| **Daerah** | **Zona Waktu** → *(UTC +7) Bangkok, Hanoi, Jakarta*, **Gunakan Format 24 jam**, **Bahasa** | ✅ |
| **Tentang** | Versi, perangkat, kredit | ✅ |

**Setel ulang ke default** hanya mengembalikan pengaturan OrangeFox — data HP tidak tersentuh.

## 15. Update HyperOS

Update HyperOS menimpa `vendor_boot`, jadi OrangeFox hilang setelah update — itu wajar.

1. **Backup** dulu (file pribadi ke PC, partisi `boot`/`init_boot`/`vendor_boot`).
2. [Kembali ke stok](#16-kembali-ke-twrp-atau-stok) — OTA sering gagal kalau partisi masih termodifikasi.
3. Update dari **Setelan** HyperOS. **Jangan wipe** — data ikut terbawa.
4. Pasang OrangeFox **versi yang cocok dengan HyperOS baru**. Belum ada di Releases? Tunggu, atau pakai stok dulu.

> ⛔ Jangan pakai menu OTA OrangeFox untuk HyperOS stok. Jangan restore Data dari versi HyperOS lama. Detail: [Update HyperOS](../update-hos.md).

## 16. Kembali ke TWRP atau stok

Semua cara di bawah **tidak menghapus data**.

| Tujuan | Di OrangeFox | Lewat PC (FASTBOOT) |
|---|---|---|
| **TWRP** | **Berkas** → zip `PAKET-TWRP-…zip` (v1.4+) → **Gesek untuk Menginstal**; atau `TWRP-rothko-….img` → **Pasang Image** → **`vendor_boot`** → geser | **`3-KEMBALI-KE-TWRP.bat`** |
| **Stok** (tanpa recovery kustom) | **Berkas** → `STOK-vendor_boot-….img` → **Pasang Image** → **`vendor_boot`** → geser → **Mulai ulang → Sistem** | **`2-KEMBALIKAN-STOK.bat`** |

Paket OrangeFox sudah membawa image TWRP rilis terbaru dan image STOK.

## 17. Reset pabrik dan FRP

> ⛔ **Jangan reset pabrik dari recovery** (Bersihkan Data, Format Data, Kembalikan ke pengaturan Pabrik). Kalau perlu reset, pakai **Setelan HyperOS → Tentang ponsel → Reset pabrik**.

Di Android 15/16, reset dari recovery dianggap tidak tepercaya. **FRP** aktif: APK tidak bisa dipasang lewat pemasang bawaan (*"Aplikasi tidak terinstal"*), sementara Play Store, MT Manager/App Manager dengan root, dan `adb install` tetap bisa.

- Terlanjur reset dan HP di layar penyiapan awal? **Masuk dengan akun Google yang sama** — jangan tinggalkan layar itu untuk restore Data.
- **Terbukti di HP owner (30 Okt 2026):** flash **ROM fastboot stok penuh** dengan Mi Flash **`clean all`** (bukan *clean all and lock*), lalu login akun Google sendiri saat penyiapan, menghilangkan FRP. Data terhapus — pindahkan backup ke PC dulu.
- ⛔ Jangan pakai **Remove FRP** di OrangeFox, "FRP unlock tool" pihak ketiga, atau mengutak-atik partisi `frp`.

Lengkapnya: [Reset & FRP](../reset-dan-frp.md).

## 18. Masalah dan log

### Mengambil log

| Situasi | Cara |
|---|---|
| OrangeFox jalan | **Pilihan → Salin Log ke kartu SD** → file ada di `Fox/logs`. Lakukan **sebelum reboot**. |
| OrangeFox jalan, ada PC | `3-AMBIL-LOG.bat` dari paket TWRP, atau `adb pull /tmp/recovery.log` |
| Dekripsi gagal | OrangeFox menyimpan `lastrecoverylog.log` di `Fox/logs` |
| Android bootloop | `4-LOG-BOOTLOOP.bat` dari paket TWRP ([Masalah & Log TWRP](../masalah-dan-log.md)) |

Kirim log **dan** foto layar saat error. Jangan menebak — log yang menunjukkan penyebabnya.

### Masalah umum

| Gejala | Solusi |
|---|---|
| Macet di **Mencoba Dekripsi** | Pakai **ofox-v1.0** atau lebih baru (paket uji sebelum 30 Okt menunggu Weaver selamanya) |
| **Pola gagal!** | Pastikan pola layar kunci yang sekarang; jangan diulang terus; kirim log |
| Tidak menemukan menu Install | Di OrangeFox, **ketuk file** di **Berkas** ([bab 8](#8-tab-berkas--file-manager-dan-memasang-file)) |
| "Muat" tidak memasang apa-apa | **Muat = Mount**, bukan Install |
| ZArchiver: **"Kesalahan Data"**, image < 64 MB | Unduhan rusak — unduh ulang, cek SHA256 ([bab 3](#3-unduh-dan-cek-file)) |
| HP terus masuk recovery | Tahan **Power ±15 detik** → **Power + Volume Bawah** → FASTBOOT → `.bat` dari PC |
| Android bootloop setelah modul | [Modul KernelSU](#12-modul-kernelsu--mengatasi-bootloop-karena-modul) |
| Android bootloop setelah kernel/root | Restore `boot`/`init_boot` ([bab 13](#13-kernel-dan-root)) |
| HP tidak terbaca di PC | **Pilihan → Muat → Aktifkan MTP**, atau ganti kabel |
| **Perbaiki FS** gagal *device or resource busy* | Matikan MTP dulu |
| APK tidak bisa dipasang setelah reset | FRP — [bab 17](#17-reset-pabrik-dan-frp) |
| Ruang Kedua (999) tidak terbuka setelah reset dari recovery | Kuncinya ikut terhapus — tidak bisa dipulihkan |
| OrangeFox hilang setelah update HyperOS | Wajar — [bab 15](#15-update-hyperos) |

## 19. Daftar larangan

Ringkasan semua yang ⛔ di HP ini — semuanya pernah atau bisa membuat HP tidak boot, data hilang, atau FRP:

- Reset pabrik, **Bersihkan Data**, **Metadata**, **Penyimpanan Internal**, **Format Data** dari recovery.
- Menulis recovery ke `boot` atau `init_boot`; **Instal Ramdisk**; **Flash ke kedua slot**; **Beralih slot**.
- **Flash OrangeFox saat ini**, **Flash Ulang OrangeFox setelah flashing ROM**, **Suntikkan OrangeFox**, **Perbaiki Bootloop Pemulihan** (me-repack recovery — belum teruji dengan `vendor_boot` dua bagian; sebagian sudah disembunyikan di rilis ini).
- **Pasang Magisk / KernelSU** dari recovery, **Nonaktifkan vbmeta AVB2.0**, **Nonaktifkan DM-Verity**, **Nonaktifkan Enkripsi Paksa**, **Aktifkan dukungan init.d**, menu **OTA**.
- **Remove FRP**, "FRP unlock tool", mengutak-atik partisi `frp`.
- File dari HP lain atau versi HyperOS lain; file dari tab *Actions*.

## 20. Istilah

| Istilah | Arti |
|---|---|
| **Recovery** | Sistem kecil terpisah untuk backup, restore, dan memasang file — TWRP atau OrangeFox |
| **`vendor_boot`** | Partisi tempat OrangeFox/TWRP tinggal, juga berisi modul untuk boot Android |
| **`boot`** / **`init_boot`** | Kernel / tempat root hasil patch |
| **FASTBOOT** | Mode bootloader (Power + Volume Bawah) untuk menulis partisi dari PC |
| **Flash** | Menulis file ke partisi |
| **Wipe** (Bersihkan) | Menghapus isi partisi |
| **Muat** (Mount) | Membuat partisi bisa dibaca/ditulis di recovery |
| **MTP** | Mode supaya PC bisa melihat penyimpanan HP |
| **Sideload** | Memasang zip dari PC lewat `adb sideload` |
| **Dekripsi** | Membuka data terenkripsi dengan pola |
| **Weaver / Gatekeeper** | Dua jalur penyimpan kunci pola; recovery memakai Gatekeeper |
| **BCB** | Tanda di partisi `misc` yang menyuruh HP masuk recovery |
| **FRP** | Perlindungan anti-maling setelah reset tidak tepercaya |
| **Slot A/B** | Dua salinan partisi; HP memakai salah satunya |
| **SHA256** | Sidik jari file untuk memastikan file utuh dan asli |

---

Kredit: [OrangeFox Recovery Project](https://gitlab.com/OrangeFox) · TeamWin Recovery Project · tree asal [JonesqPacMan](https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp) · maintainer **Cogan17**. Lihat [Keaslian & Kredit](../keaslian-dan-kredit.md).
