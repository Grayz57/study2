from otree.api import *
from typing import List
from random import choice, choices, randint, sample
import time
import datetime


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'abnarrrjeear'
    players_per_group = None

    num_parts = 1
    num_qs_per_part = 6
    num_rounds = num_parts * num_qs_per_part

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
            0: dict(winning_colors=balls_colors[0], balls_num_per_color=dict(black=21, yellow=47, red=32), fortemplate =dict( radiolist=radio_list,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50, good = 'noire')),
            1: dict(winning_colors=balls_colors[1], balls_num_per_color=dict(black=21, yellow=47, red=32), fortemplate =dict( radiolist=radio_list,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50,good = 'jaune')),
            2: dict(winning_colors=balls_colors[2], balls_num_per_color=dict(black=21, yellow=47, red=32), fortemplate =dict( radiolist=radio_list,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50,good = 'rouge')),
            3: dict(winning_colors=balls_colors[0:2], balls_num_per_color=dict(black=21, yellow=47, red=32), fortemplate =dict( radiolist=radio_list_two_event,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50, good='noire ou jaune')),
            4: dict(winning_colors=balls_colors[1:3], balls_num_per_color=dict(black=21, yellow=47, red=32), fortemplate=dict(radiolist=radio_list_two_event,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50,good='jaune ou rouge')),
            5: dict(winning_colors=balls_colors[0:3:2], balls_num_per_color=dict(black=21, yellow=47, red=32),fortemplate=dict(radiolist=radio_list_two_event,black_inf=20, black_sup=50, yellow_inf=10, yellow_sup=40, red_inf=10, red_sup=50,good='noire ou rouge')),

        },
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
    wtp = models.IntegerField(min=0, max = 300)
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
        p.rand_wtp = randint(1,10)


def tirage_gagnant (player: Player):
        player.tirage = sample(range(1, 6), 1)[0]
        player.tirage2 = sample(range(1, 6), 1)[0]
        player.participant.vars['wtp_aamb'] = player.in_round(1).wtp
        player.participant.vars['rand_wtp']= player.in_round(1).rand_wtp
        player.participant.vars['player_tirage'] = player.tirage
        player.participant.vars['player_payoff'] = player.in_round(player.tirage).payoff
        player.participant.vars['player_tirage2'] = player.tirage2
        player.participant.vars['player_payoff2'] = player.in_round(player.tirage2).payoff

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
        player.payoff = is_winning_lottery(const, player.part, player.event, decision_to_pay) - player.in_round(1).wtp
    else:
        player.payoff = is_winning_draw_from_urn(const, player.part, player.event) - player.in_round(1).wtp

# PAGES
class Decision(Page):
    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.in_round(1).wtp < player.in_round(1).rand_wtp


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player, Constants)

    @staticmethod
    def vars_for_template(player: Player):
        const = Constants
        black = const.events_table[player.part][player.event]["balls_num_per_color"]["black"]
        yellow = const.events_table[player.part][player.event]["balls_num_per_color"]["yellow"]
        red = const.events_table[player.part][player.event]["balls_num_per_color"]["red"]
        win = const.events_table[player.part][player.event]["winning_colors"]
        black_inf = const.events_table[player.part][player.event]["fortemplate"]["black_inf"]
        black_sup = const.events_table[player.part][player.event]["fortemplate"]["black_sup"]
        yellow_inf = const.events_table[player.part][player.event]["fortemplate"]["yellow_inf"]
        yellow_sup = const.events_table[player.part][player.event]["fortemplate"]["yellow_sup"]
        red_inf = const.events_table[player.part][player.event]["fortemplate"]["red_inf"]
        red_sup = const.events_table[player.part][player.event]["fortemplate"]["red_sup"]
        good =  const.events_table[player.part][player.event]["fortemplate"]["good"]
        radiolist = const.events_table[player.part][player.event]["fortemplate"]["radiolist"]
        return dict(radiolist=radiolist,black=black, red= red, yellow= yellow, win=win, black_inf=black_inf,black_sup=black_sup, yellow_inf=yellow_inf,yellow_sup=yellow_sup,red_inf=red_inf,red_sup=red_sup, good=good)



class Nouvellepartie(Page):
    body_text = "Une nouvelle partie va commencer"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6

    def before_next_page(player: Player,timeout_happened):
        tirage_gagnant(player)

class WTP(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    form_model = 'player'
    form_fields = ['wtp']

class Info(Page):

    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.in_round(1).wtp >= player.in_round(1).rand_wtp

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff_wtp(player, Constants)

    @staticmethod
    def vars_for_template(player: Player):
        const = Constants
        black = const.events_table[player.part][player.event]["balls_num_per_color"]["black"]
        yellow = const.events_table[player.part][player.event]["balls_num_per_color"]["yellow"]
        red = const.events_table[player.part][player.event]["balls_num_per_color"]["red"]
        win = const.events_table[player.part][player.event]["winning_colors"]
        black_inf = const.events_table[player.part][player.event]["fortemplate"]["black_inf"]
        black_sup = const.events_table[player.part][player.event]["fortemplate"]["black_sup"]
        yellow_inf = const.events_table[player.part][player.event]["fortemplate"]["yellow_inf"]
        yellow_sup = const.events_table[player.part][player.event]["fortemplate"]["yellow_sup"]
        red_inf = const.events_table[player.part][player.event]["fortemplate"]["red_inf"]
        red_sup = const.events_table[player.part][player.event]["fortemplate"]["red_sup"]
        good =  const.events_table[player.part][player.event]["fortemplate"]["good"]
        radiolist = const.events_table[player.part][player.event]["fortemplate"]["radiolist"]
        return dict(radiolist=radiolist,black=black, red= red, yellow= yellow, win=win, black_inf=black_inf,black_sup=black_sup, yellow_inf=yellow_inf,yellow_sup=yellow_sup,red_inf=red_inf,red_sup=red_sup, good=good)

page_sequence = [WTP,Decision,Info,Nouvellepartie]
