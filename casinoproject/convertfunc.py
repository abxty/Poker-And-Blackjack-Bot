def convertselect(text, type):
    text = str(text)
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    if type == "int":
        text = int(text)
    elif type == "non":
        text = text.replace("'", '')
    return text
