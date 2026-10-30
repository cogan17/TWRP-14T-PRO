# Checkpoint — 30 Okt 2026 (WIB)

Sesi berikutnya: baca `CLAUDE.md` dan file ini, lalu lanjut **hanya setelah owner meminta**. Jangan otomatis mem-flash, menguji HP, atau menerbitkan rilis di luar daftar "Tertunda" yang sudah disetujui owner.

## Sedang berjalan

- **Build TWRP v1.5** — [run 40991563409](https://github.com/cogan17/TWRP-14T-PRO/actions/runs/40991563409) (full build ±80 menit). Setelah sukses, *Verify* otomatis menerbitkan pre-release **v1.5** (CHANGELOG v1.5 sudah di `twrp-14.1_a16`, PR #69). Cek hasilnya; kalau gagal, investigasi dulu sebelum menjalankan ulang.

## Sudah selesai (sesi 29–30 Okt)

- **v1.4** terbit: zip paket bisa di-flash langsung di TWRP (diuji owner, berhasil).
- Perbaikan audit run 40891952288 (PR #65): gate library menolak symlink putus (+ self-test), jalur cepat menolak penghapusan/chmod, artifact paket diunggah sebelum publish, helper preloader.
- `CLAUDE.md` dari Cogan-Kernel (PR #66). Paket uji OrangeFox lengkap dengan `.bat` (PR #67).
- **Bug restore Data Android 16** (temuan owner): wipe menghapus `/data/data` yang di-bind-mount ke `/data/user/0` → `extractTarFork 255`. Patch `patches/bootable_recovery/0006` (PR #68), ikut di v1.5. Langkah darurat (`adb shell umount /data/user/0`) sudah di panduan Backup.
- Workflow tombol **Hapus log run lama** (PR #70): simpan `keep` run terbaru per workflow + sukses terakhir + `STOCK_RUN`; ada dry run; self-test `old_runs.py`.
- **OrangeFox** (branch `orangefox`): build #7 sukses ([run 40969099622](https://github.com/cogan17/TWRP-14T-PRO/actions/runs/40969099622)), Verify [40987179296](https://github.com/cogan17/TWRP-14T-PRO/actions/runs/40987179296) → artifact `PAKET-OFOX-UJI`. **Diuji owner di HP 30 Okt ±10.00 WIB: boot, sentuh, dekripsi pola berhasil** (log: Weaver gagal cepat → protector Gatekeeper → `User 0 Decrypted Successfully`). Perbaikan yang membuatnya jalan: trim proyek + swap dari `.repo`, patch vold Weaver fail-fast/Gatekeeper fallback (`patches-ofox/`), lewati repo privat libvpx/libwebm, pin `foxcli` ke `288f557`, `repo manifest -r` sebelum pangkas.
- HP owner: data kembali setelah restore; **FRP aktif** akibat reset pabrik dari TWRP (`secure_frp_mode` kembali 1 setiap boot). Play Store, bank, MT Manager/App Manager, adb normal; hanya pemasang bawaan yang diblokir. Owner memilih tidak mengutak-atik partisi `frp`.

## Tertunda (disetujui owner 30 Okt: "lakukan yg dibutuhkan", rilis ofox-v1.0 ya, hapus log = run Actions)

1. **Buku panduan** — branch `docs/buku-panduan` (commit 9b90186, belum merge): halaman TWRP selesai (Tur Menu, Reset & FRP, Root & Kernel, Tanya-Jawab, restore biasa di Backup, README). **Belum:** `docs/orangefox/` (README, pasang, menu, masalah-dan-log; ID+EN) — tautannya sudah ada di README/Tanya-Jawab/Root & Kernel, jadi merge setelah halaman ini dibuat.
2. **Rilis OrangeFox `ofox-v1.0`**, sesudah v1.5 terbit (jangan ubah Verify selagi build TWRP berjalan):
   - `orangefox`: `OF_NO_REFLASH_CURRENT_ORANGEFOX := 1` di BoardConfig (sembunyikan "Flash OrangeFox saat ini" + reflash otomatis; repack magiskboot belum teruji di vendor_boot dua fragmen).
   - `CHANGELOG-orangefox.md` / `.en.md` (`## v1.0`), tag `ofox-v1.0`.
   - Verify varian ofox: terbitkan pre-release bila versi teratas belum dirilis (kalau sudah, cukup artifact uji); nama file tanpa "UJI"; attestation; `release_notes.sh`/`tag_message.sh` menerima nama changelog.
3. **Koreksi ke owner:** di OrangeFox **"Muat" = Mount**, bukan Install. Memasang/flash: **Berkas** → ketuk file → **Pasang ZIP** / **Flash Image File** → pilih `vendor_boot`.
4. Perbarui `CLAUDE.md`: alur rilis OrangeFox, workflow hapus log, pelajaran FRP & restore.

## Langkah pertama berikutnya

Cek hasil build TWRP v1.5 (run 40991563409) dan rilis v1.5. Lalu buat `docs/orangefox/` di branch `docs/buku-panduan` dan merge lewat PR.
