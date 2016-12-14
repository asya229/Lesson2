slovar={'login':'asya229', 'passw':'qwerty', 'host':1234}

def auth(user):
    while True:
        if user == slovar['passw']:
            try:
                print("Hi, {}".format(slovar['login']))

            except KeyboardInterrupt:
                print('\n мяф')
                break
        else:
            print('Unknownu')
            break

user = input('Ведите пароль ')

auth(user)


def zapili(x):
    while x<100:
        print(x)
        x+=1


