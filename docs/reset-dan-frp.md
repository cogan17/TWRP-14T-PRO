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

## Contoh nyata di HP ini (30 Okt 2026)

Urutan yang dialami owner, sampai FRP tertinggal:

1. Reset pabrik dari TWRP.
2. Boot ke Android, masuk layar penyiapan awal.
3. Saat diminta **akun Google**, penyiapan **ditinggalkan** (tidak login) dan HP langsung masuk TWRP.
4. **Pulihkan → Data** dari backup lama.
5. Android boot normal tanpa layar penyiapan awal — Data hasil restore berasal dari HP yang sudah selesai penyiapan. FRP tetap aktif dan tidak bisa dibersihkan lagi dengan cara biasa.

Pelajarannya: layar **akun Google** di penyiapan awal adalah satu-satunya kesempatan resmi untuk mematikan FRP. Begitu Data di-restore, layar itu tidak muncul lagi.

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

## Cara ampuh: flash ROM stok penuh

**Terbukti di HP owner (30 Okt 2026):** flash ROM fastboot resmi HyperOS menghilangkan FRP — pemasang aplikasi bawaan kembali normal.

1. **Pindahkan semua backup ke PC dulu.** Flash penuh menghapus seluruh data, termasuk folder backup TWRP di memori internal.
2. Pakai ROM **fastboot** resmi dengan **versi yang sama** seperti di HP (sekarang `OS3.0.301.0.WNNIDXM`) — image TWRP/OrangeFox di Releases dibuat untuk versi itu.
3. Di Mi Flash pilih **`clean all`**. ⛔ **Jangan `clean all and lock`** — bootloader terkunci lagi dan TWRP tidak bisa dipasang sampai unlock ulang.
4. Di layar penyiapan awal, **masuk akun Google-mu sendiri** (yang terakhir dipakai di HP ini). Jangan dilewati.
5. HP sekarang stok total: TWRP, kernel dan root hilang. Pasang lagi TWRP lewat `1-PASANG-TWRP.bat` dari [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases), lalu kernel dan root seperti biasa.

## Yang tidak berhasil

- ❌ Menunggu tidak membuatnya hilang — Android menyalakannya lagi setiap boot.
- ❌ Logout lalu login Gmail di Setelan tidak cukup — tandanya diatur oleh penyiapan awal, bukan oleh akun.
- ❌ Update HyperOS (OTA) tidak menghapusnya.
- ⛔ **Jangan pakai "FRP unlock tool" pihak ketiga** — itu alat yang sama untuk membuka HP curian, banyak yang berisi malware, dan untuk HP-mu tidak diperlukan.
- ⛔ Jangan mengutak-atik partisi `frp`.

## Cara mencegahnya

1. Reset pabrik **hanya dari Setelan HyperOS**.
2. Terlanjur reset dari TWRP dan sedang di layar penyiapan? **Jangan tinggalkan layar akun Google untuk restore Data.** Selesaikan penyiapan dengan **akun Google yang sama** — itu cara resmi mematikan FRP. Catatan: di HP ini belum diuji apakah FRP tetap mati kalau sesudahnya Data di-restore.
3. Mau restore Data? **Jangan reset pabrik dulu.** **Pulihkan → Data** sudah mengosongkan Data sendiri sebelum restore, jadi reset terpisah tidak perlu. Lihat [Backup](backup.md).
4. Setelah restore Data, cek modul root (mis. NoMount) — kadang perlu dipasang ulang. Lihat [Root & Kernel](root-dan-kernel.md).
