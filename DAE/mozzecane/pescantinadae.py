from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
import sqlite3

db = sqlite3.connect("./daepescantina.db")

with open ("token.txt","r") as f:
    TOKEN = f.read()
    print(TOKEN)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("daepescantina",elenco_dae))
    app.run_polling()
    
async  def elenco_dae(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db.cursor()
    query = "SELECT * FROM DAE_Pescantina"
    cursor.execute(query)
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Via Madonna 55" , url = 'https://www.google.com/maps/dir//45.4826831,10.8672927/@45.4827667,10.7970969,12z/data=!3m1!4b1?entry=ttu')],
                                    [InlineKeyboardButton("Via Brennero, 35" , url = 'https://www.google.com/maps/dir//45.4954529,10.8734815/@45.4954314,10.8034443,12z/data=!3m1!4b1?entry=ttu')]]
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - PESCANTINA" ,reply_markup=reply_markup)
                
        
    cursor.close()

    #await update.message.reply_text(message)

if __name__ == '__main__':
    main()
