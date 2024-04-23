import logging
import os
from datetime import datetime
from PIL import Image
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def capture_frame(num_frames, output_dir):
    
    
    os.makedirs(output_dir,exist_ok=True)
    
    for i in range(num_frames):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = os.path.join(output_dir, f"image_{timestamp}.jpg")
        
        try:
            capture_command = ["libcamera-still", "-o", output_path, "--hflip","1"]
            subprocess.run(capture_command, check=True)
            logger.info(f"Image saved to: {output_path}")
            

        except subprocess.CalledProcessError as e:
            logger.error(f"An error occurred when capturing image {i+1}: {e}")
            continue  



        


def main():
    num_images = 200  
    output_dir = "images" 
    
capture_frame(num_frames, output_dir)

if __name__ == "__main__":
    main()     
