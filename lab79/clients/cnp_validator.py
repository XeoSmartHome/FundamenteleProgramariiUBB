

def is_valid_cnp(cnp: str):
    if len(cnp) != 13:
        return False
    if not cnp.isdigit():
        return False
    return True
