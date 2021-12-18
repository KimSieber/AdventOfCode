###############################################
### Advent of Code 2021
###
### Day 16 - Packet Decoder
###
### author:  Kim Sieber
### create:  17.12.2021 - 18.12.2021
################################################
from math import inf as infinite

### TEST-Data PART I
#data_hex    = 'D2FE28'                            # => 6
#data_hex    = '38006F45291200'                    # => 9 
#data_hex    = 'EE00D40C823060'                    # => 14
#data_hex    = '8A004A801A8002F478'                # => 16
#data_hex    = '620080001611562C8802118E34'        # => 12
#data_hex    = 'C0015000016115A2E0802F182340'      # => 23
#data_hex    = 'A0016C880162017C3686B18A3D4780'    # => 31
### TEST-Data PART II
#data_hex     = 'C200B40A82'                       # => 3
#data_hex     = '04005AC33890'                     # => 54
#data_hex     = '880086C3E88112'                   # => 7
#data_hex     = 'CE00C43D881120'                   # => 9
#data_hex     = 'D8005AC2A8F0'                     # => 1
#data_hex     = 'F600BC2D8F'                       # => 0
#data_hex     = '9C005AC2F8F0'                     # => 0
#data_hex     = '9C0141080250320F1802104A08'       # => 1

data_hex    = open("#16 Input", "r").read()
data_bin    = ''.join([bin(int(h,16))[2:].zfill(4) for h in data_hex])
#print ('data_hex: ',data_hex)
#print ('data_bin: ',data_bin)


def decodeLayer(data_bin, num_packages = infinite):
    result  = []
    while len(data_bin) > 0 and num_packages > 0:
        num_packages -= 1
        if int('0b'+data_bin,2) == 0:
            data_bin = None
            break
        
        typeID  = int('0b'+data_bin[3:6],2)
        version = int('0b'+data_bin[0:3],2)
        packet  = {'version': version, 'typeID': typeID}
        data_bin = data_bin[6:]
        
        if typeID == 4:
            content = ''
            while True:
                cmd      = data_bin[0:1]
                content += data_bin[1:5]
                data_bin = data_bin[5:]
                if cmd == '0':          break
            packet['content'] = int('0b'+content,2)
            result.append(packet)
        
        else:       # typeID != 4
            
            length_type_id = int(data_bin[0:1])
            data_bin       = data_bin[1:]
            
            if length_type_id == 0:                             # 15 bit = total length
                total_length           = int('0b'+data_bin[0:15],2)
                data_bin               = data_bin[15:]
                packet['content'], tmp = decodeLayer(data_bin[:total_length])
                data_bin               = data_bin[total_length:]
                result.append(packet)
            
            if length_type_id == 1:                             # 11 bit = number of sub-packets
                num_sub_packages            = int('0b'+data_bin[0:11],2)
                data_bin                    = data_bin[11:]
                packet['content'], data_bin = decodeLayer(data_bin, num_sub_packages)
                result.append(packet)
    
    return result, data_bin
    

def sumVersions(layer):
    sumV = 0
    if isinstance(layer, dict):
        sumV = layer['version']
        sumV += sumVersions(layer['content'])
    elif isinstance(layer, list):
        for sub in layer:
            sumV += sumVersions(sub)
    else:   # content = int
        sumV = 0
    return sumV


def getProduct(layer):
    if isinstance(layer, list):
        ret = []
        for lay in layer:
            ret.append(getProduct(lay))
        return ret

    if isinstance(layer, dict):
        if   layer['typeID'] == 4:    
            return layer['content']

        values = getProduct(layer['content'])
        ret = 0

        if layer['typeID'] == 0:        # sum (+)
            for v in values:
                ret += v
        elif layer['typeID'] == 1:      # product (*   *1)
            ret = 1
            for v in values:
                ret *= v
        elif layer['typeID'] == 2:      # minimum (min())
            ret = min(values)
        elif layer['typeID'] == 3:      # maximum (max())
            ret = max(values)
        elif layer['typeID'] == 5:      # greater than (1st > 2nd => 1, else 0)
            if values[0] > values[1]:   ret = 1
            else:                       ret = 0
        elif layer['typeID'] == 6:      # less than    (1st < 2nd => 1, else 0)
            if values[0] < values[1]:   ret = 1
            else:                       ret = 0
        elif layer['typeID'] == 7:      # equal to     (1st = 2nd => 1, else 0)
            if values[0] == values[1]:  ret = 1
            else:                       ret = 0
        else:
            print ('Error !!!!!!!!!!!! typeID=',layer['typeID'])
            stop()

        return ret
            
    
layer, tmp = decodeLayer(data_bin)
#print ('layer        : ', layer)
print ('Solution Part I   : ',sumVersions(layer))
print ('Solution Part II  : ',getProduct(layer)[0])