# Force Subs Bot

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.

## ⚠️ Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk membantu untuk menyimpan file yang diinginkan yang dapat diakses melalui Link Khusus.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan bot ini dengan bijak.
```

### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa 1 button atau 2 button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN

## 🛡 Installation
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<details>
    <summary> <b>🔗 Deploy Force Subs Heroku </b></summary><br/>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/poocong/ForceSubs"><img src="https://img.shields.io/badge/Deploy%20Lewat%20Web%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"" /></a></p>

<p align="center"><a href="https://telegram.dog/XTZ_HerokuBot?start=cG9vY29uZy9Gb3JjZVN1YnMgbWFzdGVy"><img src="https://img.shields.io/badge/Deploy%20Lewat%20Bot%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"" /></a></p>

</details>

<details>
    <summary> <b>🔗 Extra Custom & List Vars</b></summary>

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin di BOT
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB_CHANNEL` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB_GROUP` Masukan ID dari Group Untuk Wajib Subscribenya

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

</details>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

* [! Deploy in ur vps]

````bash
git clone https://github.com/poocong/ForceSubs
cd ForceSubs
pip3 install -r requirements.txt
cp sample_config.env config.env
# edit config.env Anda dan isi VARS menggunakan nano config.env CTRL + S untuk menyimpan VARS Anda, 
# gunakan CTRL + X untuk keluar dan kembali ke direktori ForceSubs
bash start
````

## 🏷 Support   
- Follow Channel [@PocongProject](https://t.me/PocongProject) untuk info Update bot 
- Gabung Group [@PocongUserbot](https://t.me/PocongUserbot) untuk diskusi, pelaporan bug, dan bantuan tentang bot Force Subs

## 👨🏻‍💻 Credits

-  [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
-  [Risman](https://github.com/mrismanaziz) for [File-Sharing-Man](https://github.com/mrismanaziz/File-Sharing-Man)
-  Based on [CodeXBotz](https://github.com/CodeXBotz) Repo [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)
-  [Poocong](https://github.com/poocong) for [ForceSubs](https://github.com/poocong/ForceSubs)

## 📑 License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/mrismanaziz/File-Sharing-Man/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Berikan Bintang Repo ini jika Anda menyukainya ⭐⭐⭐⭐⭐**

