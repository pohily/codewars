def meeting(s):
    s = s.upper()
    tmp = sorted([x.split(':') for x in s.split(';')])
    tmp = sorted([b + ', ' + a for a, b in tmp])
    return ''.join(['('+ x + ')' for x in tmp])