# 🩺 Issues & Logs — OrangeFox

[← OrangeFox guide](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](masalah-dan-log.md)

If something goes wrong, **don't guess** — grab a log and send it.

---

## Getting a log

| Way | Steps |
|---|---|
| **On the phone** | **Menu → Copy Log to SD**. The log is saved on internal storage (`Fox` folder). Do it **before rebooting** — the recovery log is gone once the phone restarts. |
| **From a PC, OrangeFox still running** | Run **`3-AMBIL-LOG.bat`** (*get log*) from the TWRP package, or `adb pull /tmp/recovery.log` |
| **Phone bootloops** | **`4-LOG-BOOTLOOP.bat`** from the TWRP package — see [TWRP Issues & Logs](../masalah-dan-log.en.md#for-a-bootloop--the-order-matters) |

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| Stuck at **"Trying Decryption"** | OrangeFox test packages from before 30 Oct waited forever for the Weaver chip | Use **ofox-v1.0** or newer |
| Pattern refused | Wrong pattern / protector | [Encryption & Pattern](../enkripsi-dan-pola.en.md); don't retry over and over |
| Can't find an Install menu | OrangeFox installs from **Files** | Tap the file → **Install ZIP** / **Install Image** |
| "Muat" doesn't install anything | "Muat" = **Mount**, not Install | See the [Menu Tour](menu.en.md) |
| Phone keeps entering recovery | *boot-recovery* loop | Hold **Power + Volume Down** → FASTBOOT → a `.bat` from a PC |
| Second Space won't unlock | User 999's keys were lost in a factory reset from recovery | Can't be recovered |
| APKs won't install after a factory reset | FRP | [Reset & FRP](../reset-dan-frp.en.md) |
| Restoring Data fails with `extractTarFork() … 255` | An old TWRP bug | ofox-v1.0 already carries the fix; emergency: [Backup → Restoring Data](../backup.en.md#restoring-data) |
| Want to go back to TWRP | — | [Install & Go Back](pasang.en.md#back-to-twrp) |

## Most useful to send

- The log from **Copy Log to SD**, or `recovery.log` — for almost any problem.
- `console-ramoops-0` — for a bootloop.
- A photo of the screen at the error, with a few lines above it.
