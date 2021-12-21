import lm75
from time import sleep
from gpiozero import CPUTemperature
from lcd import getLCD


def main():
    lcd = getLCD()
    sensor = lm75.LM75()

    while True:
        external = str(round(CPUTemperature().temperature, 1)).replace("\n", "") + "'C"
        lcd.message = "Internal: {}\nExternal: {}".format(external, sensor.getTemp())
        sleep(10)

if __name__ == "__main__":
    main()
