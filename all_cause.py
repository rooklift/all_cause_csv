# The graph generated here is interesting but likely misleading. Basically it shows that [vaccinated people under 60]
# die more than [unvaccinated people under 60]. But...
#
# This is likely misleading because, not considered is that the average [vaccinated person under 60] is (presumably?)
# much older than the average [unvaccinated person under 60], and so more likely to die from any cause.
#
# Data from: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/deathsbyvaccinationstatusengland
#
# I'm saving this mostly just so I can have an example of code working with csv files.

import matplotlib.pyplot as plt

with open("table4.csv") as infile:
	rawlines = infile.readlines()
	headerline = rawlines[0].strip()
	datalines = [s.strip() for s in rawlines[1:]]

headers = headerline.split(",")

datapoints = []

for line in datalines:

	datapoint = dict()
	fields = line.split(",")

	assert(len(fields) == len(headers))

	for i, field in enumerate(fields):
		datapoint[headers[i]] = field

	datapoints.append(datapoint)


unvacc_under60 = [dp for dp in datapoints if dp["Age group"] == "10-59" and dp["Vaccination status"] == "Unvaccinated"]
vacc_under60 = [dp for dp in datapoints if dp["Age group"] == "10-59" and dp["Vaccination status"] == "Second dose"]


# Graph the unvaccinated
x = [int(dp["Week number"]) for dp in unvacc_under60]
y = [100000 * float(dp["Number of deaths"]) / float(dp["Population"]) for dp in unvacc_under60]
plt.plot(x, y)

# Graph the vaccinated
x = [int(dp["Week number"]) for dp in vacc_under60]
y = [100000 * float(dp["Number of deaths"]) / float(dp["Population"]) for dp in vacc_under60]
plt.plot(x, y)

plt.xlabel("Week")
plt.ylabel("Rate per 100,000")
plt.title("All-cause mortality rate per 100,000")

plt.show()