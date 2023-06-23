from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
import sqlite3

db = sqlite3.connect("./daemozzecane.db")

with open ("token.txt","r") as f:
    TOKEN = f.read()
    print(TOKEN)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("daemozzecane",elenco_dae))
    app.run_polling()
    
async  def elenco_dae(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db.cursor()
    query = "SELECT * FROM DAE_Mozzecane"
    cursor.execute(query)
    rows = cursor.fetchall()
    lista = []
    for row in rows:
        print("Nomestruttura" , row[0]);
        print("Indirizzo" , row[1]);
        parola = "link" + lista.replace(row[4]);
        lista.append("Nome struttura:" + row[0] + '\n' + "Indirizzo:" + row[1] + '\n' + "Link:" + row[4])
        #"Link:" + row[4]
        #parola
        
    cursor.close();

    result_list = lista
    message = ''. join(result_list)
    await update.message.reply_text(message)

if __name__ == '__main__':
    main()
