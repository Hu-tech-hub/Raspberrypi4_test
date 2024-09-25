import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
LED_PIN = 18  # 사용할 핀 번호

# GPIO 설정
GPIO.setmode(GPIO.BCM)  # BCM 모드 사용
GPIO.setup(LED_PIN, GPIO.OUT)  # 핀을 출력으로 설정

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED 켜기
        time.sleep(1)  # 1초 대기
        GPIO.output(LED_PIN, GPIO.LOW)  # LED 끄기
        time.sleep(1)  # 1초 대기
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()  # GPIO 설정 초기화