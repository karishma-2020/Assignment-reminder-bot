import telebot
from apscheduler.schedulers.blocking import BlockingScheduler
from telebot import types
import mysql.connector
import re
from datetime import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kavya",
  database="reminder"
)
mycursor = mydb.cursor(buffered=True)
API_TOKEN = "5553951620:AAEcqn7mrd2OGmrT6HZNbdrr5Y0wR1RYD1I"
categories = {"Birthday": 1, "Anniversary": 2, "Meeting": 3, "Task": 4, "Other": 5}
categoryId = 0
date = ''
time = ''
context = ''
resultSet = ''
li = []
li1 = []
ltvs = []
lim = []
li1m = []
ltvsm = []
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start', 'Start'])
def Send_Welcome(message):
    cursor = mydb.cursor()
    query = "SELECT chatId FROM users WHERE chatId=%s"
    val = (message.chat.id,)
    cursor.execute(query, val)
    cursor.fetchall()
    if cursor.rowcount == 0:
        msg = bot.reply_to(message, 'Hello, Welcome to the Bot.\n\n Pls Enter a Username: \n\n/Exit')
        bot.register_next_step_handler(msg, Register_User)
    else:
        query = "SELECT chatId, displayName FROM users WHERE chatId=%s"
        val = (message.chat.id,)
        cursor.execute(query, val)
        resultSet = cursor.fetchone()
        global displayName
        global id
        displayName = str(resultSet[1])
        ID = str(resultSet[0])
        sendMessage = 'Hi ' + displayName + \
            '.\n\nWhat would you like to do today :'
        msg = bot.reply_to(message, sendMessage+"  \n\n1. /Reminder \n\n2. /Exit")

