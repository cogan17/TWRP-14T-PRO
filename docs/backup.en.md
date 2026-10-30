# 💾 Backup

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](backup.md)

Always **back up first** before experimenting. Your data is worth more than your time.

---

## Personal files (Download, DCIM, photos)

**Easiest — from normal Android:**
plug in the cable → choose **File Transfer (MTP)** → copy the folders to your PC.

**From TWRP:**
1. [Enter TWRP](masuk-twrp.en.md) → unlock with your [pattern](enkripsi-dan-pola.en.md).
2. **Advanced → File Manager**.
3. Go to `/sdcard` (or `/data/media/0`), select a folder, copy it to OTG / a flash drive.

## Key partitions (init_boot, boot, super)

1. In TWRP, open **Backup**.
2. Tick the partitions to back up — usually **boot**, **init_boot**, **super**.
3. Swipe to start.
4. The result is saved in `TWRP/BACKUPS` on internal storage.

> ✅ Copy the backup to a PC / flash drive too, in case the phone has problems.

## Restoring Data

1. [Enter TWRP](masuk-twrp.en.md) → unlock with your [pattern](enkripsi-dan-pola.en.md).
2. **Restore** → pick the backup folder → tick **Data** (and any other partitions you need) → swipe.
3. Wait until it finishes, then **Reboot → System**. The first boot can take a while.

The rules:
- **Don't factory reset first** — TWRP empties Data by itself. A reset from TWRP triggers FRP ([Reset & FRP](reset-dan-frp.en.md)).
- Restore Data only onto the **same HyperOS version** it was made on ([Update HyperOS](update-hos.en.md)).
- After restoring, reinstall root modules if one stops working ([Root & Kernel](root-dan-kernel.en.md)).

> ⚠️ **TWRP v1.4 and older:** on Android 16, restoring **Data** can fail with `extractTarFork() ... 255` in a `/data/user/0/…` folder. This is a TWRP bug, fixed in v1.5. Internal storage and the backup files stay safe.

If it happens, **don't reboot and don't Format Data**. With the phone still in TWRP, run on the PC:

```
adb shell umount /data/user/0
```

Then run **Restore → Data** again without rebooting. Once it reaches 100%, Reboot → System.

## When this helps

- Before a HyperOS update, rooting, or changing ROM.
- `init_boot` = where root (KernelSU) lives — handy to restore root quickly.
