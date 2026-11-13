# 📝 Release Notes

[← Back to README](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](CHANGELOG.md)

The top version = the latest one. All packages are shared on [Telegram](https://t.me/coganTWRP); GitHub is for announcements only.

## v2.1 — 13 Nov 2026

### ✨ What's new
- The TWRP splash screen shows **Maintained by cogan17**.

### 🔧 What's fixed
- **The top bar is no longer cluttered.** Recovery has no CPU temperature, so TWRP put the long version (`3.7.1_14-Xiaomi_14T_Pro | Cogan17`) in the top bar, and the centred clock was drawn over it, right under the camera. It now looks like HyperOS: clock on the left, the centre left free for the camera, battery on the right. The version moved under the title on the main screen.
- The version line on the splash screen now fits the screen (it was cut off on both sides).
- For HyperOS OS3.0.302.0.WNNIDXM, with all fixes from v2.0.

Tested by the owner on the phone (14 Nov 2026, HyperOS 302): the TWRP and OrangeFox splash screens show *Maintained by cogan17*; the TWRP top bar has the clock on the left, the centre free and the battery on the right; the version shows under the title; a 31 GB Data backup in OrangeFox succeeded.

## v2.0 — 9 Nov 2026

### 🔧 What's fixed
- **Android no longer sees `ro.boot.selinux=permissive`.** Since v1.0 the TWRP/OrangeFox `vendor_boot` carried `androidboot.selinux=permissive` on its cmdline, and normal Android boots with that cmdline too. SELinux stayed *Enforcing*, but detector apps (e.g. Duck Detector) flagged it as dangerous. The cmdline is now identical to stock (`bootopt=64S3,32N2,64N2`), and the recovery turns permissive by itself without touching Android.
- The automatic checks now reject an image whose cmdline or bootconfig differs from stock.
- For HyperOS OS3.0.302.0.WNNIDXM, with the 2 GHz CPU cap from v1.9.

Tested by the owner on the phone (9 Nov 2026, HyperOS 302): TWRP v2.0 and ofox-v1.4 boot, decrypt data with the pattern, and `getenforce` in the recovery Terminal shows *Permissive*. In Android, `/proc/bootconfig` no longer contains `selinux`, and Duck Detector (22:30 WIB) shows SELinux *Enforcing* and *System Properties* clean (Boot: Clean), no longer Danger.

## v1.9 — 7 Nov 2026

### 🔧 What's fixed
- **The phone no longer gets very hot during backup/restore.** Recovery has no chip temperature sensors or thermal throttling like Android, so the CPU ran at full speed up to 3.4 GHz. The mid and big cores are now capped at 2 GHz while in recovery. Tested by the owner on the phone with the same cap (7 Nov 2026, in an air-conditioned room): the phone stays only warm and backups take as long as before. Android is not affected.
- For HyperOS OS3.0.302.0.WNNIDXM, like v1.8.

## v1.8 — 4 Nov 2026

### ✨ What's new
- **For HyperOS OS3.0.302.0.WNNIDXM** (the 4 Nov 2026 update). Kernel modules (kernel `6.1.157`) and security blobs come from the official 302 ROM. That firmware is proven identical to what the owner's phone installed: the md5 of the package the phone downloaded matches, and the sha256 of `boot` in the phone's new slot equals the extracted one.
- **v1.7 stays for OS3.0.301.0.WNNIDXM.** Don't install v1.8 on 301, or v1.7 on 302.

Tested by the owner on the phone (5 Nov 2026, HyperOS 302): TWRP v1.8 opens and decrypts data with the pattern; ofox-v1.2 was installed from TWRP through Install Image, OrangeFox opens and decrypts data; Android boots normally.

Known issue: the phone gets very hot while in recovery (TWRP and OrangeFox). Don't stay in recovery longer than needed and don't charge there; the cause is being investigated.

## v1.7 — 3 Nov 2026

### 🔧 What's fixed
- The red `E:String resource 'rothko_…' not found` lines when TWRP opens are gone. The yellow warning texts from v1.6 are now also in the base language (English), which TWRP loads before Indonesian. The warnings themselves look and sit the same.

Tested by the owner on the phone (3 Nov 2026): on v1.6 the yellow warning shows on the Restore screen; on v1.7 the red lines no longer appear when TWRP opens.

## v1.6 — 3 Nov 2026

### ✨ What's new
- **Yellow warning on the Restore screen:** the swipe on this screen **restores** the backup and replaces Data (photos and Download stay safe). To delete a backup, tap **Delete Backup**.
- **Yellow warning when deleting a backup:** the swipe deletes only that backup; the data on your phone is not changed.
- The partition list on the Restore screen is a little shorter so the warning fits.

## v1.5 — 30 Oct 2026

### 🔧 What's fixed
- **Restoring Data on Android 16** no longer fails with `extractTarFork() ... 255` in a `/data/user/0/…` folder. The wipe before a restore used to delete `/data/data`, which Android keeps in use, so app data could not be put back.
- **Smaller, faster Data backups**: app data is no longer stored twice.

## v1.4 — 29 Oct 2026

### ✨ What's new
- **The package zip can be flashed straight in TWRP** (Install → zip → swipe). No unzipping, no partition to choose. The zip checks the phone and the file, writes TWRP to `vendor_boot`, then reads it back. If anything doesn't match, nothing is written.

### 🔧 What's fixed
- No more *Invalid zip file format* when installing the package zip in TWRP (it used to need unzipping, and the `TWRP-` file was easy to mix up with `STOK-`).

## v1.3 — 29 Oct 2026

### 🔧 What's fixed
- Removed menus that wrote to the wrong partition: **Install Recovery Ramdisk** (the 6th choice in Install Image), **Flash Current TWRP**, and **auto-reflash TWRP after flashing a ROM**. On this phone TWRP lives in `vendor_boot`, but those menus write to `boot` — a bootloop risk.
- Install Image now really offers only 5 choices: `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta`.

## v1.2 — 21 Oct 2026

### ✨ What's new
- **Install Image** is short, like Kernel Flasher: only `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta`. It used to list 33 partitions, many of them dangerous to pick by mistake.
- Shorter partition labels (e.g. `vendor_boot`), in Install Image and Backup.

### 🔧 What's fixed
- **Battery always 100%** in TWRP — it now shows the real percentage.

## v1.1 — 20 Oct 2026

### ✨ What's new
- **Update TWRP without FASTBOOT**: from a PC with `5-UPDATE-LEWAT-TWRP.bat` (the phone just stays in TWRP), or right on the phone via Install Image.
- Back to stock without a PC (Install Image + the STOK file).
- `TWRP-rothko-….img` and `STOK-vendor_boot-….img` are available separately on Releases — no need to unzip on the phone.
- **Proof of authenticity**: the package and image are digitally signed; build info in `/BUILD-INFO.txt`.

## v1.0 — 20 Oct 2026

First release, for HyperOS OS3.0.301.0.WNNIDXM (Android 16).

### ✨ What's new
- Boots into recovery (two-fragment vendor_boot, like stock).
- Touchscreen.
- Unlock data with your **pattern** (Gatekeeper); follows automatically when the pattern changes. Second Space (999) recognized.
- Backup / restore, fastbootd, MTP.
- Ready-made package with `.bat` scripts: install, back to stock, collect logs.
