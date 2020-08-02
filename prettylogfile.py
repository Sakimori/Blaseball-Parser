import json
with open('config.json') as json_file:
   config = json.load(json_file)

base_filepath = config["file_path"]
#filepath = 'Logs/Season 2 - Post/blaseball-log-postseason-2.json'

def set_path():
    path_append = input("Which log file needs processing?")
    filepath = base_filepath + path_append
    return filepath

def format_log_pbp():
    log_path = set_path()
    game_id = input("Game id: ")
    subdic = {}

    with open(log_path, "r") as file:
        game_file = open(base_filepath + input("Save as: "), "w")
        subdic = json.load(file)
        print(type(subdic))
        for update in subdic:
            print(type(update))
            dic = json.loads(update)
            print(dic)
            for game in dic["schedule"]:
                if game["_id"] == game_id:
                    game_file.writeline(game["lastUpdate"])
        game_file.close()

def format_log_all():
    log_path = set_path()
    big_dic = {}
    with open(log_path, "r") as raw_log:
        log_lines = raw_log.readlines()
        update_num = 0
        for line in log_lines:
            line_j = json.loads(line)
            big_dic[str(update_num)] = line_j
            update_num += 1
    
    with open(log_path+"done", "w") as dest:
        json.dump(big_dic, dest, sort_keys=True, indent = 4)
