from pyproj import CRS, Transformer

# Define BTM CRS (Sylhet-specific parameters, if accurate)
btm_crs = CRS.from_proj4(
    "+proj=tmerc +lat_0=0 +lon_0=90 +k=0.9996 +x_0=500000 +y_0=-2000000 +ellps=evrst30 +units=m +no_defs"
)

# Define UTM Zone 46N CRS
utm_crs = CRS.from_epsg(32646)

# Create transformer
transformer = Transformer.from_crs(btm_crs, utm_crs, always_xy=True)

# Get input from user
try:
    easting_btm = float(input("Enter BTM Easting: "))
    northing_btm = float(input("Enter BTM Northing: "))

    # Transform to UTM
    easting_utm, northing_utm = transformer.transform(easting_btm, northing_btm)

    print(f"UTM Coordinates:\nEasting = {easting_utm:.3f}\nNorthing = {northing_utm:.3f}")

except ValueError:
    print("Invalid input! Please enter valid numbers.")
