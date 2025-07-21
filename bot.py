import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener el token del bot desde las variables de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /hola"""
    await update.message.reply_text('¡Hola! ¿Cómo estás?')

def main():
    """Función principal del bot"""
    # Crear la aplicación
    application = Application.builder().token(TOKEN).build()

    # Añadir manejador para el comando /hola
    application.add_handler(CommandHandler("hola", hola))

    # Iniciar el bot
    print("Bot iniciado...")
    application.run_polling()

if __name__ == '__main__':
    main()
