with open ('mat_dv.txt', 'r') as f:
    win8 = []
    win9 = []
    win10 = []
    win11 = []

    win_a = []
    win_g = []

    m8 = 0
    m9 = 0
    m10 = 0
    m11 = 0

    g = 0
    a = 0

    for i in f:
        if i[-1] == '\n':
            s = i[0:-1].split(' ')
        elif i[-1] != '\n':
            s = i[0:].split()

        if s[2] == '8':
            if int(s[3]) + int(s[4]) > m8:
                m8 = int(s[3]) + int(s[4])
                win8 = s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'
            elif int(s[3]) + int(s[4]) == m8:
                win8 += s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'

        if s[2] == '9':
            if int(s[3]) + int(s[4]) > m9:
                m9 = int(s[3]) + int(s[4])
                win9 = s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'
            elif int(s[3]) + int(s[4]) == m9:
                win9 += s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'

        if s[2] == '10':
            if int(s[3]) + int(s[4]) > m10:
                m10 = int(s[3]) + int(s[4])
                win10 = s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'
            elif int(s[3]) + int(s[4]) == m10:
                win10 += s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'

        if s[2] == '11':
            if int(s[3]) + int(s[4]) > m11:
                m11 = int(s[3]) + int(s[4])
                win11 = s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'
            elif int(s[3]) + int(s[4]) == m11:
                win11 += s[0] + ' ' + s[1] + ' ' + str(int(s[3]) + int(s[4])) + '\n'

        if int(s[3]) > a:
            a = int(s[3])
            win_a = s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[3] + '\n'
        elif int(s[3]) == a:
            win_a += s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[3] + '\n'
        if int(s[4]) >= g:
            g = int(s[4])
            win_g = s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[4] + '\n'
        elif int(s[4]) == g:
            win_g += s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[4] + '\n'

    print('8: ', ''.join(win8))
    print('9: ', ''.join(win9))
    print('10: ', ''.join(win10))
    print('11: ', ''.join(win11))

    print()

    print('Алгебра: ', ''.join(win_a))
    print('Геометрия: ', ''.join(win_g))
