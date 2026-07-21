#start
height = int(input("height? "))
for i in range(1, height + 1):
    j = 0
    print()
    for j in range(1, i + 1):
        print(' * ', end='')
# the bonus
for i in range(height, 0, -1):
    j = 0
    print()
    for j in range(1, i + 1):
        print(' * ', end='')
#stop
