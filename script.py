#Query Sacramento Purple Air data (API)
#Sacramento bounding box
# NW_LAT = 38.75
# NW_LON = -121.65
# SE_LAT = 38.45
# SE_LON = -121.20

import requests 
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "FA94C4CE-4118-11F1-B596-4201AC1DC123"
url  = "https://api.purpleair.com/v1/sensors"

params = {
	"fields":"sensor_index,latitude,longitude,pm2.5_atm,confidence",
	"location_type": 0, #outdoor only
	"nwlng": -121.65,
	"nwlat": 38.75,
	"selng": -121.20,
	"selat": 38.45	
}

headers = {"X-API-Key":API_KEY}

response = requests.get(url, headers=headers, params=params) 
print("Status:",response.status_code)
print("Response text:",response.text[:500])
data = response.json()

#convert to Dataframez
#Handle API errors BEFORE Dataframe
if "error" in data:
	print("API Error:", data["description"])
else:
	df = pd.DataFrame(data["data"], columns=data["fields"])
	print(df.head())

#plot data before cleaning

plt.figure()
plt.scatter(df["longitude"], df["latitude"], s=20 + df["pm2.5_atm"]) , #size = pollution
plt.title("sacramento PM2.5 Sensor Map")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.show()

plt.figure()
plt.hist(df["pm2.5_atm"],bins=30)
plt.title("PM2.5 Distribution (Sacramento)")
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("Frequency")
plt.show()

#clean data 

df = df[df["confidence"] > 75]

df = df[df["pm2.5_atm"].notna()]
df = df[df["pm2.5_atm"] >= 0]

#apply EPA correction 
df["pm25_corrected"] = (0.52 * df["pm2.5_atm"] - 0.085 *50 + 5.71) 

#remove outliers
df = df[df["pm25_corrected"] < 500]
print(df)


#plot data AFTER cleaning

plt.figure()
plt.scatter(df["longitude"], df["latitude"], s=20 + df["pm25_corrected"]) , #size = pollution
plt.title("sacramento PM2.5 Sensor Map")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.show()

plt.figure()
plt.hist(df["pm25_corrected"],bins=30)
plt.title("PM2.5 Distribution (Sacramento)")
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("Frequency")
plt.show()



#Spatial Averaging
df["lat_round"] = df["latitude"].round(2)
df["lon_round"] = df["longitude"].round(2)

df_avg = df.groupby(["lat_round", "lon_round"])["pm25_corrected"].mean().reset_index()
# print(df_avg)

plt.figure()

scatter = plt.scatter(df_avg["lon_round"], df_avg["lat_round"], c=df_avg["pm25_corrected"])

plt.colorbar(scatter, label="PM2.5 (µg/m³)")
plt.title("Sac PM2.5 (Spatially Averaged)")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.show()

df.to_csv('purpleair_cleanpm25.csv', index=False)
