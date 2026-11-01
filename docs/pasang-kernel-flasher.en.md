# 📱 Install with Kernel Flasher (no PC)

[← Install TWRP](pasang.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](pasang-kernel-flasher.md)

> This route is only for a phone that is **already rooted** and has an **unlocked bootloader**. Not rooted yet? Use the PC route or the zip in [Install TWRP](pasang.en.md).

---

## Status

| Recovery | Status |
|---|---|
| **TWRP v1.5** | ✅ tested by the owner on the phone: partition matches the release, TWRP opens, Android boots normally, root (BakaSU) still works |
| **OrangeFox ofox-v1.0** | ⚠️ not yet tested this way |

---

## You need

- A phone that is rooted (KernelSU or BakaSU).
- Firmware **OS3.0.301.0.WNNIDXM** (*Settings → About phone*). The image must match your HyperOS version.
- Battery at least **50%**.
- The **Kernel Flasher** app.
- The image downloaded from **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)**, not from anywhere else.
- A copy of `STOK-vendor_boot-….img` on the phone **and** on a PC.

---

## TWRP

1. **Back up first** to a PC: the `TWRP/BACKUPS` folder and `STOK-vendor_boot-….img`.
2. Check the sha256 of the image you are going to write, and compare it with the release notes:
   ```
   sha256sum /sdcard/Download/TWRP-rothko-OS3.0.301.0.WNNIDXM.img
   ```
   For v1.5 it must be `ff5f9f560d5bc696d95b7360ed1b80f80ee2b0eaaa5b78ad254264423b0fdaec`.
3. Open **Kernel Flasher**. The active slot is shown at the top (e.g. *Slot A [Active]*).
4. Tap **vendor_boot**, pick the image file, and write it. **Do not** pick `boot` or `init_boot`.
5. Check the partition contents (read-only, safe):
   ```
   su -c 'n=$(wc -c < /sdcard/Download/TWRP-rothko-OS3.0.301.0.WNNIDXM.img); head -c $n /dev/block/by-name/vendor_boot_a | sha256sum'
   ```
   The result must match step 2.
6. Enter recovery: with the phone **off**, hold **Volume Up + Power**, release Power when the logo appears, then keep holding Volume Up.
7. Unlock with your pattern **once**. Do not tap **Wipe**, **Format** or **Reset**.
8. **Reboot → System**.

## OrangeFox

The steps are the same, using `OrangeFox-rothko-OS3.0.301.0.WNNIDXM.img`. Compare the hash with the `ofox-v1.0` release notes.

This route has not been tested by the owner for OrangeFox. Follow steps 5 and 6 carefully, and if something goes wrong, follow **If it fails** below.

In OrangeFox, do not use **Flash current OrangeFox**, **automatic reflash**, or **Fix recovery bootloop** (see [OrangeFox menu tour](orangefox/menu.en.md)).

---

## If it fails

- **Android can still boot:** open Kernel Flasher, tap **vendor_boot**, pick `STOK-vendor_boot-….img`, write it, then reboot.
- **Android will not boot, or recovery will not open:** enter FASTBOOT (phone off, hold **Power + Volume Down**) and run `2-KEMBALIKAN-STOK.bat` from a PC. See [Back to stock](kembali-ke-stok.en.md). This is the only way out when recovery cannot be opened.
- Do not keep rebooting into a broken recovery. That is the BCB loop and it will not fix itself.

## Notes

- This route only writes `vendor_boot`. `boot` and `init_boot` are not touched, so root stays in place.
- After a HyperOS update, **do not write an old image again**. Wait for a release for the new version. See [Update HyperOS](update-hos.en.md).
- Writing a partition is the phone owner's decision.
