# Smart Parking System Simulation

# Parking spots dictionary
# 0 = Free spot
# 1 = Occupied spot

parking_spots = {
    "P1": 1,
    "P2": 0,
    "P3": 1,
    "P4": 0,
    "P5": 1
}

# Function to check available parking
def check_available_spots(spots):
    available = []
    
    for spot, status in spots.items():
        if status == 0:
            available.append(spot)
    
    return available


# Function to guide driver to nearest spot
def guide_driver(spots):
    
    available = check_available_spots(spots)
    
    if len(available) == 0:
        print("No parking spots available")
    
    else:
        print("Available Parking Spots:", available)
        print("Guide Driver To:", available[0])


# Main program
print("Smart Parking System\n")

print("Current Parking Status")
for spot, status in parking_spots.items():
    
    if status == 0:
        print(spot, "-> Free")
    else:
        print(spot, "-> Occupied")


print("\nChecking for available parking...\n")

guide_driver(parking_spots)