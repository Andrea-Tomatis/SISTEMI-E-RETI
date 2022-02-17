'''
Vernam cipher

25.11.2021

@Andrea Tomatis
'''


#offset to reach the english alphabet converting int to char
ASCII_OFFSET = ord('a')


class Vernam():
    '''
    Vernam cipher
    ''' 

    def convert2bin(char):
        '''
        convert a character to binary
        '''
        return bin(ord(char))


    def convert2str(string):
        '''
        convert a binary string to letter
        '''
        return chr(int(string,2) + ASCII_OFFSET)


    def encript(msg, key):
        '''
        for every bit of the message
        apply the XOR with the key ones
        '''
        
        #generate the output string
        out = ''
        for j in range(len(msg)):

            #convert every letter in binary
            bit_char = Vernam.convert2bin(msg[j])[2:].zfill(8)
            bit_key = Vernam.convert2bin(key[j])[2:].zfill(8)

            #for every bit of the letter apply the XOR
            #and appends it to temporany string
            temp = ''.join(str(int(bit_char[i] != bit_key[i])) for i in range(len(bit_char)))

            #add the letter to the output
            out += Vernam.convert2str(temp)
        
        return out



def create_key(msg):
    '''
    ask a key to the user.
    The key length has to be the same of the message.
    '''
    key = ''
    while len(key) != len(msg):
        key = input('insert a key: ')
    return key




def main():
    #input string
    msg = input('insert a message: ')

    #input key
    key = create_key(msg)

    #encript message
    enc_msg = Vernam.encript(msg, key)
    print(enc_msg)



if __name__ == '__main__':
    main()