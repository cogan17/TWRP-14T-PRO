# 🩺 Masalah & Log — OrangeFox

[← Panduan OrangeFox](README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](masalah-dan-log.en.md)

Kalau ada kendala, **jangan menebak** — ambil log dan kirim.

---

## Mengambil log

| Cara | Langkah |
|---|---|
| **Di HP** | **Pilihan → Salin Log ke kartu SD**. File log tersimpan di penyimpanan internal (folder `Fox`). Lakukan **sebelum reboot** — log recovery hilang setelah HP menyala ulang. |
| **Lewat PC, OrangeFox masih jalan** | Jalankan **`3-AMBIL-LOG.bat`** dari paket TWRP, atau `adb pull /tmp/recovery.log` |
| **HP bootloop** | **`4-LOG-BOOTLOOP.bat`** dari paket TWRP — lihat [Masalah & Log TWRP](../masalah-dan-log.md#untuk-bootloop--penting-urutannya) |

## Masalah umum

| Gejala | Penyebab | Solusi |
|---|---|---|
| Macet di **"Trying Decryption"** | Paket uji OrangeFox sebelum 30 Okt menunggu chip Weaver selamanya | Pakai **ofox-v1.0** atau lebih baru |
| Pola ditolak | Pola salah / protektor | [Enkripsi & Pola](../enkripsi-dan-pola.md); jangan ulang berkali-kali |
| Tidak menemukan menu Install | Di OrangeFox, memasang lewat **Berkas** | Ketuk file → **Pasang ZIP** / **Flash Image File** |
| "Muat" tidak memasang apa-apa | "Muat" = **Mount**, bukan Install | Lihat [Tur Menu](menu.md) |
| HP terus masuk recovery | loop *boot-recovery* | Tahan **Power + Volume Bawah** → FASTBOOT → `.bat` dari PC |
| Second Space tidak terbuka | Kunci user 999 hilang setelah reset pabrik dari recovery | Tidak bisa dipulihkan |
| APK tidak bisa dipasang setelah reset pabrik | FRP | [Reset & FRP](../reset-dan-frp.md) |
| Restore Data gagal `extractTarFork() … 255` | Bug TWRP lama | ofox-v1.0 sudah membawa perbaikannya; darurat: [Backup → Restore Data](../backup.md#restore-data) |
| Ingin kembali ke TWRP | — | [Pasang & Kembali](pasang.md#kembali-ke-twrp) |

## Yang paling berguna dikirim

- Log dari **Salin Log ke kartu SD** atau `recovery.log` — untuk hampir semua masalah.
- `console-ramoops-0` — untuk bootloop.
- Foto layar saat error, dengan beberapa baris di atasnya.
