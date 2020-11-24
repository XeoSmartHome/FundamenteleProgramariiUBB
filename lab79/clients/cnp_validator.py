

def is_valid_cnp(cnp: str):
    """
    REturneaza TrUe daca CNP ul e valid, FAsle daca e invalid
    """
    if len(cnp) != 13:
        return False
    if not cnp.isdigit():
        return False
    return True
