# Masukan dari sesi CoganSU — 9 Nov 2026 (WIB)

Ditulis oleh sesi CoganSU atas permintaan owner ("Kerjakan di sesi TWRP saja"). **Belum dikerjakan apa pun di repo ini**; sesi TWRP mulai dari sini, lalu lanjut hanya setelah owner meminta.

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

# Checkpoint — 5 Nov 2026 (WIB)

Sesi berikutnya: baca `CLAUDE.md` dan file ini, lalu lanjut **hanya setelah owner meminta**. Jangan otomatis mem-flash, menguji HP, atau menerbitkan rilis.

## Status sekarang

**Tidak ada yang berjalan.** HyperOS di HP owner sudah `OS3.0.302.0.WNNIDXM` (slot B, Cogan-Kernel r38, root aktif). Rilis dibuat per firmware:

| | 302 (terbaru) | 301 |
|---|---|---|
| TWRP | **v1.8** (diuji di HP) | v1.7 |
| OrangeFox | **ofox-v1.2** (diuji di HP) | ofox-v1.1 |

Repo bersih: 48 branch lama (sisa PR yang sudah di-merge) sudah dihapus lewat workflow sekali pakai; sekarang tersisa `twrp-14.1_a16`, `orangefox`, dan (opsional, boleh dihapus manual) `docs/pedoman`. Ruleset GitHub `lindungi-branch-utama` melindungi `twrp-14.1_a16` dan `orangefox` dari penghapusan/force-push. "Automatically delete head branches" sudah diaktifkan owner, jadi branch PR berikutnya terhapus otomatis setelah merge.

## Sudah selesai (sesi 29–30 Okt 2026)

