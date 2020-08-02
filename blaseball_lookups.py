import requests
from json import *
from consolemenu import *
from consolemenu.items import *
import pyperclip

#def team_lookup_with_id(id):

def clipboard_copy(list):
    print(list)
    pyperclip.lazy_load_stub_copy(list)

def get_team_dic():
    team_defs_response = requests.get('https://blaseball.com/database/allTeams')
    if not team_defs_response:
        print(f"Server error code {team_defs_response.status_code}!")
        return None
    return team_defs_response.json()

def get_team_info(team_id):
    team_response = requests.get(f'https://blaseball.com/database/team?id={team_id}')
    if team_response:
        return team_response.json
    return None

def name_to_id(team_name):
    team_dic = get_team_dic()
    for team in team_dic:
        if team["fullName"] == team_name or team["nickname"] == team_name:
            return (team["_id"], team)
    else:
        return None

def team_lookup_menu():
    teams = get_team_dic()

    menu = ConsoleMenu("All teams:")

    for team in teams:
        name = team["fullName"]
        raw_id = team["_id"]
        slogan = team["slogan"]
        id = [raw_id]
        new_item = FunctionItem(f"{name}: {slogan}", clipboard_copy, id)
        menu.append_item(new_item)

    menu.show()