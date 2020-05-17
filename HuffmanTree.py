class HuffmanTree:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left, self.right = left, right
        self.code = ""

def get_frequencies(text):
    dic = {}
    for char in text:
        if char not in dic:
            dic[char] = 0
        dic[char] += 1
    return [(key, dic[key]) for key in dic]

def build_huffman_tree(freq_list):
    freq_list = [(HuffmanTree(e[1],e[0]), e[1]) for e in freq_list]
    while len(freq_list)>1:
        freq_list.sort(key=lambda tup: tup[1])
        freq = freq_list[0][1] + freq_list[1][1]
        Node = HuffmanTree(freq,None,freq_list[0][0],freq_list[1][0])
        freq_list.append((Node, freq))
        freq_list = freq_list[2:]
    return freq_list[0][0]

def convert_bin_string_to_bytes(compressed_text):
    padding = len(compressed_text) % 8
    if padding != 0:
        padding = 8 - padding

    byte_list = list()
    compressed_text += "0" * padding
    for i in range(0, len(compressed_text), 8):
        byte = compressed_text[i:i + 8]
        byte_list.append(int(byte, 2))
    return bytes(byte_list)

def get_codes(tree):
    dic = {} # résultat
    liste = [(tree, "")]
    while True:
        for tree in liste:
            l = []
            if tree[0].char == None:
                l.append((tree[0].right, tree[1]+"1"))
                l.append((tree[0].left, tree[1]+"0"))
                liste.remove(tree)
            liste += l
        ok = False
        for tree in liste:
            if tree[0].char == None:
                ok = True
        if not ok:
            break
    for tree in liste:
        dic[tree[0].char] = tree[1]
    return dic

def compress(huffman_tree, text):
    dic = get_codes(huffman_tree)
    res = ""
    for ch in text:
        res += dic[ch]
    return convert_bin_string_to_bytes(res)

def convert_bytes_to_bin_string(compressed_binary):
    compressed_text = ""
    for b in compressed_binary:
        compressed_text += f"{b:08b}"
    return compressed_text

def decompress(huffman_tree, compressed_binary):
    compressed_binary = convert_bytes_to_bin_string(compressed_binary)
    res = ""
    i = 0
    while i != len(compressed_binary):
        tree = huffman_tree
        while tree.char == None and i != len(compressed_binary):
            if compressed_binary[i] == "0":
                tree = tree.left
            else:
                tree = tree.right
            i += 1
        if tree.char != None:
            res += tree.char
    return res

def print_huffman_tree(tree):
    if tree.char == None:
        print(tree.freq, end = "\n")
        if tree.left != None:
            s = ""
            if len(tree.code)>0:
                for e in tree.code:
                    if e == "0":
                        s += "│     "
                    else:
                        s += "      "
            s += "├─0─"
            print(s, end = "  ")
            tree.left.code += tree.code + "0"
            print_huffman_tree(tree.left)
            tree.left.code = tree.left.code[:-1]
        if tree.right != None:
            s = ""
            if len(tree.code)>0:
                for e in tree.code:
                    if e == "0":
                        s += "│     "
                    else:
                        s += "      "
            s += "└─1─"
            print(s, end = "  ")
            tree.right.code += tree.code + "1"
            print_huffman_tree(tree.right)
            tree.right.code =  tree.right.code[:-1]
    else:
        print("'"+str(tree.freq)+" - "+tree.char+"'")


def test1():
    with open("test.txt") as file:
        text = file.readline().strip()
    print("Text :")
    print(text)
    for i in range(2):
        print()
    freq_list = get_frequencies(text)
    print("Test freq_list : ", freq_list)
    for i in range(2):
        print()
    tree = build_huffman_tree(freq_list)
    print("Test get_code(tree) : ", get_codes(tree))
    for i in range(2):
        print()
    compressed_binary = compress(tree, text)
    print("Test compress : ", compressed_binary)
    for i in range(2):
        print()
    text = decompress(tree, compressed_binary)
    print("Test decompress : ", text)
    for i in range(2):
        print()
    print("Huffman Tree :")
    print_huffman_tree(tree)

def test2():
    freq_list = [('d',10),('e',15),('c',20),('a',20),('b',24)]
    tree = build_huffman_tree(freq_list)
    print("Huffman Tree :")
    print_huffman_tree(tree)

#test1()
#test2()
