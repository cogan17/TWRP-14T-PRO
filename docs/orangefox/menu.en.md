# 🧭 OrangeFox Menu Tour

[← OrangeFox guide](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](menu.md)

What every OrangeFox menu on this phone does. If your OrangeFox shows Indonesian, the Indonesian label is given in brackets.

> Legend: ✅ safe · ⚠️ careful · ⛔ don't, unless you fully understand the consequences

The bottom bar has 4 tabs: **Files**, **Backups**, **Wipe**, **Menu**.

---

## 📁 Files (Berkas)

A full file manager. **Every install starts here** — tap the file:

| Tapped file | Option | |
|---|---|---|
| `.zip` | **Install ZIP** → **Swipe to Install** | ✅ TWRP/OrangeFox packages, AnyKernel3 kernels |
| `.img` | **Install Image** → pick the **Partition** → swipe | ⚠️ pick the right one: recovery → `vendor_boot`, kernel → `boot`, patched root → `init_boot` |
| other files | copy, move, rename, delete, zip/unzip, view/edit text | ⚠️ careful when deleting |

The **`STOK-…`** file removes the custom recovery — don't mix it up with `OrangeFox-…`/`TWRP-…`.

## 💾 Backups (Cadangkan)

- **New Backup** (Cadangan Baru) → pick partitions → swipe. Before experimenting, back up at least `boot` and `init_boot`.
- **Select Storage** (Pilih Penyimpanan) → internal storage or a USB OTG drive.
- Tap an existing backup → **Restore** (Pulihkan).

Same rules as TWRP: **Data** doesn't include internal storage, restore Data only onto the same HyperOS version, and **don't factory reset first** before a restore. See [Backup](../backup.en.md).

## 🧹 Wipe (Bersihkan)

| Option | | |
|---|---|---|
| Dalvik / ART Cache, Cache | clears caches, Android rebuilds them | ✅ |
| USB Storage | empties an OTG drive | ⚠️ |
| Metadata | metadata encryption keys | ⛔ data can't be opened again |
| Data | the same as a factory reset | ⛔ triggers **FRP** ([Reset & FRP](../reset-dan-frp.en.md)) |
| Internal Storage | photos, Download, backup files | ⛔ |
| **Format Data** tab | erases everything | ⛔ |

## ☰ Menu (Pilihan)

### Main

| Menu | Use | |
|---|---|---|
| **Mount & MTP** (Muat) | Mounts partitions, turns MTP on/off. **Not** for installing files | ✅ |
| **Partitions Management** | Info and advanced actions per partition | ⚠️ |
| **ADB & Sideload** | Install a zip from a PC: `adb sideload name.zip` | ✅ |
| **Reboot** (Mulai ulang) | System, Recovery, Bootloader (FASTBOOT), Power off | ✅ — don't switch **slots** |

### Additions

| Menu | Use | |
|---|---|---|
| **KernelSU modules** (Modul KernelSU) | List, disable or remove KernelSU modules — a lifesaver when a module bootloops the phone | ✅ |
| **C++ Addons** (Addon C++) | OrangeFox's built-in addons | ⚠️ |
| **App Manager** (Manajer Aplikasi) | View and remove installed apps | ⚠️ don't remove system apps |
| **Copy Log to SD** (Salin Log ke kartu SD) | Saves the log to storage, to send when something goes wrong | ✅ |
| **More** (Lainnya) | Terminal, fix contexts, decrypt again, and more | ⚠️ see below |

### ⛔ Don't use these on this phone

On this phone the recovery lives in **`vendor_boot`**, split in two parts like stock. OrangeFox features that **repack the recovery** or **write to `boot`/`init_boot`** are untested with that layout and can leave the recovery or Android unable to boot:

- **Flash current OrangeFox** and **auto-reflash OrangeFox after flashing a ROM** — hidden in ofox-v1.0.
- **Fix recovery bootloop**, **Inject OrangeFox** — if they show up, don't use them.
- **Install Magisk / KernelSU from recovery** (under *More*) — install root via [Root & Kernel](../root-dan-kernel.en.md) instead.
- **Install Ramdisk** and **Flash to both slots** on the Install Image page, **Switch slots** under Reboot.
- **Remove FRP** (Fox Addons), **Disable DM-Verity / Forced Encryption** (Settings → OTA & ROM).
- OrangeFox's OTA menus — to update HyperOS follow [Update HyperOS](../update-hos.en.md).

## ⚙️ Settings (gear icon)

Theme, colours, language, time zone, brightness, vibration. Safe to change.
