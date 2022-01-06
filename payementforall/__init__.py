from otree.api import *
import math

c = Currency

doc = """
Last page with questionnaire and all gains.
"""


class Constants(BaseConstants):
    name_in_url = 'eeeaezezaaeazeazezaeazpppfzin'
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
    gain1 = models.CurrencyField(initial=0)
    gain2 = models.CurrencyField(initial=0)
    gain3 = models.CurrencyField(initial=0)
    gain4 = models.CurrencyField(initial=0)
    gain5 = models.CurrencyField(initial=0)
    gain6 = models.CurrencyField(initial=0)
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
            [6, 'Doctorant'],
            [7, 'Bac + 8 - Doctorat']
        ],
        doc="plus haut niveau d'étude (années après le bac)"
    )

    discipline = models.StringField(
        label="Quel est votre discipline d'étude?",
        choices=[
            [1, 'Sciences économiques'],
            [2, 'Mathématiques'],
            [3, 'Droit'],
            [4, 'Sciences'],
            [5, 'Lettres'],
            [6, 'Sciences sociales'],
            [7, 'Autre']
        ],
        doc="Discipline d'étude"
    )

    discipline_libre = models.StringField(
        blank=True,
        label="Si autre précisez.",
        doc=""
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

            if player.participant.vars['payoff_aamb'] < 0:
                player.participant.vars['payoff_aamb'] = 0
            else:
                player.participant.vars['payoff_aamb'] = player.participant.vars['payoff_aamb']

            if player.participant.vars['payoff_arisk'] < 0:
                player.participant.vars['payoff_arisk'] = 0
            else:
                player.participant.vars['payoff_arisk'] = player.participant.vars['payoff_arisk']

            if player.participant.vars['payoff_asim'] < 0:
                player.participant.vars['payoff_asim'] = 0
            else:
                player.participant.vars['payoff_asim'] = player.participant.vars['payoff_asim']


#Si il a pas l'info le paiement devient sur partie 1



            if player.participant.vars['wtp_aamb'] < player.participant.vars['rand_wtp_aamb'] :
                player.gain1 = player.participant.vars['payoff_aamb2']
            else:
                player.gain1 = player.participant.vars['payoff_aamb']



            if player.participant.vars['wtp_arisk'] < player.participant.vars['rand_wtp_arisk'] :
                player.gain2 = player.participant.vars['payoff_arisk2']
            else:
                player.gain2 = player.participant.vars['payoff_arisk']



            if player.participant.vars['wtp_asim'] < player.participant.vars['rand_wtp_asim'] :
                player.gain3= player.participant.vars['payoff_asim2']
            else:
                player.gain3 = player.participant.vars['payoff_asim']



## PARTIE NATURAL


            if player.participant.vars['payoff_namb'] < 0:
                player.participant.vars['payoff_namb'] = 0
            else:
                player.participant.vars['payoff_namb'] = player.participant.vars['payoff_namb']

            if player.participant.vars['payoff_nrisk'] < 0:
                player.participant.vars['payoff_nrisk'] = 0
            else:
                player.participant.vars['payoff_nrisk'] = player.participant.vars['payoff_nrisk']

            if player.participant.vars['payoff_nsim'] < 0:
                player.participant.vars['payoff_nsim'] = 0
            else:
                player.participant.vars['payoff_nsim'] = player.participant.vars['payoff_nsim']


#Si il a pas l'info le paiement devient sur partie 1



            if player.participant.vars['wtp_namb'] < player.participant.vars['rand_wtp_namb'] :
                player.gain4 = player.participant.vars['payoff_namb2']
            else:
                player.gain4 = player.participant.vars['payoff_namb']



            if player.participant.vars['wtp_nrisk'] < player.participant.vars['rand_wtp_nrisk'] :
                player.gain5 = player.participant.vars['payoff_nrisk2']
            else:
                player.gain5 = player.participant.vars['payoff_nrisk']



            if player.participant.vars['wtp_nsim'] < player.participant.vars['rand_wtp_nsim'] :
                player.gain6= player.participant.vars['payoff_nsim2']
            else:
                player.gain6 = player.participant.vars['payoff_nsim']



## sortir les payoffs
            player.payoff = (player.gain1 + player.gain2 + player.gain3 + player.gain4 + player.gain5 + player.gain6) / 6
            player.payoff_euros = math.ceil(3 + float(player.payoff.to_real_world_currency(player.session)))

            # PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['female', 'age', 'nonbinaire','niveau', 'discipline','discipline_libre']

class Questionnaire1(Page):
    form_model = 'player'
    form_fields = ['Risque', 'Ambiguité1','Ambiguité2','ExpJuridique']
    def before_next_page(player: Player,timeout_happened):
        get_gains(player)

class Final_gain(Page):
    @staticmethod
    def vars_for_template(player: Player):
        ##variable artificial
        gainaamb = player.participant.vars['payoff_aamb']
        roundaamb = player.participant.vars['round_aamb']
        wtpaamb = player.participant.vars['wtp_aamb']
        randaamb = player.participant.vars['rand_wtp_aamb']
        gainaamb2 = player.participant.vars['payoff_aamb2']
        roundaamb2 = player.participant.vars['round_aamb2']

        gainarisk = player.participant.vars['payoff_arisk']
        roundarisk =player.participant.vars['round_arisk']
        wtparisk =player.participant.vars['wtp_arisk']
        randarisk =player.participant.vars['rand_wtp_arisk']
        gainarisk2 = player.participant.vars['payoff_arisk2']
        roundarisk2 =player.participant.vars['round_arisk2']

        gainasim = player.participant.vars['payoff_asim']
        roundasim =player.participant.vars['round_asim']
        wtpasim = player.participant.vars['wtp_asim']
        randasim = player.participant.vars['rand_wtp_asim']
        gainasim2 = player.participant.vars['payoff_asim2']
        roundasim2 =player.participant.vars['round_asim2']


        ## variables natural

        gainnamb = player.participant.vars['payoff_namb']
        roundnamb = player.participant.vars['round_namb']
        wtpnamb = player.participant.vars['wtp_namb']
        randnamb = player.participant.vars['rand_wtp_namb']
        gainnamb2 = player.participant.vars['payoff_namb2']
        roundnamb2 = player.participant.vars['round_namb2']

        gainnrisk = player.participant.vars['payoff_nrisk']
        roundnrisk =player.participant.vars['round_nrisk']
        wtpnrisk =player.participant.vars['wtp_nrisk']
        randnrisk =player.participant.vars['rand_wtp_nrisk']
        gainnrisk2 = player.participant.vars['payoff_nrisk2']
        roundnrisk2 =player.participant.vars['round_nrisk2']

        gainnsim = player.participant.vars['payoff_nsim']
        roundnsim =player.participant.vars['round_nsim']
        wtpnsim = player.participant.vars['wtp_nsim']
        randnsim = player.participant.vars['rand_wtp_nsim']
        gainnsim2 = player.participant.vars['payoff_nsim2']
        roundnsim2 =player.participant.vars['round_nsim2']
        return dict(gainaamb=gainaamb,roundaamb=roundaamb,wtpaamb=wtpaamb,randaamb=randaamb,gainaamb2=gainaamb2,roundaamb2=roundaamb2, gainarisk=gainarisk,roundarisk=roundarisk,wtparisk=wtparisk,randarisk=randarisk,gainarisk2=gainarisk2,roundarisk2=roundarisk2,gainasim=gainasim,roundasim=roundasim,wtpasim=wtpasim,randasim=randasim,gainasim2=gainasim2,roundasim2=roundasim2,
                    gainnamb=gainnamb,roundnamb=roundnamb,wtpnamb=wtpnamb,randnamb=randnamb,gainnamb2=gainnamb2,roundnamb2=roundnamb2, gainnrisk=gainnrisk, roundnrisk=roundnrisk,wtpnrisk=wtpnrisk,randnrisk=randnrisk,gainnrisk2=gainnrisk2,roundnrisk2=roundnrisk2,gainnsim=gainnsim,roundnsim=roundnsim,wtpnsim=wtpnsim,randnsim=randnsim, gainnsim2=gainnsim2, roundnsim2=roundnsim2)
page_sequence = [Demographics,Questionnaire1,Final_gain]