# 📝 Catatan Rilis — OrangeFox

[← Panduan OrangeFox](docs/orangefox/README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](CHANGELOG-orangefox.en.md)

Versi teratas = versi terbaru. Semua paket dibagikan lewat [Telegram](https://t.me/coganTWRP); GitHub hanya untuk pengumuman. Catatan rilis TWRP: [CHANGELOG.md](CHANGELOG.md).

## ofox-v1.3 — 7 Nov 2026

### 🔧 Perbaikan
- **HP tidak lagi sangat panas saat backup/restore.** Di recovery tidak ada sensor suhu chip dan rem panas seperti di Android, jadi CPU berjalan penuh sampai 3,4 GHz. Sekarang inti tengah dan besar dibatasi 2 GHz selama di recovery. Diuji owner di HP dengan batas yang sama (7 Nov 2026, di ruang ber-AC): HP hanya hangat, lama backup tidak berubah. Android tidak terpengaruh.
- Untuk HyperOS OS3.0.302.0.WNNIDXM; `3-KEMBALI-KE-TWRP.bat` memasang TWRP **v1.8** (rilis TWRP terbaru di GitHub).

## ofox-v1.2 — 4 Nov 2026

### ✨ Baru
- **Untuk HyperOS OS3.0.302.0.WNNIDXM** — firmware yang sama dengan TWRP v1.8 (modul kernel `6.1.157`, blob keamanan dari ROM resmi 302).
- `3-KEMBALI-KE-TWRP.bat` memasang TWRP **v1.8**.
- **ofox-v1.1 tetap untuk OS3.0.301.0.WNNIDXM.**

Diuji owner di HP (5 Nov 2026, HyperOS 302): TWRP v1.8 terbuka dan membuka data dengan pola; dari TWRP, ofox-v1.2 dipasang lewat Instal Image, OrangeFox terbuka dan membuka data; Android menyala normal.

Diketahui: HP terasa sangat panas selama berada di recovery (TWRP maupun OrangeFox). Jangan berlama-lama di recovery dan jangan mengisi daya di sana; penyebabnya sedang diselidiki.

## ofox-v1.1 — 3 Nov 2026

### ✨ Baru
- **Peringatan kuning di halaman backup** (Cadangkan → ketuk backup): **Geser untuk Mengembalikan** memulihkan backup dan menimpa Data (foto dan Download tetap aman). Untuk menghapus, ketuk **ikon tempat sampah** di kanan atas.
- **Peringatan kuning saat menghapus backup:** geseran hanya menghapus backup itu; data di HP tidak berubah.
- Teks peringatan mengikuti bahasa OrangeFox (Indonesia atau English).
- Paket kini berisi **PANDUAN-ORANGEFOX.html** (buku manual offline), dan `3-KEMBALI-KE-TWRP.bat` memasang TWRP **v1.6**.

Diuji owner di HP (3 Nov 2026): kedua peringatan kuning tampil dan terbaca, juga dengan tema gelap dan font kustom.

## ofox-v1.0 — 30 Okt 2026

Rilis pertama OrangeFox untuk rothko, firmware HyperOS OS3.0.301.0.WNNIDXM (Android 16).

### ✨ Baru
- **OrangeFox R12** (`fox_16.0`) dari device tree yang sama dengan TWRP: boot, layar sentuh, `vendor_boot` dua bagian seperti stok.
- Buka data dengan **pola** (Gatekeeper). Chip Weaver yang tidak bisa dipakai di recovery dilewati dengan cepat, jadi tidak macet di "Trying Decryption".
- Bahasa Indonesia bawaan, file manager lengkap, menu **Modul KernelSU**.
- Restore Data di Android 16 tidak gagal `extractTarFork() … 255`.
- Paket lengkap: zip bisa di-flash di TWRP/OrangeFox atau dipakai lewat PC (`1-PASANG-ORANGEFOX.bat`, `2-KEMBALIKAN-STOK.bat`, `3-KEMBALI-KE-TWRP.bat`).

### 🔒 Disembunyikan demi keamanan
- **Flash OrangeFox saat ini** dan reflash otomatis setelah flash ROM: me-repack `vendor_boot` dengan cara yang belum teruji di HP ini.

Diuji owner di HP (build uji 30 Okt 2026): boot, layar sentuh, dekripsi pola.
