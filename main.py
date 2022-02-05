from telegram import (InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup)
from telegram.ext import (Updater,CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)
BTN_bugun,BTN_botinf,BTN_friends,BTN_Boss = ('🤭Crazy memories','❗️Bot haqida',"🌐Friends' list",'🟢Boss haqida')
import random
from esap import TOKEN,DB_NAME
from Db_ga import DB_H

button = ReplyKeyboardMarkup([[BTN_botinf], [BTN_bugun, BTN_friends], [BTN_Boss]], resize_keyboard=True)
db = DB_H(DB_NAME)
user_name = dict()

def fri_but():
    friends = db.names()
    buttons = []
    tmp_b = []
    for ati in friends:
        tmp_b.append(InlineKeyboardButton(ati['name'],callback_data=ati['san']))
        if len(tmp_b) == 5:
            buttons.append(tmp_b)
            tmp_b = []
    return buttons

def start(update, context):
    update.message.reply_html("🖐🏼 hello {}  \n<i>Bu bot Mening do'stlarim tug'ilgan kunlarin 🤷🏻‍♂️ esdan chig'armau uchin ishlandi😀\n </i>".format(update.message.from_user.first_name),reply_markup=button),
    return 1

def stick(update, context):
    stickers = ('☺','😊','😇','🙂','😅','😆','😁','😄','😃','😀','😂','☺','🙃','😤','😤','😭','😢','🥺','😩','😫','😟','😕','🙁',
                '☹','️','😣','😖','😔','😞','😒','😏','🥳','🤩','😎','🤓','🧐','🤨','🤪','😜')
    a = random.randrange(0, len(stickers))
    update.message.reply_html("<b>Hozir uchin sticker</b>\n\n{}".format(stickers[a]))
    return 1

def day(update, context):
    a = random.randrange(1,148)
    photo = 'qizziq/{}.jpg'.format(a)
    message = "Bu licey vaqtida bo'lg'an qizziq voqealarimizdan uzundi . Shulardi ko'rib o'tkan vaqtlardi eslap alip yuzingizga tabbasum kelgan bo'lsa men bundan hursandman\n\n"+"<b> Aytqancha yana shu knopkani basing ! </b>"
    update.message.reply_photo(open(photo,'rb'),caption=message,parse_mode='HTML')

def botinf(update, context):
    photo = 'images/{}.png'.format("image")
    message = "Bu bot bos tomonidan <b>Dostlar</b> uchun ishlab chiqildi. \n \nBu botda do'stlarning tug'ilgan kunlarini bilib olish imkoniyatiga ega"
    message1 = " bo'lib va <b>Crazy Memories</b> licey vaqtindag'i qiziqli waqiyalardi ko'riwingizga bo'ladi ! "
    message2 = " Bot kamandalari \n\n /start botni ishga tushirish uchin \n\n Fikr mulohaza qoldirmoqchi bo'lsangiz /comment kamandasidan foydalansangiz bo'ladi "
    message3 = "\n\n Agar ichingiz pishvatrg'an bo'sa /sticker kamandasini berib ko'ring \n\n Yana bir narsa bu botda mening sevimli qo'shiqlaram bar eshitiw uchin /music kamandasini berib ko'ring"
    message4 = " Yana pastda adashmasam knopkalar chiqqan bo'liwi karak shu knopkalardan bemalol foydalana olasiz . Hozicha shular . Bu bot bashqayaqqa chig'ip ketmasin !!! katta rahmat "
    message5 = message+message1+message2+message3+message4
    update.message.reply_photo(open(photo,'rb'),caption=message5,parse_mode='HTML')

def fri(update, context):
    button1 = fri_but()
    user = update.message.from_user
    user_name[user.id] = None
    update.message.reply_html(text=" Sizga do'stimiz haqida ma'lumot bermoqchiman \n <b>Friend</b> bittasini tanlang", reply_markup=InlineKeyboardMarkup(button1))

def boss(update, context):
    photo = 'images/{}.webp'.format(45)
    message = " Bu bot <b> ?????? </b> tomonidan do'stlar uchin ishlab chiqildi ." \
              "\nBu bot sizga ozgina bo'lsa ham foydasi tekganidan hursandman . \nBiz yurishda davom etamiz . \n                  <u>HUEVO</u> "
    update.message.reply_photo(open(photo,'rb'),caption=message,parse_mode='HTML')

def inline_call(update, context):
    qw=update.callback_query
    qw.message.delete()
    date = db.get_names(int(qw.data))
    photo_path = 'images/{}.jpg'.format(int(qw.data))
    message = "Do'stim haqida ma'lumot  \n\n<i>Name</i> <b>{}</b> \n \n".format(date['name'])+"<i>SurName</i> <b>{}</b> \n \n".format(date['surname'])+'<i>Date of birthday </i> <b>{}</b> '.format(date['year'])+" <b>{}</b>".format(date['month'])+" <b>{}</b>".format(date['day']+
               " \n\nDo'stimizning tug'ilgan kunini yodda saqlang ! ")
    qw.message.reply_photo(open(photo_path,'rb'),caption=message,parse_mode='HTML')

def music(update,context):
    a = random.randrange(1,11)
    music_name='music/{}.mp3'.format(a)
    message = '<b>Music</b>'
    update.message.reply_audio(open(music_name,'rb'),caption=message,parse_mode='HTML')
    return 1

def comment(update,context):
    photo = 'images/{}.jpg'.format("comment1")
    mesage= "Siz Comment bo'limini tanladingiz ?. O'z fikr mulohazalaringizni,takliflaringizni comentariya qilib yozib qoldirishingiz mumkin\n"
    update.message.reply_photo(open(photo,'rb'),caption=mesage)
    return 2

def com(update,context):
    update.message.reply_html("<b>Fikr bildirganingiz uchin katta rahmat </b>\n <i>Yana bot funcsiyalaridan foydalanishingiz mumkin </i>")
    return 1

def main():
    updater = Updater(TOKEN,use_context=True)
    dis = updater.dispatcher
    dis.add_handler(CallbackQueryHandler(inline_call))
    conv_hand=ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            1:[
                MessageHandler(Filters.regex('^('+BTN_bugun+')$'), day),
                MessageHandler(Filters.regex('^(' + BTN_Boss + ')$'), boss),
                MessageHandler(Filters.regex('^(' + BTN_friends + ')$'), fri),
                MessageHandler(Filters.regex('^(' + BTN_botinf + ')$'), botinf),
                CommandHandler('sticker', stick),
                CommandHandler('music', music),
                CommandHandler('comment', comment),
                CommandHandler('start', start)
            ],
            2:[
                MessageHandler(Filters.text, com)
            ],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dis.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()

main()