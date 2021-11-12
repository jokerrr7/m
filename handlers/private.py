from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا **{bn}** 🎵

بامكاني تشغيل الاغاني في المكالمات الجماعيه 
قم برفعي  مشرف في قناتك مع البوت المساعد [David Music](https://t.me/YUKA_7).

قم باضافتي الى مجموعتك لتبدأ الحفله 🎶**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "لطلب المساعده", url="https://t.me/UUOUOU_7")
                  ],[
                    InlineKeyboardButton(
                        "قناة للشروحات", url="https://t.me/J_F_A_I"
                    ),
                    InlineKeyboardButton(
                        "قناة البوت", url="https://t.me/BLACK_TEAM_4"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "اضفني الى مجموعتك", url="https://t.me/MU_BL_K_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناتي الخاصه", url="https://t.me/UU_KFUF")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** يمتاز هذا البوت بالبحث والتحميل ✨
اكتب معرف البوت مع اسم الاغنيه للبحث 🔊
مثال : 
@MU_BL_K_BOT كاظم الساهر
تستطيع تحميل اي اغنيه ايضا 
بالاوامر التاليه :
- /ytp رابط الاغنيه من اليوتيوب
- /song رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه 🔊
- /play بالرد على الاغنيه او الرابط للتشغيل
- /pause لايقاف الاغنيه موقتا داخل المكالمه
- /resume لتكمله الاغنيه المتوقفه
- /stop لايقاف البوت عن تشغيل الاغنيه
- /skip لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه
- /vol لرفع مستوى صوت البوت
#ملاحظه : تستطيع ان تقوم بتشغيل اغنيه اخرى فتضاف الى الدور بعد الاغنيه الحاليه فتتنقل بينها وبين الاغاني الباقيه باستخدام امر /skip 🔖 **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناتي الخاصه", url="https://t.me/UU_KFUF")
                ],[
                    InlineKeyboardButton(
                        "الحساب المساعد", url="https://t.me/YUKA_7"
                    )
                ]
            ]
        )
   )
