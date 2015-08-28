# template file for 6.02 PS1, Python Task 4 (LZW Compression/Decompression)
import sys
from optparse import OptionParser
import struct
import array

def compress(filename):
    """
    Compresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to compress.
    Returns:
        None.
    """
    srcf = open(filename, 'rb')
    disf = open(filename + '.zl.u', 'wb')
    code = {}
    for i in range(256) :
        code[chr(i)] = i
    message = array.array("B", srcf.read())
    if len(message) == 0:
        return
    tocode = chr(message.pop(0)) 
    while len(message) > 0 and len(code) < 2**16:
        symbol = chr(message.pop(0))
        if tocode + symbol in code:
            tocode = tocode +symbol
        else:
            disf.write(struct.pack("H",code[tocode]))
            code[tocode + symbol] = len(code)
            tocode = symbol
    disf.write(struct.pack("H",code[tocode]))
    srcf.close()
    disf.close()
    return
       
def uncompress(filename):
    """
    Decompresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to decompress.
    Returns:
        None.
    """
    srcf = open(filename, 'rb')
    disf = open(filename + '.u', 'w')
    table = {}
    for i in range(256) :
        table[i] = chr(i)
    message = array.array("H", srcf.read())
    if len(message) == 0:
        return
    code =  message.pop(0) 
    string = table[code]
    disf.write(string)
    while len(message) > 0:
        code = message.pop(0) 
        if code  not in table:
            entry = string + string[0]
        else:
            entry = table[code]
        disf.write(entry)
        table[len(table)] = string + entry[0]
        string = entry
    return
    

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--filename", type="string", dest="fname", 
                      default="test", help="file to compress or uncompress")
    parser.add_option("-c", "--compress", action="store_true", dest="uncomp", 
                      default=True, help="compress file")
    parser.add_option("-u", "--uncompress", action="store_true", dest="uncomp", 
                      default=False, help="uncompress file")

    (opt, args) = parser.parse_args()
    
    if opt.uncomp == True:
        uncompress(opt.fname)
    else:
        compress(opt.fname)
