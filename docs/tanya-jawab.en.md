# ❓ FAQ

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](tanya-jawab.md)

Common questions, from real experience on this phone.

---

### Download and install

**Which file do I download?** Always from **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)**, the version that **matches your HyperOS**. Not from the *Actions* tab — the *artifacts* there are for testing, not for installing.

**`TWRP-…` vs `STOK-…`?** `TWRP-…` installs TWRP. `STOK-…` (*stock*) **removes** TWRP and goes back to Xiaomi's original. Both go to `vendor_boot`, so don't mix them up.

**The package zip is refused: *Invalid zip file format*.** Zips from v1.3 and older are for a PC only. Since **v1.4** the package zip can be flashed straight in TWRP. Use the latest version, or **Install Image** with the `TWRP-…` file.

**How do I know the file is genuine?** See [Authenticity & Credits](keaslian-dan-kredit.en.md).

### Entering and using TWRP

**How do I enter TWRP?** From a powered-off phone, hold **Power + Volume Up**. Details: [Enter TWRP](masuk-twrp.en.md).

**The phone keeps going into recovery and won't leave.** That's a *boot-recovery* loop. Hold **Power + Volume Down** until FASTBOOT, then run `1-PASANG-TWRP.bat` or `2-KEMBALIKAN-STOK.bat` from a PC.

**My pattern is refused / data won't unlock.** See [Encryption & Pattern](enkripsi-dan-pola.en.md). Don't retry the pattern over and over.

**Second Space (user 999) won't unlock.** If you ever factory reset from TWRP, Second Space's keys were erased with it and its data can't be recovered.

**The battery always shows 100%.** Fixed since **v1.2**.

**Which menus are dangerous?** See the [TWRP Menu Tour](menu-twrp.en.md).

### Backup, restore, reset

**Restoring Data fails with `extractTarFork() … 255`.** A bug in v1.4 and older, fixed in **v1.5**. Emergency steps: [Backup → Restoring Data](backup.en.md#restoring-data).

**After a factory reset from TWRP, APKs won't install.** That's **FRP**. The Play Store and MT Manager still work; flashing the full stock ROM clears it. Explained in [Reset & FRP](reset-dan-frp.en.md).

**Can I restore a Data backup onto a different HyperOS version?** No. See [Update HyperOS](update-hos.en.md).

**File system repair fails with *device or resource busy*.** Turn MTP off first: **Mount → Disable MTP**.

### Updates and more

**TWRP is gone after a HyperOS update.** Expected — the update overwrites `vendor_boot`. Install the matching TWRP again. See [Update HyperOS](update-hos.en.md).

**How do I update TWRP?** Flash the newest package zip in TWRP, or run `5-UPDATE-LEWAT-TWRP.bat` from a PC. See [Install / Update](pasang.en.md).

**Root modules act up after a restore.** Reinstall the module. See [Root & Kernel](root-dan-kernel.en.md).

**TWRP or OrangeFox?** Both are made for this phone and can replace each other. See the [OrangeFox guide](orangefox/README.en.md).
