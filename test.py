def check(string):
    l = []
    for i in range(len(string)/2):
        l.append(string[i])
        print l
        if can_build(l, string):
            return True
    return False


def can_build(l, string):
    if len(string)%len(l) == 0:
        times = len(string)/len(l)
        tmp_string = ''.join(l)
        if tmp_string*times == string:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    s = raw_input('string to be check')
    print check(s)