import logging
import os
import serial
import subprocess
from datetime import datetime
from threading import Thread
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def capture_image(output_path):
   
    try:
        capture_command = ["libcamera-still", "-o", output_path, "--hflip", "1"]
        subprocess.run(capture_command, check=True)
        logger.info(f"Image saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred: {e}")

def move_rail_and_capture_images(num_images, output_dir, rail_speed_mm_s, rail_distance_mm):
   
    rail_speed_mm_min = rail_speed_mm_s * 60
    
    serial_port = "/dev/ttyUSB0"
    
    os.makedirs(output_dir, exist_ok=True)
    try:
        with serial.Serial(serial_port, 115200, timeout=1) as ser:
            time.sleep(2)  
            ser.write(b'$X\n')  
            ser.write(b'$100=790\n')  
            ser.write(b'G10 P0 L20 X0 Y0 Z0\n') 

            interval_time = (rail_distance_mm / num_images) / rail_speed_mm_s
            
            for i in range(num_images):
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                output_path = os.path.join(output_dir, f"image_{timestamp}.jpg")

                ser.write(f'$J=G21G91X{rail_distance_mm / num_images:.2f}F{rail_speed_mm_min}\n'.encode())
                time.sleep(interval_time) 
                
                Thread(target=capture_image, args=(output_path,)).start()
                
            ser.write(b'!\n')  
            
    except serial.SerialException as e:
        logger.error(f"Failed to open serial port: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def main():
    num_images = 10  # Example: Number of images
    output_dir = "images"  # Example: Output directory for images
    rail_speed_mm_s = 5  # Rail speed in mm/s
    rail_distance_mm = 100  # Total movement in mm

    move_rail_and_capture_images(num_images, output_dir, rail_speed_mm_s, rail_distance_mm)

if __name__ == "__main__":
    main()     
