# 📘 OrangeFox Manual — Xiaomi 14T Pro (rothko)

[← OrangeFox guide](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](buku-manual.md)

One book for everything about OrangeFox on this phone, from download to going back to stock. Read it top to bottom the first time; later, jump in through the contents.

> **Menu names in this book** come from the OrangeFox `fox_16.0` source, so they match the screen. This build starts in **Indonesian**; switch to English under **Settings → Regional → Language**. Each English label is followed by the Indonesian one in brackets when it helps you find it, e.g. **Files** (*Berkas*). A few labels have no Indonesian translation and show in English either way (*Main*, *Additions*, *Partitions Management*).

**Marks:** ✅ safe · ⚠️ careful · ⛔ don't use on this phone

---

## Contents

1. [Meet OrangeFox](#1-meet-orangefox)
2. [Before you start](#2-before-you-start)
3. [Download and check the files](#3-download-and-check-the-files)
4. [Install OrangeFox](#4-install-orangefox)
5. [Enter OrangeFox](#5-enter-orangefox)
6. [Unlock your data (pattern)](#6-unlock-your-data-pattern)
7. [Screen and navigation](#7-screen-and-navigation)
8. [Files tab — file manager and installing](#8-files-tab--file-manager-and-installing)
9. [Backups tab — backup and restore](#9-backups-tab--backup-and-restore)
10. [Wipe tab](#10-wipe-tab)
11. [Menu tab — every menu](#11-menu-tab--every-menu)
12. [KernelSU modules — fixing a module bootloop](#12-kernelsu-modules--fixing-a-module-bootloop)
13. [Kernel and root](#13-kernel-and-root)
14. [OrangeFox settings](#14-orangefox-settings)
15. [Updating HyperOS](#15-updating-hyperos)
16. [Going back to TWRP or stock](#16-going-back-to-twrp-or-stock)
17. [Factory reset and FRP](#17-factory-reset-and-frp)
18. [Issues and logs](#18-issues-and-logs)
19. [The don't list](#19-the-dont-list)
20. [Glossary](#20-glossary)

---

## 1. Meet OrangeFox

OrangeFox is a TWRP-based recovery: a modern look, a full file manager, a KernelSU module manager and themes. Here it is built from **the same device tree** as TWRP, so touch, modules and decryption are the same.

| | |
|---|---|
| Base | OrangeFox R12, `fox_16.0` (Android 16) |
| Firmware | HyperOS **OS3.0.301.0.WNNIDXM** |
| Lives in | the **`vendor_boot`** partition, like TWRP |
| Tested by the owner on the phone | boot, touchscreen, pattern decryption (ofox-v1.0) |

**Worth knowing:**

- TWRP and OrangeFox **live in the same place**. Only one is installed; installing one replaces the other.
- On this phone `vendor_boot` holds two parts: a *platform* part (modules and early-boot files that **Android also uses for a normal boot**) and a *recovery* part. That is why the OrangeFox image must match **exactly** your HyperOS version.
- Your data, photos and apps are **not touched** when you install, swap or remove OrangeFox.

## 2. Before you start

- [ ] The bootloader is **unlocked**.
- [ ] Your HyperOS version (*Settings → About phone*) is the **same** as the version in the package name.
- [ ] Battery at least **50%**.
- [ ] Important data is backed up (photos and Download copied to a PC).
- [ ] **Without a PC:** TWRP or OrangeFox is already installed.
- [ ] **With a PC:** Windows, a good USB cable, and a **platform-tools** folder (with `adb.exe` and `fastboot.exe`).

## 3. Download and check the files

Download **only** from **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)** → a release tagged **`ofox-v…`** (plain `v…` tags are TWRP). Not from the *Actions* tab — those are test files that expire after 90 days.

| File | Purpose |
|---|---|
| **`PAKET-OrangeFox-rothko-<version>.zip`** | Full package: flash it in recovery **or** extract it for a PC |
| `OrangeFox-rothko-<version>.img` | The OrangeFox image alone |
| `STOK-vendor_boot-<version>.img` | Xiaomi stock — **removes** the custom recovery |

Inside the package: `1-PASANG-ORANGEFOX.bat`, `2-KEMBALIKAN-STOK.bat`, `3-KEMBALI-KE-TWRP.bat`, the OrangeFox, TWRP and STOK images, `PANDUAN-ORANGEFOX.html` (offline guide, Indonesian), `BACA-SAYA.txt` (with SHA256 sums) and `META-INF` (makes the zip flashable).

### Make sure the file is complete

An interrupted download gives a broken zip. ZArchiver reports **"Kesalahan Data"** (data error), and an image extracted from it is **smaller than 64 MB** — **never use** such a file.

**Check on the phone with Termux** (change the folder to where you downloaded):

```sh
cd /sdcard/Download
ls -l PAKET-OrangeFox-*.zip
sha256sum PAKET-OrangeFox-*.zip
```

Size and SHA256 must match the release page. Without Termux: in OrangeFox, **Files** → long-press the file → **Checksum** → *Tap here to calculate*.

**If you extract it:** extract into a **new folder** (ZArchiver: long-press the zip → *Extract to ./zip-name/*), then check that all three `.img` files are **64.00 MB** each. A zip showing up next to the extracted files is the source zip itself, not part of the package.

## 4. Install OrangeFox

### A. From TWRP (no PC — easiest)

1. Copy **`PAKET-OrangeFox-rothko-<version>.zip`** to the phone. **No need to extract it.**
2. [Enter TWRP](../masuk-twrp.en.md) → **Install** → pick the zip → swipe.
3. Wait for **Successful** → **Reboot → Recovery**.

The zip checks that the phone is a rothko and the file is intact, writes OrangeFox to `vendor_boot`, then reads it back to confirm. If anything doesn't match, **nothing is written**.

### B. From OrangeFox (updating)

**Files** (*Berkas*) → tap the new package zip → the **Install ZIP** page → **Swipe to Install** → **Menu → Reboot → Recovery**.

### C. From a PC (FASTBOOT)

1. Extract the package into the **platform-tools** folder.
2. Power off → hold **Power + Volume Down** until **FASTBOOT** shows → plug in the cable.
3. Double-click **`1-PASANG-ORANGEFOX.bat`** → follow it until **BERHASIL** (success).

The `.bat` checks the image's SHA256 before writing and writes only to `vendor_boot`.

### After installing

1. Enter OrangeFox ([chapter 5](#5-enter-orangefox)) and unlock with your pattern ([chapter 6](#6-unlock-your-data-pattern)).
2. Try the touchscreen and open **Files** — photos and Download must be visible.
3. **Menu → Reboot → System** — make sure Android boots normally.

## 5. Enter OrangeFox

### With the buttons (always works)

1. Power the phone off completely.
2. Hold **Volume Up + Power** together.
3. When the Mi logo appears, release **Power** and keep holding **Volume Up** until OrangeFox opens.

### From rooted Android (Termux)

```sh
su -c 'reboot recovery'
```

> ⚠️ Use this **only when the installed OrangeFox is known to work**. `reboot recovery` leaves a flag (*BCB*) in the `misc` partition; if the recovery is broken, the phone keeps returning to that broken recovery. The way out: hold **Power ~15 s** until it turns off → **Power + Volume Down** → FASTBOOT → a `.bat` from the PC.

Leaving OrangeFox: **Menu → Reboot → System**.

## 6. Unlock your data (pattern)

Your data is encrypted. When OrangeFox opens it shows **"Data Partition is encrypted"** and asks for the pattern.

- **Main user (0):** draw your **lock-screen pattern** — **once, carefully**. You'll see *Trying Decryption*, then *Successfully decrypted!*. Photos and Download open right away.
- **Second Space / XSpace (999):** a separate profile with its own password. Not using it? **Press back** to skip — the main data stays unlocked.
- Skipped the prompt and want to unlock later: **Menu → Other → Decrypt Data** (or **Decrypt Users** for other users).

> ⚠️ Repeated **Pattern failed!** can cause a temporary lockout. Don't keep retrying — [grab a log](#18-issues-and-logs).

Changed your pattern in Android? OrangeFox uses the new one automatically.

Under the hood: HyperOS keeps the key in the **Weaver** chip, which recovery can't read. OrangeFox on this phone is patched to fall back quickly to the **Gatekeeper** protector for the same pattern — that's why decryption no longer hangs at *Trying Decryption* since ofox-v1.0. Details: [Encryption & Pattern](../enkripsi-dan-pola.en.md).

## 7. Screen and navigation

- **Bottom bar: 4 tabs** — **Files** (*Berkas*), **Backups** (*Cadangkan*), **Wipe** (*Bersihkan*), **Menu** (*Pilihan*).
- **Navigation buttons** at the very bottom: back, home, and hide the bar. Back also cancels the pattern prompt.
- The **gear icon** at the top of the **Menu** tab opens **Settings** ([chapter 14](#14-orangefox-settings)).
- Every risky action asks for a **swipe** (*Swipe to Confirm*) — until you swipe, nothing happens.

## 8. Files tab — file manager and installing

Every install **starts here**. OrangeFox has no separate "Install" menu — **tap the file**.

### Tap a file

| File | Opens | Steps |
|---|---|---|
| `.zip` | **Install ZIP** (*Pasang Zip*) | Check **Options** (below) → **Swipe to Install** |
| `.img` | **Install Image** (*Pasang Image*) | Under **Partition**, pick the target → swipe |
| text (`.txt`, `.log`, `.sh`) | text viewer | Reading only |

**The right partition for an `.img`:**

| File | Partition |
|---|---|
| `OrangeFox-…img`, `TWRP-…img`, `STOK-vendor_boot-…img` | **`vendor_boot`** |
| kernel `boot.img` | `boot` |
| patched root `init_boot` | `init_boot` |

> ⛔ Never write a recovery to `boot` or `init_boot`.
> ⛔ On the **Install Image** page, leave **Flash to both slots** off (the default) and **don't** press **Install Ramdisk**.

**Options on the Install ZIP page:**

| Option | |
|---|---|
| **Add to Queue** / **View Queue** | ✅ install several zips in a row (max 10) |
| Reboot after installation is complete | ✅ fine |
| ZIP signature verification | ✅ leave as is |
| Unmount System / Vendor before installing a ZIP | ✅ leave as is |
| Reflash OrangeFox after flashing a ROM, Inject OrangeFox after install, Disable vbmeta AVB2.0, Add Magisk | ⛔ if shown, keep them **off** |

### Long-press a file or folder

| Option | |
|---|---|
| **Open as...** → *Text file*, *Flashable ZIP*, *Flashable image* | ✅ when OrangeFox doesn't recognise the file type |
| **Copy**, **Move**, **Rename** | ✅ |
| **Delete** | ⚠️ can't be undone |
| **Compress** / **Unpack archive** | ✅ create or open zip/tar |
| **Checksum** | ✅ MD5/SHA — to compare with the release SHA256 |
| **Information** | ✅ size, permissions, dates |
| **Edit File in nano**, **Open Terminal Here** | ⚠️ for those who know |
| **Set permissions**, **Hide** | ⚠️ don't change system file permissions |

**Multi-select:** long-press one file, tap others → **Batch actions** (*Copy*, *Move*, *Delete*).
**Favorite folders:** keep folders you open often (e.g. `Download`, `Fox/BACKUPS`).

Key locations: internal storage = `/sdcard` (same as `/data/media/0`), OrangeFox backups = `Fox/BACKUPS`, logs = `Fox/logs`.

## 9. Backups tab — backup and restore

### Make a backup

1. **Backups** (*Cadangkan*) → **New Backup**.
2. **Name**: leave *(auto generated)* or type your own.
3. Tick the **Partitions**. Most important: **`boot`**, **`init_boot`**, **`vendor_boot`**, and **Data** if needed.
4. Optional: **Enable Encryption** — only Data is encrypted; **you must remember the password**, without it the backup can't be restored.
5. **Swipe to Backup** → wait for **Backup completed**.

**Select Storage** picks where it goes (internal storage or USB OTG). Backups land in `Fox/BACKUPS/<serial>/<name>`. **Copy them to a PC too** — a reset or Format Data wipes internal storage.

**Quick Backup** uses the partition list set under **Settings → Backup → Quick backup partitions**.

### Restore

1. **Backups** → tap an existing backup (sorted by date).
2. On the **Restore Backup** page, tick the partitions to restore → **Swipe to Restore**.
3. Wait for **Restore completed** → **Menu → Reboot → System**. The first boot after restoring Data can take a while.

The same page offers **Rename Backup** and **Delete Backup**.

### Rules for Data backups

- A **Data** backup does **not** include photos and Download (internal storage). Copy those to a PC separately.
- Restore Data **only to the same HyperOS version** it was made on ([Update HyperOS](../update-hos.en.md)).
- **Don't factory reset or wipe Data before restoring** — restore empties Data by itself. A reset from recovery triggers FRP ([chapter 17](#17-factory-reset-and-frp)).
- On Android 16, `/data/data` is bound to `/data/user/0`. This OrangeFox release uses `OF_WORKAROUND_BACKUP_BUG`, so restore doesn't fail with `extractTarFork() … 255` like old TWRP did.
- After restoring Data, apps return to **the backup date**: apps installed after the backup are gone, and root modules sometimes need reinstalling ([Root & Kernel](../root-dan-kernel.en.md)).

## 10. Wipe tab

| Option | Effect | |
|---|---|---|
| **Dalvik / ART Cache**, **Cache** | Cache is cleared; Android rebuilds it | ✅ |
| **USB Storage** | Empties the OTG flash drive | ⚠️ |
| **Data** | Same as a factory reset | ⛔ triggers FRP |
| **Metadata** | Encryption keys gone, data can't be unlocked again | ⛔ |
| **Internal Storage** | Photos, Download and **backup files** deleted | ⛔ |
| **Format Data** (asks you to type `yes`) | All apps, photos, backups deleted | ⛔ |

The **Wipe** tab shows a list of partitions with checkboxes, with a **Format Data** button above it. To clear cache: tick only **Dalvik / ART Cache** and **Cache** → **Swipe to Wipe**. Double-check the ticks before swiping.

## 11. Menu tab — every menu

### Main

| Menu | Purpose | |
|---|---|---|
| **Mount & MTP** (*Muat*) | Mount/unmount partitions; **Enable MTP** so the PC sees the phone. **Not** for installing files. | ✅ |
| **Partitions Management** → **Partition Editor** | Info per partition, **Repair FS**, **Resize FS**, **Change FS** | ⚠️ only *Partition Info* is safe to poke at |
| **Partitions Management** → **Merge Snapshots**, **Unmap Super Devices** | For leftovers of an unfinished OTA | ⚠️ only when asked during troubleshooting |
| **ADB & Sideload** | Install a zip from a PC: **Swipe to Start Sideload**, then `adb sideload name.zip` on the PC | ✅ |
| **Reboot** (*Mulai ulang*) | **System**, **Recovery**, **Bootloader**, **Fastboot**, **Power Off** | ✅ — ⛔ **don't Switch slots** |

> **Repair FS** fails with *device or resource busy*? Turn MTP off first under **Mount & MTP**.

### Additions

| Menu | Purpose | |
|---|---|---|
| **KernelSU modules** | View, disable, remove modules ([chapter 12](#12-kernelsu-modules--fixing-a-module-bootloop)) | ✅ |
| **App Manager** | View and remove installed apps | ⚠️ don't remove system apps |
| **Copy Log to SD** | Saves the log to `Fox/logs` | ✅ |
| **Fox Addons** (*Addon C++*) | See the table below | ⚠️ |
| **Other** (*Lainnya*) | See the table below | ⚠️ |

**Fox Addons:**

| Option | |
|---|---|
| **Backup OrangeFox Settings**, **Reset to defaults** | ✅ OrangeFox settings only |
| **Remove password** | ✅ removes the **OrangeFox** password only ([chapter 14](#14-orangefox-settings)), not the phone's pattern |
| **Remove all survival scripts**, **Remove OrangeFox files** | ⚠️ not needed on this phone |
| **Remove FRP**, **Enable init.d support**, **Install** Magisk / KernelSU / KernelSU Next / SukiSU, AromaFM | ⛔ |

**Other:**

| Option | |
|---|---|
| **Decrypt Data**, **Decrypt Users** | ✅ unlock data if you skipped it earlier |
| **Terminal** | ⚠️ command line — only for commands you understand |
| **Fix Contexts** | ⚠️ rarely needed; OrangeFox itself warns it can stop the phone from booting |
| **Inject OrangeFox**, **Fix Recovery Bootloop** | ⛔ |

## 12. KernelSU modules — fixing a module bootloop

Android bootloops after installing a module? No reset needed:

1. Enter OrangeFox and unlock with your pattern.
2. **Menu → KernelSU modules** → wait for the list.
3. Tap the suspect module:
   - turn off **Active** — the module doesn't run at boot, or
   - **Skip mount** — the module runs without mounting its files, or
   - **Remove module next boot** / **Delete** — the module is removed.
4. **Reboot** → Android boots without that module.

Not sure which one? Disable the **most recently installed**. Still looping? Disable them one by one. Without this menu (e.g. in TWRP): **Files** → `/data/adb/modules/<module>/` → create an empty file named `disable`.

## 13. Kernel and root

Before anything: **back up** `boot` and `init_boot` ([chapter 9](#9-backups-tab--backup-and-restore)) and copy them to a PC.

| Task | Steps |
|---|---|
| Install a kernel (AnyKernel3 zip, e.g. [Cogan-Kernel](https://github.com/cogan17/Cogan-Kernel)) | **Files** → tap the zip → **Swipe to Install** → **Reboot → System** |
| Install patched root (`init_boot`) | Patch the stock `init_boot.img` in the manager app (KernelSU/Magisk) in Android → **Files** → tap the result → **Install Image** → **`init_boot`** → swipe |
| Kernel/root broke something | **Backups** → that backup → **Restore Backup** → tick `boot`/`init_boot` → swipe |
| No backup | **Install Image** the **stock** `boot`/`init_boot` from the same ROM as your HyperOS |

> ⛔ Don't use OrangeFox's **Install Magisk/KernelSU** — install root through the manager app as above.
> The root manager must match the kernel variant you have installed. More in [Root & Kernel](../root-dan-kernel.en.md).

## 14. OrangeFox settings

Open them with the **gear icon** on the **Menu** tab.

| Section | Contents | |
|---|---|---|
| **General** | Show hidden files, Auto detect file type, **Recovery performance mode** (High performance / Balanced / Power save), Force fast charge | ✅ |
| **General** — ROM flashing options | Disable vbmeta AVB2.0, Reflash OrangeFox, Inject OrangeFox | ⛔ keep off |
| **OTA & ROM** | Support OTA, Disable DM-Verity, Disable Forced Encryption | ⛔ don't change — meant for custom ROMs, not stock HyperOS |
| **Customization** | Theme (colours, accent), fonts and size, splash, navigation bar, status bar | ✅ |
| **Security** | Lock OrangeFox with a **PIN Code**, **Text password** or **Gesture key** | ⚠️ not needed on this phone — forgetting it locks you out of your own recovery. Already set? Remove it with **Fox Addons → Remove password** |
| **Display** | Brightness, screen timeout | ✅ |
| **Vibration** | Button, keyboard and action vibration | ✅ |
| **Backup** | Enable compression, Digest verification, Quick backup partitions | ✅ |
| **Regional** | **Time Zone** → *(UTC +7) Bangkok, Hanoi, Jakarta*, **Use 24-hour clock**, **Language** | ✅ |
| **About** | Version, device, credits | ✅ |

**Reset to defaults** only resets OrangeFox's own settings — the phone's data isn't touched.

## 15. Updating HyperOS

A HyperOS update overwrites `vendor_boot`, so OrangeFox is gone afterwards — that's expected.

1. **Back up** first (personal files to a PC; the `boot`/`init_boot`/`vendor_boot` partitions).
2. [Go back to stock](#16-going-back-to-twrp-or-stock) — OTAs often fail while partitions are modified.
3. Update from HyperOS **Settings**. **Don't wipe** — your data carries over.
4. Install the OrangeFox **version matching the new HyperOS**. Not in Releases yet? Wait, or stay on stock for now.

> ⛔ Don't use OrangeFox's OTA menu for stock HyperOS. Don't restore Data from an older HyperOS version. Details: [Update HyperOS](../update-hos.en.md).

## 16. Going back to TWRP or stock

None of these erase data.

| Goal | In OrangeFox | From a PC (FASTBOOT) |
|---|---|---|
| **TWRP** | **Files** → `PAKET-TWRP-…zip` (v1.4+) → **Swipe to Install**; or `TWRP-rothko-….img` → **Install Image** → **`vendor_boot`** → swipe | **`3-KEMBALI-KE-TWRP.bat`** |
| **Stock** (no custom recovery) | **Files** → `STOK-vendor_boot-….img` → **Install Image** → **`vendor_boot`** → swipe → **Reboot → System** | **`2-KEMBALIKAN-STOK.bat`** |

The OrangeFox package already carries the latest released TWRP image and the STOK image.

## 17. Factory reset and FRP

> ⛔ **Don't factory reset from recovery** (wiping Data, Format Data, Factory Reset). If you need a reset, use **HyperOS Settings → About phone → Factory reset**.

On Android 15/16 a reset from recovery counts as untrusted. **FRP** turns on: APKs won't install through the built-in installer (*"App not installed"*), while the Play Store, MT Manager/App Manager with root and `adb install` still work.

- Already reset and sitting on the setup screens? **Sign in with the same Google account** — don't leave that screen to restore Data.
- **Proven on the owner's phone (30 Oct 2026):** flashing the **full stock fastboot ROM** with Mi Flash **`clean all`** (not *clean all and lock*), then signing in with your own Google account during setup, cleared FRP. It erases data — copy your backups to a PC first.
- ⛔ Don't use OrangeFox's **Remove FRP**, third-party "FRP unlock tools", or tamper with the `frp` partition.

More in [Reset & FRP](../reset-dan-frp.en.md).

## 18. Issues and logs

### Grabbing a log

| Situation | How |
|---|---|
| OrangeFox runs | **Menu → Copy Log to SD** → the file is in `Fox/logs`. Do it **before rebooting**. |
| OrangeFox runs, PC at hand | `3-AMBIL-LOG.bat` from the TWRP package, or `adb pull /tmp/recovery.log` |
| Decryption failed | OrangeFox saves `lastrecoverylog.log` in `Fox/logs` |
| Android bootloops | `4-LOG-BOOTLOOP.bat` from the TWRP package ([TWRP Issues & Logs](../masalah-dan-log.en.md)) |

Send the log **and** a photo of the screen at the error. Don't guess — the log shows the cause.

### Common issues

| Symptom | Fix |
|---|---|
| Stuck at **Trying Decryption** | Use **ofox-v1.0** or newer (test builds before 30 Oct waited for Weaver forever) |
| **Pattern failed!** | Make sure it's your current lock-screen pattern; don't keep retrying; send a log |
| Can't find an Install menu | In OrangeFox, **tap the file** in **Files** ([chapter 8](#8-files-tab--file-manager-and-installing)) |
| "Muat" doesn't install anything | **Muat = Mount**, not Install |
| ZArchiver: **"Kesalahan Data"**, image < 64 MB | Broken download — download again and check SHA256 ([chapter 3](#3-download-and-check-the-files)) |
| Phone keeps booting into recovery | Hold **Power ~15 s** → **Power + Volume Down** → FASTBOOT → `.bat` from the PC |
| Android bootloops after a module | [KernelSU modules](#12-kernelsu-modules--fixing-a-module-bootloop) |
| Android bootloops after kernel/root | Restore `boot`/`init_boot` ([chapter 13](#13-kernel-and-root)) |
| PC doesn't see the phone | **Menu → Mount & MTP → Enable MTP**, or try another cable |
| **Repair FS** fails with *device or resource busy* | Turn MTP off first |
| APKs won't install after a reset | FRP — [chapter 17](#17-factory-reset-and-frp) |
| Second Space (999) won't open after a reset from recovery | Its key was wiped with it — it can't be recovered |
| OrangeFox gone after a HyperOS update | Expected — [chapter 15](#15-updating-hyperos) |

## 19. The don't list

Everything marked ⛔ on this phone in one place — each can (or did) leave the phone unbootable, lose data, or trigger FRP:

- Factory reset, wiping **Data**, **Metadata**, **Internal Storage**, or **Format Data** from recovery.
- Writing a recovery to `boot` or `init_boot`; **Install Ramdisk**; **Flash to both slots**; **Switch slots**.
- **Flash current OrangeFox**, **Reflash OrangeFox after flashing a ROM**, **Inject OrangeFox**, **Fix Recovery Bootloop** (they repack the recovery — untested with the two-part `vendor_boot`; some are already hidden in this release).
- **Install Magisk / KernelSU** from recovery, **Disable vbmeta AVB2.0**, **Disable DM-Verity**, **Disable Forced Encryption**, **Enable init.d support**, the **OTA** menu.
- **Remove FRP**, "FRP unlock tools", tampering with the `frp` partition.
- Files for another phone or another HyperOS version; files from the *Actions* tab.

## 20. Glossary

| Term | Meaning |
|---|---|
| **Recovery** | A small separate system for backup, restore and installing files — TWRP or OrangeFox |
| **`vendor_boot`** | The partition OrangeFox/TWRP lives in; it also holds modules Android needs to boot |
| **`boot`** / **`init_boot`** | The kernel / where patched root lives |
| **FASTBOOT** | Bootloader mode (Power + Volume Down) for writing partitions from a PC |
| **Flash** | Writing a file to a partition |
| **Wipe** | Erasing a partition's contents |
| **Mount** (*Muat*) | Making a partition readable/writable in recovery |
| **MTP** | The mode that lets a PC browse the phone's storage |
| **Sideload** | Installing a zip from a PC with `adb sideload` |
| **Decryption** | Unlocking encrypted data with your pattern |
| **Weaver / Gatekeeper** | Two places a pattern's key is protected; recovery uses Gatekeeper |
| **BCB** | A flag in the `misc` partition that tells the phone to boot into recovery |
| **FRP** | Anti-theft protection after an untrusted reset |
| **A/B slots** | Two copies of the partitions; the phone runs from one of them |
| **SHA256** | A file's fingerprint, to confirm it's complete and genuine |

---

Credits: [OrangeFox Recovery Project](https://gitlab.com/OrangeFox) · TeamWin Recovery Project · original tree [JonesqPacMan](https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp) · maintainer **Cogan17**. See [Authenticity & Credits](../keaslian-dan-kredit.en.md).
