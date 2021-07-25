import random

def uwufy(message):
    message = message.replace('L', 'W')
    message = message.replace('R', 'W')
    message = message.replace('l', 'w')
    message = message.replace('r', 'w')
    message = message.replace("no", "nyo")
    message = message.replace("mo", "myo")
    message = message.replace("No", "Nyo")
    message = message.replace("Mo", "Myo")
    message = message.replace("na", "nya")
    message = message.replace("ni", "nyi")
    message = message.replace("nu", "nyu")
    message = message.replace("ne", "nye")
    message = message.replace("anye", "ane")
    message = message.replace("inye", "ine")
    message = message.replace("onye", "one")
    message = message.replace("unye", "une")
    if message.endswith('.'):
        message = message[:-1]
        message+= ', uwu!'
    elif message.endswith('?'):
        message = message[:-1]
        message+= ', uwu?'
    elif message.endswith('!'):
        message = message[:-1]
        message+= ', uwu, senpai!'
    else: message+= ' uwu'
    return message 

def hmmstring():
    hmstring = "H"
    hmlength = random.randint(15, 25)
    for _ in range(0, hmlength):
        flag = random.randint(0, 2)
        if flag:
            hmstring += 'M'
        else:
            hmstring += 'm'
    hmstring += 'm'
    return hmstring
