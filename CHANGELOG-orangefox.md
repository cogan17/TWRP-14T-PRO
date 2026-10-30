# 📝 Catatan Rilis — OrangeFox

[← Panduan OrangeFox](docs/orangefox/README.md) · <img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> [English](CHANGELOG-orangefox.en.md)

Versi teratas = versi terbaru di [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases) (tag `ofox-…`). Catatan rilis TWRP: [CHANGELOG.md](CHANGELOG.md).

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
