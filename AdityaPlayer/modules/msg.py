# AdityaPlayer (Telegram bot project )
# Copyright (C) 2021  Aditya Halder

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from AdityaPlayer.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**👋 Ɦɘɭɭø [{}](tg://user?id={}),**\n\n**🤖 Ɩ ƛɱ ƛɳ Ʌɗⱱɑɳƈɘɗ Ƥɤɘɱɩʋɱ Ɱʋsɩƈ Ƥɭɑƴɘɤ Ɓøʈ Ƈɤɘɑʈɘɗ Ɓƴ [Ʌɗɩtyɑ](t.me/AdityaHalder) ƒøɤ Ƥɭɑƴɩɳʛ Ɱʋsɩƈ ɩɳ Ƭɘɭɘʛɤɑɱ Ƈɦɑɳɳɘɭs & Ɠɤøʋƥs.**\n\n**✅ Sɘɳɗ Ɱɘ /help ƒøɤ Ɱøɤɘ Ɩɳƒø ...**"
      HELP_MSG = [
        ".",
f"""
**👋 Ɦɘƴ Wɘɭƈøɱɘ Ɓɑƈƙ ʈø {PROJECT_NAME}**

**♻️ {PROJECT_NAME} Ƈɑɳ Ƥɭɑƴ Ɱʋsɩƈ ɩɳ Yøʋɤ Ɠrøʋƥs & Ƈɦɑɳɳɘɭs Vøɩƈɘ Ƈɦɑʈs.**

**🤖 Ʌssɩsʈɑɲʈ Ʋsɘɤɓøʈ >> @{ASSISTANT_NAME}**\n\n**Ƈɭɩƈƙ Ɲɘxʈ ƒøɤ Iɳsʈɤʋƈʈɩøɳs ...**
""",

f"""
**⚙ Sɘʈʈɩɳʛ ƲƤ ⚙**

1) Ɱɑƙɘ Ɱɘ Ʌɗɱɩɳ Iɳ Ɠɤøʋƥ/Ƈɦɑɳɳɘɭ
2) Sʈɑɤʈ ɑ Vøɩƈɘ Ƈɦɑʈ
3) Sɘɳɗ /play [Søɳʛ Ɲɑɱɘ] ƒøɤ ʈɦɘ Fɩɤsʈ Ƭɩɱɘ Ɓƴ ɑɳ Ʌɗɱɩɳ

**Ɩƒ Ʌssɩsʈɑɲʈ Ʋsɘɤɓøʈ Jøɩɳɘɗ Ƭɦɘɳ Eɲjøƴ Ɱʋsɩƈ, Iƒ Ɲøʈ Ƭɦɘɳ Ʌɗɗ @{ASSISTANT_NAME} ʈø Yøʋɤ Ɠɤøʋƥ ɑɳɗ Ʀɘʈɤƴ**

**Føɤ Ƈɦɑɳɳɘɭ Ɱʋsɩƈ Ƥɭɑƴ**
1) Ɱɑƙɘ Ɱɘ Ʌɗɱɩɳ øƒ Yøʋɤ Ƈɦɑɳɳɘɭ 
2) Sɘɳɗ /userbotjoinchannel ɩɳ Lɩɳƙɘɗ Ɠɤøʋƥ
3) Ɲøω Sɘɳɗ Ƈøɱɱɑɳɗs ɩɳ Lɩɳƙɘɗ Ɠɤøʋƥ

**Ƈøɱɱɑɳɗs**

**🎧 Søɳʛ Ƥɭɑƴɩɳʛ**

- /yt [Søɳʛ Ɲɑɱɘ] : Ƥɭɑƴ Søɳʛ Vɩɑ YøʋƬʋɓɘ Ɱʋsɩƈ (ωɩʈɦ ƈɦøsɘ øƥʈɩøŋ)
- /play [Søɳʛ Ɲɑɱɘ] : Ƥɭɑƴ Søɳʛ Vɩɑ YøʋƬʋɓɘ Ɱʋsɩƈ (ωɩʈɦøʋʈ ƈɦøsɘ øƥʈɩøŋ)
- /play [Vɩɗɘø   Lɩɳƙ] : Ƥɭɑƴ Søɳʛ Vɩɑ YøʋƬʋɓɘ Lɩɳƙ
- /play [Ƭɑʛ  ʈø Fɩɭɘ] : Ƥɭɑƴ ɤeplied audio
- /dplay: Ƥɭɑƴ Søɳʛ Vɩɑ Ɗɘɘʑɘɤ
- /splay: Ƥɭɑƴ Søɳʛ Vɩɑ Jɩø Sɑɑⱱɳ

**🔄 Ƥɭɑƴɘɤ Ƈøɲʈɤøɭ**

- /player: Øƥɘɳ Sɘʈʈɩɳʛs Ɱɘɳʋ øƒ Ƥɭɑƴɘɤ
- /skip: Sƙɩƥ ʈɦɘ Ƈʋɤɤɘɲʈ Ƭɤɑƈƙ
- /pause: Ƥɑʋsɘ Ƈʋɤɤɘɲʈ Ƭɤɑƈƙ
- /resume: Ʀɘsʋɱɘ ʈɦɘ Ƥɑʋsɘɗ Ƭɤɑƈƙ
- /end: Sʈøƥ ʈɦɘ Ɱɘɗɩɑ Ƥɭɑƴɘɤ
- /cuɤɤent: Sɦøωs ʈɦɘ Ƈʋɤɤɘɲʈ Ƥɭɑƴɩɳʛ Ƭɤɑƈƙ
- /playlist: Sɦøωs ʈɦɘ Søɳʛs Ƥɭɑƴɭɩsʈ

**Ƥɭɑƴɘɤ Ƈøɱɱɑɳɗs ɑɤɘ Øŋɭƴ ƒøɤ Ʌɗɱɩɳs øƒ ʈɦɘ Ɠɤøʋƥ.**
""",
        
f"""
**🎧 Ƈɦɑɳɳɘɭ Ɱʋsɩƈ Ƥɭɑƴ**

🤖 Føɤ Lɩɳƙɘɗ Ɠɤøʋƥ Ʌɗɱɩɳs Øŋɭƴ:

- /cplay [song name] - Ƥɭɑƴ Søɳʛ Vɩɑ YøʋƬʋɓɘ
- /cdplay [song name] - Ƥɭɑƴ Søɳʛ Vɩɑ Ɗɘɘʑɘɤ
- /csplay [song name] - Ƥɭɑƴ Søɳʛ Vɩɑ Jɩø Sɑɑⱱɳ
- /cplaylist - Sɦøωs ʈɦɘ Søɳʛs Ƥɭɑƴɭɩsʈ
- /cccurrent - Sɦøωs ʈɦɘ Ƈʋɤɤɘɲʈ Ƥɭɑƴɩɳʛ Ƭɤɑƈƙ
- /cplayer - Sɦøωs ʈɦɘ Ƈʋɤɤɘɲʈ Ƥɭɑƴɩɳʛ Ƭɤɑƈƙ & Ƥɑɳɘɭ
- /cpause - Ƥɑʋsɘ Ƈʋɤɤɘɲʈ Ƭɤɑƈƙ
- /cresume - Ʀɘsʋɱɘ ʈɦɘ Ƥɑʋsɘɗ Ƭɤɑƈƙ
- /cskip - Sƙɩƥ ʈɦɘ Ƈʋɤɤɘɲʈ Ƭɤɑƈƙ
- /cend - Sʈøƥ ʈɦɘ Ɱɘɗɩɑ Ƥɭɑƴɘɤ
- /userbotjoinchannel - Iɳⱱɩʈɘ Ʌssɩsʈɑɲʈ ʈø Yøʋɤ Ƈɦɑʈ

**channel ɩs Ʌɭsø Ƈɑɳ ɓɘ Ʋsɘɗ Iɳsʈɘɑɗ øƒ c** ( /cplay = /channelplay )

⚪️ **Iƒ Yøʋ Ɗøɲ'ʈ Lɩƙɘ ʈø Ƥɭɑƴ ɩɳ Lɩɳƙɘɗ Ɠɤøʋƥ:**

1) Ɠɘʈ Yøʋɤ Ƈɦɑɳɳɘɭ IƊ.
2) Ƈɤɘɑʈɘ ɑ Ɠɤøʋƥ ωɩʈɦ Ƭɩʈʈɭɘ:~ Channel Music: your_channel_id
3) Ʌɗɗ Ɓøʈ ɑs Ƈɦɑɳɳɘɭ Ʌɗɱɩɳ ωɩʈɦ Fʋɭɭ Ƥɘɤɱɩssɩøɳs
4) Ʌɗɗ @{ASSISTANT_NAME} ʈø ʈɦɘ Ƈɦɑɳɳɘɭ ɑs ɑɳ Ʌɗɱɩɳ.
5) Sɩɱƥɭƴ Sɘɳɗ Ƈøɱɱɑɳɗs ɩɳ Yøʋɤ Ɠɤøʋƥ.
""",

f"""
**🛠 Ɱøɤɘ Ƭøøɭs**

- /reload: ʋƥɗɑʈɘs Ʌɗɱɩɳ Iɳƒø øƒ Yøʋɤ Ɠɤøʋƥ. Ƭɤƴ ɩʈ ɩƒ Ɓøʈ ɩsɲ'ʈ Ʀɘƈøʛɳɩʑɘ Ʌɗɱɩɳs
- /userbotjoin: Iɳⱱɩʈɘ @{ASSISTANT_NAME} Ʋsɘɤɓøʈ ʈø Yøʋr Ƈɦɑʈ

**⚔️ Ƈøɱɱɑɳɗs ƒøɤ Sʋɗø Ʋsɘɤs**

 - /userbotleaveall - Ʀɘɱøⱱɘ Ʌssɩsʈɑɲʈ Fɤøɱ Ʌɭɭ Ƈɦɑʈs
 - /gcast <Ʀɘƥɭƴ ʈø Ɱɘssɑʛɘ> - Ɠɭøɓɑɭɭƴ Ɓɤøɑɗƈɑsʈ Ʀɘƥɭɩɘɗ Ɱɘssɑʛɘ ʈø Ʌɭɭ Ƈɦɑʈs
 - /pmpermit [on/off] - Eɳɑɓɭɘ øɤ Ɗɩsɑɓɭɘ ƤɱƤɘɤɱɩʈ Ɱɘssɑʛɘ
**Sʋɗø Ʋsɘɤs Ƈɑɳ Exɘƈʋʈɘ ɑɲƴ Ƈøɱɱɑɳɗs ɩɳ ɑɲƴ Ɠɤøʋƥs**

"""
      ]

