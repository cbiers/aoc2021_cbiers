def hexToBin(l):
    eq =    {
                "0": "0000",
                "1": "0001",
                "2": "0010",
                "3": "0011",
                "4": "0100",
                "5": "0101",
                "6": "0110",
                "7": "0111",
                "8": "1000",
                "9": "1001",
                "A": "1010",
                "B": "1011",
                "C": "1100",
                "D": "1101",
                "E": "1110",
                "F": "1111"
            }
    res = ""
    for c in l:
        res += eq[c]
    return res

def binToDec(bits):
    res = 0
    for b in bits:
        res *= 2
        if b == "1":
            res += 1
    return res

def decodeSubPacketsLen(b, l):
    res = []
    index = 0
    while index < l:
        curr = decodePacket(b[index:])
        res.append(curr)
        index += curr["length"]
    return res

def decodeSubPacketsNum(b, n):
    res = []
    index = 0
    for i in range(n):
        curr = decodePacket(b[index:])
        res.append(curr)
        index += curr["length"]
    return res

def getNextMultFour(n):
    while n % 4 != 0:
        n += 1
    return n

def totalLength(s):
    total = 0
    for p in s:
        total += p["length"]
    return total

def decodePacket(b):
    res = {}
    res["version"] = binToDec(b[:3])
    res["type"] = binToDec(b[3:6])
    if res["type"] != 4:
        res["lengthid"] = binToDec(b[6])
        if res["lengthid"] == 0:
            res["totallength"] = binToDec(b[7:22])
            res["subpackets"] = decodeSubPacketsLen(b[22:22+res["totallength"]], res["totallength"])
            res["length"] = 22 + res["totallength"]
        else:
            res["numsubpackets"] = binToDec(b[7:18])
            res["subpackets"] = decodeSubPacketsNum(b[18:], res["numsubpackets"])
            res["length"] = 18 + totalLength(res["subpackets"])
    else:
        curr = 6
        bits = ""
        last = False
        while(not last):
            g = b[curr:curr+5]
            if g[0] == "0":
                last = True
            bits += g[1:]
            curr += 5
        res["value"] = binToDec(bits)
        res["length"] = curr
    return res

def evaluate(p):
    res = 0
    if p["type"] == 0:
        for packet in p["subpackets"]:
            res += evaluate(packet)
    elif p["type"] == 1:
        res = 1
        for packet in p["subpackets"]:
            res *= evaluate(packet)
    elif p["type"] == 2:
        res = min([evaluate(packet) for packet in p["subpackets"]])
    elif p["type"] == 3:
        res = max([evaluate(packet) for packet in p["subpackets"]])
    elif p["type"] == 4:
        return p["value"]
    elif p["type"] == 5:
        if evaluate(p["subpackets"][0]) > evaluate(p["subpackets"][1]):
            res = 1
        else:
            res = 0
    elif p["type"] == 6:
        if evaluate(p["subpackets"][0]) < evaluate(p["subpackets"][1]):
            res = 1
        else:
            res = 0
    elif p["type"] == 7:
        if evaluate(p["subpackets"][0]) == evaluate(p["subpackets"][1]):
            res = 1
        else:
            res = 0
    return res

f = open("in.txt", "r")
line = f.readlines()[0][:-1]

bits = hexToBin(line)

packets = decodePacket(bits)

print evaluate(packets)
