from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def config(app):
    app.config['DISCORD_WEBHOOK_URL'] = environ.get('DISCORD_WEBHOOK_URL')
    app.config['DISCORD_WEBHOOK_LIMIT'] = int(environ.get('DISCORD_WEBHOOK_LIMIT', '3'))
    app.config['DISCORD_WEBHOOK_MESSAGE'] = environ.get('DISCORD_WEBHOOK_MESSAGE')
    app.config['DISCORD_WEBHOOK_CHALL'] = environ.get('DISCORD_WEBHOOK_CHALL', 'True').lower() in ('true', '1')
    app.config['DISCORD_WEBHOOK_CHALL_UPDATE'] = environ.get('DISCORD_WEBHOOK_CHALL_UPDATE', 'False').lower() in ('true>    app.config['DISCORD_WEBHOOK_CHALL_UNPUBLISHED'] = environ.get('DISCORD_WEBHOOK_CHALL_UNPUBLISHED', 'False').lower()>    app.config['DISCORD_WEBHOOK_CHALL_MESSAGE'] = environ.get('DISCORD_WEBHOOK_CHALL_MESSAGE')
    app.config['DISCORD_WEBHOOK_FSTRING'] = environ.get('DISCORD_WEBHOOK_FSTRING', 'False').lower() in ('true', '1')


