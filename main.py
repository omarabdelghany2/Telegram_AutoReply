# pip install python-telegram-bot
from telegram.ext import *
from keys import token
from openpyxl import load_workbook

import keys

print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('I can help you if you want to inform about grades if a student Enter (/Grade : Omar mohamed abdelghany) like this form without brackets ')


# Lets us use the /custom command
def Grade_command(update, context):
    

    text = str(update.message.text).lower()
    StudentName=text[text.find(':')+1:len(text)]
    print(StudentName)

    #now we got the name of student lets search for him in excel sheet
    sheet = book.active
    rows = sheet.rows
    flag=False
    for row in rows :
        if(row[1].value==StudentName.lower()) :
            grade= row[3].value
            update.message.reply_text(str(grade))
            flag=True
            break
    if(flag==False):        
         update.message.reply_text('this name not found OR maybe u entered in wrong form enter /Grade : name')   

    
   


def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'I\'m good!'

    return 'I don\'t understand' #5087593687


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type     
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@triai2000bot' in text:
            new_text = text.replace('@triai2000bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    book = load_workbook('ayman_data.xlsx')
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('Grade', Grade_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()