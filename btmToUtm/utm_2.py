import tkinter as tk
from tkinter import messagebox
from pyproj import CRS, Transformer

# Define BTM CRS (Sylhet-specific parameters)
btm_crs = CRS.from_proj4(
    "+proj=tmerc +lat_0=0 +lon_0=90 +k=0.9996 +x_0=500000 +y_0=-2000000 +ellps=evrst30 +units=m +no_defs"
)

# Define UTM Zone 46N CRS
utm_crs = CRS.from_epsg(32646)

# Create transformer
transformer = Transformer.from_crs(btm_crs, utm_crs, always_xy=True)

def convert_coordinates():
    try:
        easting_btm = float(easting_entry.get())
        northing_btm = float(northing_entry.get())
        easting_utm, northing_utm = transformer.transform(easting_btm, northing_btm)
        result_label.config(
            text=f"UTM Coordinates:\nEasting: {easting_utm:.3f}\nNorthing: {northing_utm:.3f}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric coordinates.")

# Set up the GUI
root = tk.Tk()
root.title("BTM to UTM Converter (Sylhet)")

# Input fields
tk.Label(root, text="BTM Easting:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
easting_entry = tk.Entry(root, width=20)
easting_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="BTM Northing:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
northing_entry = tk.Entry(root, width=20)
northing_entry.grid(row=1, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_coordinates)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11), fg="green")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
