input_line = int(input())
for i in range(input_line):

    # 既定打数を受け取る
    pars = input().rstrip().split(',')
    # 打数を受け取る
    strokes = input().rstrip().split(',')

    # int型に変換
    pars = map(int, pars)
    strokes = map(int, strokes)

    # ゴルフスコアを判定
    score_dict = {1: 'ボギー', 0: 'パー', -1: 'バーディ', -2: 'イーグル', -3: 'アルバトロス'}
    result_list = []
    for par, stroke in zip(pars, strokes):
        score = stroke - par
        if score > 1:
            result_list.append(f"{score}ボギー")
        elif score == -4:
            result_list.append("コンドル")
        elif stroke == 1:
            result_list.append("ホールインワン")
        elif score in score_dict:
            result_list.append(score_dict[score])

    # 結果を表示
    results = ",".join(result_list)
    print(results)
