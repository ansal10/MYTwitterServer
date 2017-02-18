import os

env = os.environ.get('env')

if env is None:
    from config.development import *
elif env.lower() == 'heroku':
    from config.heroku import *
elif env.lower() == 'development':
    from config.development import *
elif env.lower() == 'production':
    from config.production import *
else:
    from config.development import *
