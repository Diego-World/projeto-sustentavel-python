from Constants import DATA_STAGE_LOGIN_FILE, DATA_MASTER_LOGIN_FILE
import json

def copy_login_data_stage_to_master():
    with open(DATA_STAGE_LOGIN_FILE, "r") as stageData:
        data = json.load(stageData)
        print("Carregou da stage " + str(data))
    with open(DATA_MASTER_LOGIN_FILE, "a") as masterData:
        masterData.write(str(json.dumps(data)) + '\n')
        print("Escreveu na master " + str(data))
    with open(DATA_STAGE_LOGIN_FILE, "w") as stageData:
        stageData.write("")

class StageHelper:
    pass
