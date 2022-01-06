from os import environ

SESSION_CONFIGS = [
dict(
        name='Sessionmercredimatin',
        display_name='mercredimatin',
        app_sequence=['nsim'],
        num_demo_participants=3,
    ),
    dict(
        name='ALL',
        app_sequence=['nrisk','attendrelesautres1', 'namb','attendrelesautres2', 'nsim','attendrelesautres3','arisk','attendrelesautres4','aamb','attendrelesautres5','asim', 'payementforall'],
        num_demo_participants=1,
    ),
    dict(
        name='TEST23123',
        app_sequence=['nrisk', 'namb', 'nsim', 'Payementtest2'],
        num_demo_participants=2,
    ),
    dict(
        name='TEST14H',
        app_sequence=['arisk','aamb','asim','Payement14h'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=.02, participation_fee=0.00, doc=""
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
