from os import environ

SESSION_CONFIGS = [
    dict(
        name='ALL',
        app_sequence=['nsimilar','nrisk','namb','asim','arisk','aamb', 'Payement'],
        num_demo_participants=2,
    ),
    dict(
        name='TESTNSIM',
        app_sequence=['nsimilar','payementtest'],
        num_demo_participants=2,
    ),
     dict(
         name= 'namb',
         app_sequence=['namb'],
         num_demo_participants=1,
     ),
    dict(
        name='nrisk',
        app_sequence=['nrisk'],
        num_demo_participants=1,
    ),

    dict(
        name='aamb',
        app_sequence=['aamb'],
        num_demo_participants=1,
    ),
    dict(
        name='arisj',
        app_sequence=['arisk'],
        num_demo_participants=1,
    ),
    dict(
        name='asim',
        app_sequence=['asim'],
        num_demo_participants=1,
    ),
    dict(
        name='test',
        app_sequence=['testoun'],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['events_table']
SESSION_FIELDS = ['cases_by_similarity']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3443132666447'
