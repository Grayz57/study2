from otree.api import *
from typing import List
from random import choice, choices, randint, sample
import csv
import time
import datetime


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'eeeazaa'
    players_per_group = None

    num_parts = 2
    num_qs_per_part = 6  # 8
    num_rounds = num_parts * num_qs_per_part

    # Urn and Lottery
    balls_num = 100
    balls_colors = ['low', 'mid', 'high']

    num_columns = 2
    num_choices = 20
    radio_list_choices = list(range(1, num_choices + 1))
    radio_list_probabilities = [0, 1, 2] + [n for n in range(5, 75, 5)] + [85, 100]
    radio_list_probabilities_two_events = [0, 20] + [n for n in range(35, 95, 5)] + [93, 95, 97, 98, 99, 100]
    radio_list = list(zip(radio_list_choices, radio_list_probabilities))
    radio_list_two_event = list(zip(radio_list_choices, radio_list_probabilities_two_events))


    events_table = {
        0: {
            0: dict(winning_colors=balls_colors[0], balls_num_per_color=dict(low=0, mid=0, high=100),fortemplate=dict(aide='/static/aidedouai/douai1.png',radiolist=radio_list,barem='de 55 000€ ou moins', low_inf=0, low_sup=55000, mid_sup=60000,high_sup=60000, image='/static/ambiguity/ambiguitedouai.png', tribunal_judiciaire='Douai (59)',cour_appel='Douai (59)', mariage='29 ans', valeur_communauté='134 231', age_c='52',santé='Parfaite santé', revenus_annuels='7 104', age_d='53',santé_d='parfaite santé', revenus_d='37 584')),
            1: dict(winning_colors=balls_colors[1], balls_num_per_color=dict(low=0, mid=0, high=100),fortemplate=dict(aide='/static/aidedouai/douai2.png',radiolist=radio_list,barem='comprise entre 55 000€ et 60 000€', low_inf=0, low_sup=55000, mid_sup=60000,high_sup=60000, image='/static/ambiguity/ambiguitedouai.png', tribunal_judiciaire='Douai (59)',cour_appel='Douai (59)', mariage='29 ans', valeur_communauté='134 231', age_c='52',santé='Parfaite santé', revenus_annuels='7 104', age_d='53',santé_d='parfaite santé', revenus_d='37 584')),
            2: dict(winning_colors=balls_colors[2], balls_num_per_color=dict(low=0, mid=0, high=100),fortemplate=dict(aide='/static/aidedouai/douai3.png',radiolist=radio_list,barem='de 60 000€ ou plus', low_inf=0, low_sup=55000, mid_sup=60000, high_sup=60000,image='/static/ambiguity/ambiguitedouai.png', tribunal_judiciaire='Douai (59)',cour_appel='Douai (59)', mariage='29 ans', valeur_communauté='134 231', age_c='52',santé='Parfaite santé', revenus_annuels='7 104', age_d='53',santé_d='parfaite santé', revenus_d='37 584')),
            3: dict(winning_colors=balls_colors[0:2], balls_num_per_color=dict(low=0, mid=0, high=100),fortemplate=dict(aide='/static/aidedouai/douai4.png',radiolist=radio_list_two_event,barem='de moins de 60 000€', low_inf=0, low_sup=55000, mid_sup=60000,high_sup=60000, image='/static/ambiguity/ambiguitedouai.png', tribunal_judiciaire='Douai (59)',cour_appel='Douai (59)', mariage='29 ans', valeur_communauté='134 231', age_c='52',santé='Parfaite santé', revenus_annuels='7 104', age_d='53',santé_d='parfaite santé', revenus_d='37 584')),
            4: dict(winning_colors=balls_colors[0:3:2], balls_num_per_color=dict(low=0, mid=0, high=100),fortemplate=dict(aide='/static/aidedouai/douai5.png',radiolist=radio_list_two_event,barem='de 55 000€ ou moins ou de 60000€ ou plus', low_inf=0, low_sup=55000,mid_sup=60000, high_sup=60000, image='/static/ambiguity/ambiguitedouai.png',tribunal_judiciaire='Douai (59)', cour_appel='Douai (59)', mariage='29 ans',valeur_communauté='134 231', age_c='52', santé='Parfaite santé',revenus_annuels='7 104', age_d='53', santé_d='parfaite santé', revenus_d='37 584')),
            5: dict(winning_colors=balls_colors[1:3], balls_num_per_color=dict(low=0, mid=0, high=100), fortemplate=dict(aide='/static/aidedouai/douai6.png',radiolist=radio_list_two_event,barem='de plus de 55 000€', low_inf=0, low_sup=55000, mid_sup=60000, high_sup=60000,image='/static/ambiguity/ambiguitedouai.png', tribunal_judiciaire='Douai (59)', cour_appel='Douai (59)',mariage='29 ans', valeur_communauté='134 231', age_c='52', santé='Parfaite santé',revenus_annuels='7 104', age_d='53', santé_d='parfaite santé', revenus_d='37 584')),
        },

        1: {
            0: dict(winning_colors=balls_colors[0], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon1.png',radiolist=radio_list,barem='de 40 000€ ou moins', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/ambiguity/ambiguiteavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            1: dict(winning_colors=balls_colors[1], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon2.png',radiolist=radio_list,barem='entre 40 000€ et 45000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/ambiguity/ambiguiteavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            2: dict(winning_colors=balls_colors[2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon3.png',radiolist=radio_list,barem='de 45 000€ ou plus', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/ambiguity/ambiguiteavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            3: dict(winning_colors=balls_colors[0:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon4.png',radiolist=radio_list_two_event,barem='de moins de 45 000€', low_inf=0, low_sup=40000, mid_sup=45000,high_sup=45000, image='/static/ambiguity/ambiguiteavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),
            5: dict(winning_colors=balls_colors[1:3], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon5.png',radiolist=radio_list_two_event,barem='de plus de 40 000€', low_inf=0, low_sup=40000, mid_sup=45000, high_sup=45000,image='/static/ambiguity/ambiguiteavignon.png', tribunal_judiciaire='Avignon (84)',cour_appel='Nîmes (30)', mariage='18 ans', valeur_communauté='195 000', age_c='47',santé='Parfaite santé', revenus_annuels='11 448', age_d='49',santé_d='parfaite santé', revenus_d='31 896')),
            4: dict(winning_colors=balls_colors[0:3:2], balls_num_per_color=dict(low=100, mid=0, high=0),fortemplate=dict(aide='/static/aideavignon/avignon6.png',radiolist=radio_list_two_event,barem='de 40 000€ ou moins ou de 45 000€ ou plus', low_inf=0, low_sup=40000,mid_sup=45000, high_sup=45000, image='/static/ambiguity/ambiguiteavignon.png',tribunal_judiciaire='Avignon (84)', cour_appel='Nîmes (30)', mariage='18 ans',valeur_communauté='195 000', age_c='47', santé='Parfaite santé',revenus_annuels='11 448', age_d='49', santé_d='parfaite santé', revenus_d='31 896')),

        }
    }


    bonus = 20

    # Bubble Chart
    bubble_chart_title = ''


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part = models.IntegerField()
    event = models.IntegerField()
    ambiguity = models.IntegerField(min=1, max=Constants.num_choices)
    timeSpent = models.FloatField()
    decision_to_pay = models.IntegerField(min=1, max=Constants.num_choices)
    tirage = models.IntegerField()
    rand_wtp = models.IntegerField()
    wtp = models.IntegerField()

    # Bubble chart
    case_id = models.StringField(initial='955')
    decision = models.IntegerField(initial=0)


# FUNCTIONS
def creating_session(subsession: Subsession):
    const = Constants

    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.events_table = {
                part: sample(range(len(events)), k=len(events)) for part, events in const.events_table.items()
            }

        # Bubble Chart
        cases = read_csv_table('cases')
        for case in cases:
            add_timestamp_to_case(case)
            add_table_to_case(case)
        subsession.session.cases_by_similarity = cases

    round_number = subsession.round_number
    for p in subsession.get_players():
        part_num, event_num = get_event(const, round_number)
        p.part = part_num
        p.event = p.participant.events_table[part_num][event_num]
        p.rand_wtp = randint(1, 10)
def tirage_gagnant(player: Player):
    player.tirage = sample(range(1, 12), 1)[0]
    player.participant.vars['round_nsimilar'] = player.tirage
    player.participant.vars['payoff_nsimilar'] = player.in_round(player.tirage).payoff


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
        player.payoff = is_winning_lottery(const, player.part, player.event, decision_to_pay) - player.rand_wtp
    else:
        player.payoff = is_winning_draw_from_urn(const, player.part, player.event) - player.rand_wtp


# Bubble Chart
def read_csv_table(file_name, path='nsimilar/static/task/data/') -> list:
    with open(f'{path}{file_name}.csv', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def add_timestamp_to_case(case: dict):
    case['timestamp'] = time.mktime(datetime.datetime.strptime(case['Date'], "%d/%m/%Y").timetuple())


def add_table_to_case(case: dict):
    case['table'] = '<div class="highcharts-data-point-info">' + \
                    f'<p>La décision ' \
                    f' en date du <b class="color-amber">{case["Date"]}</b> présente ' \
                    f'<b class="color-amber">{case["Taux de correspondance"]}%</b> de correspondance ' \
                    f'avec votre requête.</p>' + \
                    '<ul class="fs-smaller">' + \
                    ''.join(f'<li>{k}: {v}</li>' for k, v in case.items()
                            if k not in ['Taux de correspondance', 'Date', 'case_id', 'timestamp']) + \
                    '</ul>' + \
                    '</div>'


def get_cases_series_by_decision(cases: list, decision: str) -> List[dict]:
    return [
        dict(
            x=case['timestamp'] * 1000,
            y=int(case['Taux de correspondance']),
            z=int(case['Montant de la prestation compensatoire']),
            case_id=case['case_id'],
            pension=case['Montant de la prestation compensatoire'],
            date=case['Date'],
            table=case['table']
        ) for case in cases if case['Decision'] == decision
    ]


# PAGES

class Decision(Page):
    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.wtp < player.rand_wtp

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

    @staticmethod
    def js_vars(player: Player):
        const = Constants
        if player.round_number < 7:
            case_id = "955"
        else:
            case_id = "500"
        cases = player.session.cases_by_similarity
        cases = [case for case in cases if case['case_id'] == case_id]
        cases_series = dict(
            condemnation=dict(
                name='Condamnation',
                data=get_cases_series_by_decision(cases, 'Condamnation')
            ),
            condemnation_no=dict(
                name='Absence de condamnation',
                data=get_cases_series_by_decision(cases, 'Non Condamnation')
            )
        )

        return dict(
            bubble_chart_title=const.bubble_chart_title,
            cases_series=cases_series
        )

class Info(Page):
    form_model = 'player'
    form_fields = ['ambiguity', 'timeSpent']

    @staticmethod
    def is_displayed(player:Player):
        return player.wtp >= player.rand_wtp

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

    @staticmethod
    def js_vars(player: Player):
        const = Constants
        if player.round_number < 7:
            case_id = "955"
        else:
            case_id = "500"
        cases = player.session.cases_by_similarity
        cases = [case for case in cases if case['case_id'] == case_id]
        cases_series = dict(
            condemnation=dict(
                name='Condamnation',
                data=get_cases_series_by_decision(cases, 'Condamnation')
            ),
            condemnation_no=dict(
                name='Absence de condamnation',
                data=get_cases_series_by_decision(cases, 'Non Condamnation')
            )
        )

        return dict(
            bubble_chart_title=const.bubble_chart_title,
            cases_series=cases_series
        )
class Nouvelleurne(Page):
    body_text = "Une nouvelle urne va être générée"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6

class Nouvellepartie(Page):
    body_text = "Une nouvelle partie va commencer"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 12

    def before_next_page(player: Player,timeout_happened):
        tirage_gagnant(player)

class WTP(Page):
    form_model = 'player'
    form_fields = ['wtp']

page_sequence = [WTP,Decision,Info,Nouvelleurne,Nouvellepartie]
