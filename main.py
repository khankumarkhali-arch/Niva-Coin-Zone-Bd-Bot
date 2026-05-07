from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    
    welcome_text = f"""🎉 স্বাগতম, {user_name}!

❌ Coin buy: OFF
🚨 Emergency contracts: ON  
📞 Support: @Niva_CoinZoneBd

🚀 Fast selling, premium support & secure service!"""
    
    keyboard = [
        [InlineKeyboardButton("🛒 RESTART BOT", url="https://t.me/" + context.bot.username + "?start=start")],
        [InlineKeyboardButton("📞 SUPPORT", url="https://t.me/Niva_CoinZoneBd")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot চালু হইছে...")
app.run_polling()