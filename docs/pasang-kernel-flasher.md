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
   Untuk v1.7 hasilnya harus `52bb80208b91f71f27fdc46ce30cfa9d1a4f4c6d72a46feacc186397877bd826`. Versi lain: lihat SHA256 di catatan rilisnya.
3. Buka **Kernel Flasher**. Di kartu **Device**, *Slot Suffix* menunjukkan slot aktif (`_a` atau `_b`). Ketuk **View** di kartu slot yang bertanda **[Active]** (mis. *Slot A [Active]*).
4. Ketuk **Flash**, lalu **Flash Partition Image**. **Jangan** pilih **Flash AK3 Zip**, **Flash AK3 Zip using mkbootfs** atau **Flash KernelSU LKM Driver** — ketiganya untuk kernel dan root, bukan recovery.
5. Di daftar partisi, ketuk **vendor_boot**, pilih file image, lalu tunggu sampai muncul **Done**. **Jangan** pilih `boot`, `init_boot` atau partisi lain. Tombol **Reboot** di layar itu belum perlu ditekan.
6. Cek isi partisi (hanya membaca, aman):
   ```
   su -c 'n=$(wc -c < /sdcard/Download/TWRP-rothko-OS3.0.301.0.WNNIDXM.img); head -c $n /dev/block/by-name/vendor_boot_a | sha256sum'
   ```
   Hasilnya harus sama dengan langkah 2. Kalau slot aktif **B**, ganti `vendor_boot_a` dengan `vendor_boot_b`.
7. Masuk recovery: HP **mati**, tahan **Volume Atas + Power**, lepas Power saat logo muncul, lalu tahan Volume Atas.
8. Buka pola layar kunci **sekali saja**. Jangan tekan **Wipe**, **Format** atau **Reset**.
9. **Reboot → System**.

## OrangeFox

Langkahnya sama, dengan file `OrangeFox-rothko-OS3.0.301.0.WNNIDXM.img` dan folder backup `Fox/BACKUPS`. Untuk ofox-v1.1, hash di langkah 2 dan 6 harus `b6cbe63a19021b5f26a4ba089266b367ddeb6e604720c2720a4a1ade61e327f5`.

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
