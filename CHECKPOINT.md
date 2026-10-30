# Checkpoint — 30 Okt 2026 (WIB)

Sesi berikutnya: baca `CLAUDE.md` dan file ini, lalu lanjut **hanya setelah owner meminta**. Jangan otomatis mem-flash, menguji HP, atau menerbitkan rilis.

## Status sekarang

**Tidak ada yang berjalan.** TWRP dan OrangeFox sama-sama punya rilis resmi terbaru dan bisa saling menggantikan.

| | Versi terbaru | |
|---|---|---|
| TWRP | **v1.5** | restore Data Android 16 diperbaiki, backup tanpa duplikat |
| OrangeFox | **ofox-v1.0** | rilis pertama; diuji owner di HP (boot, sentuh, dekripsi pola) |

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
- **KSUN vs BakaSU setelah restore**: restore Data mengembalikan aplikasi sesuai tanggal backup (KSUN kembali, BakaSU — dipasang setelah backup — hilang). Root di kernel (`boot`), bukan `init_boot`; manager harus cocok dengan varian kernel yang terpasang. Dicatat di [Root & Kernel](docs/root-dan-kernel.md).

## Belum terbukti / pertanyaan terbuka

- Owner belum konfirmasi apakah saat penyiapan awal (setelah reset pabrik dari TWRP, sebelum restore Data) sempat **login akun Google** atau melewatinya. Ini menentukan apakah perlu peringatan tambahan di [Reset & FRP](docs/reset-dan-frp.md) soal restore Data setelah sempat boot ke Android pasca-reset. **Jangan tambahkan peringatan itu sampai owner menjawab** — jangan menebak penyebabnya.
- `docs/pedoman` (branch lama, PR #28 ditutup tanpa merge) belum dihapus — aman dihapus manual kapan saja, tapi workflow sengaja tidak menyentuhnya.

## Langkah pertama berikutnya

Tidak ada pekerjaan yang menggantung. Tunggu permintaan owner berikutnya (mis. uji OrangeFox lebih jauh, jawaban soal login Google saat reset, atau topik baru).
