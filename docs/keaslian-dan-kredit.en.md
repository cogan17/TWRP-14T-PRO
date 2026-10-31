# 🔏 Authenticity & Credits

[← Back to README](../README.en.md) · <img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> [Bahasa Indonesia](keaslian-dan-kredit.md)

TWRP and OrangeFox for rothko in this repo are built and released automatically by GitHub Actions from **[cogan17/TWRP-14T-PRO](https://github.com/cogan17/TWRP-14T-PRO)**. The release packages (zip) and their TWRP/OrangeFox images are **digitally signed**, so anyone can prove where they came from. (`STOK-vendor_boot` is deliberately not signed — it's Xiaomi's original file, not made by this repo.)

> What this proves is that **these TWRP and OrangeFox builds/ports for rothko** were built and released from cogan17's repo. TWRP itself is the work of TeamWin, OrangeFox the work of the OrangeFox Recovery Project, together with the contributors listed under [Credits](#-credits).

---

## How to check authenticity

1. **Proof page:** **[github.com/cogan17/TWRP-14T-PRO/attestations](https://github.com/cogan17/TWRP-14T-PRO/attestations)** — the list of signed files with their fingerprints (sha256).
2. **With the GitHub CLI:**
   ```
   gh attestation verify <file> --repo cogan17/TWRP-14T-PRO
   ```
   Only official files from this repo pass.
3. **On the phone** (TWRP → *Advanced → Terminal*; OrangeFox → *Menu → Other → Terminal*):
   - `cat /BUILD-INFO.txt` — origin repo, commit and build date.
   - Compare the partition with the sha256 of the `.img` file on the [Releases](https://github.com/cogan17/TWRP-14T-PRO/releases) page:
     ```
     head -c 67108864 /dev/block/by-name/vendor_boot$(getprop ro.boot.slot_suffix) | sha256sum
     ```
     (`67108864` = the `.img` file size in bytes.)

## What it proves — and what it doesn't

| If someone… | Result |
|---|---|
| re-shares a release file and claims they made it | ✅ refuted — its fingerprint matches this repo's signature |
| changes the file slightly (e.g. the name in `BUILD-INFO.txt`) | ✅ exposed — it becomes a different file that fails verification for this repo |
| forks the repo and builds it themselves | ✅ their signature names **their repo**; the dated commit history here shows who came first |
| copies the code | not prevented (open project) — but its origin can still be proven |

`BUILD-INFO.txt` is just a stamp anyone can edit; the **digital signature** is the proof.

---

## 🙏 Credits

| Who | Contribution |
|---|---|
| **[JonesqPacMan](https://github.com/JonesqPacMan)** | Original rothko device tree: [android_device_xiaomi_rothko_twrp](https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp) ("Initial Release", 21 Sep 2025). This repo continues directly from its last commit (`b246a04`). The same tree is used for **both TWRP and OrangeFox** |
| **Cogan17** | Maintainer: port to HyperOS 3 / Android 16, pattern decryption (Gatekeeper), two-fragment vendor_boot, firmware sync, end-user package & scripts, CI and releases; **OrangeFox** port (`fox_16.0` build, Weaver→Gatekeeper vold patch, install/go-back package) |
| **[TeamWin Recovery Project](https://twrp.me)** | TWRP itself — also the base of OrangeFox |
| **[OrangeFox Recovery Project](https://gitlab.com/OrangeFox)** | OrangeFox itself: recovery code, theme, the `fox_16.0` manifest, `foxcli`. Core team per OrangeFox's *About* page: **DarthJabba9**, **MrYacha**, **fordownloads** |
| **[minimal-manifest-twrp](https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp)** | TWRP build source manifest |
| **AOSP (Google) & LineageOS** | Android platform code built along with it |
| **phhusson** | `vendor_lptools` |
| **[ssut / payload-dumper-go](https://github.com/ssut/payload-dumper-go)** | Extracts the official firmware in the workflow |
| **[XiaomiFirmwareUpdater](https://github.com/XiaomiFirmwareUpdater)** | Official ROM catalog |
| **Xiaomi & MediaTek** | Firmware, kernel modules and vendor blobs — taken from the official ROM, property of their respective owners |

Want to use this tree for your own repo? Go ahead — keep the credits above, and read the [technical notes](../arsip/developer.en.md) first.
