from Constants import DATA_STAGE_FILE, DATA_MASTER_FILE
import json

def copy_data_stage_to_master():
    with open(DATA_STAGE_FILE, "r") as stageData:
        data = json.load(stageData)
        print("Carregou da stage " + str(data))
    with open(DATA_MASTER_FILE, "a") as masterData:
        masterData.write(str(json.dumps(data)) + '\n')
        print("Escreveu na master " + str(data))
    with open(DATA_STAGE_FILE, "w") as stageData:
        stageData.write("")

class StageHelper:
    pass
