# 📝 Release Notes

[← Back to README](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](CHANGELOG.md)

The top version = the latest one on [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases).

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
