import datetime
import sys


def display_calendar(year, month):
    """
    year(年)・month(月)のカレンダーを表示します
    :param year: 表示するカレンダーの年
    :param month: 表示するカレンダーの月
    """
    # 現在の日付を取得
    today = datetime.date.today()

    # カレンダーを表示する年を設定
    current_year = year

    # 表示するカレンダーの初日の日付を取得
    first_date = datetime.date(current_year, month, 1)

    # 表示するカレンダーが12月の場合を考慮
    next_month_year = current_year
    next_month = month + 1
    if month == 12:
        next_month_year += 1
        next_month = 1

    # 表示するカレンダーの日付リストを取得
    last_day = (datetime.date(next_month_year, next_month, 1) - datetime.timedelta(days=1)).day
    is_current_month = current_year == today.year and month == today.month
    days = ["  "] * first_date.weekday()
    for i in range(1, last_day + 1):
        day = str(i).rjust(2)
        if is_current_month and i == today.day:
            days.append('\033[7m'+ day +'\033[0m')
        else:
            days.append(day)

    # カレンダーを表示
    print(first_date.strftime("%B %Y").center(20))
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
    不正なオプションや値が入力された場合は、エラーメッセージを表示します。
    :param args: コマンドライン引数（sys.argv）のリスト
    """
    today = datetime.date.today()
    year, month = today.year, today.month
    if len(args) != 1:
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
            # 2つめの引数が1~12でない場合はエラー文を出して終了
            input_int = int(args[2])
            if input_int < 1 or 12 < input_int:
                error_msg(input_int)
                sys.exit(1)
            # 入力値を月として受け取る
            month = input_int
        else:
            print(f"Unsupported option: {args[1]} (only -m is allowed)")
            sys.exit(1)
    display_calendar(year, month)


if __name__ == "__main__":
    check_args(sys.argv)
