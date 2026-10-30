# 🔁 Reset Pabrik & FRP

[← Kembali ke README](../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](reset-dan-frp.en.md)

> ⛔ **Jangan reset pabrik dari TWRP.** Kalau perlu reset, pakai **Setelan HyperOS → Tentang ponsel → Reset pabrik**.

---

## Apa itu FRP?

**FRP (Factory Reset Protection)** adalah perlindungan anti-maling di Android. Setelah reset yang **tidak** dilakukan lewat Setelan Android, Android menganggap HP mungkin dicuri dan membatasi fungsinya sampai pemiliknya terbukti — dengan **masuk akun Google yang sama** di layar penyiapan awal.

Di Android 15/16 (HyperOS 3), reset dari TWRP **termasuk** reset yang tidak dipercaya. Akibatnya FRP aktif, dan karena layar penyiapan awal sudah terlewat, tandanya tetap tertinggal.

## Gejalanya

- Memasang APK dengan cara biasa (ketuk dari file manager) gagal: **"Aplikasi tidak terinstal"**.
- Di log Android tertulis: `Can't install packages while in secure FRP`.
- Fungsi lain normal.

## Yang tetap berjalan normal

| Cara pasang aplikasi | Saat FRP aktif |
|---|---|
| **Play Store** (termasuk aplikasi bank) | ✅ normal |
| **MT Manager** / **App Manager** dengan root | ✅ berhasil |
| `adb install` / `pm install` dari PC | ✅ berhasil |
| Ketuk APK → pemasang bawaan HyperOS | ❌ diblokir |

Jadi HP tetap bisa dipakai sehari-hari. APK dari luar Play Store cukup dipasang lewat MT Manager atau App Manager.

## Cara resmi menghilangkannya

FRP hilang secara resmi saat HP melewati **layar penyiapan awal** dan kamu **masuk akun Google yang sama** seperti sebelum reset. Itu terjadi kalau suatu saat kamu reset **lewat Setelan HyperOS** (data terhapus — backup dulu).

- ❌ Menunggu tidak membuatnya hilang — Android menyalakannya lagi setiap boot.
- ❌ Logout lalu login Gmail di Setelan tidak cukup — tandanya diatur oleh penyiapan awal, bukan oleh akun.
- ❌ Update HyperOS (OTA) tidak menghapusnya.
- ⛔ **Jangan pakai "FRP unlock tool" pihak ketiga** — itu alat yang sama untuk membuka HP curian, banyak yang berisi malware, dan untuk HP-mu tidak diperlukan.
- ⛔ Jangan mengutak-atik partisi `frp`.

## Cara mencegahnya

1. Reset pabrik **hanya dari Setelan HyperOS**.
2. Mau restore Data? **Jangan reset pabrik dulu.** **Pulihkan → Data** sudah mengosongkan Data sendiri sebelum restore, jadi reset terpisah tidak perlu. Lihat [Backup](backup.md).
3. Setelah restore Data, cek modul root (mis. NoMount) — kadang perlu dipasang ulang. Lihat [Root & Kernel](root-dan-kernel.md).
