import serial
import time

def MoveLeftOne():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)  
    ser.write(b'$X\n')
    ser.write(b'$100=790\n')
    ser.write(b'G10 P0 L20 X0 Y0 Z0\n')
    ser.write(b'$J=G21G91X-1F400\n')
    time.sleep(2)
    
    ser.close()

def MoveLeftFive():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)  
    ser.write(b'$X\n')
    ser.write(b'$100=790\n')
    ser.write(b'G10 P0 L20 X0 Y0 Z0\n')
    ser.write(b'$J=G21G91X-5F400\n')
    time.sleep(2)
    
    ser.close()
    
    
def MoveRightOne():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)  
    ser.write(b'$X\n')
    ser.write(b'$100=790\n')
    ser.write(b'G10 P0 L20 X0 Y0 Z0\n')
    ser.write(b'$J=G21G91X1F400\n')    
    time.sleep(2)
    
    ser.close()
    
def MoveRightFive():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)  
    ser.write(b'$X\n')
    ser.write(b'$100=790\n')
    ser.write(b'G10 P0 L20 X0 Y0 Z0\n')
    ser.write(b'$J=G21G91X5F400\n')    
    time.sleep(2)
    
    ser.close()
    
    
def main():
    print("Select an option:")
    print("1. Move Left 1 mm")
    print("2. Move Left 5 mm")
    print("3. Move Right 1 mm")
    print("4. Move Right 5 mm")
    print("5. Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                print("Moving left 1 mm...")
                MoveLeftOne()
            elif choice == 2:
                print("Moving left 5 mm...")
                MoveLeftFive()
            elif choice == 3:
                print("Moving right 1 mm...")
                MoveRightOne()
            elif choice == 4:
                print("Moving right 5 mm...")
                MoveRightFive()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose from 1 to 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()