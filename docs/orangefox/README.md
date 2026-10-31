# 🦊 OrangeFox untuk Xiaomi 14T Pro

[← Kembali ke README](../../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](README.en.md)

OrangeFox adalah recovery turunan TWRP dengan tampilan baru dan fitur tambahan. Di repo ini OrangeFox dibangun dari **device tree yang sama** dengan TWRP, jadi perangkat keras, modul, dan dekripsinya sama-sama sudah teruji.

> TWRP dan OrangeFox **tinggal di tempat yang sama** (`vendor_boot`). Yang terpasang hanya salah satu, dan keduanya bisa saling menggantikan kapan saja.

---

## Status

| | |
|---|---|
| Basis | OrangeFox R12 (`fox_16.0`, Android 16) |
| Firmware | HyperOS OS3.0.301.0.WNNIDXM |
| Boot, layar sentuh | ✅ diuji owner di HP |
| Dekripsi data dengan **pola** | ✅ diuji owner di HP |
| Bahasa Indonesia | ✅ bawaan |
| Second Space (user 999) | ⚠️ sama seperti TWRP |

## TWRP atau OrangeFox?

| | TWRP | OrangeFox |
|---|---|---|
| Tampilan | klasik | modern, tema bisa diganti |
| File manager | dasar | lengkap (pilih banyak, zip/unzip, editor) |
| Modul KernelSU dari recovery | ❌ (lewat File Manager manual) | ✅ menu **Modul KernelSU** |
| Ukuran | lebih kecil | lebih besar, tetap muat |
| Stabilitas di HP ini | paling lama diuji | baru (v1.0) |

Ragu? Pakai **TWRP**. Mau fitur lebih? Coba **OrangeFox** — kembali ke TWRP hanya butuh satu langkah.

## Panduan

| | |
|---|---|
| 📘 **[Buku Manual Lengkap](buku-manual.md)** | Semua dalam satu buku: unduh, pasang, setiap menu, backup, root, pengaturan, masalah |
| 📥 **[Pasang & Kembali](pasang.md)** | Pasang OrangeFox, update, kembali ke TWRP atau stok |
| 🧭 **[Tur Menu OrangeFox](menu.md)** | Fungsi tiap menu, mana yang berbahaya |
| 🩺 **[Masalah & Log](masalah-dan-log.md)** | Kalau ada kendala |
| 📝 **[Catatan Rilis](../../CHANGELOG-orangefox.md)** | Yang baru dan diperbaiki tiap versi `ofox-…` |

Panduan TWRP yang juga berlaku untuk OrangeFox: [Masuk recovery](../masuk-twrp.md) · [Enkripsi & Pola](../enkripsi-dan-pola.md) · [Backup](../backup.md) · [Update HyperOS](../update-hos.md) · [Root & Kernel](../root-dan-kernel.md) · [Reset & FRP](../reset-dan-frp.md)

## Kredit

[OrangeFox Recovery Project](https://gitlab.com/OrangeFox) · TeamWin Recovery Project · tree asal [JonesqPacMan](https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp) · maintainer **Cogan17**. Lihat [Keaslian & Kredit](../keaslian-dan-kredit.md).
