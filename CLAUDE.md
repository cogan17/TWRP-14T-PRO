# Aturan untuk asisten AI di repo ini

Recovery untuk Xiaomi 14T Pro (`rothko`, HyperOS, Android 16) di `cogan17/TWRP-14T-PRO`. Tree asal dari [JonesqPacMan](https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp); kredit lengkap di [docs/keaslian-dan-kredit.md](docs/keaslian-dan-kredit.md). Cara kerja ini diambil dari [Cogan-Kernel/CLAUDE.md](https://github.com/cogan17/Cogan-Kernel/blob/main/CLAUDE.md) (owner, 29 Okt 2026).

## Tanpa atribusi AI

- Author dan committer memakai identitas owner: `git config user.name Cogan` dan `git config user.email 79615344+cogan17@users.noreply.github.com`.
- Pesan commit **tanpa** `Co-Authored-By: Claude …`, `Claude-Session: …` atau atribusi AI lain. Pesan commit dan PR dalam bahasa Indonesia.
- Deskripsi PR **tanpa** footer "Generated with Claude Code" atau tautan sesi. Tag rilis berupa annotated tag berisi catatan rilis, tanpa baris AI.
- Branch kerja memakai nama biasa: `feat/…`, `fix/…`, `docs/…`, `chore/…`. Perubahan masuk ke `twrp-14.1_a16` lewat PR (squash).

## Waktu

- Waktu untuk owner selalu ditulis dalam **WIB** (Jakarta, UTC+7), misalnya "17.29 WIB". Kalau sumbernya UTC (GitHub, log), ubah dulu ke WIB.

## Isi repo

- **`twrp-14.1_a16`** (default): TWRP 14.1, device tree, dokumen, paket rilis (`release/`), workflow. Firmware acuan ada di `.github/firmware.env`.
- **`orangefox`**: varian OrangeFox `fox_16.0` (eksperimen), memakai device tree yang sama ditambah `vendorsetup.sh` dan pengaturan `OF_*`. Setiap push ke branch ini memicu *Build OrangeFox* (±1,5 jam); perubahan yang bukan untuk build diberi `[skip ci]`. Hasilnya hanya artifact `PAKET-OFOX-UJI-…` (image, `.bat` pasang, kembali ke TWRP dan ke stok; zip-nya bisa di-flash di TWRP), belum dirilis.
- **Alur build**: *Build TWRP* (±80 menit, hanya lewat tombol atau saat `build-twrp.yml` berubah) → *Verify* (otomatis, ±3 menit) memecah image jadi dua fragmen seperti stok, menjalankan gate, lalu merilis. Perubahan yang hanya menyentuh `recovery/root` cukup lewat *Verify* manual (jalur cepat) dengan run build terakhir.
- **Dokumen dua bahasa**: semua yang terjangkau dari README punya versi Indonesia (utama) dan English (`*.en.md`), termasuk `arsip/`. Isi paket rilis (`.bat`, `BACA-SAYA.txt`, `PANDUAN-TWRP.html`) boleh hanya Indonesia.
- **Isi tiap bahasa harus sesuai bahasanya**: bagian English tidak boleh menyalin teks Indonesia, dan sebaliknya.
- **Rilis per versi**: versi diambil dari judul `## vX.Y` teratas di `CHANGELOG.md` dan `CHANGELOG.en.md` (harus sama). Setiap versi punya rilis dan tag sendiri, berisi "Baru" dan "Perbaikan", dan **tidak pernah dihapus atau ditimpa** (`replace` hanya dipakai bila owner memintanya). Rilis berisi zip paket (bisa di-flash di TWRP atau dipakai lewat PC), `TWRP-….img` dan `STOK-vendor_boot-….img`, dengan tanda tangan attestation.

## Pelajaran yang tetap berlaku

- **Image harus mengikuti struktur stok.** TWRP tinggal di `vendor_boot` dengan dua fragmen: platform (`lib/modules`, `first_stage_ramdisk`, harus **identik dengan stok** karena dipakai Android saat boot normal) dan `recovery`. Jangan menulis TWRP ke `boot` atau `init_boot`; menu yang melakukannya (repack tools) dimatikan sejak v1.3.
- **Diagnosa dengan bukti, bukan keyakinan.** Bandingkan artefak yang berhasil dengan yang rusak sebelum mengubah kode. Tulis jelas mana yang terukur lokal, mana yang sudah dibuktikan CI, dan mana yang sudah dibuktikan di HP.
- **Gate gagal, bukan lolos diam-diam.** Gate Verify (fragmen, ukuran, dtb, modul, fstab, library) menghentikan rilis. Jangan pernah mengubahnya jadi peringatan.
- **Jalur darurat tetap aman.** Tidak pernah wipe data. File `STOK-` dan `2-KEMBALIKAN-STOK.bat` selalu ikut paket ([kembali ke stok](docs/kembali-ke-stok.md)). Ingat loop BCB: `reboot recovery` ke recovery yang rusak terus berulang; jalan keluarnya FASTBOOT. Flash selalu keputusan owner.
- **Unduh hanya dari Releases.** Artifact Actions bertahan 90 hari dan bukan untuk pengguna; yang permanen hanya file rilis.
- **Instruksi yang bisa dibaca dua arah: tanya dulu.** Hal berisiko (flash, partisi, rilis) dibicarakan dulu, ringkas dan mudah dipahami orang awam.

## Hemat run workflow

- **Jangan boros Actions.** Jalankan workflow hanya bila sudah yakin hasilnya akan benar: kode sudah dicek lokal (tes, `bash -n`, parse YAML, uji dengan file asli bila bisa).
- **Gagal = investigasi dulu, bukan coba-coba.** Baca log, temukan penyebabnya, perbaiki sekali dengan benar, baru jalankan ulang. Jangan berputar-putar dengan run berulang.
- **Investigasi secukupnya.** Jangan terlalu lama; cari bukti yang menentukan, lalu putuskan.
- **Cepat bukan berarti teledor.** Kerjakan dengan bijaksana.

## Uji di HP

- Owner menguji di HP **hanya build yang akan dirilis**, atau build uji yang sudah disepakati (mis. OrangeFox tahap 1). Kompatibilitas lain dibuktikan di CI.
- Label "diuji di HP" hanya untuk build yang benar-benar diuji owner.

## Checkpoint

- Bila owner menulis **checkpoint**: hentikan semua pekerjaan saat itu juga, tanpa mengecek apa pun satu per satu.
- Simpan keadaan terakhir ke [`CHECKPOINT.md`](CHECKPOINT.md): apa yang sedang berjalan, apa yang sudah selesai, apa yang tertunda, dan langkah pertama berikutnya. Commit dan push ke `twrp-14.1_a16` lewat PR.
- Sesi berikutnya **mulai dari `CHECKPOINT.md`**, lalu lanjut hanya setelah owner meminta.
