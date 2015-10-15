import time import sleep


def setup_ultrasound(TRIG, ECHO):
    logging.info("Setting pins {} and {} to TRIG and ECHO".format(TRIG, ECHO))
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    time.sleep(1)
    GPIO.output(TRIG, False)
    logging.info("Waiting For Sensor To Settle")
    time.sleep(2)


def ultrasound_ping(TRIG, ECHO):
    setup_ultrasound(TRIG, ECHO)
    logging.log("Start Ultrasound Ping")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    logging.log("Distance:", distance, "cm")

    GPIO.cleanup()

    return distance
