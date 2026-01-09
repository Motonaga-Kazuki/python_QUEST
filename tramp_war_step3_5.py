#トランプゲームの戦争を実装
#戦争はカードの大小を競うゲーム。勝ったほうがカードをもらう。
#手札がなくなったら負け、多くカードを持ってたら勝ち

#step3:プレイヤー2人

#カードをcardクラスとして定義してやる
#辞書がいらなくなったり、カードの追加もできる

#1. カードクラスの設定
#クラスは設計図→カードの設計をしてやって、具体的な値はインスタンスするときに決定

class Card:
    #コンストラクタを定義
    #これはインスタンス生成の時に自動的に呼び出されるメソッド
    def __init__(self, suit, rank, strength):
        self.suit = suit
        self.rank = rank 
        self.strength =strength
        
    #printの設定、print()を使うとき呼び出される
    def __repr__(self):
        if self.suit == "JK":
            return "JOKER"
        else:
            return f"{self.suit}-{self.rank}"
    
import random

#1.ゲーム開始宣言

print("--- 戦争を開始します。---")


#2.カードを配る処理

#カードを準備
suits = ["スペード", "ハート", "ダイヤ", "クラブ"]
ranks = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K", "A"]

#JOKERを1枚作成
joker = Card("JK", "JOKER", 13)

#classを用いてリスト(デッキ)をつくる

deck = [Card(s, r, i) for s in suits for i,r in enumerate(ranks)]
#for s in suits →suitをそれぞれ固定
#for i,r in enumerate(ranks)
#→iは0から12、rはranksを0から12番目まで取得、enumerateでそれをペアにできる
#iはそのままカードの強さの数値として使える

#jokerを加える
deck.append(joker)

random.shuffle(deck)

#デッキの表示
#print(deck)

#どちらのプレイヤーの手札が27枚になるかを決定
random_player = random.randint(1,2)

#1ならplayer1が、2ならplayer2が27枚になる
if random_player == 1:
    p1_hand = deck[:26]
    p2_hand = deck[26:]
    
else:
    p1_hand = deck[26:]
    p2_hand = deck[:26]

print(">> カードが配られました。")
print(">> ジョーカーのスートはJKとします。")

#3一番上のカードを表向きに出す処理

#戦争！と宣言
print("--- 戦争！---")
#playerの手札(リスト)の一番目(ここでは末尾)のカードを出す
#player1とplayer2の手札がある限り、継続するのでwhile文

table = [] #引き分けの時にカードをためるリスト

while len(p1_hand) > 0 and len(p2_hand) > 0:
    input(">> Enterキーを押して、同時にカードを出します")
    
    #popメソッドで末尾から一つ取り出す
    card1 = p1_hand.pop()
    card2 = p2_hand.pop()
    table.extend([card1,card2]) #まとめて場に置く
    
    #カードは全てクラスの設計図通りに定義されている
    #例えば今、classでのstrength変数はiに該当する
    #その変数を使いたいときはcard1.strengthのように書く
    
    #suitとrankを変数に入れておく
    c1_suit = card1.suit
    c2_suit = card2.suit
    c1_rank = card1.rank
    c2_rank = card2.rank
    
    
    
    #カードの内容を表示
    print(f">> プレイヤー1のカードは{c1_suit}の{c1_rank}です。")
    print(f">> プレイヤー2のカードは{c2_suit}の{c2_rank}です。")

    #大小比較
    if card1.strength > card2.strength:
        print(">> プレイヤー1が勝ちました。")
        #勝ったほうが表の場のカードを手札に加える(リスト一番上に)
        #.insert(0, table.pop())で、リストの一番上に全て加える
        random.shuffle(table)
        while table:  #tableが空になるまで繰り返す
            p1_hand.insert(0,table.pop())
       
    
    elif card1.strength < card2.strength:
        print(">> プレイヤー2が勝ちました。")
        #勝ったほうが表のカードを手札に加える(リスト一番上に)
        #.insert(0, table.pop())で、リストの一番上に全て加える
        random.shuffle(table)
        while table:  #tableが空になるまで繰り返す
            p2_hand.insert(0,table.pop())
    
    #A同士の世界一の処理、Aのstrengthは12        
    elif card1.strength == 12 and card2.strength == 12:
        if c1_suit == "スペード":
            print(">> プレイヤー1はスペードのAなので世界一です。")
            random.shuffle(table)
            while table:
                p1_hand.insert(0,table.pop())
                
        elif c2_suit == "スペード":
            print(">> プレイヤー2はスペードのAなので世界一です。")
            random.shuffle(table)
            while table:
                p2_hand.insert(0,table.pop())
                
        else:
            #引き分けの処理
            #場の一時的なリストを作ってカードをためている
            #そのままループが続く
            print(">> 引き分けです")
    
    else:
        #引き分けの処理
        #場の一時的なリストを作ってカードをためている
        #そのままループが続く
        print(">> 引き分けです")
        
    #5. 結果発表

#変数に手札枚数を代入
p1_final_hand = len(p1_hand)
p2_final_hand = len(p2_hand)
print(p1_hand)
print(p2_hand)

#player1か2かどっちが0枚かで分岐        
if p1_final_hand == 0:
    print(">> プレイヤー1の手札がなくなりました。")
    print(
        f">> プレイヤー1の手札の枚数は{p1_final_hand}枚です。プレイヤー2の手札の枚数は{p2_final_hand}枚です。"
    )
    print(">> プレイヤー2が1位、プレイヤー1が2位です。")
    print("--- 戦争を終了します。---") 
    
else:
    print(">> プレイヤー2の手札がなくなりました。")
    print(
        f">> プレイヤー1の手札の枚数は{p1_final_hand}枚です。プレイヤー2の手札の枚数は{p2_final_hand}枚です。"
    )
    print(">> プレイヤー1が1位、プレイヤー2が2位です。")
    print("--- 戦争を終了します。---")
    





        