# ❓ Tanya-Jawab

[← Kembali ke README](../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](tanya-jawab.en.md)

Pertanyaan yang sering muncul, dari pengalaman nyata di HP ini.

---

### Unduh dan pasang

**File mana yang diunduh?** Selalu dari **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)**, versi yang **sama dengan HyperOS-mu**. Jangan dari tab *Actions* — file *artifact* di sana untuk pengujian, bukan untuk dipasang.

**Bedanya `TWRP-…` dan `STOK-…`?** `TWRP-…` = memasang TWRP. `STOK-…` = **menghapus** TWRP, kembali ke bawaan Xiaomi. Keduanya ke `vendor_boot`, jadi jangan sampai tertukar.

**Zip paket ditolak: *Invalid zip file format*.** Zip v1.3 ke bawah memang hanya untuk PC. Sejak **v1.4** zip paket bisa langsung di-flash di TWRP. Pakai versi terbaru, atau **Install Image** dengan file `TWRP-…`.

**Bagaimana memastikan file-nya asli?** Lihat [Keaslian & Kredit](keaslian-dan-kredit.md).

### Masuk dan memakai TWRP

**Bagaimana masuk TWRP?** Dari HP mati, tahan **Power + Volume Atas**. Detail: [Masuk TWRP](masuk-twrp.md).

**HP terus masuk recovery dan tidak keluar.** Itu loop *boot-recovery*. Tahan **Power + Volume Bawah** sampai FASTBOOT, lalu jalankan `1-PASANG-TWRP.bat` atau `2-KEMBALIKAN-STOK.bat` dari PC.

**Pola ditolak / data tidak terbuka.** Lihat [Enkripsi & Pola](enkripsi-dan-pola.md). Jangan mengulang pola berkali-kali.

**Second Space (user 999) tidak bisa dibuka.** Kalau sebelumnya pernah reset pabrik dari TWRP, kunci Second Space ikut terhapus dan datanya tidak bisa dipulihkan.

**Baterai selalu 100%.** Sudah diperbaiki sejak **v1.2**.

**Menu mana yang berbahaya?** Lihat [Tur Menu TWRP](menu-twrp.md).

### Backup, restore, reset

**Restore Data gagal `extractTarFork() … 255`.** Bug di v1.4 ke bawah, diperbaiki di **v1.5**. Langkah darurat: [Backup → Restore Data](backup.md#restore-data).

**Setelah reset pabrik dari TWRP, APK tidak bisa dipasang.** Itu **FRP**. Play Store dan MT Manager tetap bisa. Penjelasan: [Reset & FRP](reset-dan-frp.md).

**Boleh restore backup Data ke HyperOS versi lain?** Tidak. Lihat [Update HyperOS](update-hos.md).

**Repair sistem file gagal *device or resource busy*.** Matikan MTP dulu: **Mount → Nonaktifkan MTP**.

### Update dan lainnya

**TWRP hilang setelah update HyperOS.** Wajar — update menimpa `vendor_boot`. Pasang lagi TWRP versi yang cocok. Lihat [Update HyperOS](update-hos.md).

**Bagaimana update TWRP?** Flash zip paket terbaru di TWRP, atau `5-UPDATE-LEWAT-TWRP.bat` dari PC. Lihat [Pasang / Update](pasang.md).

**Setelah restore, modul root aneh.** Pasang ulang modulnya. Lihat [Root & Kernel](root-dan-kernel.md).

**TWRP atau OrangeFox?** Keduanya untuk HP ini dan bisa saling menggantikan. Lihat [panduan OrangeFox](orangefox/README.md).
