from prettylogfile import *
from requests import *
from consolemenu import *
from consolemenu.items import *
from blaseball_lookups import *
from prettylogfile import *

def hello():
    print("hello world")
#format_log_all("Logs/Season 2 - Post/blaseball-log-postseason-2.json")

menu = ConsoleMenu("Blaseball Parser Main Menu", "By Sakimori#1228")

hi_item = FunctionItem("Say hi!", hello)
id_lookups_item = FunctionItem("Copy a team id to clipboard", team_lookup_menu)
full_format_item = FunctionItem("Format an entire log file", format_log_all)
play_by_play_item = FunctionItem("Debug pbp parser", format_log_pbp)



menu.append_item(hi_item)
menu.append_item(id_lookups_item)
menu.append_item(full_format_item)
menu.append_item(play_by_play_item)

menu.show()