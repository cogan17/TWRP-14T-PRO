# 🧭 TWRP Menu Tour

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](menu-twrp.md)

What every TWRP menu on this phone does, **when to use it**, and **which parts are dangerous**. If your TWRP shows Indonesian, the Indonesian label is given in brackets.

> Legend: ✅ safe · ⚠️ careful · ⛔ don't, unless you fully understand the consequences

---

## 📦 Install

| Feature | Use | |
|---|---|---|
| Pick a **zip** → swipe | Installs a zip: the TWRP package (v1.4+), a kernel (AnyKernel3), a flashable module | ✅ |
| **Install Image** (bottom right) | Writes an `.img` file to a partition. Only 5 choices: `boot`, `init_boot`, `vendor_boot`, `dtbo`, `vbmeta` | ⚠️ pick the right partition |

- Updating TWRP: `TWRP-rothko-….img` → **`vendor_boot`**. Never `boot` or `init_boot`.
- The **`STOK-…`** file (*stock*) removes TWRP. Don't mix it up with the `TWRP-…` file.
- Root/kernel: see [Root & Kernel](root-dan-kernel.en.md).

## 🧹 Wipe (Format)

| Feature | Use | |
|---|---|---|
| **Swipe to factory reset** (Geser untuk reset pabrik) | Erases Data (except internal storage) | ⛔ triggers **FRP** on Android 15/16 — see [Reset & FRP](reset-dan-frp.en.md) |
| **Format Data** | Erases **all** Data **including internal storage** (photos, Download, TWRP backups) | ⛔ |
| **Advanced Wipe** (Hapus lainnya) | Pick partitions one by one | ⚠️ |
| ↳ Dalvik / ART Cache | Clears app caches; safe, Android rebuilds them | ✅ |
| ↳ **Repair or Change File System** | **Repair** = check & fix the file system (fsck). **Change** = reformat | ✅ Repair · ⛔ Change |

> If Repair fails with *device or resource busy*: turn MTP off first (**Mount → Disable MTP**).

## 💾 Backup (Cadangkan)

Backs partitions up to `TWRP/BACKUPS` on internal storage. Full guide: [Backup](backup.en.md).

- **Data** does not include internal storage (photos/Download). Copy those separately over MTP.
- Before experimenting, back up at least **`boot`** and **`init_boot`**.
- Copy the backup folder to a PC — if the phone dies, a backup on the phone dies with it.

## ♻️ Restore (Pulihkan)

Puts a backup back. ⚠️ Restore **Data** only onto the **same HyperOS version** it was made on ([why](update-hos.en.md)). On v1.4 and older, restoring Data can fail with `extractTarFork() 255` — the emergency steps are in [Backup → Restoring Data](backup.en.md#restoring-data); fixed in v1.5.

## 🔌 Mount

| Feature | Use |
|---|---|
| Tick partitions | Mounts a partition so its files can be read |
| **Enable / Disable MTP** | Access phone storage from a PC over USB. Turn it off while repairing a file system |

## ⚙️ Settings (Pengaturan)

Language, time zone, brightness, vibration and zip verification. Safe to change.

## 🛠️ Advanced (Lainnya)

| Feature | Use | |
|---|---|---|
| **File Manager** | Copy, move, delete files (including `/data` once decrypted) | ⚠️ careful when deleting |
| **Terminal** | A shell right on the phone | ⚠️ |
| **ADB Sideload** | Install a zip from a PC: `adb sideload name.zip` | ✅ |
| **Copy Log** | Copies `recovery.log` to storage, to send when something goes wrong | ✅ |

*Flash Current TWRP* and *Install Recovery Ramdisk* were **removed on purpose** in v1.3: on this phone both write to the wrong partition.

## 🔄 Reboot

| Choice | Result | |
|---|---|---|
| **System** | Boots Android | ✅ |
| **Recovery** | Back into TWRP | ✅ |
| **Bootloader** | FASTBOOT mode (for the `.bat` scripts on a PC) | ✅ |
| **Fastboot** (fastbootd) | Userspace fastboot, for dynamic partitions | ⚠️ |
| **Power off** | Turns the phone off | ✅ |
| **Slot A / B** | Switches the active slot | ⛔ leave it unless you understand A/B |

> ⚠️ If TWRP is misbehaving, don't use *Reboot → Recovery* again and again — the phone can get stuck in a loop. The way out is FASTBOOT (Power + Volume Down). See [Enter TWRP](masuk-twrp.en.md).
