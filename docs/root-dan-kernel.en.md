# 🪄 Root & Kernel

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](root-dan-kernel.md)

Installing a kernel or root through TWRP, and how to recover when something goes wrong. A kernel with built-in root and SUSFS for this phone: [Cogan-Kernel](https://github.com/cogan17/Cogan-Kernel).

---

## Which partition holds what

| Partition | Contents | What may be written there |
|---|---|---|
| `boot` | Kernel | A kernel (AnyKernel3 zip) or stock `boot` |
| `init_boot` | Early ramdisk; where *patched* root lives (KernelSU LKM / Magisk) | A patched or stock `init_boot` |
| `vendor_boot` | **TWRP** + vendor modules | Only the `TWRP-…` or `STOK-…` file from this package |

> ⛔ Never write TWRP to `boot` or `init_boot`.

## Before you start: back up

**Backup** → tick **`boot`** and **`init_boot`** → swipe. Copy the result to a PC. With this, any kernel/root mistake can be undone in a minute.

## Install a kernel (AnyKernel3 zip)

1. Copy the kernel zip to the phone.
2. TWRP → **Install** → pick the zip → swipe.
3. **Reboot → System**.

An AnyKernel3 zip only replaces the kernel in `boot`; the ramdisk and TWRP are untouched.

## Install patched root (`init_boot`)

1. Patch the stock `init_boot.img` with the root manager app (KernelSU / Magisk) in Android.
2. Copy the result to the phone.
3. TWRP → **Install** → **Install Image** → pick the file → **`init_boot`** → swipe.

## If the kernel/root breaks (bootloop)

- **Fastest:** TWRP → **Restore** → pick that backup → tick `boot` / `init_boot` → swipe.
- **No backup:** **Install Image** the **stock** `boot`/`init_boot` from the same ROM as your HyperOS.

## A module causes a bootloop

1. Enter TWRP, unlock with your [pattern](enkripsi-dan-pola.en.md).
2. **Advanced → File Manager** → `/data/adb/modules/`.
3. Open the suspect module's folder and create an empty file named **`disable`** (or delete the module folder).
4. **Reboot → System**.

> OrangeFox has a **KernelSU modules** menu for this — see the [OrangeFox guide](orangefox/menu.en.md).

## After restoring Data

Module state comes back from the backup and sometimes no longer fits. If a module stops working as usual (e.g. NoMount), **reinstall it**. APKs won't install after a factory reset from TWRP? That's FRP, not a module — see [Reset & FRP](reset-dan-frp.en.md).
