from otree.api import *
import math

c = Currency

doc = """
Last page with questionnaire and all gains.
"""


class Constants(BaseConstants):
    name_in_url = 'eeeazin'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    payoff_euros = models.FloatField()
    round_arisk = models.IntegerField()
    payoff_arisk = models.IntegerField()
    gain1_part1 = models.CurrencyField(initial=0)
    gain2_part1 = models.CurrencyField(initial=0)
    gain3_part1 = models.CurrencyField(initial=0)
    gain4_part1 = models.CurrencyField(initial=0)



    female = models.IntegerField(
        min=-1, max=1,
        choices=[
            [1, "Femme"],
            [0, "Homme"],
            [-1, "Autre"]
        ],
        label="Quel est votre genre?",
        widget=widgets.RadioSelect,
        doc="[1, Femme], [0,Homme], [-1, Autre]"
    )

    age = models.IntegerField(
        min=14, max=70,
        label="Quel est votre âge?",
        doc="Age en années"
    )

    nonbinaire = models.StringField(
        blank=True,
        label="Si vous avez choisi autre, vous pouvez préciser, (si vous le souhaitez) votre genre ici  ?",
        doc="Genre +"
    )

    niveau = models.IntegerField(
        label="Quel est votre plus haut niveau d'étude validé?",
        choices=[
            [0, 'Baccalauréat'],
            [1, 'Bac + 1'],
            [2, 'Bac + 2'],
            [3, 'Bac + 3 - Licence'],
            [4, 'Bac + 4'],
            [5, 'Bac + 5 - Master'],
            [6, 'Bac + 8 - Doctorat']
        ],
        doc="plus haut niveau d'étude (années après le bac)"
    )

    discipline = models.StringField(
        label="Quel est votre discipline d'étude?",
        doc="Discipline d'étude"
    )

    # Questionnaire

    Risque = models.IntegerField(
        min=0, max=10,
        choices=range(0, 11),
        label="Diriez-vous que vous avez tendance à prendre des risques dans votre vie de manière générale? (Veuillez indiquer votre opinion sur cette échelle où 0 signifie 'Je ne prends jamais de risque' et 10 signifie 'Je prends constamment des risques').",
        widget=widgets.RadioSelectHorizontal,
        doc="0 = jamais de risque 10 = constamment du risque"
    )

    Ambiguité1 = models.IntegerField(
        min=0, max=10,
        choices=range(0, 11),
        label="Quand vous n'avez aucune information sur une situation, diriez-vous que vous avez tendance à être quelqu'un d'extrêmement prudent ou d'extrèmement imprudent dans votre vie de manière générale ? (Veuillez indiquer votre opinion sur cette échelle où 0 signifie 'Je suis extrêmement prudent' et 10 signifie 'Je suis extrêmement imprudent').",
        widget=widgets.RadioSelectHorizontal,
        doc="0 = extrêmement prudent 10 = extrêmement imprudent"
    )

    Ambiguité2 = models.IntegerField(
        min=0, max=10,
        choices=range(0, 11),
        label="Quand vous n'avez aucune information sur une situation, vous considérez vous comme extrêmement pessimiste ou extrêmement optimise quant à l'issue de cette dernière ?  (Veuillez indiquer votre opinion sur cette échelle où 0 signifie 'Je suis extrêmement pessimiste' et 10 signifie 'Je suis extrêmement optimiste').",
        widget=widgets.RadioSelectHorizontal,
        doc="0 = extrêmement pessimiste 10 = extrêmement optimiste")


    ExpJuridique = models.IntegerField(
        min=0, max=1,
        choices=[
            [1, "Oui"],
            [0, "Non"],
        ],
        label="Est-ce que vous, ou un de vos proche, avez déjà connu un divorce?",
        widget=widgets.RadioSelect,
        doc="[1, Oui], [0,Non]"
    )

def get_gains(player:Player):
            player.gain1_part1 = player.participant.vars['payoff_nsimilar']
            player.gain2_part1 = player.participant.vars['payoff_nsimilar']
            player.gain3_part1 = player.participant.vars['payoff_nsimilar']
            player.payoff = (player.gain1_part1 + player.gain2_part1 + player.gain3_part1) / 3
            player.payoff_euros = math.ceil(3 + float(player.payoff.to_real_world_currency(player.session)))

# PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['female', 'age', 'nonbinaire','niveau', 'discipline']

class Questionnaire1(Page):
    form_model = 'player'
    form_fields = ['Risque', 'Ambiguité1','Ambiguité2','ExpJuridique']
    def before_next_page(player: Player,timeout_happened):
        get_gains(player)
class Retrievegains(WaitPage):
    after_all_players_arrive = 'get_gains'

class Final_gain(Page):
    @staticmethod
    def vars_for_template(player: Player):
        gainaamb = player.participant.vars['payoff_aamb']
        roundaamb =player.participant.vars['round_aamb']
        gainarisk = player.participant.vars['payoff_arisk']
        roundarisk =player.participant.vars['round_arisk']
        gainasim=player.participant.vars['payoff_asim']
        roundasim=player.participant.vars['round_asim']
        roundnamb=player.participant.vars['round_namb']
        gainnamb=player.participant.vars['payoff_namb']
        roundnrisk=player.participant.vars['round_nrisk']
        gainnrisk=player.participant.vars['payoff_nrisk']
        gainnsimilar = player.participant.vars['payoff_nsimilar']
        roundnsimilar = player.participant.vars['round_nsimilar']


        #total = player.payoff_euros

        return dict(gainaamb=gainaamb,roundaamb=roundaamb,gainarisk=gainarisk,roundarisk=roundarisk,gainasim=gainasim,roundasim=roundasim,roundnamb=roundnamb,gainnamb=gainnamb,roundnrisk=roundnrisk,gainnrisk=gainnrisk,gainnsimilar=gainnsimilar, roundnsimilar=roundnsimilar)
page_sequence = [Demographics,Questionnaire1,Final_gain]
