# Telegram Bot

Bot básico de Telegram con comando /hola.

## Requisitos

- Python 3.11
- Token de bot de Telegram (obtener de [@BotFather](https://t.me/BotFather))
- Docker (opcional)

## Configuración

1. Clonar el repositorio
2. Copiar el archivo `.env.example` a `.env`
3. Añadir el token del bot en el archivo `.env`

## Ejecución local

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el bot
python bot.py
```

## Ejecución con Docker

```bash
# Construir la imagen
docker build -t telegram-bot .

# Ejecutar el contenedor
docker run -d --env-file .env telegram-bot
```

## Comandos disponibles

- `/hola` - Responde con un saludo
