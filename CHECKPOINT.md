# Masukan dari sesi CoganSU — 9 Nov 2026 (WIB)

Ditulis oleh sesi CoganSU atas permintaan owner ("Kerjakan di sesi TWRP saja"). **Selesai** (9 Nov 2026): **v2.0 / ofox-v1.4** (PR #105; OrangeFox: manifest `fox_16.0` dikunci ke 31 Okt karena perubahan upstream 8 Nov menambah `external/util-linux` yang bentrok dengan `libblkid`). cmdline `vendor_boot` = stok `bootopt=64S3,32N2,64N2`, recovery permissive sendiri (patch `patches/system_core/0001`), gate Verify cmdline/bootconfig = stok. **Diuji owner di HP** (22.30 WIB): kedua recovery membuka data; Android `/proc/bootconfig` tanpa `selinux`, Duck Detector SELinux Enforcing, System Properties tidak lagi Danger. Paket diunduh owner (ARSIP 9 Nov) lalu semua artifact dihapus; perubahan berikutnya perlu Extract stock + build penuh. Bagian di bawah adalah catatan asal.

## Temuan: `vendor_boot` TWRP/OrangeFox membocorkan `androidboot.selinux=permissive` ke Android normal

- **Gejala** (Duck Detector, laporan 9 Nov 2026 16.44 WIB, HP dari boot 8 Nov ±17.49 WIB): *System Properties* **Danger** karena `ro.boot.selinux: permissive`. Laporan 6 Nov (sebelum `vendor_boot` TWRP/OrangeFox dipasang lagi) masih `enforcing`.
- **Bukti di HP** (owner, 9 Nov ±16.51 WIB, Android normal, bukan recovery):
  ```
  $ su -c 'cat /proc/bootconfig | grep -i selinux; getenforce'
  androidboot.selinux = "permissive"
  Enforcing
  ```
  SELinux yang berjalan tetap *Enforcing* (HyperOS `user` mengabaikan permintaan permissive), tetapi `ro.boot.selinux` ikut `permissive`. Ketidakcocokan itulah yang ditangkap pendeteksi.
- **Sumber**: `BoardConfig.mk:101`, sama di `twrp-14.1_a16` dan `orangefox`, sejak *Initial Release* (`7987908`):
  ```
  BOARD_VENDOR_CMDLINE := "bootopt=64S3,32N2,64N2 androidboot.selinux=permissive"
  ```
  Recovery rothko ada di `vendor_boot` (`BOARD_MOVE_RECOVERY_RESOURCES_TO_VENDOR_BOOT := true`), dan cmdline `vendor_boot` dipakai **juga saat Android boot biasa**, bukan hanya recovery.
- **Bukan dari CoganSU / Cogan Kernel**: keduanya tidak pernah menulis `androidboot.selinux` (dicek di kedua repo, 9 Nov).

## Yang perlu dikerjakan (setelah owner meminta)

1. Cocokkan dulu dengan cmdline `vendor_boot` **stok 302** (`extract-stock.yml` mencetak header `vendor_boot`, termasuk `cmdline`; atau `unpack_bootimg.py` pada `STOK-vendor_boot` v1.8). Dugaan: stok hanya `bootopt=64S3,32N2,64N2` tanpa `androidboot.selinux`. Pastikan dengan bukti, jangan menebak.
2. Hapus `androidboot.selinux=permissive` dari `BOARD_VENDOR_CMDLINE` di **kedua** branch, supaya Android normal kembali sama dengan stok.
3. Pastikan recovery tetap bisa bekerja tanpa parameter itu: periksa apakah TWRP/OrangeFox `fox_16.0` (build eng/userdebug) sudah permissive sendiri, atau perlu `setenforce 0` lewat `init.recovery.*.rc` yang hanya ada di ramdisk recovery. Uji di HP: TWRP dan OrangeFox boot, sentuh, dekripsi pola, mount Data, backup/restore kecil.
4. Uji Android normal sesudah flash: `cat /proc/bootconfig | grep -i selinux` harus kosong, `getprop ro.boot.selinux` kosong atau `enforcing`, `getenforce` = `Enforcing`, lalu Duck Detector *System Properties* tidak lagi Danger.
5. Rilis TWRP dan OrangeFox baru per firmware seperti biasa; catat di CHANGELOG bahwa versi lama membocorkan `ro.boot.selinux=permissive`.

Catatan: temuan *ADB Runtime* dan *Dangerous Apps* di laporan yang sama bukan urusan repo ini (adbd yang tetap jalan, dan SUSFS/HMA).

---

# Checkpoint — 9 Nov 2026 (WIB)

Sesi berikutnya: baca `CLAUDE.md` dan file ini, lalu lanjut **hanya setelah owner meminta**. Jangan otomatis mem-flash, menguji HP, atau membagikan paket.

## Status sekarang

- HP owner: HyperOS `OS3.0.302.0.WNNIDXM` (slot B), Cogan-Kernel r38, root aktif.
- Versi terbaru: **TWRP v2.0** (image sha256 `5f670024…`) dan **OrangeFox ofox-v1.4** (`dab7b88c…`), 302, diuji owner di HP 9 Nov: cmdline `vendor_boot` sama dengan stok, CPU dibatasi 2 GHz dari v1.9. Untuk 301: v1.7 / ofox-v1.1.
- **Distribusi lewat Telegram** (https://t.me/coganTWRP), bukan GitHub. Owner menghapus semua rilis, tag, artifact dan log run (7–8 Nov 2026); semua versi tersimpan di arsip `ARSIP-…` milik owner (7 Nov: sampai v1.9 / ofox-v1.3; 9 Nov: v2.0 / ofox-v1.4). Artifact dihapus lagi 9 Nov setelah diunduh. Di GitHub tersisa branch `twrp-14.1_a16` dan `orangefox` saja.
- Karena artifact ikut terhapus: versi berikutnya perlu **Extract stock blobs** lalu **Build TWRP** dan **Build OrangeFox** penuh (bukan jalur cepat).
- README punya ajakan saling menghargai di kotak CAUTION (PR #102).

## Riwayat singkat

- v1.0–v1.5 (20–30 Okt): boot, sentuh, dekripsi pola, backup/restore, zip bisa di-flash, perbaikan restore Data Android 16.
- v1.6–v1.7 (3 Nov): peringatan kuning di layar Pulihkan, hilangnya `E:String resource`.
- OrangeFox ofox-v1.0–v1.1 (30 Okt–3 Nov), buku manual OrangeFox (31 Okt).
- Firmware 302 (4–5 Nov): v1.8 / ofox-v1.2, diuji owner di HP; update HyperOS tanpa kehilangan root ([panduan](docs/update-hos.md)).
- Panas di recovery (5–7 Nov): tidak ada sensor suhu/rem panas di recovery; CPU dibatasi 2 GHz → v1.9 / ofox-v1.3.
- SELinux (9 Nov): `androidboot.selinux=permissive` bocor ke Android lewat cmdline `vendor_boot` → v2.0 / ofox-v1.4, diuji owner di HP.

## Belum terbukti / pertanyaan terbuka

- OrangeFox memakai manifest `fox_16.0` 31 Okt (dikunci di `build-ofox.yml`). Saat versi recovery OrangeFox yang dirombak sudah publik, buka kuncinya dan uji ulang.
- BUILD-INFO OrangeFox memberi label "Build TWRP" pada link run Build OrangeFox (`verify-image.yml` baris 126); rapikan di versi berikutnya.
- Update lewat OTA inkremental dengan partisi termodifikasi belum diuji (yang diuji: ROM penuh).
- Issue #83: uji ulang reset pabrik dengan login Google dulu (pengingat, bukan kewajiban).
- Beban sistem ±12 di recovery walau CPU menganggur (proses tertahan, belum diperiksa; kemungkinan tidak terkait panas).

## Langkah pertama berikutnya

Tidak ada pekerjaan yang tertunda. Owner membagikan v2.0 / ofox-v1.4 di Telegram. Tunggu permintaan owner berikutnya.
