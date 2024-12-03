from gaussmeter_reader import GaussmeterReader
from datetime import datetime
import time

def main():
    port = 'COM3'  # Ver cual es!!
    gaussmeter = GaussmeterReader(port)

    try:
        print("Starting Gaussmeter readings (Press Ctrl+C to stop)")
        while True:
            time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            field = gaussmeter.read_gaussmeter()

            print(f"Date: {time_now} | Field: {field:.3f} G")

            time.sleep(.01)  # Cambiar sleep_time
    except KeyboardInterrupt:
        print("\nStopping Gaussmeter readings.")
    finally:
        # CERRAR
        gaussmeter.close()

if __name__ == "__main__":
    main()