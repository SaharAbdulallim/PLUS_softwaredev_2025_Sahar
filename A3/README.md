#By Sahar Mohamed
# 🛰️ Assignment A3 – Sentinel-2 RGB & NDVI (Downsampled) via STAC + Rasterio

## 📌 Overview

This notebook demonstrates how to:
1. Query the Microsoft Planetary Computer STAC API for a Sentinel-2 L2A scene over Bucharest (April 2024).
2. Sign the STAC item to retrieve authenticated COG URLs for bands B02 (Blue), B03 (Green), B04 (Red), and B08 (NIR).
3. Read each band directly with **rasterio**, downsampling by a factor of 4 to reduce memory usage.
4. Compute NDVI = (NIR – Red) / (NIR + Red) on the downsampled arrays.
5. Apply a percentile stretch for RGB display and plot RGB alongside NDVI.
6. Save the downsampled NDVI as a GeoTIFF
   
It relates to our final project "Developing QGIS Plugin for VirtuGhan" and supports the Tiler, Extractor and Engine modules which perform on-the-fly tile retrieval and index computation.


---

## 🧰 Libraries Used

- **pystac-client**  
  To query STAC items from Microsoft Planetary Computer  
  (https://pystac-client.readthedocs.io/)

- **planetary-computer**  
  To sign STAC items for authenticated COG access  
  (https://github.com/microsoft/planetary-computer)

- **rasterio**  
  To open, resample, and write GeoTIFFs  
  (https://rasterio.readthedocs.io/)

- **numpy**  
  For array operations and NDVI calculation  
  (https://numpy.org/doc/)

- **matplotlib**  
  For plotting RGB and NDVI side by side  
  (https://matplotlib.org/stable/)

---

## 🗺️ Area of Interest

- **Location**: Bucharest, Romania  
- **Bounding Box**: `[26.05, 44.38, 26.15, 44.48]`  
- **Time Range**: April 1 2024 – April 30 2024  
- **Cloud Cover Filter**: `< 30 %`

---

## 🧪 Workflow Summary

1. **Connect to STAC API**  
   - Use `pystac-client` (Planetary Computer endpoint) to search Sentinel-2 L2A scenes over the AOI and date range, filtering for cloud cover < 30 %.

2. **Select and Sign a STAC Item**  
   - Retrieve the first available item, then apply `planetary_computer.sign(item)` to get authenticated COG URLs for B02, B03, B04, and B08.

3. **Downsampled Band Reads**  
   - For each band (B02, B03, B04, B08), use `rasterio.open(href)` with `out_shape=(height//4, width//4)` and `Resampling.bilinear` to read a ¼-resolution array.  
   - Update the transform in metadata to reflect the new resolution.

4. **Inspect Band Statistics**  
   - Print `np.nanmin` and `np.nanmax` for Red, Green, Blue, and NIR to confirm valid reflectance values (e.g., ~0–16 000).

5. **Compute NDVI**  
   - NDVI = (NIR – Red) / (NIR + Red), masking `(NIR + Red) == 0` to `NaN`.  
   - Print NDVI valid pixel count and min/max (should lie within –1…+1).

6. **Percentile Stretch & RGB Display**  
   - Apply a 2–98 percentile stretch to each of Red, Green, and Blue separately:  
     ```python
     def stretch_pct(band, p_lo=2, p_hi=98):
         lo = np.nanpercentile(band, p_lo)
         hi = np.nanpercentile(band, p_hi)
         stretched = (band - lo) / (hi - lo)
         return np.clip(stretched, 0, 1)
     ```
   - Stack the stretched Red, Green, Blue into an `(H, W, 3)` array for display.

7. **Plot Side by Side**  
   - Left: RGB composite (`imshow(rgb_disp)`)  
   - Right: NDVI (`imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)`)  
   - Include a colorbar showing the full NDVI range.


---



