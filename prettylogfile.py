import json
with open('config.json') as json_file:
    config = json.load(json_file)

#filepath = config["file_path"] + input("Path to file in logs folder: ")
filepath = 'Logs/Season 2 - Post/blaseball-log-postseason-2.json'

with open(filepath, "r") as unpretty_log:
    updatecount = 0
    newlog = open(filepath+"temp", "w")
    newlog.write("{ \n")

    for line in unpretty_log:
        if updatecount == 0:
            newlog.write("\"update {}\" : \n".format(updatecount) + line[0:len(line)-1])
        else:
            newlog.write(",\n""\"update {}\" : \n".format(updatecount) + line[0:len(line)-1])
        updatecount += 1
    
    newlog.write("\n}")
    newlog.close()

with open(filepath+"temp", "r") as unpretty_log:
   unprettylog = json.load(unpretty_log)

with open(filepath+"pretty", "w") as dest:
   json.dump(unprettylog, dest, indent = 4)