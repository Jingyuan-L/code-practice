num = int(input().strip())
cards = list(map(list, input().strip().split()))
for card in cards:
    if len(card) > 2:
        card[1] = card[1] + card[2]


# print(cards)


def is_same_type(cards):
    for i in range(1, len(cards)):
        if cards[i][0] == cards[i - 1][0]:
            continue
        else:
            return False
    return True


if num <= 1:
    print("GaoPai")
else:
    card_num = [i[1] for i in cards]
    huangjia = False
    shun = False
    if card_num == ['A', 'K', 'Q', 'J', '10']:
        huangjia = True
    if card_num in [
        # ['A', 'K', 'Q', 'J', '10'],
        ['K', 'Q', 'J', '10', '9'],
        ['Q', 'J', '10', '9', '8'],
        ['J', '10', '9', '8', '7'],
        ['10', '9', '8', '7', '6'],
        ['9', '8', '7', '6', '5'],
        ['8', '7', '6', '5', '4'],
        ['7', '6', '5', '4', '3'],
        ['6', '5', '4', '3', '2'],
        ['5', '4', '3', '2', 'A']
    ]:
        shun = True
    same_type = is_same_type(cards)
    card_count = {}
    for i in range(num):
        if cards[i][1] not in card_count:
            card_count[cards[i][1]] = 1
        else:
            card_count[cards[i][1]] += 1
    # print(card_count)
    pair_num = 0
    tri_num = 0
    four_num = 0
    for i in card_count.keys():
        if card_count[i] == 2:
            pair_num += 1
        elif card_count[i] == 3:
            tri_num += 1
        elif card_count[i] == 4:
            four_num += 1
    if huangjia and same_type:
        print("HuangJiaTongHuaShun")
    elif shun and same_type:
        print("TongHuaShun")
    elif four_num >= 1:
        print("SiTiao")
    elif tri_num >= 1 and pair_num >= 1:
        print("HuLu")
    elif same_type:
        print("TongHua")
    elif shun:
        print("ShunZi")
    elif tri_num >= 1:
        print("SanTiao")
    elif pair_num >= 2:
        print("LiangDui")
    elif pair_num >= 1:
        print("YiDui")
    else:
        print("GaoPai")
