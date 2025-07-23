import os
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener el token del bot desde las variables de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start"""
    welcome_message = (
        "🎓 ¡Bienvenido a English Speaking Assistant! 🗣️\n\n"
        "Soy tu bot personal para practicar inglés. Estoy aquí para ayudarte "
        "a mejorar tus habilidades de speaking y pronunciación.\n\n"
        "Estos son los comandos disponibles:\n"
        "/start - Muestra este mensaje de bienvenida\n"
        "/practice - Iniciar una sesión de práctica\n"
        "/pronunciation - Tips de pronunciación\n"
        "/vocabulary - Palabra del día\n"
        "/exercises - Ejercicios de speaking\n"
        "/progress - Ver tu progreso\n"
        "/help - Obtener ayuda\n\n"
        "¡Empecemos a practicar! 🚀"
    )
    await update.message.reply_text(welcome_message)

async def practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /practice"""
    await update.message.reply_text(
        "🎯 Selecciona un tema para practicar:\n"
        "- Presentaciones personales\n"
        "- Situaciones cotidianas\n"
        "- Entrevistas de trabajo\n"
        "- Viajes y turismo\n\n"
        "(Funcionalidad en desarrollo) 🔧"
    )

async def pronunciation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /pronunciation"""
    await update.message.reply_text(
        "🗣️ Tips de pronunciación:\n\n"
        "1. Practica el sonido 'th'\n"
        "2. Diferencia entre 'i' corta y larga\n"
        "3. La importancia del stress en palabras\n\n"
        "(Más contenido próximamente) 📚"
    )

async def vocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /vocabulary"""
    await update.message.reply_text(
        "📖 Palabra del día:\n\n"
        "Endeavor (verbo)\n"
        "Significado: Esforzarse por lograr algo\n"
        "Ejemplo: 'I will endeavor to improve my English skills'\n"
        "Pronunciación: /enˈdevər/"
    )

async def exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /exercises"""
    await update.message.reply_text(
        "🎤 Ejercicios de speaking disponibles:\n\n"
        "1. Repetición de frases\n"
        "2. Descripción de imágenes\n"
        "3. Respuesta a preguntas\n"
        "4. Conversación libre\n\n"
        "(Selecciona pronto tu ejercicio) ⏳"
    )

async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /progress"""
    await update.message.reply_text(
        "📊 Tu progreso:\n\n"
        "- Sesiones completadas: 0\n"
        "- Palabras aprendidas: 0\n"
        "- Nivel actual: Principiante\n"
        "- Próximo nivel: 🎯 Intermedio\n\n"
        "(Funcionalidad en desarrollo) 🔧"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /help"""
    await update.message.reply_text(
        "❓ Ayuda:\n\n"
        "- Usa /start para comenzar\n"
        "- Selecciona un comando del menú\n"
        "- Practica diariamente\n"
        "- Revisa tu progreso\n\n"
        "¿Necesitas más ayuda? ¡Pronto tendremos soporte personalizado! 🤝"
    )

async def setup_commands(application: Application):
    """Configura los comandos del bot para que aparezcan en el menú"""
    commands = [
        BotCommand("start", "Iniciar el bot y ver comandos disponibles"),
        BotCommand("practice", "Iniciar una sesión de práctica"),
        BotCommand("pronunciation", "Tips de pronunciación"),
        BotCommand("vocabulary", "Palabra del día"),
        BotCommand("exercises", "Ejercicios de speaking"),
        BotCommand("progress", "Ver tu progreso"),
        BotCommand("help", "Obtener ayuda"),
    ]
    await application.bot.set_my_commands(commands)

def main():
    """Función principal del bot"""
    # Crear la aplicación
    application = Application.builder().token(TOKEN).build()

    # Añadir manejadores para los comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("practice", practice))
    application.add_handler(CommandHandler("pronunciation", pronunciation))
    application.add_handler(CommandHandler("vocabulary", vocabulary))
    application.add_handler(CommandHandler("exercises", exercises))
    application.add_handler(CommandHandler("progress", progress))
    application.add_handler(CommandHandler("help", help))

    # Configurar los comandos en el menú
    application.job_queue.run_once(lambda ctx: setup_commands(application), 0)

    # Iniciar el bot
    print("Bot iniciado...")
    application.run_polling()

if __name__ == '__main__':
    main()
