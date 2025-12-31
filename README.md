## How to Run
pip install -r requirements.txt
python src/main.py

 ## Approach
- Selected four corner points of the wall
- Applied perspective transformation using OpenCV
- Calculated pixel-to-mm scale using reference laser measurements
- Estimated wall dimensions

## Assumptions
- Wall is planar
- Laser lines are horizontal
- Camera distortion is negligible

## Future Work
- Level 2: Camera calibration and lens distortion removal
- Level 3: Non-rigid transformations such as Thin Plate Spline

 ## Note: 
 Images are stored under data/raw and data/reference and can be viewed via Raw/Download on GitHub.
 
 ##Note :
 This project is currently under debugging and improvement.

