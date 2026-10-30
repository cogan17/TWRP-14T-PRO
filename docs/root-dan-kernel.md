# 🪄 Root & Kernel

[← Kembali ke README](../README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](root-dan-kernel.en.md)

Memasang kernel atau root lewat TWRP, dan cara pulih kalau ada yang salah. Kernel dengan root bawaan dan SUSFS untuk HP ini: [Cogan-Kernel](https://github.com/cogan17/Cogan-Kernel).

---

## Partisi mana untuk apa

| Partisi | Isi | Yang boleh ditulis |
|---|---|---|
| `boot` | Kernel | Kernel (zip AnyKernel3) atau `boot` stok |
| `init_boot` | Ramdisk awal; tempat root model *patch* (KernelSU LKM / Magisk) | `init_boot` hasil patch atau stok |
| `vendor_boot` | **TWRP** + modul vendor | Hanya `TWRP-…` atau `STOK-…` dari paket ini |

> ⛔ Jangan pernah menulis TWRP ke `boot` atau `init_boot`.

## Sebelum mulai: cadangkan

**Cadangkan** → centang **`boot`** dan **`init_boot`** → geser. Salin hasilnya ke PC. Dengan ini, kesalahan apa pun di kernel/root bisa dibatalkan dalam satu menit.

## Pasang kernel (zip AnyKernel3)

1. Salin zip kernel ke HP.
2. TWRP → **Install** → pilih zip → geser.
3. **Reboot → System**.

Zip AnyKernel3 hanya mengganti kernel di `boot`; ramdisk dan TWRP tidak tersentuh.

## Pasang root model patch (`init_boot`)

1. Patch `init_boot.img` stok dengan aplikasi root manager (KernelSU / Magisk) di Android.
2. Salin hasilnya ke HP.
3. TWRP → **Install** → **Install Image** → pilih file → **`init_boot`** → geser.

## Kalau kernel/root bermasalah (bootloop)

- **Cara tercepat:** TWRP → **Pulihkan** → pilih backup tadi → centang `boot` / `init_boot` → geser.
- **Tanpa backup:** **Install Image** file `boot`/`init_boot` **stok** dari ROM yang sama dengan HyperOS-mu.

## Modul membuat bootloop

1. Masuk TWRP, buka kunci dengan [pola](enkripsi-dan-pola.md).
2. **Lainnya → File Manager** → `/data/adb/modules/`.
3. Masuk ke folder modul yang dicurigai, buat file kosong bernama **`disable`** (atau hapus folder modulnya).
4. **Reboot → System**.

> OrangeFox punya menu **Modul KernelSU** untuk hal ini — lihat [panduan OrangeFox](orangefox/menu.md).

## Setelah restore Data

Status modul ikut dari backup dan kadang tidak cocok lagi. Kalau ada modul yang tidak bekerja seperti biasa (contoh: NoMount), **pasang ulang modulnya**. APK tidak bisa dipasang setelah reset pabrik dari TWRP? Itu FRP, bukan modul — lihat [Reset & FRP](reset-dan-frp.md).
