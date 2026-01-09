#トランプゲームの戦争を実装
#戦争はカードの大小を競うゲーム。勝ったほうがカードをもらう。
#手札がなくなったら負け、多くカードを持ってたら勝ち

#step1:プレイヤー2人
import random

#1.ゲーム開始宣言

print("--- 戦争を開始します。---")


#2.カードを配る処理

#カードを準備
suits = ["スペード", "ハート", "ダイヤ", "クラブ"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K"]

#52枚のデッキを作成、リスト内包表記
#suitを先に固定して、それに対してAからKの組み合わせを作成
deck = [f"{suit}-{rank}" for suit in suits for rank in ranks]

#デッキの中身確認
#print(deck)

#シャッフル
random.shuffle(deck)

#2人に配る→26枚でスライスする処理をする
player1_hand = deck[:26] #deckの前半26枚
player2_hand = deck[26:] #deckの後半26枚

#プレイヤーの手札確認
#print(len(player1_hand), player1_hand)
#print(len(player2_hand), player2_hand)

print(">> カードが配られました。")


#3.カードの強弱を決定

#辞書を使う、ランクごとの強さを定義
#文字列に数値を与え、比較できるようにする
strength_map = {
    "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
    "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14
}


#4.一番上のカードを表向きに出す処理

#戦争！と宣言
print("--- 戦争！---")
#player1の手札(リスト)の一番目(ここでは末尾)のカードを出す
#player1とplayer2の手札がある限り、継続するのでwhile文

table = [] #引き分けの時にカードをためるリスト

while len(player1_hand) > 0 and len(player2_hand) > 0:
    input(">> Enterキーを押して、同時にカードを出します")
    
    #popメソッドで末尾から一つ取り出す
    card1 = player1_hand.pop()
    card2 = player2_hand.pop()
    table.extend([card1,card2]) #まとめて場に置く
    
    #rankのみを参照したいのでsplit(-)で分割して、辞書で数値に変換
    card1_rank_num = strength_map[card1.split("-")[1]]
    card2_rank_num = strength_map[card2.split("-")[1]]

    #カードのsuitとrankを変数に入れておく
    card1_suit = card1.split("-")[0]
    card2_suit = card2.split("-")[0]
    card1_rank = card1.split("-")[1]
    card2_rank = card2.split("-")[1]
    
    #カードの内容を表示
    print(f">> プレイヤー1のカードは{card1_suit}の{card1_rank}です。")
    print(f">> プレイヤー2のカードは{card2_suit}の{card2_rank}です。")

    #大小比較
    if card1_rank_num > card2_rank_num:
        print(">> プレイヤー1が勝ちました。")
        #勝ったほうが表の場のカードを手札に加える(リスト一番上に)
        #.insert(0, table.pop())で、リストの一番上に全て加える
        random.shuffle(table)
        while table:  #tableが空になるまで繰り返す
            player1_hand.insert(0,table.pop())
       
    
    elif card1_rank_num < card2_rank_num:
        print(">> プレイヤー2が勝ちました。")
        #勝ったほうが表のカードを手札に加える(リスト一番上に)
        #.insert(0, table.pop())で、リストの一番上に全て加える
        random.shuffle(table)
        while table:  #tableが空になるまで繰り返す
            player2_hand.insert(0,table.pop())
    
    else:
        #引き分けの処理
        #場の一時的なリストを作ってカードをためている
        #そのままループが続く
        print("引き分けです")
        
    
    
    
    
    



