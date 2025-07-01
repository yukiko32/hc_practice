import datetime
import sys


def display_calendar(m):
    """
    今年のm月のカレンダーを表示します
    :param m: 表示するカレンダーの月（1~12）
    """
    # 現在の日付を取得
    dt = datetime.date.today()

    # カレンダーを表示する年に現在の年を設定
    y = dt.year

    # 表示するカレンダーの年・月を取得
    display_month = datetime.date(y, m, 1)

    # 表示するカレンダーが12月の場合を考慮
    next_month_y = y
    next_m = m + 1
    if m == 12:
        next_month_y += 1
        next_m = 1

    # 表示するカレンダーの日付リストを取得
    last_day = (datetime.date(next_month_y, next_m, 1) - datetime.timedelta(days=1)).day
    this_month = y == dt.year and m == dt.month
    days = ["  "] * display_month.weekday()
    for i in range(1, last_day + 1):
        d = str(i).rjust(2)
        if this_month and i == dt.day:
            days.append('\033[7m'+ d +'\033[0m')
        else:
            days.append(d)

    # カレンダーを表示
    print(display_month.strftime("%B %Y").center(20))
    print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")
    for i in range(0, len(days), 7):
        week = " ".join(days[i: i+7])
        print(week)


def error_msg(error_value):
    """
    error_valueに対するエラーメッセージを表示します
    :param error_value: エラー判定されたコマンドラインの入力値
    """
    print(f"{error_value} is neither a month number (1..12) nor a name")


def check_args(args):
    """
    コマンドライン引数をチェックし、カレンダーを表示します。

    引数が無い場合は、現在の月のカレンダーを表示します。
    「-m 月」を指定した場合は、その月のカレンダーを表示します。
    不正なオプションや値が入力された場合は、エラーメッセージを出力します。
    :param args: コマンドライン引数（sys.argv）のリスト
    """
    # 引数がない場合は今月のカレンダーを表示
    if len(args) == 1:
        month = datetime.date.today().month
        display_calendar(month)
        sys.exit(0)
    # 1つめの引数が-mの場合
    if args[1] == "-m":
        # 2つめの引数がない場合はエラー文を出して終了
        if len(args) == 2:
            print("Missing month number after -m option")
            sys.exit(1)
        # 2つめの引数が半角数字でない場合はエラー文を出して終了
        input_value = args[2]
        if not (input_value.isdigit() and input_value.isascii()):
            error_msg(input_value)
            sys.exit(1)
        # 2つめの引数が1~12の場合はその月のカレンダーを表示
        input_int = int(args[2])
        if 1 <= input_int <= 12:
            display_calendar(input_int)
            sys.exit(0)
        else:
            # 1~12以外の場合はエラー文を出して終了
            error_msg(input_int)
            sys.exit(1)
    # 1つめの引数が-m以外の場合はエラー文を出して終了
    print(f"Unsupported option: {args[1]} (only -m is allowed)")
    sys.exit(1)


if __name__ == "__main__":
    check_args(sys.argv)
