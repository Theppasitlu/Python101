def is_undergrad(sid):
    if str(sid)[2] in ["0","3","4"]:
        return True
    else:
        return False

def get_faculty( sid ):
    if str(sid)[8:10] == "21" :
        return "ENG"
    elif str(sid)[8:10] == "22":
        return "ART"
    elif str(sid)[8:10] == "23":
        return "SCI"
    else:
        return "OTHER"

def get_status( sid ):
    X = []
    if str(sid)[2] in ["0","3","4"]  :X.append("U")
    elif str(sid)[2] in ["1","7","8"]:X.append("G")

    if str(sid)[8:10] == "21"   :X.append("ENG")
    elif str(sid)[8:10] == "22" :X.append("ART")
    elif str(sid)[8:10] == "23" :X.append("SCI")
    else                        :X.append("OTHER")
    return X

exec(input().strip())