- **v1.4**: zip paket bisa di-flash langsung di TWRP (diuji owner, berhasil).
- Perbaikan audit run 40891952288 (PR #65): gate library menolak symlink putus (+ self-test), jalur cepat Verify menolak penghapusan/chmod yang tak didukung, artifact paket diunggah sebelum publish, helper preloader `mtk_plpath_utils` diperbaiki.
- `CLAUDE.md` diambil dari Cogan-Kernel dan disesuaikan (PR #66).
- Paket uji OrangeFox lengkap dengan `.bat` pasang/kembali (PR #67).
- **Bug restore Data Android 16** (temuan owner, 30 Okt dini hari): wipe sebelum restore menghapus `/data/data` yang di-bind-mount vold ke `/data/user/0`, sehingga restore gagal `extractTarFork() 255`. Patch `patches/bootable_recovery/0006` (PR #68), terbit di **v1.5**. Langkah darurat (`adb shell umount /data/user/0`) ada di panduan Backup.
- Workflow tombol **Hapus log run lama** (PR #70): per workflow menyimpan `keep` run terbaru + sukses terakhir + `STOCK_RUN`; ada dry run; self-test `old_runs.py`.
- **Buku panduan lengkap, dua bahasa** (PR #72): TWRP — Tur Menu, Reset & FRP, Root & Kernel, Tanya-Jawab, langkah restore biasa di Backup. OrangeFox (`docs/orangefox/`) — Beranda, Pasang & Kembali, Tur Menu, Masalah & Log. Semua tautan/anchor dicek otomatis (0 masalah).
- **OrangeFox** (branch `orangefox`, `fox_16.0`): setelah 7 percobaan build (OOM, repo privat libvpx/libwebm, `repo manifest -r` gagal, dependensi `foxcli`), build #7 sukses. **Diuji owner di HP 30 Okt ±10.00 WIB: boot, sentuh, dekripsi pola berhasil** (log: Weaver gagal cepat → protector Gatekeeper → `User 0 Decrypted Successfully`). Perbaikan kunci: trim proyek + swap dari `.repo`, patch vold Weaver fail-fast/Gatekeeper fallback (`patches-ofox/`), lewati repo privat libvpx/libwebm, pin `foxcli` ke commit `288f557`, `repo manifest -r` dipindah sebelum pangkas (audit run 40951823094, PR tersendiri).
- **Rilis OrangeFox `ofox-v1.0`** (PR #75 + build + Verify): `OF_NO_REFLASH_CURRENT_ORANGEFOX := 1` menyembunyikan "Flash OrangeFox saat ini" dan reflash otomatis (repack magiskboot belum teruji dengan `vendor_boot` dua fragmen). `CHANGELOG-orangefox.md`/`.en.md`, tag `ofox-v1.0`, paket `PAKET-OrangeFox-rothko-….zip` (bisa di-flash, berisi `.bat` pasang/kembali ke TWRP/stok), attestation. **Terbit**, prerelease.
- **Workflow sekali pakai hapus branch** (PR #73, dihapus lagi PR #74): 44 branch lama dihapus, aturan ketat (hanya branch dengan PR merged yang masih menunjuk commit yang sama persis).
- Ruleset GitHub `lindungi-branch-utama` + "Automatically delete head branches" diaktifkan owner (lewat UI, bukan API — restrict deletions, block force pushes, target Default + `orangefox`).
- **FRP owner**: factory reset dari TWRP memicu FRP Android 15/16 (`secure_frp_mode` reset ke 1 tiap boot). Play Store, bank, MT Manager/App Manager, adb tetap normal; hanya pemasang bawaan yang diblokir. Owner memilih tidak mengutak-atik partisi `frp`; didokumentasikan di [Reset & FRP](docs/reset-dan-frp.md).
- **Jawaban owner soal penyiapan awal** (30 Okt 2026): setelah reset dari TWRP, owner sampai di layar akun Google, **tidak login**, langsung masuk TWRP lalu Restore Data. Urutan ini dan pelajarannya (layar akun Google = satu-satunya kesempatan resmi mematikan FRP; jangan ditinggalkan untuk restore) ditambahkan ke [Reset & FRP](docs/reset-dan-frp.md). Belum diuji: apakah FRP tetap mati bila login dulu lalu Data di-restore — ditulis jelas sebagai belum diuji.
- **KSUN vs BakaSU setelah restore**: restore Data mengembalikan aplikasi sesuai tanggal backup (KSUN kembali, BakaSU — dipasang setelah backup — hilang). Root di kernel (`boot`), bukan `init_boot`; manager harus cocok dengan varian kernel yang terpasang. Dicatat di [Root & Kernel](docs/root-dan-kernel.md).

- **FRP hilang lewat flash ROM stok penuh** (owner, 30 Okt 2026): pemasang aplikasi bawaan normal lagi. Ditambahkan ke [Reset & FRP](docs/reset-dan-frp.md) bagian "Cara ampuh". Setelah flash, HP stok total — TWRP/kernel/root perlu dipasang ulang.

- **Buku Manual OrangeFox lengkap** (31 Okt 2026): `docs/orangefox/buku-manual.md` + `.en.md` (20 bab), dan `PANDUAN-ORANGEFOX.html` di paket diperluas jadi buku manual (19 bagian). Nama menu diambil dari kode sumber OrangeFox `fox_16.0` (`gui/theme`, `id_ID.xml`) — label lama yang keliru diperbaiki ("Flash Image File" → **Pasang Image**, "Pasang ZIP" → **Pasang Zip**). HTML baru ikut paket pada rilis OrangeFox berikutnya.

- **Firmware 302** (4–5 Nov 2026): owner update 301 → 302 lewat Pembaruan tanpa kehilangan root (Kernel Flasher AK3 ke slot cadangan sebelum *Mulai ulang*; [panduan](docs/update-hos.md)). Bukti firmware: md5 paket di HP = md5 ROM CI, sha256 `boot_b` HP = `boot.img` ekstraksi, dan `STOK-vendor_boot` v1.8 (`0a441a7a…`) = `vendor_boot_b` HP. Extract stock run 41866003349 (PR #91, #92), build TWRP 41867830228, OrangeFox 41867920837.

## Belum terbukti / pertanyaan terbuka

- v1.8 dan ofox-v1.2 diuji owner 5 Nov 2026 (boot, dekripsi, Android normal); `/BUILD-INFO.txt` tidak sempat dicek.
- **HP sangat panas di recovery** (TWRP dan OrangeFox, laporan owner 5 Nov 2026). Belum diselidiki.
- Update lewat OTA inkremental dengan partisi termodifikasi belum diuji (yang diuji: ROM penuh).
- Issue #83: uji ulang reset pabrik dengan login Google dulu (pengingat, bukan kewajiban).
- `docs/pedoman` (branch lama, PR #28 ditutup tanpa merge) belum dihapus — aman dihapus manual kapan saja.

## Langkah pertama berikutnya

Tunggu owner. Kandidat berikutnya: selidiki panas di recovery (dengan bukti: suhu/frekuensi CPU dan log thermal dari recovery).
