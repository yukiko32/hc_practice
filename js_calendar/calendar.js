/**
 * 年と月を指定してカレンダーを表示する
 * @param {Object} params - 年月のオブジェクト
 * @param {number} params.year - 表示するカレンダーの年
 * @param {number} params.month - 表示するカレンダーの月（1-12月は0-11とする）
 * @returns {void}
 */
const displayCalendar = ({ year, month }) => {
  // タイトル表示
  const yyyy = String(year);
  const mm = String(month + 1);  // 表示のため+1する
  console.log(`      ${mm}月 ${yyyy}`);
  console.log("日 月 火 水 木 金 土");

  // 月末日、月初の曜日の数値、今日の日付を取得
  const lastDay = new Date(year, month + 1, 0).getDate();
  const firstDayOfWeek = new Date(year, month).getDay();  // 日曜-土曜: 0-6
  const today = new Date();
  const currentDate = today.getDate();

  // 表示する月が今月か判定
  const isCurrentMonth = today.getFullYear() === year && today.getMonth() === month;

  // 月初日までの空白を表示
  process.stdout.write("   ".repeat(firstDayOfWeek));

  // 月初から月末までの日付を表示
  for (let i = 1; i <= lastDay; i++) {
    const day = String(i).padStart(2, " ");

    // 日付を表示（当日の場合は色を反転）
    if (isCurrentMonth && i === currentDate) {
      process.stdout.write("\x1b[7m" + day + "\x1b[0m" + " ");
    } else {
      process.stdout.write(day + " ");
    }
    // 一週間区切りで改行
    (i + firstDayOfWeek) % 7 === 0 && process.stdout.write("\n");  // 左辺がtrueの場合、右辺を実行
  }
  process.stdout.write("\n");
}

/**
 * 現在の年月、または現在の年と入力された月を取得する
 * @returns {{year: number, month: number}} 年と月のオブジェクト（1-12月は0-11とする）
 */
const getDate = () => {
  // 現在の年月を設定
  const year = new Date().getFullYear();
  let month = new Date().getMonth();

  // コマンドラインでオプションが渡された場合は月を設定
  const option = "-m";
  if (process.argv[2] === option) {
    // 1月〜12月の範囲でない場合はエラーを出す
    const arg = process.argv[3];
    const numArg = Number(arg);
    if (Number.isNaN(numArg) || !(numArg >= 1 && numArg <= 12)) {
      console.error(`${arg} is neither a month number (1..12) nor a name`);
      process.exit(1);
    }
    // 月を設定（0-11で扱うため1を引く）
    month = numArg - 1;
  }

  return { year, month };
}

/**
 * 年月を取得してカレンダーを表示する
 * @returns {void}
 */
const main = () => {
  const date = getDate();
  displayCalendar(date);
}


main();
