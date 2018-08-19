# Python - 3.4.3

from struct import pack, unpack

# 功能
#     編碼至 ASCII85
# 參數
#     binary: 原始資料 (str)
# 回傳值
#     ASCII85 資料 (str)
def toAscii85(binary):
    # str 轉 bytes
    if type(binary) == str:
        binary = bytes(map(ord, binary))

    # 結尾處增加 '\0' 補齊至 4 的倍數
    paddings = (4 - (len(binary) % 4)) % 4
    if paddings:
        binary += b'\0' * paddings

    # 4 個位元組為一組轉換為 32位元無號整數
    u32s = unpack('>%dI' % (len(binary) // 4), binary)

    # 將每個整數轉換為 ASCII85
    blocks = []
    for u32 in u32s:
        b = u32
        block = [0] * 5
        for i in range(4, -1, -1):
            b, block[i] = b // 85, chr(b % 85 + 33)
        blocks.append(''.join(block))

    # 移除與填充數量相同的字數
    if paddings:
        blocks[-1] = blocks[-1][:-paddings]

    # 將 '!!!!!' 替換為 'z', 並在頭尾補上 '<~' 與 '~>'
    return '<~%s~>' % ''.join([block if block != '!!!!!' else 'z' for block in blocks])

# 功能
#     從 ASCII85 解碼
# 參數
#     data: ASCII85 資料 (str)
# 回傳值
#     原始資料 (str)
def fromAscii85(data):
    # 移除頭尾 '<~' 與 '~>', 並將 'z' 替換為 '!!!!!'
    ascii85 = data[2:-2].replace('z', '!!!!!')

    # 篩選非 ASCII85 字元的字
    ascii85 = [c for c in ascii85 if ((ord(c) >= 33) and (ord(c) <= 117))]

    # 結尾處增加 'u' 補齊至 5 的倍數
    paddings = (5 - (len(ascii85) % 5)) % 5
    if paddings:
        ascii85 += 'u' * paddings

    # ASCII85 轉二進位資料
    binarys = [ord(b) - 33 for b in ascii85]
    text = b''
    for i in range(0, len(binarys), 5):
        u32 = 0
        for j in range(i, i + 5):
            u32 = u32 * 85 + binarys[j]
        text += pack('>I', u32)

    # 移除與填充數量相同的字數
    if paddings:
        text = text[:-paddings]

    return ''.join(map(chr, text))