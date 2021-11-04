# 날짜와 시간 처리 모듈
import locale
from datetime import date, time, datetime, timedelta

date_obj = date(2020, 10, 9)
time_obj = time(15, 23, 21)
datetime_obj = datetime(2021, 8, 15, 20, 19, 45)

print("[date 클래스로 날짜 지정]", date_obj)
print("[date 클래스의 속성 이용] {0}/{1}/{2}".format(date_obj.year,
                                             date_obj.month,
                                             date_obj.day))
print("[time 클래스로 시각 지정]", time_obj)
print("[time 클래스의 속성 지정] {0}/{1}/{2}".format(time_obj.hour,
                                             time_obj.minute,
                                             time_obj.second))

print("[datetime 클래스로 날짜와 시각 지정]", datetime_obj)


# date 객체 혹은 datetime 객체끼리는 서로 빼기 연산을 할 수 있습니다.
# 이때 연산결과는 timedelta 객체가 됩니다.
print('\n- timedelta')
date_obj2 = date(2020, 10, 15)
diff_date = date_obj2 - date_obj
print(diff_date)
print("두 날짜의 차이: {}일".format(diff_date.days))
print("{0}의 일 주일 전 날짜: {1}".format(date_obj, date_obj - timedelta(weeks=1)))
print("{0}의 1시간 30분 후 날찌 및 시각: {1}".format(datetime_obj, datetime_obj + timedelta(hours=1, minutes=30)))

print('\n- today(), now() 메서드')
today = date.today()
now = datetime.now()
print("오늘의 날짜: {0}-{1}-{2}".format(today.year, today.month, today.day))
print("현재의 날짜 및 시각: {}".format(now))

print('\n- strftime() 메서드')
# 한글, 한국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
print(now.strftime("[날짜] %Y-%m-%d, %A [시간] %H:%M%S (%p)"))
# 영어, 미국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
print(now.strftime("[날짜] %Y-%m-%d, %A [시간] %H:%M%S (%p)"))
