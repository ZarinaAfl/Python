
def is_prefix(s1, s2):
    '''
    :param s1: possible prefix
    :param s2: source string
    :return: true of s1 is prefix of s2, false otherwise
    '''

    if len(s1) > len(s2):
        return False
    else:
        i = 0
        f = True
        while i < len(s1) and f:
            if s1[i] != s2[i]:
                f = False
            i+=1

    return f

