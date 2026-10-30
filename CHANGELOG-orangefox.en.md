# 📝 Release Notes — OrangeFox

[← OrangeFox guide](docs/orangefox/README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](CHANGELOG-orangefox.md)

The top version = the latest one on [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases) (tags `ofox-…`). TWRP release notes: [CHANGELOG.en.md](CHANGELOG.en.md).

## ofox-v1.0 — 30 Oct 2026

The first OrangeFox release for rothko, firmware HyperOS OS3.0.301.0.WNNIDXM (Android 16).

### ✨ What's new
- **OrangeFox R12** (`fox_16.0`) from the same device tree as TWRP: boots, touchscreen, a two-part `vendor_boot` like stock.
- Unlock data with your **pattern** (Gatekeeper). The Weaver chip, which can't be used in recovery, is skipped quickly, so it no longer hangs at "Trying Decryption".
- Indonesian built in, a full file manager, a **KernelSU modules** menu.
- Restoring Data on Android 16 doesn't fail with `extractTarFork() … 255`.
- A full package: the zip can be flashed in TWRP/OrangeFox or used from a PC (`1-PASANG-ORANGEFOX.bat`, `2-KEMBALIKAN-STOK.bat`, `3-KEMBALI-KE-TWRP.bat`).

### 🔒 Hidden for safety
- **Flash current OrangeFox** and auto-reflash after flashing a ROM: they repack `vendor_boot` in a way not yet tested on this phone.

Tested by the owner on the phone (test build, 30 Oct 2026): boot, touchscreen, pattern decryption.
