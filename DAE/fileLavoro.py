from telegram import Update, constants
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  CallbackContext, ApplicationBuilder,CommandHandler,ContextTypes
import sqlite3

db = sqlite3.connect("./daemozzecane.db")
db2 = sqlite3.connect("./daepastrengo.db")
db3 = sqlite3.connect("./daesommacampagna.db")
db4 = sqlite3.connect("./daepescantina.db")
db5 = sqlite3.connect("./daevigasio.db")
db6 = sqlite3.connect("./daevillafranca.db")
db7 = sqlite3.connect("./daevaleggio.db")
db8 = sqlite3.connect("./daesona.db")
db9 = sqlite3.connect("./daebussolengo.db")
db10 = sqlite3.connect("./daecastelnuovo.db")




with open ("token.txt","r") as f:
    TOKEN = f.read()
    print(TOKEN)
async def start(update, context):
    # Messaggio di benvenuto
    message = "<b>Benvenuto nel mio bot su Telegram!</b>\n\n"
    message += "<b>Utilizza i comandi seguenti per interagire con me:</b>\n"
    message += "<b>Il link del sito : https://s1010413a.wixsite.com/DAEa</b> " + "\n"
    message += "<b>/start - se vuoi vedere il link della mappa te lo lascio qua sotto</b>" + "\n" + "https://www.google.it/maps/d/viewer?mid=189tQm44H0dwd233Uh00fXqy5T1kUb_k&ll=45.417915599999986%2C10.8983839&z=11" + "\n"  
    message += "<b>/mozzecane - DAE </b>\n"
    message += "<b>/pastrengo - DAE </b>\n"
    message += "<b>/vigasio - DAE </b>\n"
    message += "<b>/villafranca - DAE </b>\n"
    message += "<b>/valeggio - DAE </b>\n"
    message += "<b>/sona - DAE </b>\n"
    message += "<b>/bussolengo - DAE </b>\n"
    message += "<b>/castelnuovo - DAE </b>\n"
    message += "<b>/sommacampagna - DAE </b>\n"

    # Invia il messaggio di benvenuto
    await context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=constants.ParseMode.HTML)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
 
    app.add_handler(CommandHandler( "start" , start))
    app.add_handler(CommandHandler("Mozzecane",mozzecane))
    app.add_handler(CommandHandler("Pastrengo",pastrengo))
    app.add_handler(CommandHandler("Sommacampagna",sommacampagna))
    app.add_handler(CommandHandler("Pescantina",pescantina))
    app.add_handler(CommandHandler("Vigasio",vigasio))
    app.add_handler(CommandHandler("Villafranca",villafranca))
    app.add_handler(CommandHandler("Valeggio",valeggio))
    app.add_handler(CommandHandler("Sona",sona))
    app.add_handler(CommandHandler("Bussolengo",bussolengo))
    app.add_handler(CommandHandler("Castelnuovo",castelnuovo))
    app.run_polling()


