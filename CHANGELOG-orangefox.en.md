# 📝 Release Notes — OrangeFox

[← OrangeFox guide](docs/orangefox/README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](CHANGELOG-orangefox.md)

The top version = the latest one. All packages are shared on [Telegram](https://t.me/coganTWRP); GitHub is for announcements only. TWRP release notes: [CHANGELOG.en.md](CHANGELOG.en.md).

## ofox-v1.5 — 13 Nov 2026

### ✨ What's new
- The OrangeFox splash screen shows **Maintained by cogan17** under OrangeFox Recovery, also after the splash is changed in the settings.

### 🔧 What's fixed
- `BUILD-INFO.txt`: the run link is now labelled "Build" (it said "Build TWRP" although it is the OrangeFox run).
- For HyperOS OS3.0.302.0.WNNIDXM; `3-KEMBALI-KE-TWRP.bat` installs TWRP **v2.1**.

### ⚠️ Known issue
- **Do not back up Data in OrangeFox if the screen flickered.** The flicker means OrangeFox crashed and restarted itself. The trigger: the backup name is cleared with the ✕ button (or replaced by the automatic name) while the cursor is in the middle of the text, and you then type. After the restart OrangeFox no longer stores the folders' encryption keys in the Data backup, so that backup may not restore correctly. Use TWRP to back up and restore Data. To be fixed in ofox-v1.6.

Tested by the owner on the phone (14 Nov 2026, HyperOS 302): the TWRP and OrangeFox splash screens show *Maintained by cogan17*; the TWRP top bar has the clock on the left, the centre free and the battery on the right; the version shows under the title; a 31 GB Data backup in OrangeFox succeeded.

## ofox-v1.4 — 9 Nov 2026

### 🔧 What's fixed
- **Android no longer sees `ro.boot.selinux=permissive`.** Since v1.0 the TWRP/OrangeFox `vendor_boot` carried `androidboot.selinux=permissive` on its cmdline, and normal Android boots with that cmdline too. SELinux stayed *Enforcing*, but detector apps (e.g. Duck Detector) flagged it as dangerous. The cmdline is now identical to stock (`bootopt=64S3,32N2,64N2`), and the recovery turns permissive by itself without touching Android.
- The automatic checks now reject an image whose cmdline or bootconfig differs from stock.
- For HyperOS OS3.0.302.0.WNNIDXM; `3-KEMBALI-KE-TWRP.bat` installs TWRP **v2.0**.

Tested by the owner on the phone (9 Nov 2026, HyperOS 302): TWRP v2.0 and ofox-v1.4 boot, decrypt data with the pattern, and `getenforce` in the recovery Terminal shows *Permissive*. In Android, `/proc/bootconfig` no longer contains `selinux`, and Duck Detector (22:30 WIB) shows SELinux *Enforcing* and *System Properties* clean (Boot: Clean), no longer Danger.

## ofox-v1.3 — 7 Nov 2026

### 🔧 What's fixed
- **The phone no longer gets very hot during backup/restore.** Recovery has no chip temperature sensors or thermal throttling like Android, so the CPU ran at full speed up to 3.4 GHz. The mid and big cores are now capped at 2 GHz while in recovery. Tested by the owner on the phone with the same cap (7 Nov 2026, in an air-conditioned room): the phone stays only warm and backups take as long as before. Android is not affected.
- For HyperOS OS3.0.302.0.WNNIDXM; `3-KEMBALI-KE-TWRP.bat` installs TWRP **v1.8** (the latest TWRP release on GitHub).

## ofox-v1.2 — 4 Nov 2026

### ✨ What's new
- **For HyperOS OS3.0.302.0.WNNIDXM** — the same firmware as TWRP v1.8 (kernel `6.1.157` modules, security blobs from the official 302 ROM).
- `3-KEMBALI-KE-TWRP.bat` installs TWRP **v1.8**.
- **ofox-v1.1 stays for OS3.0.301.0.WNNIDXM.**

Tested by the owner on the phone (5 Nov 2026, HyperOS 302): TWRP v1.8 opens and decrypts data with the pattern; ofox-v1.2 was installed from TWRP through Install Image, OrangeFox opens and decrypts data; Android boots normally.

Known issue: the phone gets very hot while in recovery (TWRP and OrangeFox). Don't stay in recovery longer than needed and don't charge there; the cause is being investigated.

## ofox-v1.1 — 3 Nov 2026

### ✨ What's new
- **Yellow warning on a backup's page** (Backups → tap a backup): **Swipe to Restore** restores the backup and replaces Data (photos and Download stay safe). To delete it, tap the **trash icon** at the top right.
- **Yellow warning when deleting a backup:** the swipe deletes only that backup; the data on your phone is not changed.
- The warning follows OrangeFox's language (Indonesian or English).
- The package now includes **PANDUAN-ORANGEFOX.html** (offline manual, Indonesian), and `3-KEMBALI-KE-TWRP.bat` installs TWRP **v1.6**.

Tested by the owner on the phone (3 Nov 2026): both yellow warnings show and are readable, also with a dark theme and a custom font.

## ofox-v1.0 — 30 Oct 2026

The first OrangeFox release for rothko, firmware HyperOS OS3.0.301.0.WNNIDXM (Android 16).

### ✨ What's new
- **OrangeFox R12** (`fox_16.0`) from the same device tree as TWRP: boots, touchscreen, a two-part `vendor_boot` like stock.
- Unlock data with your **pattern** (Gatekeeper). The Weaver chip, which can't be used in recovery, is skipped quickly, so it no longer hangs at "Trying Decryption".
- Indonesian built in, a full file manager, a **KernelSU modules** menu.
- Restoring Data on Android 16 doesn't fail with `extractTarFork() … 255`.
- A full package: the zip can be flashed in TWRP/OrangeFox or used from a PC (`1-PASANG-ORANGEFOX.bat`, `2-KEMBALIKAN-STOK.bat`, `3-KEMBALI-KE-TWRP.bat`).

### 🔒 Hidden for safety
- **Flash current OrangeFox** and auto-reflash after flashing a ROM: they repack `vendor_boot` in a way not yet tested on this phone.

Tested by the owner on the phone (test build, 30 Oct 2026): boot, touchscreen, pattern decryption.
