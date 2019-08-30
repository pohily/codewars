def generate_hashtag(s):
    hashtag = '#'
    capital = True

    for letter in s:
        if letter.isspace():
            capital = True
        else:
            if capital:
                hashtag += letter.upper()
            else:
                hashtag += letter.lower()
            capital = False
            
    return hashtag if 1 < len(hashtag) < 141 else False