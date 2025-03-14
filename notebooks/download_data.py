import airbase

'''
The most common air pollutants are:

Particulate Matter (PM2.5 and PM10): Tiny solid and liquid particles in the air, mainly from vehicle exhaust, 
                                     industrial emissions, wildfires, and dust storms. PM2.5 is especially dangerous 
                                     as it can penetrate deep into the lungs and bloodstream.

Carbon Monoxide (CO): A colorless, odorless gas mainly produced by incomplete combustion in vehicles, industrial processes, 
                      and residential heating.

Nitrogen Oxides (NOₓ): Gases (mainly NO and NO₂) from vehicle emissions, power plants, and industrial activities that 
                       contribute to smog and acid rain.

Sulfur Dioxide (SO₂): Produced by burning fossil fuels (especially coal) and industrial processes, leading to acid rain 
                      and respiratory problems.

Ozone (O₃): A secondary pollutant formed when NOₓ and volatile organic compounds (VOCs) react in sunlight. 
            Ground-level ozone is a major component of smog.

Volatile Organic Compounds (VOCs): Gases from solvents, paints, vehicle exhaust, and industrial processes. 
                                   Some VOCs, like benzene and formaldehyde, are carcinogenic.

Ammonia (NH₃): Released mainly from agricultural activities, such as fertilizers and livestock waste, contributing 
               to fine particulate pollution.

Lead (Pb): A toxic metal that was historically emitted from leaded gasoline and industrial processes, 
           still a concern near smelting facilities.

Each of these pollutants has serious environmental and health effects, including respiratory diseases, cardiovascular issues, and climate change impacts.
'''

client = airbase.AirbaseClient()
# r = client.request("Verified", "IT", "DE", "PL", "FR", "CH", "GB", poll=["PM2.5", "PM10", "NO", "NO2", "NO3", "O3", "CO", "Co", "SO2", "NH3", "Pb"])
r = client.request("Verified", "IT", "DE", "PL", "FR", "CH", "GB", "ES", poll=["PM2.5"])
r.download(dir="data", skip_existing=True)
client.download_metadata("data/metadata.csv")