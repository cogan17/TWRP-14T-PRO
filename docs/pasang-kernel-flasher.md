# 📱 Pasang lewat Kernel Flasher (tanpa PC)

[← Pasang TWRP](pasang.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](pasang-kernel-flasher.en.md)

> Cara ini hanya untuk HP yang **sudah root** dan bootloader-nya **sudah ter-unlock**. Belum root? Pakai cara PC atau zip di [Pasang TWRP](pasang.md).

---

## Status

| Recovery | Status |
|---|---|
| **TWRP v1.5** | ✅ diuji owner di HP (1 Nov 2026): partisi cocok dengan rilis, TWRP terbuka, Android normal, root (BakaSU) tetap aktif |
| **OrangeFox ofox-v1.0** | ✅ diuji owner di HP (1 Nov 2026): partisi cocok dengan rilis, OrangeFox terbuka dan membaca penyimpanan, Android normal, root tetap aktif |

---

## Yang disiapkan

- HP sudah root (KernelSU atau BakaSU).
- Firmware **OS3.0.301.0.WNNIDXM** (*Setelan → Tentang ponsel*). Image harus sama dengan versi HyperOS.
- Baterai minimal **50%**.
- Aplikasi **Kernel Flasher**.
- Image diunduh dari **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)**, bukan dari sumber lain.
- Salinan `STOK-vendor_boot-….img` di HP **dan** di PC.

---

## TWRP

1. **Backup dulu** ke PC: folder `TWRP/BACKUPS` dan `STOK-vendor_boot-….img`.
2. Cek sha256 image yang akan ditulis, lalu cocokkan dengan catatan rilis:
   ```
   sha256sum /sdcard/Download/TWRP-rothko-OS3.0.301.0.WNNIDXM.img
   ```
   Untuk v1.5 hasilnya harus `ff5f9f560d5bc696d95b7360ed1b80f80ee2b0eaaa5b78ad254264423b0fdaec`.
3. Buka **Kernel Flasher**. Slot aktif tampil di atas (mis. *Slot A [Active]*).
4. Tekan **vendor_boot**, pilih file image, lalu tulis. **Jangan** pilih `boot` atau `init_boot`.
5. Cek isi partisi (hanya membaca, aman):
   ```
   su -c 'n=$(wc -c < /sdcard/Download/TWRP-rothko-OS3.0.301.0.WNNIDXM.img); head -c $n /dev/block/by-name/vendor_boot_a | sha256sum'
   ```
   Hasilnya harus sama dengan langkah 2.
6. Masuk recovery: HP **mati**, tahan **Volume Atas + Power**, lepas Power saat logo muncul, lalu tahan Volume Atas.
7. Buka pola layar kunci **sekali saja**. Jangan tekan **Wipe**, **Format** atau **Reset**.
8. **Reboot → System**.

## OrangeFox

Langkahnya sama, dengan file `OrangeFox-rothko-OS3.0.301.0.WNNIDXM.img` dan folder backup `Fox/BACKUPS`. Untuk ofox-v1.0, hash di langkah 2 dan 5 harus `13e99fcd0315c352b620981fa6f74299933c924ee0a62d35b2031d12940c33a3`.

Di OrangeFox, jangan pakai **Flash OrangeFox saat ini**, **reflash otomatis**, atau **Fix recovery bootloop** (lihat [Tur Menu OrangeFox](orangefox/menu.md)).

---

## Kalau gagal

- **Android masih bisa boot:** buka Kernel Flasher, tekan **vendor_boot**, pilih `STOK-vendor_boot-….img`, tulis, lalu reboot.
- **Android tidak bisa boot, atau recovery tidak terbuka:** masuk FASTBOOT (HP mati, tahan **Power + Volume Bawah**) lalu jalankan `2-KEMBALIKAN-STOK.bat` dari PC. Lihat [Kembali ke stok](kembali-ke-stok.md). Ini satu-satunya jalan keluar kalau recovery tidak bisa dibuka.
- Jangan reboot berulang ke recovery yang rusak. Itu loop BCB dan tidak akan selesai sendiri.

## Catatan

- Cara ini hanya menulis `vendor_boot`. `boot` dan `init_boot` tidak disentuh, jadi root tetap di tempatnya.
- Setelah HyperOS di-update, **jangan tulis ulang image lama**. Tunggu rilis untuk versi baru, lihat [Update HyperOS](update-hos.md).
- Menulis partisi adalah keputusan pemilik HP.
