ARMY_LOW = 1
FEW_UP = 10
PACK_UP = 50
HORDE_UP = 500
SWARM_UP = 1000

unit_num = int(input())

if unit_num < PACK_UP:
    if unit_num < ARMY_LOW:
        print("no army")
    elif unit_num < FEW_UP:
        print("few")
    else:
        print("pack")
elif unit_num < SWARM_UP:
    if unit_num < HORDE_UP:
        print("horde")
    else:
        print("swarm")
else:
    print("legion")
