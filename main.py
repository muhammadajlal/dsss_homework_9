from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from llm_handler import generate_response  # Import the LLM handler function

# Function to handle the "/start" command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI Assistant bot. How can I help you today?")

# Function to handle all text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    try:
        # Generate a response using the LLM
        response = generate_response(message)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"Sorry, an error occurred: {str(e)}")

def main():
    TOKEN = "7966020556:AAEZcgFRGPhcHn7btTcYjyn2eO4XJbKMRlM" 
    application = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()