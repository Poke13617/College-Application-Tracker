import math

# Safety accRate >= 75
# Match accRate > 25
# Reach accRate =< 25
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
REACH_ACCEPTANCE_RATE = 25.0
MAX_IDEAL_DISTANCE = 500
MILES_PER_GALLON = 28.0
GAS_PRICE = 3.50

collegeName = []
location = []
annTuition = []
disFromHome = []
accRate = []
total4yrTuits = []
classification = []
print("=" * 50)
print("COLLEGE APPLICATION TRACKER")
print("=" * 50)
print("Track your college applications and analyze your options!")
print("=" * 50)
print("\n")
NAME = input("What is your name? ")
print("\nWelcome " + NAME + ", let's track your college applications.\n")
print("Please enter information for 3 colleges you're considering:")
for i in range(0,3):
    print("---College #" + str(i+1) + "---")
    collegeName.append(input("College name: "))
    location.append(input("Location (City, State): "))
    annTuition.append(int(input("Annual tuition ($): ")))
    disFromHome.append(int(input("Distance from home (miles): ")))
    accRate.append(float(input("Acceptance rate(%): ")))
    print("\n")
print("\n\n")
print("=" * 50)
print("YOUR COLLEGE APPLICATION SUMMARY")
print("=" * 50)
print("\n")

for i in range(0,3):
    total4yrTuits.append(annTuition[i] * 4)
    if accRate[i] > AVG_ACCEPTANCE_RATE:
        classification.append("Safety")
    elif accRate[i] <= AVG_ACCEPTANCE_RATE and accRate[i] > REACH_ACCEPTANCE_RATE:
        classification.append("Match")
    elif accRate[i] <= REACH_ACCEPTANCE_RATE:
        classification.append("Reach")

for i in range(0,3):
    print("College " + str(i+1) + ": " + collegeName[i])
    print("Location: " + location[i])
    print(f"Annual Tuition: ${annTuition[i]:,.2f}")
    print("Distance from Home: " + str(float(disFromHome[i])) + " miles")
    print("Acceptance Rate: " + str(accRate[i]) + "%")
    print("Classification: " + classification[i])
    print(f"4-Year Total Cost: ${total4yrTuits[i]:,.2f}\n")

print("=" * 50)
print("FINANCIAL ANALYSIS")
print("=" * 50)
totalAppFees = APPLICATION_FEE * 3
avAnnTuition = sum(annTuition) / len(annTuition)
total4yrTuits = sum(annTuition)

priciest = collegeName[annTuition.index(max(annTuition))]
cheapest = collegeName[annTuition.index(min(annTuition))]

priceDifference = max(annTuition) - min(annTuition)

print(f"Total Application Fees: ${totalAppFees:.2f}")
print(f"Average Annual Tuition: ${avAnnTuition:.2f}")
print(f"Total 4-year Tuition (All Schools): ${total4yrTuits:.2f}")
print("\n")

print(f"Most affordable: {cheapest} (${min(annTuition):.2f}/year)")
print(f"Most Expensive: {priciest} (${max(annTuition):.2f}/year)")
print(f"Price Difference: ${priceDifference:.2f}/year")

print("")
print("=" * 50)
print("DISTANCE & TRAVEL ANALYSIS")
print("=" * 50)

avgDist = sum(disFromHome) / len(disFromHome)
totalDist = sum(disFromHome)
gallons = math.ceil(totalDist/MILES_PER_GALLON)
estTravCost = gallons * GAS_PRICE
disSpread = ((totalDist / len(disFromHome)))

print("Average Distance: " + str(avgDist) + " miles")

print("Total Distance (visiting all, round trips): " + str(totalDist) + " miles")

print("Estimated Fuel Needed: " + str(gallons) + " gallons")

print(f"Estimated Travel Cost: {estTravCost:,.2f}")

print("Distance Spread (Standard Deviation): " + str(disSpread) + " miles\n")

print("=" * 50)
print("ACCEPTANCE RATE ANALYSIS")
print("=" * 50)

avgAcceptanceRate = sum(accRate) / len(accRate)

print("Your Average Acceptance Rate: " + str(avgAcceptanceRate) + "%")
print('National Average: ' + str(AVG_ACCEPTANCE_RATE) + "\n\n")

print("Your Application Balance:")
print(" Safety Schools: " + str(classification.count("Safety")))
print(" Match Schools: " + str(classification.count("Match")))
print(" Reach Schools: " + str(classification.count("Reach")))
print("")

print("=" * 50)
print("RECOMMENDATIONS FOR " + NAME)
print("=" * 50)
if classification.count("Safety") == 0:
    print("Consider adding a safety school to your list!")
elif classification.count("Reach") == 0 // classification.count("Reach") == 1:
    print("Don't be afraid to apply to a reach school - you might surprise yourself!")
else: 
    print("You have a balanced mix of schools!")


if totalDist > MAX_IDEAL_DISTANCE:
    print("Your schools are " + str(totalDist) + " miles away - consider travel costs!")
else:
    print("Your schools are within a resonable distance (avg: " + str(totalDist) + " miles)" )


if avAnnTuition > 50000:
    print("Average tuition is high - research scholarship opportunities!")
else:
    print("Average tuition of $" + str(avAnnTuition) + " is moderate - good planning!")

