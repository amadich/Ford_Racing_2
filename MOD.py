import os

# Specify the directory path
directory = r"C:\Program Files (x86)\Empire Interactive\Ford Racing 2\DATA\ASCII\CARS"

# Specify the files to modify
files_to_modify = ["ENGDATA.dat", "GEARDATA.dat"]

# Specify the modification parameters
torque_modifier = "9.35"
clutch_speed = "0"
clutch_max_power = "99999"

# Function to modify ENGDATA.dat
def modify_engdata():
    engdata_path = os.path.join(directory, "ENGDATA.dat")

    with open(engdata_path, "r") as file:
        engdata = file.readlines()

    # Find and modify the TORQUE_MODIFIER line
    for i, line in enumerate(engdata):
        if line.startswith(":TORQUE_MODIFIER"):
            engdata[i] = f":TORQUE_MODIFIER\t\t\t{torque_modifier}\n"
            break

    with open(engdata_path, "w") as file:
        file.writelines(engdata)

    print("ENGDATA.dat modified successfully.")

# Function to modify GEARDATA.dat
def modify_geardata():
    geardata_path = os.path.join(directory, "GEARDATA.dat")

    with open(geardata_path, "r") as file:
        geardata = file.readlines()

    # Find and modify the CLUTCH_SPEED and CLUTCH_MAX_POWER lines
    for i, line in enumerate(geardata):
        if line.startswith(":CLUTCH_SPEED"):
            geardata[i] = ":CLUTCH_SPEED\t\t" + clutch_speed + "\n"
        elif line.startswith(":CLUTCH_MAX_POWER"):
            geardata[i] = ":CLUTCH_MAX_POWER\t" + clutch_max_power + "\n"

    with open(geardata_path, "w") as file:
        file.writelines(geardata)

    print("GEARDATA.dat modified successfully.")

# Main function to perform modifications
def main():
    # Check if the directory exists
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    # Modify ENGDATA.dat if it exists
    if "ENGDATA.dat" in os.listdir(directory):
        modify_engdata()
    else:
        print("ENGDATA.dat not found.")

    # Modify GEARDATA.dat if it exists
    if "GEARDATA.dat" in os.listdir(directory):
        modify_geardata()
    else:
        print("GEARDATA.dat not found.")

# Run the main program
main()
