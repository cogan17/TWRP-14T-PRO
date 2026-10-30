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

## A real case on this phone (30 Oct 2026)

What the owner did, ending with FRP stuck on:

1. Factory reset from TWRP.
2. Booted into Android and reached the setup screens.
3. When asked for a **Google account**, **left setup** (no sign-in) and went straight to TWRP.
4. **Restore → Data** from an older backup.
5. Android booted normally with no setup screens — the restored Data came from a phone that had already finished setup. FRP stayed on and can no longer be cleared the normal way.

The lesson: the **Google account** screen during setup is the only official chance to turn FRP off. Once Data is restored, that screen never comes back.

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

## What works: flash the full stock ROM

**Proven on the owner's phone (30 Oct 2026):** flashing the official HyperOS fastboot ROM cleared FRP — the built-in app installer works again.

1. **Copy all backups to a PC first.** A full flash erases all data, including the TWRP backup folder on internal storage.
2. Use the official **fastboot** ROM of the **same version** as on the phone (currently `OS3.0.301.0.WNNIDXM`) — the TWRP/OrangeFox images in Releases are built for that version.
3. In Mi Flash pick **`clean all`**. ⛔ **Not `clean all and lock`** — that relocks the bootloader and TWRP can't be installed until you unlock again.
4. On the setup screens, **sign in with your own Google account** (the one last used on this phone). Don't skip it.
5. The phone is now fully stock: TWRP, kernel and root are gone. Reinstall TWRP with `1-PASANG-TWRP.bat` from [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases), then your kernel and root as usual.

## What doesn't work

- ❌ Waiting doesn't clear it — Android turns it back on at every boot.
- ❌ Signing out of and back into Gmail in Settings isn't enough — the flag is owned by the setup screens, not by the account.
- ❌ A HyperOS update (OTA) doesn't remove it.
- ⛔ **Don't use third-party "FRP unlock tools"** — they are the same tools used to unlock stolen phones, many carry malware, and your phone doesn't need them.
- ⛔ Don't tamper with the `frp` partition.

## How to avoid it

1. Factory reset **only from HyperOS Settings**.
2. Already reset from TWRP and sitting on the setup screens? **Don't leave the Google account screen to restore Data.** Finish setup with the **same Google account** — that's the official way to turn FRP off. Note: it hasn't been tested on this phone whether FRP stays off if Data is restored afterwards.
3. Restoring Data? **Don't factory reset first.** **Restore → Data** already empties Data by itself before restoring, so a separate reset isn't needed. See [Backup](backup.en.md).
4. After restoring Data, check your root modules (e.g. NoMount) — they sometimes need reinstalling. See [Root & Kernel](root-dan-kernel.en.md).
