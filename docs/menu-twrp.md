# 🧭 Tur Menu TWRP

[← Kembali ke README](../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](menu-twrp.en.md)

Penjelasan setiap menu TWRP di HP ini: **apa gunanya**, **kapan dipakai**, dan **mana yang berbahaya**. TWRP-mu berbahasa Indonesia, jadi label Indonesia ditulis lebih dulu, label Inggris di dalam kurung.

> Tanda: ✅ aman · ⚠️ hati-hati · ⛔ jangan, kecuali benar-benar paham akibatnya

---

## 📦 Install

| Fitur | Guna | |
|---|---|---|
| Pilih file **zip** → geser | Memasang zip: paket TWRP (v1.4+), kernel (AnyKernel3), modul flashable | ✅ |
| **Install Image** (kanan bawah) | Menulis file `.img` ke partisi. Pilihan hanya 5: `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta` | ⚠️ pilih partisi yang benar |

- Update TWRP: `TWRP-rothko-….img` → **`vendor_boot`**. Jangan ke `boot` atau `init_boot`.
- File **`STOK-…`** = menghapus TWRP (kembali ke stok). Jangan tertukar dengan file `TWRP-…`.
- Root/kernel: lihat [Root & Kernel](root-dan-kernel.md).

## 🧹 Format (Wipe)

| Fitur | Guna | |
|---|---|---|
| **Geser untuk reset pabrik** | Menghapus Data (kecuali penyimpanan internal) | ⛔ memicu **FRP** di Android 15/16 — lihat [Reset & FRP](reset-dan-frp.md) |
| **Format Data** | Menghapus **semua** Data **termasuk penyimpanan internal** (foto, Download, file backup TWRP) | ⛔ |
| **Hapus lainnya** (Advanced Wipe) | Pilih partisi satu per satu | ⚠️ |
| ↳ Dalvik / ART Cache | Membersihkan cache aplikasi; aman, Android membangunnya ulang | ✅ |
| ↳ **Perbaiki atau Ubah Sistem File** | **Perbaiki** = cek & betulkan sistem file (fsck). **Ubah** = format ulang | ✅ Perbaiki · ⛔ Ubah |

> Kalau Perbaiki gagal dengan *device or resource busy*: matikan MTP dulu (**Mount → Nonaktifkan MTP**).

## 💾 Cadangkan (Backup)

Mencadangkan partisi ke `TWRP/BACKUPS` di penyimpanan internal. Panduan lengkap: [Backup](backup.md).

- **Data** tidak berisi penyimpanan internal (foto/Download). Salin itu terpisah lewat MTP.
- Sebelum bereksperimen, cadangkan minimal **`boot`** dan **`init_boot`**.
- Salin folder backup ke PC — kalau HP rusak, backup di HP ikut hilang.

## ♻️ Pulihkan (Restore)

Mengembalikan backup. ⚠️ Restore **Data** hanya ke **versi HyperOS yang sama** dengan saat backup ([alasannya](update-hos.md)). Di v1.4 ke bawah, restore Data bisa gagal `extractTarFork() 255` — langkah daruratnya ada di [Backup → Restore Data](backup.md#restore-data); diperbaiki di v1.5.

## 🔌 Mount

| Fitur | Guna |
|---|---|
| Centang partisi | Memasang (mount) partisi agar isinya bisa dibaca |
| **Aktifkan / Nonaktifkan MTP** | Akses penyimpanan HP dari PC lewat kabel. Matikan saat Perbaiki sistem file |

## ⚙️ Pengaturan (Settings)

Bahasa, zona waktu, kecerahan, getar, dan opsi verifikasi zip. Aman diubah.

## 🛠️ Lainnya (Advanced)

| Fitur | Guna | |
|---|---|---|
| **File Manager** | Menyalin, memindah, menghapus file (termasuk di `/data` setelah dekripsi) | ⚠️ hati-hati menghapus |
| **Terminal** | Perintah shell langsung di HP | ⚠️ |
| **ADB Sideload** | Memasang zip dari PC: `adb sideload nama.zip` | ✅ |
| **Salin Log** | Menyalin `recovery.log` ke penyimpanan, untuk dikirim saat ada masalah | ✅ |

Menu *Flash Current TWRP* dan *Install Recovery Ramdisk* **sengaja dihapus** sejak v1.3, karena di HP ini keduanya menulis ke partisi yang salah.

## 🔄 Reboot

| Pilihan | Hasil | |
|---|---|---|
| **System** | Masuk Android | ✅ |
| **Recovery** | Masuk TWRP lagi | ✅ |
| **Bootloader** | Masuk mode FASTBOOT (untuk `.bat` dari PC) | ✅ |
| **Fastboot** (fastbootd) | Fastboot di userspace, untuk partisi dinamis | ⚠️ |
| **Matikan** | Mematikan HP | ✅ |
| **Slot A / B** | Mengganti slot aktif | ⛔ jangan diubah kecuali paham A/B |

> ⚠️ Kalau TWRP sedang bermasalah, jangan pakai *Reboot → Recovery* berulang — HP bisa terjebak loop. Jalan keluarnya FASTBOOT (Power + Volume Bawah). Lihat [Masuk TWRP](masuk-twrp.md).
