# 🧭 Tur Menu OrangeFox

[← Panduan OrangeFox](README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](menu.en.md)

Penjelasan setiap menu OrangeFox di HP ini. Label Indonesia sesuai tampilan OrangeFox, label Inggris di dalam kurung.

> Tanda: ✅ aman · ⚠️ hati-hati · ⛔ jangan, kecuali benar-benar paham akibatnya

Di bawah layar ada 4 tab: **Berkas**, **Cadangkan**, **Bersihkan**, **Pilihan**.

---

## 📁 Berkas (Files)

File manager lengkap. **Semua pemasangan dimulai dari sini** — ketuk file-nya:

| File yang diketuk | Pilihan | |
|---|---|---|
| `.zip` | **Pasang Zip** → **Gesek untuk Menginstal** | ✅ paket TWRP/OrangeFox, kernel AnyKernel3 |
| `.img` | **Pasang Image** → pilih **Partisi** → geser | ⚠️ pilih yang benar: recovery → `vendor_boot`, kernel → `boot`, root patch → `init_boot` |
| file lain | salin, pindah, ganti nama, hapus, zip/unzip, lihat/edit teks | ⚠️ hati-hati menghapus |

File **`STOK-…`** menghapus recovery kustom — jangan tertukar dengan `OrangeFox-…`/`TWRP-…`.

## 💾 Cadangkan (Backups)

- **Cadangan Baru** → pilih partisi → geser. Sebelum bereksperimen, cadangkan minimal `boot` dan `init_boot`.
- **Pilih Penyimpanan** → simpan di penyimpanan internal atau USB OTG.
- Ketuk backup yang ada → **Pulihkan** (Restore).

Aturannya sama dengan TWRP: **Data** tidak berisi penyimpanan internal, restore Data hanya ke versi HyperOS yang sama, dan **jangan reset pabrik dulu** sebelum restore. Lihat [Backup](../backup.md).

## 🧹 Bersihkan (Wipe)

| Pilihan | | |
|---|---|---|
| Dalvik / ART Cache, Cache | membersihkan cache, Android membangunnya ulang | ✅ |
| Penyimpanan USB | mengosongkan flashdisk OTG | ⚠️ |
| Metadata | kunci enkripsi metadata | ⛔ data tidak bisa dibuka lagi |
| Data | sama dengan reset pabrik | ⛔ memicu **FRP** ([Reset & FRP](../reset-dan-frp.md)) |
| Penyimpanan Internal | foto, Download, file backup | ⛔ |
| Tab **Format Data** | menghapus semuanya | ⛔ |

## ☰ Pilihan (Menu)

### Main

| Menu | Guna | |
|---|---|---|
| **Muat** (Mount & MTP) | Memasang partisi, menyalakan/mematikan MTP. **Bukan** untuk memasang file | ✅ |
| **Partitions Management** | Info dan aksi tingkat lanjut per partisi | ⚠️ |
| **ADB & Sideload** | Memasang zip dari PC: `adb sideload nama.zip` | ✅ |
| **Mulai ulang** (Reboot) | System, Recovery, Bootloader (FASTBOOT), Power off | ✅ — jangan ganti **slot** |

### Additions

| Menu | Guna | |
|---|---|---|
| **Modul KernelSU** | Melihat, mematikan atau menghapus modul KernelSU — penyelamat saat modul membuat bootloop | ✅ |
| **Addon C++** | Addon bawaan OrangeFox | ⚠️ |
| **Manajer Aplikasi** (App Manager) | Melihat dan menghapus aplikasi terpasang | ⚠️ jangan hapus aplikasi sistem |
| **Salin Log ke kartu SD** (Copy Log to SD) | Menyimpan log ke penyimpanan, untuk dikirim saat ada masalah | ✅ |
| **Lainnya** (More) | Terminal, perbaiki konteks, dekripsi ulang, dan lain-lain | ⚠️ lihat di bawah |

### ⛔ Yang tidak boleh dipakai di HP ini

Di HP ini recovery tinggal di **`vendor_boot`** dengan susunan dua bagian seperti stok. Fitur OrangeFox yang **me-repack recovery** atau **menulis ke `boot`/`init_boot`** belum teruji dengan susunan itu dan bisa membuat recovery atau Android tidak bisa boot:

- **Flash OrangeFox saat ini** dan **reflash OrangeFox otomatis setelah flash ROM** — disembunyikan di ofox-v1.0.
- **Fix recovery bootloop**, **Inject OrangeFox** — kalau muncul, jangan dipakai.
- **Pasang Magisk / KernelSU dari recovery** (di *Lainnya*) — pasang root lewat [Root & Kernel](../root-dan-kernel.md) saja.
- **Instal Ramdisk** dan **Flash ke kedua slot** di halaman Pasang Image, **Beralih slot** di Mulai ulang.
- **Remove FRP** (Addon C++), **Nonaktifkan DM-Verity / Enkripsi Paksa** (Pengaturan → OTA & ROM).
- Menu OTA OrangeFox — untuk update HyperOS ikuti [Update HyperOS](../update-hos.md).

## ⚙️ Pengaturan (ikon roda gigi)

Tema, warna, bahasa, zona waktu, kecerahan, getar. Aman diubah.
