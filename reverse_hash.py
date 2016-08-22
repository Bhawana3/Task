
source = 'acdegilmnoprstuw'

"""
Hash:
    base_h = 7
    h -> h*37 + k,  k E [0,15]

=> Reverse Hash:
    h -> (h-k)/37,  base_h = 7
"""
def reverse_hash (h):
    # h is an integer
    global source
    msg = ''
    while h > 7:
        k = 0
        for i in range(len(source)):
            if (h-i) % 37 == 0:
                k = i
                break
        msg += source[k]
        h = (h-k)/37

    # If base_h is not 7 => invalid input received
    if h != 7:
        raise Exception('Hashed string is invalid')

    msg = msg[::-1]         # reverse to get the original msg
    return msg

def hash_func (s):
    global source
    h = 7
    for letter in s:
        h = h * 37 + source.index(letter)
    return h


if __name__ == '__main__':
    #s = 'leepadg'
    #user_input = hash_func (s)
    user_input = int('930846109532517')
    #user_input = input()
    original_msg = reverse_hash (user_input)

    #print s
    print 'User input is:', user_input
    print 'The original string is:', original_msg
    print 'Hashing again to verify:', hash_func(original_msg)

    assert (hash_func(original_msg) == user_input), "Reverse hash found is incorrect"
    print 'Reverse hash working correctly'
