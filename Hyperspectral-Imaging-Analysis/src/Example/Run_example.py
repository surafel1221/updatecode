from spectral import open_image,imshow
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from tkinter import messagebox, simpledialog
from spectral import open_image, imshow
import tkinter as tk


def load_dispaly_Cube(image_path):
    img = open_image(image_path).load()

    def normalize_band(band):
        return (band - band.min()) / (band.max() - band.min())

    initial_band = 0
    normalized_img = normalize_band(img[:, :, initial_band])

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)  # Adjust subplot to make room for the slider
    
    band_display = plt.imshow(normalized_img, cmap='gray')
    ax.set_title(f'Band {initial_band+1}')
    
    ax_band = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    band_slider = Slider(
        ax=ax_band,
        label='Band',
        valmin=0,
        valmax=img.shape[2]-1,  # Max band index
        valinit=initial_band,
        valstep=1
    )
    
    def update(val):
        band = band_slider.val
        normalized_img = normalize_band(img[:, :, band])
        band_display.set_data(normalized_img)
        ax.set_title(f'Band {band+1}')
        fig.canvas.draw_idle()
    
    band_slider.on_changed(update)
    
    plt.show()

def Display_RGB():
    image_path = "C:\\Users\\suraf\\New folder (2)\\Hyperspectral-Imaging-Analysis\\src\\Example\\92AV3C (2).lan"
    Rband = 29
    Gband = 19
    Bband = 9

    try:
        img = open_image(image_path).load()
        imshow(img, (Rband, Gband, Bband))
    except Exception as e:
        root = tk.Tk()  
        root.withdraw()  
        messagebox.showerror("Error", f"An error occurred: {e}", parent=root)
        root.destroy() 

    
