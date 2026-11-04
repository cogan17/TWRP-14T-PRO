# 🔄 Update HyperOS Without Losing Data

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](update-hos.md)

When a HyperOS update arrives, TWRP and root usually **disappear with it**. This is the **safe** way to update — your data stays intact, with no risky restore.

---

## ✅ The safe way (recommended)

This way your data **carries over by itself**, so there is **no manual `/data` restore** (and no risk of conflicts):

1. **Back up first** — data, personal files, **and** the `boot`/`init_boot`/`vendor_boot` partitions. See [Backup](backup.en.md). This is your safety net.
2. **[Go back to stock](kembali-ke-stok.en.md)** first (remove TWRP/root) — *incremental* OTAs often **fail** while partitions are still modified. If the Updater downloads a **full ROM**, this step isn't needed and root can be kept: see [Update without losing root](#-update-without-losing-root-full-rom-tested-on-the-phone).
3. **Take the OTA from Settings → do NOT wipe.** An OTA does **not** erase `/data`, so your apps and data stay.
4. **Install TWRP + root again** (the version matching the new HyperOS).

> 💡 The point: let the OTA carry your data. A manual restore is the last resort.

---

## 🔑 Update without losing root (full ROM, tested on the phone)

**Tested by the owner on the phone, 4 Nov 2026:** updated `OS3.0.301.0.WNNIDXM` → `OS3.0.302.0.WNNIDXM` through the Updater app with TWRP and Cogan-Kernel still installed. HyperOS 302 booted from slot B with Cogan-Kernel (`uname -r`: `6.1.138-android14-11-g44bda9e8f6e9-ab13792638`), and root was kept.

Why it works: this phone uses **A/B slots**. The Updater writes the new system to the **spare slot**, and the phone only switches to it on **Restart**. Before that restart, the root kernel can be written to the spare slot first.

**Requirements**
- The Updater downloads a **full ROM** (file name `…ota_full…zip` in `Download/downloaded_rom`). A full ROM doesn't check the old partitions' contents, so TWRP and a custom kernel don't block it. An *incremental* OTA (a delta) is untested and will likely fail on modified partitions.
- A rooted phone with **Kernel Flasher** and **Termux**.
- The Cogan-Kernel zip of the **same variant** you have installed (KernelSU Next or BakaSU). Proven on 302 (stock kernel modules 6.1.157): Cogan-Kernel `6.1.138-android14-11-g44bda9e8f6e9`.
- A PC for the emergency route.

**Steps**
1. **Back up** as usual (see [Backup](backup.en.md)) and copy it to a PC.
2. Let the Updater download. While it shows **Extracting**, copy the zip out of `Download/downloaded_rom` into another folder. The Updater deletes it when done, and it is useful as a stock backup.
3. From that copy, extract the new stock `boot.img` with a payload dumper app and **keep it on the PC**. It is your way out if step 6 goes wrong.
4. Wait for the **Restart now** button. **Don't press it yet.**
5. Record the starting state (read-only):
   ```sh
   su -c 's=$(getprop ro.boot.slot_suffix); o=$([ "$s" = _a ] && echo _b || echo _a); echo "active=$s spare=$o"; for p in boot$s boot$o vendor_boot$o; do echo "$p $(sha256sum /dev/block/by-name/$p | cut -c1-64)"; done'
   ```
6. **Kernel Flasher** → tap **View** on the **spare** slot's card (the one *not* marked *[Active]*) → **Flash** → **Flash AK3 Zip** → pick the Cogan-Kernel zip → wait for **Done!**. The AnyKernel3 log must name `boot_b` (or `boot_a`), the spare slot. Don't press **Reboot** in Kernel Flasher.
7. Run the step 5 command again. Correct result:
   - the **active** slot's `boot` is unchanged;
   - the **spare** slot's `boot` **changed**: the root kernel is written;
   - the **spare** slot's `vendor_boot` is unchanged: the new stock modules are intact.

   If anything differs, **stop** and don't restart.
8. Press **Restart now**. The first boot takes longer than usual.

**Stuck on the logo or bootlooping:** hold Power ~15 s → **Power + Volume Down** (FASTBOOT), then from the PC:
```
fastboot flash boot_b boot.img
fastboot reboot
```
(Use `boot_a` instead if the spare slot was A.) The phone returns to the new stock version without root; your data is safe.

**After the update**
- **TWRP/OrangeFox are gone**: the new slot's `vendor_boot` is stock. Install the version **built for the new firmware** (see the release title). Never install an older image.
- The `STOK-vendor_boot` file from an older package is **not stock any more** either. Use the one from the release matching the new firmware.

---

## ⚠️ Don't restore an old `/data` backup onto a different HyperOS version

This is the mistake that most often breaks phones. A full `/data` restore is **only safe onto the SAME OS version**.

Why it conflicts: `/data` contains **system data** (`/data/system`) holding the **lock-screen and encryption keys** (pattern/PIN), tied to the old HyperOS build and the security chip. Restored onto a new HyperOS, the typical symptoms are:

- 🔒 Pattern/PIN **rejected**, data **fails to decrypt**.
- 💥 Settings / SystemUI **force-closes**, or a **bootloop**.

---

## If you must move data between versions

Not the full `/data`. Split it:

| Kind | How | Safe? |
|---|---|---|
| **Personal files** (photos, Download, documents) | copy normally via MTP / File Manager | ✅ always safe |
| **Apps + their data** | use an app backup: **Swift Backup** / **Neo Backup** | ✅ safe (doesn't touch system data) |
| **Full `/data` (.win)** | TWRP restore | ⛔ only onto the same OS version |

---

## The trap that surprises people

TWRP's **"Data"** backup **does NOT include photos / internal storage by default** (`/data/media`). So if you only back up "Data", **your photos are not backed up.** Tick internal storage too, or copy it manually via MTP.

> **Golden rule:** OTA without wipe = data safe automatically. Restore `/data` = only onto the same OS version.
