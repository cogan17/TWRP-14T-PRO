# 🔁 Factory Reset & FRP

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](reset-dan-frp.md)

> ⛔ **Don't factory reset from TWRP.** If you need a reset, use **HyperOS Settings → About phone → Factory reset**.

---

## What is FRP?

**FRP (Factory Reset Protection)** is Android's anti-theft protection. After a reset that was **not** done through Android's Settings, Android assumes the phone may be stolen and restricts it until the owner proves themselves — by **signing in with the same Google account** on the setup screens.

On Android 15/16 (HyperOS 3), a reset from TWRP **counts** as an untrusted reset. FRP turns on, and because the setup screens were skipped, the flag stays behind.

## Symptoms

- Installing an APK the normal way (tap it in a file manager) fails: **"App not installed"**.
- Android's log says: `Can't install packages while in secure FRP`.
- Everything else works.

## What still works

| How the app is installed | While FRP is on |
|---|---|
| **Play Store** (banking apps included) | ✅ normal |
| **MT Manager** / **App Manager** with root | ✅ works |
| `adb install` / `pm install` from a PC | ✅ works |
| Tap an APK → HyperOS's built-in installer | ❌ blocked |

So the phone stays usable every day. Install APKs from outside the Play Store through MT Manager or App Manager.

## The official way to clear it

FRP is cleared officially when the phone goes through the **setup screens** and you **sign in with the same Google account** as before the reset. That happens if you ever reset **from HyperOS Settings** (this erases data — back up first).

- ❌ Waiting doesn't clear it — Android turns it back on at every boot.
- ❌ Signing out of and back into Gmail in Settings isn't enough — the flag is owned by the setup screens, not by the account.
- ❌ A HyperOS update (OTA) doesn't remove it.
- ⛔ **Don't use third-party "FRP unlock tools"** — they are the same tools used to unlock stolen phones, many carry malware, and your phone doesn't need them.
- ⛔ Don't tamper with the `frp` partition.

## How to avoid it

1. Factory reset **only from HyperOS Settings**.
2. Restoring Data? **Don't factory reset first.** **Restore → Data** already empties Data by itself before restoring, so a separate reset isn't needed. See [Backup](backup.en.md).
3. After restoring Data, check your root modules (e.g. NoMount) — they sometimes need reinstalling. See [Root & Kernel](root-dan-kernel.en.md).
