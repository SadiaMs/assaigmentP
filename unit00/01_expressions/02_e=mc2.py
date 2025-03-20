"""
🔬 Einstein's Mass-Energy Equivalence Formula 🔬
------------------------------------------------
This program takes mass (m) as input and calculates energy (E) 
using Einstein's famous equation:  E = m * C^2
where:
    C = 299,792,458 m/s (Speed of Light)
"""

# Define the speed of light in meters per second
C: int = 299792458  

def main():
    print("\n🌟 Einstein's Energy Formula 🌟\n")
    
    try:
        # Take mass input from the user
        mass_in_kg: float = float(input("🔢 Enter mass in kg: "))

        # Calculate energy using the formula E = m * C^2
        energy_in_joules: float = mass_in_kg * (C ** 2)

        # Display the calculated energy
        print("\n⚡ e = m * C^2... ⚡")
        print(f"📌 m = {mass_in_kg} kg")
        print(f"📌 C = {C} m/s")
        print(f"\n💡 {energy_in_joules:.2e} joules of energy will be produced! 🚀")
    
    except ValueError:
        # Handle invalid inputs (non-numeric values)
        print("\n❌ Please enter a valid number! ❌")

# Standard Python practice to ensure the script runs correctly
if __name__ == '__main__':
    main()
