# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /vars - Untuk melihat variable bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by @pocongonlen</b>
"""

    close = [
        [InlineKeyboardButton("close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("help & command", callback_data="help"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("about me", callback_data="about"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Jasa Pembuatan Bot: <a href='https://t.me/PoocongOnlen/182'>Pocongonlenstore v4</a>
 • Owner Repo: @kyyyynocounter

👨‍💻 Develoved by @pocongonlen</b>
"""
