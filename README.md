sacramento-air-quality
Python based analysis of PM2.5 air quality using PurpleAir API data
This project analyzes fine particulate matter (PM2.5) in Sacramento, California using real-time PurpleAir sensor data. It focuses on spatial and temporal variability in air pollution and applies EPA-based correction factors to improve measurement accuracy.
  
 Objectives
•	Collect live PM2.5 data from PurpleAir API
•	Clean and filter sensor data for quality control
•	Apply EPA correction to improve accuracy
•	Visualize:
o	Spatial pollution distribution
o	Time-series trends
o	Pollution variability across sensors
 
Methods
•	Python (Pandas, Requests, Matplotlib)
•	PurpleAir API
•	EPA PM2.5 correction equation
•	Spatial filtering using latitude/longitude bounding box
 
Key Outputs
•	Sacramento PM2.5 heat map
•	24-hour time series of air pollution
•	Distribution of PM2.5 across sensors
 
Key Insight

PM2.5 concentrations show spatial clustering and temporal variation consistent with traffic emissions and atmospheric inversion conditions in the Sacramento Valley.
 
Tools Used
•	Python
•	Pandas
•	Matplotlib
•	PurpleAir API
 
Future Improvements
•	Integration with EPA AirNow monitors
•	Machine learning prediction of PM2.5 levels
•	GIS mapping using ArcGIS / QGIS
 
