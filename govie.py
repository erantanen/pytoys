#! /usr/bin/env python


# this is kinda of a gag program made for a friend
# who is transitioning from contractor to govie


def rotation():
    for ich in range(5):
        print("\t chair-spins")


def status(blah):
    if blah == "new":
        return "panic"
    elif blah == "old":
        return "whatever"

eyeRoll = 'sits at desk--> drinks coffee'


def govie():
    print("\n\n As a government employee, \n")
    yOu = input('\t please enter your status "old " or " new": ')
    stat = status(yOu)
    print("\n Your current state of mind is ", stat)
    if yOu == "old":
        print(eyeRoll)
    rotation()


govie()
