# 🔄 Update HyperOS Tanpa Kehilangan Data

[← Kembali ke README](../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](update-hos.en.md)

Saat HyperOS keluar update, TWRP & root biasanya **ikut hilang**. Ini cara update yang **aman** — datamu tetap utuh, tanpa restore yang berisiko.

---

## ✅ Cara aman (disarankan)

Dengan cara ini datamu **terbawa sendiri**, jadi **tidak perlu restore `/data` manual** (dan tidak ada risiko bentrok):

1. **Backup dulu** — data, file pribadi, **dan** partisi `boot`/`init_boot`/`vendor_boot`. Lihat [Backup](backup.md). Ini jaring pengaman.
2. **[Kembali ke stok](kembali-ke-stok.md)** dulu (buang TWRP/root) — OTA *incremental* sering **gagal** kalau partisi masih termodifikasi. Kalau Pembaruan mengunduh **ROM penuh**, langkah ini tidak perlu dan root bisa dipertahankan: lihat [Update tanpa kehilangan root](#-update-tanpa-kehilangan-root-rom-penuh-diuji-di-hp).
3. **Ambil OTA dari Setelan → JANGAN wipe.** OTA **tidak** menghapus `/data`, jadi aplikasi & datamu tetap ada.
4. **Pasang TWRP + root lagi** (versi yang cocok dengan HOS baru).

> 💡 Intinya: biarkan OTA bawa datamu sendiri. Restore manual itu pilihan terakhir.

---

## 🔑 Update tanpa kehilangan root (ROM penuh, diuji di HP)

**Diuji owner di HP 4 Nov 2026:** update `OS3.0.301.0.WNNIDXM` → `OS3.0.302.0.WNNIDXM` lewat aplikasi Pembaruan, dengan TWRP dan Cogan-Kernel masih terpasang. HyperOS 302 menyala dengan Cogan-Kernel dan root tetap ada.

Kenapa bisa: HP ini memakai **slot A/B**. Pembaruan menulis sistem baru ke **slot cadangan**, dan HP baru pindah ke sana setelah **Mulai ulang**. Sebelum restart, kernel root bisa ditulis dulu ke slot cadangan itu.

**Syarat**
- Aplikasi Pembaruan mengunduh **ROM penuh**, dengan nama file `…ota_full…zip` di `Download/downloaded_rom`. ROM penuh tidak mengecek isi partisi lama, jadi TWRP dan kernel kustom tidak menghalanginya. OTA *incremental* (selisih) belum diuji dan kemungkinan gagal kalau partisi sudah diubah.
- HP sudah root, dengan aplikasi **Kernel Flasher** dan **Termux**.
- Zip Cogan-Kernel **varian yang sama** dengan yang terpasang (KernelSU Next atau BakaSU). Cogan-Kernel ACK 6.1.176 terbukti jalan di 302 (modul kernel 6.1.157).
- Ada PC untuk jalan darurat.

**Langkah**
1. **Backup** seperti biasa (lihat [Backup](backup.md)), salin ke PC.
2. Biarkan Pembaruan mengunduh. Selagi tertulis **Mengekstrak**, salin zip dari `Download/downloaded_rom` ke folder lain. Pembaruan menghapus zip itu setelah selesai, padahal isinya berguna sebagai cadangan stok.
3. Dari salinan zip itu, ambil `boot.img` stok versi baru dengan aplikasi payload dumper, lalu **simpan di PC**. Ini penyelamat kalau langkah 6 gagal.
4. Tunggu sampai muncul tombol **Mulai ulang sekarang**. **Jangan ditekan dulu.**
5. Catat kondisi awal (hanya membaca):
   ```sh
   su -c 's=$(getprop ro.boot.slot_suffix); o=$([ "$s" = _a ] && echo _b || echo _a); echo "aktif=$s cadangan=$o"; for p in boot$s boot$o vendor_boot$o; do echo "$p $(sha256sum /dev/block/by-name/$p | cut -c1-64)"; done'
   ```
6. **Kernel Flasher** → ketuk **View** di kartu slot **cadangan** (yang *tidak* bertanda *[Active]*) → **Flash** → **Flash AK3 Zip** → pilih zip Cogan-Kernel → tunggu **Done!**. Log AnyKernel3 harus menyebut `boot_b` (atau `boot_a`), yaitu slot cadangan. Jangan tekan **Reboot** di Kernel Flasher.
7. Jalankan lagi perintah langkah 5. Yang benar:
   - `boot` slot **aktif** tidak berubah;
   - `boot` slot **cadangan** **berubah**: kernel root sudah tertulis;
   - `vendor_boot` slot **cadangan** tidak berubah: modul stok versi baru utuh.

   Kalau ada yang tidak sesuai, **berhenti**, jangan restart.
8. Tekan **Mulai ulang sekarang**. Boot pertama lebih lama dari biasanya.

**Kalau macet di logo atau bootloop:** tahan Power ±15 detik → **Power + Volume Bawah** (FASTBOOT), lalu dari PC:
```
fastboot flash boot_b boot.img
fastboot reboot
```
(`boot_b` diganti `boot_a` kalau slot cadangan tadi A.) HP kembali ke stok versi baru tanpa root, dan data aman.

**Setelah update**
- **TWRP/OrangeFox hilang**, karena `vendor_boot` slot baru berisi stok. Pasang versi yang **sesuai firmware baru** (lihat judul rilis). Jangan memasang image versi lama.
- File `STOK-vendor_boot` dari paket lama juga **bukan stok lagi**. Pakai dari rilis yang sesuai firmware baru.

---

## ⚠️ Jangan restore backup `/data` lama ke HOS versi beda

Ini kesalahan yang paling sering bikin HP bermasalah. Restore full `/data` **hanya aman ke versi OS yang SAMA**.

Kenapa bentrok? Di `/data` ada **data sistem** (`/data/system`) yang menyimpan **kunci kunci-layar + enkripsi** (pola/PIN), terikat ke build HOS lama + chip keamanan. Kalau ditimpa ke HOS baru, gejalanya khas:

- 🔒 Pola/PIN **ditolak**, data **gagal didekripsi**.
- 💥 Settings / SystemUI **force close**, atau **bootloop**.

---

## Kalau tetap harus pindah data antar-versi

Jangan full `/data`. Pisahkan:

| Jenis | Cara | Aman? |
|---|---|---|
| **File pribadi** (foto, Download, dokumen) | salin biasa lewat MTP / File Manager | ✅ selalu aman |
| **Aplikasi + datanya** | pakai app backup: **Swift Backup** / **Neo Backup** | ✅ aman (tak sentuh data sistem) |
| **Full `/data` (.win)** | restore TWRP | ⛔ hanya ke versi OS yang sama |

---

## Jebakan yang sering bikin kaget

Backup **"Data"** di TWRP **secara default TIDAK termasuk foto/internal storage** (`/data/media`). Jadi kalau cuma backup "Data", **foto-fotomu belum ter-backup.** Centang juga internal storage, atau salin manual lewat MTP.

> **Aturan emas:** OTA tanpa wipe = data aman otomatis. Restore `/data` = cuma ke versi OS yang sama.
