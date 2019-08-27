def create_phone_number(n):
    one = ''.join(n[:3])
    two = ''.join(n[3:6])
    three = ''.join(n[6:])
    return f'({one}) {two}-{three}'