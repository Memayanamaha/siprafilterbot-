class script(object):
    START_TXT = """ð·ð´ð»Lo {},
ð¼ð ð½ð°ð¼ð´ ð¸ð <a href=https://t.me/{}>{}</a> I am A Simple Auto Filter + Manual Filter + Extra Features Bot. I Can Provide Movies In Telegram Groups.I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy"""
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """â® ð¼ð ð½ð°ð¼ð´: {}
â® ð²ðð´ð°ðð¾ð: <a href=https://t.me/CyniteOfficial>Ð½Î±ÑÐ¼Î±Ð¸</a>
â® ð»ð¸ð±ðð°ðð: ð¿ððð¾ð¶ðð°ð¼
â® ð»ð°ð½ð¶ðð°ð¶ð´: ð¿ððð·ð¾ð½ ð¹
â® ð³ð°ðð° ð±ð°ðð´: ð¼ð¾ð½ð¶ð¾ ð³ð±
â® ð±ð¾ð ðð´ððð´ð: ð·ð´ðð¾ðºð
â® ð±ðð¸ð»ð³ ððð°ððð: v1.0.2 [ ð±ð´ðð° ]"""

    PRIVATEBOT_TXT = """<b>ð¿ðð¸ðð°ðð´ ð±ð¾ð ðµð¾ð ðð¾ð</b>
<b>âºâº ð³ð¾ ðð¾ð ðð°ð½ð ð° ð±ð¾ð ðð°ð¼ð´ ð»ð¸ðºð´ ðð·ð¸ð</b>
<b>âºâº ðð¸ðð· ð°ð»ð» ðð¾ðð ð²ðð´ð³ð¸ðð</b>
<b>âºâº ðð¸ðð· ðð¾ðð ð¾ðð½ð´ððð·ð¸ð¿</b>
<b>âºâº ð²ð¾ð½ðð°ð²ð ð¼ð´ <a href=https://t.me/CyniteOfficial>Ð½Î±ÑÐ¼Î±Ð¸</a></b>"""

    SOURCE_TXT = """<b>Donation</b>

âª¼ <b>ðð¨ð® ððð§ ðð¨ð§ðð­ð ðð§ð² ðð¦ð¨ð®ð§ð­ ðð¨ð® ððð¯ð ð³. 

<b>âââââââââá Payment Methods áâââââââââ

â® ðð¼ð¼ð´ð¹ð²ð£ð®ð
â® ð£ð®ðððº
â® ð£ðµð¼ð»ð²ð£ð²
â® ð£ð®ðð£ð®ð¹

_ðð¨ð§ð­ððð­ ðð ðð¨ð« ðð§ð¨ð° ððð¨ð®ð­ ðð¡ð ððð²ð¦ðð§ð­ ðð§ðð¨_
ââââââââââââá <a href=https://t.me/CyniteOfficial><b>Ð½Î±ÑÐ¼Î±Ð¸</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and Zsearcher will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Zsá´á´Êá´Êá´Ê should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¾ /filter - <code>add a filter in chat</code>
â¾ /filters - <code>list all the filters of a chat</code>
â¾ /del - <code>delete a specific filter in chat</code>
â¾ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Zsearcher Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Zsá´á´Êá´Êá´Ê supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Cynitebots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¾ /connect  - <code>connect a particular chat to your PM</code>
â¾ /disconnect  - <code>disconnect from a chat</code>
â¾ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Zsá´á´Êá´Êá´Ê

<b>Commands and Usage:</b>
â¾ /id - <code>get id of a specifed user.</code>
â¾ /info  - <code>get information about a user.</code>
â¾ /imdb  - <code>get the film information from IMDb source.</code>
â¾ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my Oá¯áEáâ¡

<b>Commands and Usage:</b>
â¾ /logs - <code>to get the rescent errors</code>
â¾ /stats - <code>to get status of files in db.</code>
â¾ /delete - <code>to delete a specific file from db.</code>
â¾ /users - <code>to get list of my users and ids.</code>
â¾ /chats - <code>to get list of the my chats and ids </code>
â¾ /leave  - <code>to leave from a chat.</code>
â¾ /disable  -  <code>do disable a chat.</code>
â¾ /ban  - <code>to ban a user.</code>
â¾ /unban  - <code>to unban a user.</code>
â¾ /channel - <code>to get list of total connected channels</code>
â¾ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â® ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â® ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â® ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â® ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â® ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#ððð°ðð«ð¨ð®ð©
â® ðð«ð¨ð®ð© âºâº {}(<code>{}</code>)
â® ðð¨ð­ðð¥ ððð¦ððð«ð¬ âºâº <code>{}</code>
â® ððððð ðð² âºâº {}
"""
    LOG_TEXT_P = """#ððð°ðð¬ðð«
â® ðð âºâº <code>{}</code>
â® ððð¦ð âºâº {}
"""
    CARBON_TXT = """ <b>ð²ð°ðð±ð¾ð½ ð¼ð¾ð³ðð»ð´</b>

<b>ðð¾ð ð²ð°ð½ ð±ð´ð°ððð¸ðµð ðð¾ðð ð²ð¾ð³ð´ð ð±ð ððð¸ð½ð¶ ðð·ð ðµð´ð°ðððð´...</b>

<b>ð²ð¾ð¼ð¼ð°ð½ð³.!</b>
<b>/carbon âºâº ðð´ð¿ð»ð ðð¾ ð°ð½ð ðð´ðð ð¼ð´ððð°ð¶ð´</b>

<b>ðð¾ððºð ð¾ð½ ð±ð¾ðð· ð¶ðð¾ðð¿ ð°ð½ð³ ð¿ð¼</b>
<b>ð²ðð´ð³ð¸ðð âºâº</b> <a href=https://youtube.com/channel/UCiaz-J50QhtJ73XEEjP_aLQ>á´á´á´ÊÉ´Éªá´á´Ê-á´ÊÉ´Éªá´á´</a></b>"""
