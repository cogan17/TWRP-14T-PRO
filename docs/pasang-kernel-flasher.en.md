# 📱 Install with Kernel Flasher (no PC)

[← Install TWRP](pasang.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](pasang-kernel-flasher.md)

> This route is only for a phone that is **already rooted** and has an **unlocked bootloader**. Not rooted yet? Use the PC route or the zip in [Install TWRP](pasang.en.md).

---

## Status

| Recovery | Status |
|---|---|
| **TWRP v1.5** | ✅ tested by the owner on the phone (1 Nov 2026): partition matches the release, TWRP opens, Android boots normally, root (BakaSU) still works |
| **OrangeFox ofox-v1.0** | ✅ tested by the owner on the phone (1 Nov 2026): partition matches the release, OrangeFox opens and reads storage, Android boots normally, root still works |

---

## You need

- A phone that is rooted (KernelSU or BakaSU).
- Firmware **OS3.0.302.0.WNNIDXM** (v1.8, ofox-v1.2) or **OS3.0.301.0.WNNIDXM** (v1.7, ofox-v1.1) — see *Settings → About phone*. The image must match your HyperOS version.
- Battery at least **50%**.
- The **Kernel Flasher** app.
- The image downloaded from **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)**, not from anywhere else.
- A copy of `STOK-vendor_boot-….img` on the phone **and** on a PC.

---

## TWRP

1. **Back up first** to a PC: the `TWRP/BACKUPS` folder and `STOK-vendor_boot-….img`.
2. Check the sha256 of the image you are going to write, and compare it with the release notes:
   ```
   sha256sum /sdcard/Download/TWRP-rothko-OS3.0.302.0.WNNIDXM.img
   ```
   For v1.8 it must be `74e1038e136464d4926adcf35e55cda3a9e07c8e3bce89fd1a7658d2bade34ea` (v1.7 for 301: `52bb80208b91f71f27fdc46ce30cfa9d1a4f4c6d72a46feacc186397877bd826`). Other versions: see the SHA256 in their release notes.
3. Open **Kernel Flasher**. In the **Device** card, *Slot Suffix* shows the active slot (`_a` or `_b`). Tap **View** on the slot card marked **[Active]** (e.g. *Slot A [Active]*).
4. Tap **Flash**, then **Flash Partition Image**. **Do not** choose **Flash AK3 Zip**, **Flash AK3 Zip using mkbootfs** or **Flash KernelSU LKM Driver** — those three are for kernels and root, not recovery.
5. In the partition list, tap **vendor_boot**, pick the image file, and wait for **Done**. **Do not** pick `boot`, `init_boot` or any other partition. You don't need the **Reboot** button on that screen yet.
6. Check the partition contents (read-only, safe):
   ```
   su -c 'n=$(wc -c < /sdcard/Download/TWRP-rothko-OS3.0.302.0.WNNIDXM.img); head -c $n /dev/block/by-name/vendor_boot_a | sha256sum'
   ```
   The result must match step 2. If the active slot is **B**, use `vendor_boot_b` instead of `vendor_boot_a`.
7. Enter recovery: with the phone **off**, hold **Volume Up + Power**, release Power when the logo appears, then keep holding Volume Up.
8. Unlock with your pattern **once**. Do not tap **Wipe**, **Format** or **Reset**.
9. **Reboot → System**.

## OrangeFox

The steps are the same, using `OrangeFox-rothko-OS3.0.302.0.WNNIDXM.img` and the `Fox/BACKUPS` backup folder. For ofox-v1.2 the hash in steps 2 and 6 must be `88f613b66f966546514816184a67673bd37a5f8f2aa9cb7730eb0e406c07a1fe` (ofox-v1.1 for 301: `b6cbe63a19021b5f26a4ba089266b367ddeb6e604720c2720a4a1ade61e327f5`).

In OrangeFox, do not use **Flash current OrangeFox**, **automatic reflash**, or **Fix recovery bootloop** (see [OrangeFox menu tour](orangefox/menu.en.md)).

---

## If it fails

- **Android can still boot:** open Kernel Flasher, tap **vendor_boot**, pick `STOK-vendor_boot-….img`, write it, then reboot.
- **Android will not boot, or recovery will not open:** enter FASTBOOT (phone off, hold **Power + Volume Down**) and run `2-KEMBALIKAN-STOK.bat` from a PC. See [Back to stock](kembali-ke-stok.en.md). This is the only way out when recovery cannot be opened.
- Do not keep rebooting into a broken recovery. That is the BCB loop and it will not fix itself.

## Notes

- This route only writes `vendor_boot`. `boot` and `init_boot` are not touched, so root stays in place.
- After a HyperOS update, **do not write an old image again**. Wait for a release for the new version. See [Update HyperOS](update-hos.en.md).
- Kernel Flasher can also write the root kernel to the **spare slot** before an update's restart, so root isn't lost. See [Update without losing root](update-hos.en.md#-update-without-losing-root-full-rom-tested-on-the-phone).
- Writing a partition is the phone owner's decision.