@bot.message_handler(commands=['Reminder'])
def get(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/Add_Reminder')
    itembtn2 = types.KeyboardButton('/View_Reminders')
    itembtn3 = types.KeyboardButton('/Delete_Reminders')
    itembtn4 = types.KeyboardButton('/Exit')
    markup.add(itembtn1,itembtn2,itembtn3,itembtn4)
    msg = bot.reply_to(message, "options : ",reply_markup=markup)

@bot.message_handler(commands=['Exit'])
def Exit(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('/Start')
    markup.add(itembtn)
    msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
    bot.register_next_step_handler(msg, Send_Welcome)

def Register_User(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        cursor = mydb.cursor()
        query = ("INSERT INTO users(chatId, displayName) VALUES (%s,%s)")
        val = (message.chat.id, message.text)
        cursor.execute(query, val)
        msg = bot.reply_to(message, 'User Registered.\n/Start')
        mydb.commit()
        bot.register_next_step_handler(msg, Send_Welcome)

@bot.message_handler(commands=['Add_Reminder'])
def Add_Reminder(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/Birthday')
        itembtn2 = types.KeyboardButton('/Anniversary')
        itembtn3 = types.KeyboardButton('/Meeting')
        itembtn4 = types.KeyboardButton('/Task')
        itembtn5 = types.KeyboardButton('/Other')
        itembtn6 = types.KeyboardButton('/Exit')
        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6)
        msg = bot.reply_to(message, "Please select a category for the new reminder:",reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Category_Reminder_Date)


def Add_Category_Reminder_Date(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        value=value.replace('/','')
        global categories
        global categoryId
        categoryId = categories[value]
        markup = types.ReplyKeyboardMarkup(row_width=6)
        itembtn1 = types.KeyboardButton('01')
        itembtn2 = types.KeyboardButton('02')
        itembtn3 = types.KeyboardButton('03')
        itembtn4 = types.KeyboardButton('04')
        itembtn5 = types.KeyboardButton('05')
        itembtn6 = types.KeyboardButton('06')
        itembtn7 = types.KeyboardButton('07')
        itembtn8 = types.KeyboardButton('08')
        itembtn9 = types.KeyboardButton('09')
        itembtn10 = types.KeyboardButton('10')
        itembtn11 = types.KeyboardButton('11')
        itembtn12 = types.KeyboardButton('12')
        itembtn13 = types.KeyboardButton('13')
        itembtn14 = types.KeyboardButton('14')
        itembtn15 = types.KeyboardButton('15')
        itembtn16 = types.KeyboardButton('16')
        itembtn17 = types.KeyboardButton('17')
        itembtn18 = types.KeyboardButton('18')
        itembtn19 = types.KeyboardButton('19')
        itembtn20 = types.KeyboardButton('20')
        itembtn21 = types.KeyboardButton('21')
        itembtn22 = types.KeyboardButton('22')
        itembtn23 = types.KeyboardButton('23')
        itembtn24 = types.KeyboardButton('24')
        itembtn25 = types.KeyboardButton('25')
        itembtn26 = types.KeyboardButton('26')
        itembtn27 = types.KeyboardButton('27')
        itembtn28 = types.KeyboardButton('28')
        itembtn29 = types.KeyboardButton('29')
        itembtn20 = types.KeyboardButton('20')
        itembtn31 = types.KeyboardButton('31')
        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11,itembtn12,itembtn13,itembtn14,itembtn15,itembtn16,itembtn17,itembtn18,itembtn19,itembtn20,itembtn21,itembtn22,itembtn23,itembtn24,itembtn25,itembtn26,itembtn27,itembtn28,itembtn29,itembtn20,itembtn31)
        msg = bot.reply_to(message, 'Enter Date :\n\n/Exit',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Month)

def Add_Month(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    elif re.match(r"^(0?[1-9]|[12][0-9]|3[01])$", str(value)):        
        global date
        date = value  
        markup = types.ReplyKeyboardMarkup(row_width=3) 
        jan = types.KeyboardButton('January')
        feb = types.KeyboardButton('February')
        mar = types.KeyboardButton('March')
        apr = types.KeyboardButton('April')
        may = types.KeyboardButton('May')
        jun = types.KeyboardButton('June')
        jul = types.KeyboardButton('July')
        aug = types.KeyboardButton('August')
        sep = types.KeyboardButton('September')
        oct = types.KeyboardButton('October')
        nov = types.KeyboardButton('November')
        dec = types.KeyboardButton('December')
        markup.add(jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)
        msg = bot.reply_to(message, 'Enter Month :\n\n/Exit',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Year)

def Add_Year(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else :        
        global date
        if(value=='January'):
            value = '01'
        if(value=='February'):
            value = '02'
        if(value=='March'):
            value = '03'
        if(value=='April'):
            value = '04'
        if(value=='May'):
            value = '05'
        if(value=='June'):
            value = '06'
        if(value=='July'):
            value = '07'
        if(value=='August'):
            value = '08'
        if(value=='September'):
            value = '09'
        if(value=='October'):
            value = '10'
        if(value=='November'):
            value = '11'
        if(value=='December'):
            value = '12'
        date = value + '-' + date  
        markup = types.ReplyKeyboardMarkup(row_width=4) 
        y2019 = types.KeyboardButton('2019')
        y2020 = types.KeyboardButton('2020')
        y2021 = types.KeyboardButton('2021')
        y2022 = types.KeyboardButton('2022')
        y2023 = types.KeyboardButton('2023')
        y2024 = types.KeyboardButton('2024')
        y2025 = types.KeyboardButton('2025')
        y2026 = types.KeyboardButton('2026')
        y2027 = types.KeyboardButton('2027')
        y2028 = types.KeyboardButton('2028')
        y2029 = types.KeyboardButton('2029')
        y2030 = types.KeyboardButton('2030')
        markup.add(y2019,y2020,y2021,y2022,y2023,y2024,y2025,y2026,y2027,y2028,y2029,y2030)
        msg = bot.reply_to(message, 'Enter Year :\n\n/Exit',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Time)        

def Add_Time(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:        
        global date        
        date = value + '-' + date  
        markup = types.ReplyKeyboardMarkup(row_width=4)
        itembtn12am = types.KeyboardButton('12 AM')
        itembtn1am = types.KeyboardButton('01 AM')
        itembtn2am = types.KeyboardButton('02 AM')
        itembtn3am = types.KeyboardButton('03 AM')
        itembtn4am = types.KeyboardButton('04 AM')
        itembtn5am = types.KeyboardButton('05 AM')
        itembtn6am = types.KeyboardButton('06 AM')
        itembtn7am = types.KeyboardButton('07 AM')
        itembtn8am = types.KeyboardButton('08 AM')
        itembtn9am = types.KeyboardButton('09 AM')
        itembtn10am = types.KeyboardButton('10 AM')
        itembtn11am = types.KeyboardButton('11 AM')
        itembtn12pm = types.KeyboardButton('12 PM')
        itembtn1pm = types.KeyboardButton('01 PM')
        itembtn2pm = types.KeyboardButton('02 PM')
        itembtn3pm = types.KeyboardButton('03 PM')
        itembtn4pm = types.KeyboardButton('04 PM')
        itembtn5pm = types.KeyboardButton('05 PM')
        itembtn6pm = types.KeyboardButton('06 PM')
        itembtn7pm = types.KeyboardButton('07 PM')
        itembtn8pm = types.KeyboardButton('08 PM')
        itembtn9pm = types.KeyboardButton('09 PM')
        itembtn10pm = types.KeyboardButton('10 PM')
        itembtn11pm = types.KeyboardButton('11 PM')
        markup.add(itembtn12am,itembtn1am,itembtn2am,itembtn3am,itembtn4am,itembtn5am,itembtn6am,itembtn7am,itembtn8am,itembtn9am,itembtn10am,itembtn11am,itembtn12pm,itembtn1pm,itembtn2pm,itembtn3pm,itembtn4pm,itembtn5pm,itembtn6pm,itembtn7pm,itembtn8pm,itembtn9pm,itembtn10pm,itembtn11pm)        
        msg = bot.reply_to(message, 'Enter Hour :\n\n/Exit',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Minute)

def Add_Minute(message):
    value = message.text
    if (value == '/Exit'):
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:        
        global time
        time = value[0:2]
        time1=value[3:6] 
        tmp=0 
        if(time1=="AM" and time=="12"):
            time="00"
        elif(time1=="PM" and time=="12"):
            print("")
        else:
            if(time1=="PM"):
                tmp=int(time,10)
                tmp=tmp+12
                time=str(tmp)
        markup = types.ReplyKeyboardMarkup(row_width=4)
        itembtn1 = types.KeyboardButton('00')
        itembtn2 = types.KeyboardButton('05')
        itembtn3 = types.KeyboardButton('10')
        itembtn4 = types.KeyboardButton('15')
        itembtn5 = types.KeyboardButton('20')
        itembtn6 = types.KeyboardButton('25')
        itembtn7 = types.KeyboardButton('30')
        itembtn8 = types.KeyboardButton('35')
        itembtn9 = types.KeyboardButton('40')
        itembtn10 = types.KeyboardButton('45')
        itembtn11 = types.KeyboardButton('50')
        itembtn12 = types.KeyboardButton('55')
        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11,itembtn12)
        msg = bot.reply_to(message, 'Enter Minute :\n\n/Exit',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Context)

def Add_Context(message):
    value = message.text
    global time
    time = time+':'+value
    global categoryId,msg
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.')
        bot.register_next_step_handler(msg, Send_Welcome,reply_markup=markup)
    else:    
        markup = types.ReplyKeyboardMarkup()
        markup = types.ReplyKeyboardRemove(selective=False)
        if categoryId == 1 :
            msg = bot.reply_to(message, 'Whose Birthday it is ?',reply_markup=markup)       
        elif categoryId == 2 :
            msg = bot.reply_to(message, 'Whose Anniversary it is ?',reply_markup=markup)
        elif categoryId == 3 :
            msg = bot.reply_to(message, 'Where is the meeting ?',reply_markup=markup)
        elif categoryId == 4 :
            msg = bot.reply_to(message, 'What task it is ?',reply_markup=markup)
        elif categoryId == 4:
            msg = bot.reply_to(message, 'What reminder it is ?',reply_markup=markup)
        bot.register_next_step_handler(msg, Add_Reminder_To_DB)   

def Add_Reminder_To_DB(message):
    value = message.text
    global categoryId
    global date
    global time
    global output
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        if categoryId == 1:
            cursor = mydb.cursor()
            query = ("INSERT INTO reminders(chatId, date, time, message) VALUES (%s,%s,%s,%s)")
            output = 'Reminder : Wish Happy Birthday to '+str(value)
            val = (message.chat.id, date, time, output)
            cursor.execute(query, val)
            mydb.commit()
        elif categoryId == 2:
            cursor = mydb.cursor()
            query = ("INSERT INTO reminders(chatId, date, time, message) VALUES (%s,%s,%s,%s)")
            output = 'Reminder : Wish Happy Anniversary to '+str(value)
            val = (message.chat.id, date, time, output)
            cursor.execute(query, val)
            mydb.commit()
        elif categoryId == 3:
            cursor = mydb.cursor()
            query = ("INSERT INTO reminders(chatId, date, time, message) VALUES (%s,%s,%s,%s)")
            output = 'Reminder : You have a meeting at '+str(value)
            val = (message.chat.id, date, time, output)
            cursor.execute(query, val)
            mydb.commit()
        elif categoryId == 4:
            cursor = mydb.cursor()
            query = ("INSERT INTO reminders(chatId, date, time, message) VALUES (%s,%s,%s,%s)")
            output = 'Reminder : You have to '+str(value)
            val = (message.chat.id, date, time, output)
            cursor.execute(query, val)
            mydb.commit()
        elif categoryId == 5:
            cursor = mydb.cursor()
            query = ("INSERT INTO reminders(chatId, date, time, message) VALUES (%s,%s,%s,%s)")
            output = 'Reminder : '+str(value)
            val = (message.chat.id, date, time, output)
            cursor.execute(query, val)
            mydb.commit()
        msg = bot.reply_to(message, 'Reminder Added \n/Add_Reminder \n/Exit')

        def reminder_update():
            bot.send_message(message.chat.id, output)

        sched = BlockingScheduler()
        sched.add_job(reminder_update, 'date', timezone="Asia/Kolkata",run_date=datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(time[0:2]), int( time[3:])))

        sched.start()
@bot.message_handler(commands=['View_Reminders'])
def View_Reminders(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        cursor = mydb.cursor()
        query = ("SELECT DISTINCT date FROM reminders WHERE chatId= %s ORDER BY date ASC")
        val = (message.chat.id,)
        cursor.execute(query, val)
        resultset=cursor.fetchall()
        msgstr=''
        if(cursor.rowcount==0):
            msg = bot.reply_to(message,"Nothing to View /Start")
            bot.register_next_step_handler(msg, Send_Welcome)
        else:
            for i in resultset:
                msgstr+='\nDate : '+str(i[0])+'\n'
                query = ("SELECT time, message FROM reminders WHERE chatId = %s AND date = %s ORDER BY time ASC")
                val = (message.chat.id,i[0])
                cursor.execute(query, val)
                resultset2 = cursor.fetchall()
                for j in resultset2:
                    msgstr+=j[0]+' => '+j[1]+'\n'
            msg = bot.reply_to(message,msgstr+"\n\n/Exit")
            bot.register_next_step_handler(msg, Send_Welcome)

@bot.message_handler(commands=['Delete_Reminders'])
def Delete_Reminders(message):
    global msgstr
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        cursor = mydb.cursor()
        query = ("SELECT date,time,message FROM reminders WHERE chatId= %s ORDER BY date,time ASC")
        val = (message.chat.id,)
        cursor.execute(query, val)
        global resultSet
        resultSet=cursor.fetchall()
        if(cursor.rowcount==0):
            msg = bot.reply_to(message,"Nothing to Delete /Start")
            bot.register_next_step_handler(msg, Send_Welcome)
        else:
            msgstr = '\n'
            count = 1
            for i in resultSet:
                msgstr+='/'+str(count)+' :['+i[0]+' '+i[1]+'] '+i[2]+'\n\n'
                count+=1
        msg = bot.reply_to(message,msgstr+"\n\n/Exit")
        bot.register_next_step_handler(msg, Delete)


@bot.message_handler(commands=['Delete'])
def Delete(message):
    value = message.text
    if value == '/Exit':
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('/Start')
        markup.add(itembtn)
        msg = bot.reply_to(message, 'Well then, Good Bye.',reply_markup=markup)
        bot.register_next_step_handler(msg, Send_Welcome)
    else:
        global resultSet
        cursor = mydb.cursor()
        value = value.replace('/','')
        indexValue = int(value) - 1        
        query = ("DELETE FROM reminders WHERE chatId= %s AND date=%s AND time=%s AND message=%s")
        val = (message.chat.id,resultSet[indexValue][0],resultSet[indexValue][1],resultSet[indexValue][2])
        cursor.execute(query, val)
        mydb.commit()
        msg = bot.reply_to(message, 'Reminder Deleted.\n/Start')
        bot.register_next_step_handler(msg, Send_Welcome)
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling()