async def all_funct(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
     await mozzecane(update, context)
     await pastrengo(update, context)
     await sommacampagna(update, context)
     await pescantina(update, context)
     await villafranca(update, context)
     await valeggio(update, context)
     await sona(update, context)
     await bussolengo(update, context)
     await castelnuovo(update, context)
     
     
     
     
async  def mozzecane(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db.cursor()   
    list = []
    query = "SELECT * FROM dae"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Impianto sportivo 2" , url = 'https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu')],
                                    [InlineKeyboardButton("Municipio" , url = 'https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu')],
                                    [InlineKeyboardButton("Municipio c-interno" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Centro famiglia" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Piazzale Chiesa" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Centro Baco da seta" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Impianto sportivo" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("palazzetto" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")],
                                    [InlineKeyboardButton("Circolo Auser" , url = "https://www.google.com/maps/dir//45.3094931,10.8177888/@45.3095833,10.7478998,12z?entry=ttu")]]
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - MOZZECANE" ,reply_markup=reply_markup)
   

    
                
    for row in rows:
         list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
 
         
    
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)
    
    
async  def pastrengo(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db2.cursor()   
    list = []
    query = "SELECT * FROM DAE_Pastrengo"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Farmacia Alla Madonna" , url = 'https://www.google.com/maps/dir//45.5049284,10.7958367/@45.5048906,10.7936138,17z?entry=ttu')],
               [InlineKeyboardButton("Carabinieri Comando Stazione Pastrengo" , url = 'https://www.google.com/maps/dir//45.4936402,10.7989083/@45.4936262,10.7967711,17z?entry=ttu')],
               [InlineKeyboardButton("Scuola Secondaria di 1°grado di Pastrengo" , url = "https://www.google.com/maps/dir//45.4930434,10.7985805/@45.4930362,10.7285485,12z?entry=ttu")]]
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - PASTRENGO" ,reply_markup=reply_markup)
                
    for row in rows:
          list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
    
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)


async  def sommacampagna(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db3.cursor()   
    list = []
    query = "SELECT * FROM DAE_Sommacampagna"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Polizia Locale" , url = 'https://www.google.com/maps/dir//45.4073917,10.8407097/@45.40737,10.7706716,12z?entry=ttu')],
        [InlineKeyboardButton("Farmacia Comunale" , url = 'https://www.google.com/maps/dir//45.4075546,10.8411458/@45.4075582,10.8389519,17z?entry=ttu')],
        [InlineKeyboardButton("Dispensario Farmaceutico di Custoza" , url = "https://www.google.com/maps/dir//45.3773706,10.7958713/@45.377287,10.7258337,12z?entry=ttu")],
        [InlineKeyboardButton("Protezione Civile" , url = "https://www.google.com/maps/dir//45.4169143,10.8960606/@45.416909,10.8260124,12z?entry=ttu")],
        [InlineKeyboardButton("Scuola Primaria di Sommacampagna" , url = "https://www.google.com/maps/dir//45.4102039,10.8457731/@45.4101827,10.7757331,12z?entry=ttu")],
        [InlineKeyboardButton("Scuola Primaria di Caselle" , url = "https://www.google.com/maps/dir//45.4162133,10.9010016/@45.4161566,10.8309742,12z?entry=ttu")],
        [InlineKeyboardButton("Scuola Primaria di Custoza" , url = "https://www.google.com/maps/dir//45.3772118,10.797271/@45.3771233,10.7269659,12z?entry=ttu")],
        [InlineKeyboardButton("Scuola Secondaria di Sommacampagna" , url = "https://www.google.com/maps/dir//45.4051466,10.8494366/@45.4051199,10.8473513,17z?entry=ttu")],
        [InlineKeyboardButton("Scuola Secondaria di Caselle" , url = "https://www.google.com/maps/dir//45.4155525,10.9016495/@45.4155056,10.8995582,17z?entry=ttu")],
        [InlineKeyboardButton("Centro Sociale di Caselle" , url = 'https://www.google.com/maps/dir//45.4169143,10.8960606/@45.416909,10.8260124,12z?entry=ttu')],
        [InlineKeyboardButton("Baita Alpini Sommacampagna" , url = "https://www.google.com/maps/dir//45.4067038,10.8481782/@45.4067105,10.7781398,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Sommacampagna/Palestra" , url = "https://www.google.com/maps/dir//45.4095141,10.8454946/@45.4094954,10.775452,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Sommacampagna/Campo Calcio" , url = "https://www.google.com/maps/dir//45.4095697,10.8458084/@45.4094954,10.775452,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Sommacampagna/Esterno Bar" , url = "https://www.google.com/maps/dir//45.4096884,10.8456582/@45.4094954,10.775452,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Sommacampagna/Interno Bar" , url = "https://www.google.com/maps/dir//45.4097233,10.8455211/@45.4094954,10.775452,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Sommacampagna/Tamburello" , url = "https://www.google.com/maps/dir//45.4094728,10.8458108/@45.4094954,10.775452,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Caselle/Beach Tennis e Ciclisti" , url = "https://www.google.com/maps/dir//45.4180492,10.8979977/@45.4183075,10.8277672,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Caselle/Calcio" , url = "https://www.google.com/maps/dir//45.4179156,10.8983839/@45.4177979,10.8280232,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Caselle/Judo" , url = "https://www.google.com/maps/dir//45.4180587,10.897708/@45.4183075,10.8277672,12z?entry=ttu")],
        [InlineKeyboardButton("Impianti sportivi di Caselle/Tennis" , url = "https://www.google.com/maps/dir//45.4181098,10.8974827/@45.4180911,10.8275499,12z?entry=ttu")],
        [InlineKeyboardButton("Palestra di Caselle" , url = "https://www.google.com/maps/dir//45.4181173,10.8981586/@45.4180899,10.827916,12z?entry=ttu")]]
    
        
    

    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - SOMMACAMPAGNA" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)
async  def pescantina(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db4.cursor()   
    list = []
    query = "SELECT * FROM DAE_Pescantina"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Dae 1 " , url = 'https://www.google.com/maps/dir//45.4826831,10.8672927/@45.4827667,10.7970969,12z?entry=ttu')],
               [InlineKeyboardButton("dae 2 " , url = 'https://www.google.com/maps/dir//45.4954529,10.8734815/@45.4954314,10.8034443,12z?entry=ttu')]]
    
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - PESCANTINA" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge)
async  def vigasio(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db5.cursor()   
    list = []
    query = "SELECT * FROM DAE_Vigasio1"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Scuola Secondaria I.C. Rita Levi Montalcini " , url = 'https://www.google.com/maps/dir//45.3157796,10.937759/@45.3157656,10.8678164,12z?entry=ttu')],
               [InlineKeyboardButton("Stadio Comunale Umberto Capone " , url = 'https://www.google.com/maps/dir//45.3212323,10.9442542/@45.3210953,10.87418,12z?entry=ttu')],
               [InlineKeyboardButton("Parrocchia LocalitÃ  Isolalta" , url = 'https://www.google.com/maps/dir//45.3366401,10.9236867/@45.3366435,10.8538378,12z?entry=ttu')],
               [InlineKeyboardButton("Chiesa di Vigasio " , url = 'https://www.google.com/maps/dir//45.3169411,10.9405042/@45.3169075,10.8704881,12z?entry=ttu')],
               [InlineKeyboardButton("Piazzale Scuole I.C. Rita Levi Montalcini" , url = 'https://www.google.com/maps/dir//45.3160749,10.9380009/@45.3168912,10.8720609,12z?entry=ttu')],
               [InlineKeyboardButton("Piazzale Chiesa LocalitÃ  Forette" , url = 'https://www.google.com/maps/dir//45.3484058,10.9460745/@45.3484089,10.9438478,17z?entry=ttu')],
               [InlineKeyboardButton("Palazzetto dello Sport" , url = 'https://www.google.com/maps/dir//45.3202104,10.9450936/@45.3201674,10.8751597,12z?entry=ttu')]]
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - VIGASIO" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)
async  def villafranca(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db6.cursor()   
    list = []
    query = "SELECT * FROM DAE_Villafranca"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Campo da Hockey" , url = 'https://www.google.com/maps/dir//45.3505847,10.8281903/@45.3505331,10.758128,12z?entry=ttu')],
               [InlineKeyboardButton("Biblioteca" , url = 'https://www.google.com/maps/dir//45.353737,10.8432519/@45.3537081,10.7732335,12z?entry=ttu')],
               [InlineKeyboardButton("Palazzetto dello sport" , url = 'https://www.google.com/maps/dir//45.3546137,10.8308094/@45.3545089,10.7607697,12z?entry=ttu')],
               [InlineKeyboardButton("Municipio" , url = 'https://www.google.com/maps/dir//45.3509572,10.8459413/@45.3509119,10.7758896,12z?entry=ttu')],
               [InlineKeyboardButton("Farmacia Madonna del Popolo" , url = 'https://www.google.com/maps/dir//45.3582814,10.8383884/@45.3583072,10.768476,12z?entry=ttu')],
               [InlineKeyboardButton("Campi da Tennis" , url = 'https://www.google.com/maps/dir//45.3509603,10.82816/@45.3509879,10.7581519,12z?entry=ttu')],
               [InlineKeyboardButton("Polizia Municipale" , url = 'https://www.google.com/maps/dir//45.3491213,10.8448818/@45.3490559,10.7749207,12z?entry=ttu')],
	       [InlineKeyboardButton("Casa di riposo" , url = 'https://www.google.com/maps/dir//45.3504032,10.845185/@45.3504122,10.7748579,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola superiore Carlo Anti" , url = 'https://www.google.com/maps/dir//45.3575482,10.839895/@45.3575207,10.7698319,12z?entry=ttu')],
               [InlineKeyboardButton("Campo da Tamburello" , url = 'https://www.google.com/maps/dir//45.3547641,10.8304004/@45.3547561,10.760569,12z?entry=ttu')],
               [InlineKeyboardButton("Campo da Baseball" , url = 'https://www.google.com/maps/dir//45.3559553,10.8281808/@45.3558813,10.7581671,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola materna S. Giuseppe" , url = 'https://www.google.com/maps/dir//45.3544163,10.8464192/@45.3543646,10.7762755,12z?entry=ttu')],
               [InlineKeyboardButton("Palazzo del Trattato con Museo" , url = 'https://www.google.com/maps/dir//45.3531614,10.8416358/@45.3531209,10.7716098,12z?entry=ttu')],
	       [InlineKeyboardButton("Circolo Noi" , url = 'https://www.google.com/maps/dir//45.3439375,10.8078006/@45.3439023,10.7377677,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3421937,10.8179802/@45.3421545,10.7479313,12z?entry=ttu')],
               [InlineKeyboardButton("Centro Sociale" , url = 'https://www.google.com/maps/dir//45.331151,10.790868/@45.3310755,10.7209236,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3264198,10.7879635/@45.3263368,10.7179316,12z?entry=ttu')],
               [InlineKeyboardButton("Palazzetto dello sport" , url = 'https://www.google.com/maps/dir//45.3261256,10.7881684/@45.3263368,10.7179316,12z?entry=ttu')],
               [InlineKeyboardButton("Centro Sociale" , url = 'https://www.google.com/maps/dir//45.3254128,10.8326528/@45.3253929,10.8305236,17z?entry=ttu')],
	       [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3296694,10.8340902/@45.32982,10.8320613,17z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3795121,10.8789982/@45.3795225,10.8090054,12z?entry=ttu')],
               [InlineKeyboardButton("Farmacia comunale" , url = 'https://www.google.com/maps/dir//45.391453,10.9155326/@45.3914343,10.9133395,17z?entry=ttu')],
               [InlineKeyboardButton("Delegazione Centro prelievi" , url = 'https://www.google.com/maps/dir//45.3944275,10.913748/@45.3943856,10.8437147,12z?entry=ttu')],
               [InlineKeyboardButton("Palazzetto dello sport" , url = 'https://www.google.com/maps/dir//45.3930191,10.9128176/@45.393013,10.8428069,12z?entry=ttu')],
               [InlineKeyboardButton("Campi da calcio" , url = 'https://www.google.com/maps/dir//45.3905043,10.9106733/@45.3903934,10.840607,12z?entry=ttu')],
	       [InlineKeyboardButton("Circolo NOI" , url = 'https://www.google.com/maps/dir//45.3948523,10.9145175/@45.3947599,10.8445117,12z?entry=ttu')],
               [InlineKeyboardButton("Campi da Tennis" , url = 'https://www.google.com/maps/dir//45.3930071,10.9118358/@45.3928501,10.8419336,12z?entry=ttu')],
               [InlineKeyboardButton("Casa del Popolo" , url = 'https://www.google.com/maps/dir//45.3755778,10.9181904/@45.3756614,10.8481497,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3692685,10.9240337/@45.3691296,10.8540581,12z?entry=ttu')],
               [InlineKeyboardButton("Parrocchia" , url = 'https://www.google.com/maps/dir//45.3734238,10.9448872/@45.373363,10.874928,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi" , url = 'https://www.google.com/maps/dir//45.3731187,10.937479/@45.3730428,10.867449,12z?entry=ttu')]]
     
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - Villafranca" ,reply_markup=reply_markup)
    
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)
    
async  def valeggio(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db7.cursor()   
    list = []
    query = "SELECT * FROM DAE_Valeggio"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Impianti sportivi capoluogo spogiatoio calcio" , url = 'https://www.google.com/maps/dir//45.3563817,10.746072/@45.356385,10.6760539,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi capoluogo palazzina tennis" , url = 'https://www.google.com/maps/dir//45.3567537,10.7431802/@45.3565692,10.6732589,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi capoluogo palazzetto sport" , url = 'https://www.google.com/maps/dir//45.3565861,10.7433089/@45.3565692,10.6732589,12z?entry=ttu')],
               [InlineKeyboardButton("Piazza Carlo Alberto Municipio" , url = 'https://www.google.com/maps/dir//45.3541294,10.7343891/@45.3540953,10.6643536,12z?entry=ttu')],
               [InlineKeyboardButton("Colonie elioterapiche Borghetto" , url = 'https://www.google.com/maps/dir//45.3530148,10.7226999/@45.3536569,10.6531325,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi Salionze" , url = 'https://www.google.com/maps/dir//45.4053432,10.7211066/@45.4054117,10.651094,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria Collodi" , url = 'https://www.google.com/maps/dir//45.3521397,10.7355975/@45.3521917,10.6657194,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola Secondaria Foroni" , url = 'https://www.google.com/maps/dir//45.3558415,10.7435343/@45.3558414,10.6735543,12z?entry=ttu')],
               [InlineKeyboardButton("Ricreatorio Parrocchiale Grest Valeggio" , url = 'https://www.google.com/maps/dir//45.3525029,10.7363148/@45.3524829,10.6662756,12z?entry=ttu')]]
    
    
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - VALEGGIO" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)

async  def sona(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db8.cursor()   
    list = []
    query = "SELECT * FROM DAE_Sona"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Farmacia di Sona" , url = 'https://www.google.com/maps/dir//45.4335078,10.833381/@45.4334723,10.8312685,17z?entry=ttu')],
               [InlineKeyboardButton("Palestra della scuola secondaria Anna Frank" , url = 'https://www.google.com/maps/dir//45.431393,10.8965538/@45.4313628,10.8265077,12z?entry=ttu')],
               [InlineKeyboardButton("Ufficio Postale di Palazzolo" , url = 'https://www.google.com/maps/dir//45.4525009,10.8181742/@45.452515,10.748083,12z?entry=ttu')],
               [InlineKeyboardButton("Ufficio Anagrafe di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4329251,10.8901231/@45.4329157,10.8199012,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra della scuola secondaria Virgilio" , url = 'https://www.google.com/maps/dir//45.4384076,10.8266335/@45.4384041,10.8244706,17z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria Collodi" , url = 'https://www.google.com/maps/dir//45.4288585,10.7893579/@45.4288584,10.7871311,17z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria di Sona Aleardi" , url = 'https://www.google.com/maps/dir//45.4354144,10.8301261/@45.4354299,10.8279313,17z?entry=ttu')],
	       [InlineKeyboardButton("Scuola Primaria di Palazzolo San Giovanni Bosco" , url = 'https://www.google.com/maps/dir//45.4528622,10.8195138/@45.4528343,10.7495516,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra impianti sportivi di San Giorgio in Salici" , url = 'https://www.google.com/maps/dir//45.4242458,10.7850694/@45.4242294,10.7828892,17z?entry=ttu')],
               [InlineKeyboardButton("Palestra degli impianti sportivi di Sona" , url = 'https://www.google.com/maps/dir//45.429365,10.8256962/@45.4293494,10.7557181,12z?entry=ttu')],
               [InlineKeyboardButton("CPalestra degli impianti sportivi di Palazzolo" , url = 'https://www.google.com/maps/dir//45.4485064,10.818566/@45.4485754,10.7485574,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra di Lugagnano - Esterno" , url = 'https://www.google.com/maps/dir//45.4336407,10.879233/@45.4337856,10.8094351,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4322177,10.8816989/@45.4322646,10.8117176,12z?entry=ttu')],
	       [InlineKeyboardButton("Impianti sportivi di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4361867,10.8864816/@45.4329477,10.8196698,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi Rugby Sona" , url = 'https://www.google.com/maps/dir//45.4404687,10.8234678/@45.4404692,10.7534207,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria di Lugagnano - Silvio Pellico 2" , url = 'https://www.google.com/maps/dir//45.431604,10.8960562/@45.4314441,10.8258787,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi Lugagnano - Largo Weiler" , url = 'https://www.google.com/maps/dir//45.432375,10.8808447/@45.4323605,10.8107203,12z?entry=ttu')],
               [InlineKeyboardButton("Farmacia di San Giorgio in Salici" , url = 'https://www.google.com/maps/dir//45.4267204,10.7862145/@45.4267457,10.7840276,17z?entry=ttu')],
               [InlineKeyboardButton("Baita Alpini Lugagnano" , url = 'https://www.google.com/maps/dir//45.431636,10.8926865/@45.4315858,10.8226443,12z?entry=ttu')],
	       [InlineKeyboardButton("Baita Alpini Palazzolo di Sona" , url = 'https://www.google.com/maps/dir//45.4346381,10.8318069/@45.4346319,10.7617842,12z?entry=ttu')],
               [InlineKeyboardButton("Casa Il Girasole" , url = 'https://www.google.com/maps/dir//45.4346381,10.8318069/@45.4346319,10.7617842,12z?entry=ttu')]]
    
    
			   
			   
    
    
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - SONA" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)
    

async  def bussolengo(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db9.cursor()   
    list = []
    query = "SELECT * FROM DAE_Bussolengo"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Farmacia di Sona" , url = 'https://www.google.com/maps/dir//45.4335078,10.833381/@45.4334723,10.8312685,17z?entry=ttu')],
               [InlineKeyboardButton("Palestra della scuola secondaria Anna Frank" , url = 'https://www.google.com/maps/dir//45.431393,10.8965538/@45.4313628,10.8265077,12z?entry=ttu')],
               [InlineKeyboardButton("Ufficio Postale di Palazzolo" , url = 'https://www.google.com/maps/dir//45.4525009,10.8181742/@45.452515,10.748083,12z?entry=ttu')],
               [InlineKeyboardButton("Ufficio Anagrafe di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4329251,10.8901231/@45.4329157,10.8199012,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra della scuola secondaria Virgilio" , url = 'https://www.google.com/maps/dir//45.4384076,10.8266335/@45.4384041,10.8244706,17z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria Collodi" , url = 'https://www.google.com/maps/dir//45.4288585,10.7893579/@45.4288584,10.7871311,17z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria di Sona Aleardi" , url = 'https://www.google.com/maps/dir//45.4354144,10.8301261/@45.4354299,10.8279313,17z?entry=ttu')],
	       [InlineKeyboardButton("Scuola Primaria di Palazzolo San Giovanni Bosco" , url = 'https://www.google.com/maps/dir//45.4528622,10.8195138/@45.4528343,10.7495516,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra impianti sportivi di San Giorgio in Salici" , url = 'https://www.google.com/maps/dir//45.4242458,10.7850694/@45.4242294,10.7828892,17z?entry=ttu')],
               [InlineKeyboardButton("Palestra degli impianti sportivi di Sona" , url = 'https://www.google.com/maps/dir//45.429365,10.8256962/@45.4293494,10.7557181,12z?entry=ttu')],
               [InlineKeyboardButton("CPalestra degli impianti sportivi di Palazzolo" , url = 'https://www.google.com/maps/dir//45.4485064,10.818566/@45.4485754,10.7485574,12z?entry=ttu')],
               [InlineKeyboardButton("Palestra di Lugagnano - Esterno" , url = 'https://www.google.com/maps/dir//45.4336407,10.879233/@45.4337856,10.8094351,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4322177,10.8816989/@45.4322646,10.8117176,12z?entry=ttu')],
	       [InlineKeyboardButton("Impianti sportivi di Lugagnano" , url = 'https://www.google.com/maps/dir//45.4361867,10.8864816/@45.4329477,10.8196698,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi Rugby Sona" , url = 'https://www.google.com/maps/dir//45.4404687,10.8234678/@45.4404692,10.7534207,12z?entry=ttu')],
               [InlineKeyboardButton("Scuola Primaria di Lugagnano - Silvio Pellico 2" , url = 'https://www.google.com/maps/dir//45.431604,10.8960562/@45.4314441,10.8258787,12z?entry=ttu')],
               [InlineKeyboardButton("Impianti sportivi Lugagnano - Largo Weiler" , url = 'https://www.google.com/maps/dir//45.432375,10.8808447/@45.4323605,10.8107203,12z?entry=ttu')],
               [InlineKeyboardButton("Farmacia di San Giorgio in Salici" , url = 'https://www.google.com/maps/dir//45.4267204,10.7862145/@45.4267457,10.7840276,17z?entry=ttu')],
               [InlineKeyboardButton("Baita Alpini Lugagnano" , url = 'https://www.google.com/maps/dir//45.431636,10.8926865/@45.4315858,10.8226443,12z?entry=ttu')],
	       [InlineKeyboardButton("Baita Alpini Palazzolo di Sona" , url = 'https://www.google.com/maps/dir//45.4346381,10.8318069/@45.4346319,10.7617842,12z?entry=ttu')],
               [InlineKeyboardButton("Casa Il Girasole" , url = 'https://www.google.com/maps/dir//45.4346381,10.8318069/@45.4346319,10.7617842,12z?entry=ttu')]]
    
    
    
			   
			   
    
    
    
    
    
    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - BUSSOLENGO" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:   " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)


async  def castelnuovo(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    cursor = db10.cursor()   
    list = []
    query = "SELECT * FROM DAE_Castelnuovo"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    bottoni = [[InlineKeyboardButton("Unione sportiva Dilettantistica Castelnuovo D/G - Impianto sportivo di Castelnuovo D/G" , url = 'https://www.google.com/maps/dir//45.4414088,10.7470727/@45.4413713,10.6770516,12z?entry=ttu')],
               [InlineKeyboardButton("Unione sportiva Dilettantistica Castelnuovo D/G - Impianto sportivo di Sandrà; Via S'Antonio - Sandrà;Negli orari di apertura;Sì;" , url = 'https://www.google.com/maps/dir//45.4649775,10.7875369/@45.4649779,10.7175105,12z?entry=ttu')],
               [InlineKeyboardButton("ASD Sportiva Cavalcaselle - Impianto sportivo di Cavalcaselle" , url = 'https://www.google.com/maps/dir//45.4334798,10.7343347/@45.4334546,10.6643216,12z?entry=ttu')],
               [InlineKeyboardButton("Circolo La Bandiera Oliosi - Impianto sportivo di Oliosi" , url = 'https://www.google.com/maps/dir//45.4069982,10.7533678/@45.4069541,10.6834351,12z?entry=ttu')],
               [InlineKeyboardButton("Istituto Comprensivo Montini - Scuola Primaria Cavalcaselle" , url = 'https://www.google.com/maps/dir//45.4404619,10.7476894/@45.4404324,10.677518,12z?entry=ttu')],
               [InlineKeyboardButton("Istituto Comprensivo Montini - Scuola Media Castelnuovo D/G" , url = 'https://www.google.com/maps/dir//45.4438442,10.7645678/@45.4438403,10.7623832,17z?entry=ttu')],
               [InlineKeyboardButton("Istituto Comprensivo Montini - Scuola Primaria Castelnuovo D/G" , url = 'https://www.google.com/maps/dir//45.4284601,10.7621661/@45.4282948,10.6921485,12z?entry=ttu')],
	       [InlineKeyboardButton("Istituto Comprensivo Montini - Scuola Primaria Sandrà" , url = 'https://www.google.com/maps/dir//45.4397737,10.7646631/@45.4396323,10.6947228,12z?entry=ttu')],
               [InlineKeyboardButton("Protezione Civile di Castelnuovo D/G - Mobile - Fissa" , url = 'https://www.google.com/maps/dir//45.4284601,10.7621661/@45.4282948,10.6921485,12z?entry=ttu')],
               [InlineKeyboardButton("Corpo di Polizia Locale - Mobile" , url = 'https://www.google.com/maps/dir//45.4397737,10.7646631/@45.4396323,10.6947228,12z?entry=ttu')],
               [InlineKeyboardButton("Atrio comune Pian Terreno - Comune Castelnuovo D/G" , url = 'https://www.google.it/maps/d/viewer?mid=189tQm44H0dwd233Uh00fXqy5T1kUb_k&ll=45.440695%2C10.763632099999988&z=11')],
               [InlineKeyboardButton("Teatro DIM Sandrà - DIM Sandrà" , url = 'https://www.google.com/maps/dir//45.457917,10.7851179/@45.4579116,10.7147108,12z?entry=ttu')],
               [InlineKeyboardButton("Tennis Struttura Coperta - Impianto sportivo di Castelnuovo D/G" , url = 'https://www.google.com/maps/dir//45.442971,10.7506173/@45.4429041,10.6806097,12z?entry=ttu')],
	       [InlineKeyboardButton("Palazzetto dello Sport - Impianto sportivo di Castelnuovo D/G" , url = 'https://www.google.com/maps/dir//45.4420828,10.750907/@45.4420606,10.6808677,12z?entry=ttu')]]
			   

    
    reply_markup = InlineKeyboardMarkup(bottoni)

    await update.message.reply_text( "DAE - CASTELNUOVO" ,reply_markup=reply_markup)
                
    for row in rows:
       list.append(" <b>Nome Struttura</b>:    " + row[0] + "\n" + "<b>Manutenzione</b>:    " + row[2] + "\n" + "<b>Disponibilita</b> " + row[3] + "\n");
       
    cursor.close()
    result_list = list
    messagge = ''.join(result_list)
    await update.message.reply_text(messagge , parse_mode=constants.ParseMode.HTML)



    
    





if __name__ == '__main__':
    main()
