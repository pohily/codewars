MORSE_CODE = {' ':    '', '.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }
def decodeBits(bits):
    bits = bits.strip('0')
    
    if not '1' in bits:
        return ''
    
    start = bits.index('1')
    if '0' in bits:
        end = bits[start:].index('0')
        lenth = end - start

        if lenth % 3 == 0:
            if ('0' + '1' * (lenth // 3) + '0') in ('0' + bits + '0'):
                lenth //= 3
            elif ('1' + '0' * (lenth // 3) + '1') in bits and '1' * lenth in bits:
                lenth //= 3
    else:
        lenth = bits.count('1')

    return bits.replace('1'*3*lenth, '-').replace('0'*3*lenth, ' ').replace('1'*lenth, '.').replace('0'*lenth, '')

def decodeMorse(morseCode):
    
    morseCode = morseCode.split(" ")
    
    result = ''
    for letter in morseCode[1:]:
        if letter == '':
            result += ' '
            continue
        result += MORSE_CODE[letter]
    return MORSE_CODE[morseCode[0]].upper() + result.replace('  ', ' ')

print(decodeMorse(decodeBits('101')))



"""
def decodeBits(bits):
    import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))

    """