from otree.api import *
from typing import List
from random import choice, choices, randint, sample
import time
import datetime


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'abarrar'
    players_per_group = None

    num_parts = 2
    num_qs_per_part = 6
    num_rounds = num_parts * num_qs_per_part

    alea = randint(4,10)
    # Urn and Lottery
    balls_num = 100
    balls_colors = ['black', 'yellow', 'red']


    num_columns = 2
    num_choices = 20
    radio_list_choices = list(range(1, num_choices + 1))
    radio_list_probabilities = [0, 1, 2] + [n for n in range(5, 75, 5)] + [85, 100]
    radio_list_probabilities_two_events = [0, 20] + [n for n in range(35, 95, 5)] + [93, 95, 97, 98, 99, 100]
    radio_list = list(zip(radio_list_choices, radio_list_probabilities))
    radio_list_two_event = list(zip(radio_list_choices, radio_list_probabilities_two_events))

    events_table = {
        0: {
            0: dict(winning_colors=balls_colors[0], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon1.png',radiolist=radio_list,barem='de 40 000€ ou moins', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            1: dict(winning_colors=balls_colors[1], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon2.png',radiolist=radio_list,barem='entre 40 000€ et 45000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            2: dict(winning_colors=balls_colors[2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon3.png',radiolist=radio_list,barem='de 45 000€ ou plus', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/risk/risqueavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            3: dict(winning_colors=balls_colors[0:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon4.png',radiolist=radio_list_two_event,barem='de moins de 45 000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            5: dict(winning_colors=balls_colors[1:3], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon5.png',radiolist=radio_list_two_event,barem='de plus de 40 000€', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/risk/risqueavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            4: dict(winning_colors=balls_colors[0:3:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon6.png',radiolist=radio_list_two_event,barem='de 40 000€ ou moins ou de 45 000€ ou plus', low_inf=0, low_sup=40000,mid_sup=45000, high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),

        },
        1: {
            0: dict(winning_colors=balls_colors[0], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon1.png',radiolist=radio_list,barem='de 40 000€ ou moins', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            1: dict(winning_colors=balls_colors[1], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon2.png',radiolist=radio_list,barem='entre 40 000€ et 45000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            2: dict(winning_colors=balls_colors[2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon3.png',radiolist=radio_list,barem='de 45 000€ ou plus', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/risk/risqueavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            3: dict(winning_colors=balls_colors[0:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon4.png',radiolist=radio_list_two_event,barem='de moins de 45 000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            5: dict(winning_colors=balls_colors[1:3], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon5.png',radiolist=radio_list_two_event,barem='de plus de 40 000€', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/risk/risqueavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            4: dict(winning_colors=balls_colors[0:3:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon6.png',radiolist=radio_list_two_event,barem='de 40 000€ ou moins ou de 45 000€ ou plus', low_inf=0, low_sup=40000,mid_sup=45000, high_sup=45000, image='/static/risk/risqueavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),

        }
    }

    bonus = 1000

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part = models.IntegerField()
    event = models.IntegerField()
    ambiguity = models.IntegerField(min=1, max=Constants.num_choices)
    decision_to_pay = models.IntegerField(min=1, max=Constants.num_choices)
    timeSpent = models.FloatField()
    tirage= models.IntegerField()
    tirage2=models.IntegerField()
    rand_wtp = models.IntegerField()
    wtp = models.IntegerField(min=0, max= 300)
# FUNCTIONS


def creating_session(subsession: Subsession):
    const = Constants
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.events_table = {
                part: sample(range(len(events)), k=len(events)) for part, events in const.events_table.items()
            }

    round_number = subsession.round_number
    for p in subsession.get_players():
        part_num, event_num = get_event(const, round_number)
        p.part = part_num
        p.event = p.participant.events_table[part_num][event_num]
        p.rand_wtp = randint(0, 300)


def tirage_gagnant (player: Player):
        player.tirage = sample(range(1, 12), 1)[0]
        player.tirage2 = sample(range(1,6),1)[0]
        player.participant.vars['round_nrisk'] = player.tirage
        player.participant.vars['payoff_nrisk'] = player.in_round(player.tirage).payoff
        player.participant.vars['wtp_nrisk'] = player.in_round(7).wtp
        player.participant.vars['rand_wtp_nrisk']= player.in_round(7).rand_wtp

        player.participant.vars['round_nrisk2'] = player.tirage2
        player.participant.vars['payoff_nrisk2'] = player.in_round(player.tirage2).payoff
def get_rnd_decision(const: Constants):
    return randint(1, const.num_choices)


def get_event(const: Constants, round_number: int):
    return divmod(round_number - 1, const.num_qs_per_part)


def get_balls(const: Constants, part: int, event: int) -> List[str]:
    return [color for color in const.balls_colors
            for _ in range(const.events_table[part][event]['balls_num_per_color'][color])]


def draw_ball(balls: List[str]):
    ball = choice(balls)
    return ball


def is_winning_draw_from_urn(const: Constants, part: int, event: int):
    return [0, const.bonus][draw_ball(get_balls(const, part, event)) in const.events_table[part][event]['winning_colors']]


def is_winning_lottery(const: Constants, part: int, event: int, decision_num: int):
    probs = const.radio_list_probabilities_two_events \
        if len(const.events_table[part][event]['winning_colors']) > 1 else const.radio_list_probabilities
    return choices([const.bonus, 0], weights=[probs[decision_num - 1], 100 - probs[decision_num - 1]])[0]


def play_lottery(ambiguity, decision_num):
    return decision_num >= ambiguity


def set_payoff(player: Player, const: Constants):
    decision_to_pay = get_rnd_decision(const)
    player.decision_to_pay = decision_to_pay
    if play_lottery(player.ambiguity, decision_to_pay):
        player.payoff = is_winning_lottery(const, player.part, player.event, decision_to_pay)
    else:
        player.payoff = is_winning_draw_from_urn(const, player.part, player.event)

def set_payoff_wtp(player: Player, const: Constants):
    decision_to_pay = get_rnd_decision(const)
    player.decision_to_pay = decision_to_pay
    if play_lottery(player.ambiguity, decision_to_pay):
        player.payoff = is_winning_lottery(const, player.part, player.event, decision_to_pay) - player.in_round(7).rand_wtp
    else:
        player.payoff = is_winning_draw_from_urn(const, player.part, player.event) - player.in_round(7).rand_wtp
# PAGES
class Decision(Page):
    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.round_number < 7

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player, Constants)

    @staticmethod
    def vars_for_template(player: Player):
        const = Constants
        low_inf = const.events_table[player.part][player.event]["fortemplate"]["low_inf"]
        low_sup = const.events_table[player.part][player.event]["fortemplate"]["low_sup"]
        mid_sup = const.events_table[player.part][player.event]["fortemplate"]["mid_sup"]
        high_sup = const.events_table[player.part][player.event]["fortemplate"]["high_sup"]
        barem = const.events_table[player.part][player.event]["fortemplate"]["barem"]
        image_path = const.events_table[player.part][player.event]["fortemplate"]["image"]
        tribunal = const.events_table[player.part][player.event]["fortemplate"]["tribunal_judiciaire"]
        appel= const.events_table[player.part][player.event]["fortemplate"]["cour_appel"]
        mariage = const.events_table[player.part][player.event]["fortemplate"]["mariage"]
        communaute = const.events_table[player.part][player.event]["fortemplate"]["valeur_communauté"]
        age_c= const.events_table[player.part][player.event]["fortemplate"]["age_c"]
        sante_c= const.events_table[player.part][player.event]["fortemplate"]["santé"]
        revenus_c= const.events_table[player.part][player.event]["fortemplate"]["revenus_annuels"]
        age_d = const.events_table[player.part][player.event]["fortemplate"]["age_d"]
        sante_d = const.events_table[player.part][player.event]["fortemplate"]["santé_d"]
        revenus_d= const.events_table[player.part][player.event]["fortemplate"]["revenus_d"]
        radiolist = const.events_table[player.part][player.event]["fortemplate"]["radiolist"]
        aide = const.events_table[player.part][player.event]["fortemplate"]["aide"]
        return dict(aide=aide,radiolist=radiolist,low_inf=low_inf,low_sup=low_sup,mid_sup=mid_sup,high_sup=high_sup,barem=barem,image=image_path,tribunal=tribunal,appel=appel,mariage=mariage,communaute=communaute,age_c=age_c,sante_c=sante_c,revenus_c=revenus_c, age_d=age_d, sante_d=sante_d,revenus_d=revenus_d)



class Nouvellepartie(Page):
    body_text = "Une nouvelle partie va commencer"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 12

    def before_next_page(player: Player,timeout_happened):
        tirage_gagnant(player)

class WTP(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 7
    form_model = 'player'
    form_fields = ['wtp']
class Info(Page):

    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.round_number > 6

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff_wtp(player, Constants)

    @staticmethod
    def vars_for_template(player: Player):
        const = Constants
        low_inf = const.events_table[player.part][player.event]["fortemplate"]["low_inf"]
        low_sup = const.events_table[player.part][player.event]["fortemplate"]["low_sup"]
        mid_sup = const.events_table[player.part][player.event]["fortemplate"]["mid_sup"]
        high_sup = const.events_table[player.part][player.event]["fortemplate"]["high_sup"]
        barem = const.events_table[player.part][player.event]["fortemplate"]["barem"]
        image_path = const.events_table[player.part][player.event]["fortemplate"]["image"]
        tribunal = const.events_table[player.part][player.event]["fortemplate"]["tribunal_judiciaire"]
        appel= const.events_table[player.part][player.event]["fortemplate"]["cour_appel"]
        mariage = const.events_table[player.part][player.event]["fortemplate"]["mariage"]
        communaute = const.events_table[player.part][player.event]["fortemplate"]["valeur_communauté"]
        age_c= const.events_table[player.part][player.event]["fortemplate"]["age_c"]
        sante_c= const.events_table[player.part][player.event]["fortemplate"]["santé"]
        revenus_c= const.events_table[player.part][player.event]["fortemplate"]["revenus_annuels"]
        age_d = const.events_table[player.part][player.event]["fortemplate"]["age_d"]
        sante_d = const.events_table[player.part][player.event]["fortemplate"]["santé_d"]
        revenus_d= const.events_table[player.part][player.event]["fortemplate"]["revenus_d"]
        radiolist = const.events_table[player.part][player.event]["fortemplate"]["radiolist"]
        aide = const.events_table[player.part][player.event]["fortemplate"]["aide"]
        return dict(aide=aide,radiolist=radiolist,low_inf=low_inf,low_sup=low_sup,mid_sup=mid_sup,high_sup=high_sup,barem=barem,image=image_path,tribunal=tribunal,appel=appel,mariage=mariage,communaute=communaute,age_c=age_c,sante_c=sante_c,revenus_c=revenus_c, age_d=age_d, sante_d=sante_d,revenus_d=revenus_d)

page_sequence = [WTP,Info,Decision,Nouvellepartie]
