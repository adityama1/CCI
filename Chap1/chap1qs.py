import sys


def main():
    if len(sys.argv)<2:
        print "Not input provided"
        sys.exit(0)
    input_string = sys.argv[1]+sys.argv[2]
    #dic = {}
    num = 0
    for i in input_string:
        char_val = ord(i)
        if not num & 1 << char_val:
            num = num | 1 << char_val
        else:
            print "duplicate: " + i

'''
    #hash table implementation
    for i in range(0,len(input_string)):
        try:
            if dic[input_string[i]]:
                print "Duplicate: %s" %(input_string[i])
        except:
            dic[input_string[i]] = 1
    #Sort the string in nlgn and check neighboring chars
'''
if __name__ == '__main__':
    main()