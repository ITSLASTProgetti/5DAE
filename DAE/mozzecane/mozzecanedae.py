from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
import sqlite3

def get_token(token_file):
    with open (token_file,"r") as f:
        return f.read()
    

def main():
    TOKEN = get_token("token.txt")
    print(TOKEN)
    db = sqlite3.connect("./daedemo.db")
    app = ApplicationBuilder().token(TOKEN).build()
    #app.add_handler(CommandHandler("daemozzecane",elenco_dae_mozzecane))
    app.add_handler(CommandHandler("comuni",elenco_comuni(db)))
    app.run_polling()
    

async def elenco_comuni(db):
    query = "SELECT DISTINCT Comune FROM DAE_Veneto"
    print(query)
    cursor = db.cursor()
    print ("cursor")
    cursor.execute(query)
    print("esegui")
    rows = cursor.fetchall()
    print(rows)
    
    
async  def elenco_dae_mozzecane(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db.cursor()
    query = "SELECT * FROM DAE_Mozzecane"
    cursor.execute(query)
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Impianto sportivo 2" , url = 'https://www.google.com/maps/dir//45.3110818,10.8242112/@45.3110608,10.7541723,12z?entry=ttu')],
                                    [InlineKeyboardButton("Municipio" , url = 'https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu')],
                                    [InlineKeyboardButton("Municipio c-interno" , url = "https://www.google.com/maps/dir//45.3095247,10.8180767/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Centro famiglia" , url = "https://www.google.com/maps/dir//45.3195351,10.8310744/@45.319527,10.8288983,17z?entry=ttu")],
                                    [InlineKeyboardButton("Piazzale Chiesa" , url = "https://www.google.com/maps/dir//45.3085168,10.817186/@45.3083875,10.7471324,12z?entry=ttu")],
                                    [InlineKeyboardButton("Centro Baco da seta" , url = "https://www.google.com/maps/dir//45.306129,10.8153423/@45.3061615,10.7455298,12z?entry=ttu")],
                                    [InlineKeyboardButton("Impianto sportivo" , url = "https://www.google.com/maps/dir//45.3072852,10.8142031/@45.3075985,10.7444353,12z?entry=ttu")],
                                    [InlineKeyboardButton("palazzetto" , url = "https://www.google.com/maps/dir//45.3111473,10.8241348/@45.3110608,10.7541723,12z?entry=ttu")],
                                    [InlineKeyboardButton("Circolo Auser" , url = "https://www.google.com/maps/dir//45.3148368,10.8581046/@45.314834,10.8559142,17z?entry=ttu")]]
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - MOZZECANE" ,reply_markup=reply_markup)
    cursor.close()

    #await update.message.reply_text(message)
    

if __name__ == '__main__':
    main()
