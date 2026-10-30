# 📥 Install & Go Back — OrangeFox

[← OrangeFox guide](README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](pasang.md)

---

## Download

Open **[Releases](https://github.com/cogan17/TWRP-14T-PRO/releases)** → a release tagged **`ofox-v…`** (not `v…`, which is TWRP). The firmware version in its title must **match** your HyperOS (*Settings → About phone*).

| File | Use |
|---|---|
| **`PAKET-OrangeFox-rothko-<version>.zip`** (*package*) | The full package: flash it in recovery **or** extract it for a PC |
| `OrangeFox-rothko-<version>.img` | The OrangeFox image alone (for Install/Flash Image) |
| `STOK-vendor_boot-<version>.img` (*stock*) | Xiaomi's original — **removes** the custom recovery |

What's in the package:

| File | Use |
|---|---|
| `1-PASANG-ORANGEFOX.bat` (*install OrangeFox*) | Install OrangeFox from a PC (FASTBOOT) |
| `2-KEMBALIKAN-STOK.bat` (*back to stock*) | Back to stock, no custom recovery |
| `3-KEMBALI-KE-TWRP.bat` (*back to TWRP*) | Reinstall the latest TWRP from a PC (FASTBOOT) |
| `OrangeFox-…img` · `TWRP-…img` · `STOK-…img` | The three images above, sha256-checked by the `.bat` scripts |
| `PANDUAN-ORANGEFOX.html` | Full step-by-step guide (in Indonesian), works offline and prints |
| `BACA-SAYA.txt` (*read me*) | Short how-to + SHA256 |

---

## Install OrangeFox

### From TWRP (no PC — easiest)

1. Copy **`PAKET-OrangeFox-rothko-<version>.zip`** to the phone. **No need to extract it.**
2. [Enter TWRP](../masuk-twrp.en.md) → **Install** → pick that zip → swipe.
3. Wait for **Berhasil** (*success*) → **Reboot → Recovery**.

The zip checks the phone and the file, writes OrangeFox to `vendor_boot`, then reads it back. If anything doesn't match, **nothing is written**.

### From a PC (FASTBOOT)

1. Extract the package into the **platform-tools** folder.
2. Power off → hold **Power + Volume Down** until **FASTBOOT** → plug in the cable.
3. Double-click **`1-PASANG-ORANGEFOX.bat`** → follow the prompts.

### First start

- Enter OrangeFox the same way as TWRP: from a powered-off phone, hold **Power + Volume Up**.
- OrangeFox asks for your **pattern** → draw your lock-screen pattern. Data, photos and Download open up.
- Try the touchscreen, then **Menu → Reboot → System** to make sure Android starts normally.

## Update OrangeFox

Same as installing: flash the new package zip in OrangeFox (**Files** → tap the zip → **Install ZIP**), or run `1-PASANG-ORANGEFOX.bat` from a PC.

## Back to TWRP

| From | How |
|---|---|
| **OrangeFox** | **Files** → tap the TWRP package zip (`PAKET-TWRP-…zip`, v1.4+) → **Install ZIP** → swipe |
| **OrangeFox** (image) | **Files** → tap `TWRP-rothko-….img` → **Flash Image File** → pick **`vendor_boot`** → swipe |
| **PC** | Phone in FASTBOOT → **`3-KEMBALI-KE-TWRP.bat`** |

> ⚠️ In the Indonesian OrangeFox UI, **"Muat" means *Mount***, not Install. Installing a file always starts from **Files** (tap the file).

## Back to stock (no custom recovery)

Phone in FASTBOOT → **`2-KEMBALIKAN-STOK.bat`**. Or in OrangeFox: **Files** → `STOK-vendor_boot-….img` → **Flash Image File** → **`vendor_boot`**.

## ⚠️ Important

- The **`STOK-…`** file removes the custom recovery. Don't mix it up with `OrangeFox-…` or `TWRP-…`.
- **Don't factory reset** from recovery — it triggers FRP ([Reset & FRP](../reset-dan-frp.en.md)).
- Phone keeps entering recovery and won't leave? Hold **Power + Volume Down** until FASTBOOT, then run a `.bat` from a PC.
- Nothing on this page erases data on the phone.
