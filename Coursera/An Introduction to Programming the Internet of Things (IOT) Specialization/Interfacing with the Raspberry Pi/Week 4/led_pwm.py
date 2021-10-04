import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 23

GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 1000)
pwm.start(0)

while True:
    try:
        for i in range(100):
            pwm.ChangeDutyCycle(i)
            time.sleep(.01)
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.01)
    except KeyboardInterrupt:
        pwm.stop()  # stop PWM
        print("\n Stopped")
        GPIO.cleanup()  # cleanup all GPIO
        print("\n Cleaned Up GPIO")
        exit()