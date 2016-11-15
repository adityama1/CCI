import sys


def main():
    count = 1
    new = []
    strng = 'abc'#cccaaa'
    for i in xrange(len(strng)-1):
        if strng[i] == strng[i+1]:
            count+=1
        else:
            new.append(strng[i])
            new.append(count)
            count = 1
    new.append(strng[i+1])
    new.append(count)
    print new
    for i in xrange(0,len(new),2):
        if new[i+1]!=1:
            return new

'''
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