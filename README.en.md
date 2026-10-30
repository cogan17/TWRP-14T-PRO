<h1 align="center">TWRP · Xiaomi 14T Pro</h1>

<p align="center">
  <img src="https://files.catbox.moe/66e3dq.png" alt="TWRP + Xiaomi" width="220"/>
</p>

<p align="center">
  <code>rothko</code> &nbsp;·&nbsp; HyperOS &nbsp;·&nbsp; Android 16
</p>

<p align="center">
  <a href="README.md"><img src="https://flagcdn.com/24x18/id.png" width="22" alt=""> Bahasa Indonesia</a> &nbsp;·&nbsp; <b><img src="https://flagcdn.com/24x18/gb.png" width="22" alt=""> English</b>
</p>

<p align="center">
  <a href="https://github.com/cogan17/TWRP-14T-PRO/releases"><b>⬇️ Download</b></a>
  &nbsp;·&nbsp;
  <a href="docs/pasang.en.md"><b>📖 Guide</b></a>
  &nbsp;·&nbsp;
  <a href="CHANGELOG.en.md"><b>📝 Release Notes</b></a>
  &nbsp;·&nbsp;
  <a href="https://t.me/coganTWRP"><b>💬 Telegram Community</b></a>
</p>

> [!CAUTION]
> **Understand the risks before using recovery.** Mistakes during flashing, wiping, or restoring can cause data loss or leave the device unusable. Keep important backups outside the device and read [how to return to stock](docs/kembali-ke-stok.en.md). You decide which actions to perform in TWRP; the maintainer/developer accepts no responsibility for resulting damage or data loss.

> [!TIP]
> A patched kernel with integrated **SUSFS** and additional features is available. [Check it out](https://github.com/cogan17/Cogan-Kernel).

---

### 📖 User Guide

|   |   |
|---|---|
| 📥 **[Install / Update TWRP](docs/pasang.en.md)** | From a PC (`.bat`) or straight from TWRP |
| 🔑 **[Enter TWRP](docs/masuk-twrp.en.md)** | Buttons or Termux |
| 🧭 **[TWRP Menu Tour](docs/menu-twrp.en.md)** | What each menu does, which are dangerous |
| 💾 **[Backup](docs/backup.en.md)** | Data & key partitions |
| 🔄 **[Update HyperOS](docs/update-hos.en.md)** | Update without losing data |
| 🪄 **[Root & Kernel](docs/root-dan-kernel.en.md)** | Install a kernel/root, recover from a bootloop |
| ↩️ **[Back to Stock](docs/kembali-ke-stok.en.md)** | Undo TWRP / fix bootloop |
| 🔐 **[Encryption & Pattern](docs/enkripsi-dan-pola.en.md)** | Unlock encrypted data |
| 🔁 **[Reset & FRP](docs/reset-dan-frp.en.md)** | Why not to factory reset from TWRP |
| 🩺 **[Issues & Logs](docs/masalah-dan-log.en.md)** | When something goes wrong |
| ❓ **[FAQ](docs/tanya-jawab.en.md)** | Common questions |

### 🦊 OrangeFox

A second recovery for this phone: OrangeFox, with a new look, a full file manager and KernelSU module management. It can be swapped with TWRP at any time. **[OrangeFox guide →](docs/orangefox/README.en.md)**

---

<details>
<summary>📱 <b>Device specifications</b></summary>

| Item | Detail |
|---|---|
| Chipset | MediaTek Dimensity 9300+ |
| CPU | 4× Cortex-X4 up to 3.4 GHz |
| GPU | Immortalis-G720 MC12 |
| RAM | 12 / 16 GB |
| Display | 1220 × 2712 |
| Released | September 2024 (Android 14) |

</details>

<details>
<summary>✨ <b>What works</b></summary>

- ✅ Boot to recovery (platform + recovery fragments)
- ✅ Touchscreen
- ✅ Metadata + FBE decryption with the **pattern** (Gatekeeper)
- ✅ Change the pattern → follows automatically
- ✅ Second Space (user 999) recognized
- ✅ Backup / restore, fastbootd, MTP

</details>

---

<p align="center">
  Maintainer <b>Cogan17</b> &nbsp;·&nbsp; original tree <a href="https://github.com/JonesqPacMan/android_device_xiaomi_rothko_twrp"><b>JonesqPacMan</b></a> &nbsp;·&nbsp; <b>TeamWin Recovery Project</b>
  <br><a href="docs/keaslian-dan-kredit.en.md">🔏 Authenticity & full credits</a>
</p>
