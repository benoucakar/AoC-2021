hex = {
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
inp = open("input/day16.txt", "r")
bin = ""
for z in inp.readline()[:-1]:
    bin += hex[z]
inp.close()

def bin_to_int(bin):
    rbin = bin[::-1]
    temp = 0
    for i in range(len(bin)):
        if rbin[i] == "1":
            temp += 2**i
    return temp

super_g_sez = []
def main(index, meja_packets=len(bin), meja_dolz=len(bin)):
    g_sez = []
    g_index = index
    while g_index < meja_dolz and len(g_sez) < meja_packets:
        # packet version
        if g_index + 11 >= len(bin): # dolzina najkrajsega moznega paketa
            break
        p_vers_str = ""
        for _ in range(3):
            p_vers_str += bin[g_index]
            g_index += 1
        p_vers = bin_to_int(p_vers_str)
        # type ID
        t_ID_str = ""
        for _ in range(3):
            t_ID_str += bin[g_index]
            g_index += 1
        t_ID = bin_to_int(t_ID_str)
        # literal value
        if t_ID == 4: 
            literal_value_str = ""
            flag_lv = True
            while flag_lv:
                container = ""
                for _ in range(5):
                    container += bin[g_index]
                    g_index += 1
                if container[0] == "0":
                    flag_lv = False
                literal_value_str += container[1:]
            literal_value = bin_to_int(literal_value_str)
            g_sez.append((p_vers, t_ID, literal_value))         
        else:
            length_type_ID = bin[g_index]
            g_index += 1
            if length_type_ID == "0":
                total_length_str = ""
                for _ in range(15):
                    total_length_str += bin[g_index]
                    g_index += 1
                total_length = bin_to_int(total_length_str)
                sets, indx = main(g_index, meja_dolz=(total_length + g_index))
                for s in sets:
                    super_g_sez.append(s)
                g_index = indx
                g_sez.append((p_vers, t_ID, [len(super_g_sez) - 1 - i for i in range(len(sets))]))
            else:
                num_of_sub_imed_cont_str = ""
                for _ in range(11):
                    num_of_sub_imed_cont_str += bin[g_index]
                    g_index += 1
                num_of_sub_imed_cont = bin_to_int(num_of_sub_imed_cont_str)
                sets, indx = main(g_index, meja_packets=num_of_sub_imed_cont)
                for s in sets:
                    super_g_sez.append(s)
                g_index = indx
                g_sez.append((p_vers, t_ID, [len(super_g_sez) - 1 - i for i in range(len(sets))]))
    return (g_sez, g_index)
for s in main(0)[0]:
    super_g_sez.append(s)

def value(packet):
    ID = packet[1]
    s = packet[2]
    if ID == 0:
        return sum([value(super_g_sez[p]) for p in s])
    elif ID == 1:
        acc = 1
        for p in s:
            acc *= value(super_g_sez[p])
        return acc
    elif ID == 2:
        return min([value(super_g_sez[p]) for p in s])
    elif ID == 3:
        return max([value(super_g_sez[p]) for p in s])
    elif ID == 4:
        return s
    elif ID == 5:
        return int(value(super_g_sez[s[0]]) < value(super_g_sez[s[1]]))
    elif ID == 6:
        return int(value(super_g_sez[s[0]]) > value(super_g_sez[s[1]]))
    elif ID == 7:
        return int(value(super_g_sez[s[0]]) == value(super_g_sez[s[1]]))

# --------------------------

print("1. del: ")
print(sum([s[0] for s in super_g_sez]))
print("2. del: ")
print(value(super_g_sez[-1]))