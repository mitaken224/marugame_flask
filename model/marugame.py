import csv
import operator
import os
import random


def selection(budget):
    # うどんのメニュー(csv)を配列udon_dataに格納
    # csvには各うどんの名前、量、価格が入っている
    udon_data = []
    with open("data/udon.csv", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            row[2] = int(row[2])  # 価格をint型にする
            udon_data.append(row)

    # udon_dataを価格順(昇順)にソート
    udon_data = sorted(udon_data, key=operator.itemgetter(2))


    # サイドメニュー(csv)を配列side_menu_dataに格納
    # csvには各サイドメニューの名前、種類、価格が入っている
    side_menu_data = []
    with open("data/side_menu.csv", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            row[2] = int(row[2])  # 価格をint型にする
            side_menu_data.append(row)

    # side_menu_dataを価格順(昇順)にソート
    side_menu_data = sorted(side_menu_data, key=operator.itemgetter(2))

    budget = int(budget)  # 予算をint型にする
    money = budget  # 残金money -> 商品を買うごとに価格分引いていく
    

    ###うどんの選択###

    # 乱数を設定する際のパラメータをudon_dataの配列数で初期化
    param = len(udon_data)

    # うどんが買えたかどうかフラグ(買えない(False)で初期化)
    udon_flg = False

    # 所持金の範囲内でうどんを1杯買う
    while True:
        # 0以上param未満の整数をランダムに選出
        rand = random.randrange(param)

        # rand番目に安いうどんが買えない場合、
        # それより安いうどんから再抽選する
        # 最も安いうどんも買えなければループ終了
        if udon_data[rand][2] > money:
            if rand == 0:
                break  # udon_flg = False のままループ終了
            param = rand
            continue

        # うどんを買うことができた
        udon_flg = True

        udon = udon_data[rand]
        udon[2] = int(udon[2])  # うどんの価格をint型に変換
    
        break

    # うどんを買えたかどうかで分岐する
    if udon_flg:
        money -= udon[2]  # 予算からうどん代を引く
    else:
        udon = []


    ###サイドメニューの選択###

    # 選ばれたサイドメニューの名前・種類・価格を格納する配列
    s_result = []

    # 乱数を設定する際のパラメータをside_menu_dataの配列数で初期化
    param = len(side_menu_data)

    # 所持金が残っている限りサイドメニューを買い続ける
    while True:
        # 0以上param未満の整数をランダムに選出
        rand = random.randrange(param)

        # rand番目に安いサイドメニューが買えない場合、
        # それより安いメニューから再抽選する
        # 最も安いメニューも買えなければループ終了
        if side_menu_data[rand][2] > money:
            if rand == 0:
                break
            param = rand
            continue

        side_menu = side_menu_data[rand]
        side_menu[2] = int(side_menu[2])  # サイドメニューの価格をint型にする
        s_result.append(side_menu)  # サイドメニューの名前・種類・価格を格納する

        # 予算からサイドメニュー代を引く
        money -= side_menu[2]


    ###合計金額の算出###
    sum = budget - money  # 合計金額=予算-残金

    ###選出されたうどん、サイドメニューと合計金額を返す###
    return udon, s_result, sum