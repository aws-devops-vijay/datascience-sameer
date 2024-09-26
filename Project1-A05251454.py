import tkinter as tk
from tkinter import ttk

# Comprehensive conclusion list for backward chaining
conclusion_list = [
    ["Battery problem", "Battery is weak", "Check battery connections", "Replace battery"],
    ["Starter motor issue", "Starter doesn't engage", "Check starter", "Replace starter"],
    ["Bad alternator", "Battery not charging", "Check alternator", "Replace alternator"],
    ["Engine overheating", "Temperature gauge high", "Check coolant", "Replace thermostat"],
    ["Transmission fluid leak", "Fluid low", "Check for leaks", "Fix transmission leak"],
    ["Worn-out clutch", "Slipping clutch", "Check clutch pedal", "Replace clutch"],
    ["Warped rotors", "Brakes squeaking", "Check brake rotors", "Replace rotors"],
    ["Worn brake pads", "Brakes grinding", "Check brake pads", "Replace brake pads"],
    ["Rich fuel mixture", "Smoke from exhaust", "Check fuel system", "Adjust air-fuel mixture"],
    ["Oil burning", "Oil on ground", "Check seals", "Replace engine seals"],
    ["Coolant leak", "Coolant low", "Check for leaks", "Repair coolant leak"],
    ["Wheel alignment issue", "Steering off", "Check alignment", "Realign wheels"],
    ["Unbalanced tires", "Vibrating at speed", "Check tire balance", "Balance the tires"],
    ["Radiator failure", "Overheating", "Check radiator", "Replace radiator"],
    ["Faulty piston rings", "Excessive oil consumption", "Check piston rings", "Replace piston rings"],
    ["Turbocharger failure", "Loss of power", "Check turbocharger", "Replace or repair turbocharger"],
    ["Air filter clogged", "Reduced performance", "Check air intake", "Replace air filter"],
    ["Thermostat stuck", "Engine overheating", "Check thermostat", "Replace thermostat"],
    ["Cooling fan failure", "Overheating", "Check fan operation", "Replace cooling fan"],
    ["Oil pump failure", "Low oil pressure", "Check oil pump", "Replace oil pump"],
    ["Fuel injector issue", "Engine misfiring", "Check injectors", "Clean or replace fuel injectors"],
    ["Timing belt worn", "Engine noise", "Check timing belt", "Replace timing belt"],
    ["Exhaust manifold leak", "Loud exhaust", "Check manifold", "Repair exhaust manifold"],
    ["Faulty oxygen sensor", "Check engine light", "Check oxygen sensor", "Replace oxygen sensor"],
    ["Fuel pressure low", "Engine stalling", "Check fuel pressure regulator", "Replace if necessary"],
    ["Catalytic converter clogged", "Reduced performance", "Check exhaust flow", "Replace catalytic converter"],
    ["Throttle body dirty", "Poor acceleration", "Check throttle body", "Clean throttle body"],
    ["PCV valve stuck", "Engine issues", "Check PCV system", "Replace PCV valve"],
    ["Vibration from suspension", "Unstable ride", "Check suspension components", "Replace as needed"],
    ["Water pump leak", "Coolant low", "Check water pump", "Replace water pump"],
    ["Cracked cylinder head", "Engine overheating", "Check cylinder head", "Repair or replace cylinder head"],
    ["Fuel pump failure", "No fuel delivery", "Check fuel pump", "Replace fuel pump"],
    ["Overheating transmission", "Transmission slipping", "Check transmission cooler", "Replace or repair cooler"],
    ["Misfiring engine", "Loss of power", "Check ignition system", "Check coils and plugs"],
    ["Vacuum leak", "Rough idle", "Check vacuum lines", "Repair vacuum lines"],
    ["Ignition coil failure", "Engine misfire", "Check ignition coils", "Replace ignition coils"],
    ["Timing chain stretched", "Engine noise", "Check timing chain", "Replace timing chain"],
]

# Global variables
variable_list = [None] * 16  
derived_global_variable_list = []

def search_con(variable):
    for i, rule in enumerate(conclusion_list):
        if variable in rule:
            return i + 1
    return None

def rule_to_clause(ri):
    clause_number = 4 * (ri - 1) + 1
    update_VL(clause_number)

def clause_to_rule(ci):
    rule_index = (ci - 1) // 4
    return rule_index + 1 if rule_index < len(conclusion_list) else None

def update_VL(ci):
    for i in range(ci, ci + 4):
        if i < len(variable_list) and variable_list[i] is None:
            variable = input(f"Please provide the value for variable at index {i}: ")
            variable_list[i] = variable
        elif i >= len(variable_list):
            break

def validate_Ri(ri):
    rule = conclusion_list[ri - 1]
    satisfied = True
    for var in rule[:-1]:  
        if var not in variable_list:
            satisfied = False
            break
    return satisfied

def process_backward_chaining(variable):
    while True:
        ri = search_con(variable)
        if not ri:
            break
        rule_to_clause(ri)
        if validate_Ri(ri):
            conclusion = conclusion_list[ri - 1][-1]  
            derived_global_variable_list.append(conclusion)
            return conclusion

def forward_chain(diagnosis):
    recommendations = {
        "Battery problem": "Replace or Recharge the Battery",
        "Starter motor issue": "Replace the Starter Motor",
        "Bad alternator": "Replace or Repair the Alternator",
        "Engine overheating": "Check Coolant System, Replace Thermostat",
        "Transmission fluid leak": "Fix Transmission Leak",
        "Worn-out clutch": "Replace Clutch",
        "Warped rotors": "Replace Rotors",
        "Worn brake pads": "Replace Brake Pads",
        "Rich fuel mixture": "Adjust Air-Fuel Mixture",
        "Oil burning": "Check Engine Seals, Replace if Necessary",
        "Coolant leak": "Repair Coolant Leak",
        "Wheel alignment issue": "Realign Wheels",
        "Unbalanced tires": "Balance the Tires",
        "Radiator failure": "Replace Radiator",
        "Faulty piston rings": "Replace piston rings",
        "Turbocharger failure": "Replace or repair turbocharger",
        "Air filter clogged": "Replace air filter",
        "Thermostat stuck": "Replace thermostat",
        "Cooling fan failure": "Check and replace cooling fan",
        "Oil pump failure": "Replace oil pump",
        "Fuel injector issue": "Clean or replace fuel injector",
        "Timing belt worn": "Replace timing belt",
        "Exhaust manifold leak": "Repair exhaust manifold",
        "Faulty oxygen sensor": "Replace oxygen sensor",
        "Fuel pressure low": "Check and replace fuel pressure regulator",
        "Catalytic converter clogged": "Replace catalytic converter",
        "Throttle body dirty": "Clean throttle body",
        "PCV valve stuck": "Replace PCV valve",
        "Vibration from suspension": "Check and replace suspension components",
        "Water pump leak": "Replace water pump",
        "Cracked cylinder head": "Repair or replace cylinder head",
        "Fuel pump failure": "Replace fuel pump",
        "Overheating transmission": "Check and replace transmission cooler",
        "Misfiring engine": "Check ignition coils and spark plugs",
        "Vacuum leak": "Repair vacuum lines",
        "Ignition coil failure": "Replace ignition coil",
        "Timing chain stretched": "Replace timing chain",
        
        "Suspension problems": "Inspect suspension components thoroughly",
        "Brake fluid leak": "Inspect brake lines and fluid reservoir",
        "Fuel tank leak": "Check for cracks in the fuel tank",
        "Battery corrosion": "Clean battery terminals and connections",
        "Engine knocking": "Check engine bearings and oil level",
        "A/C system failure": "Check refrigerant levels and compressor",
        "Transmission overheating": "Inspect transmission fluid level and cooler",
    }
    return recommendations.get(diagnosis, "Consult a Professional Mechanic")



def update_symptoms(*args):
    symptom_var.set("")  
    selected_problem = problem_var.get()
    symptoms = symptom_options.get(selected_problem, [])
    symptom_dropdown['values'] = symptoms  # Update the values directly
    if symptoms:
        symptom_var.set(symptoms[0])  # Set the first symptom as default


def diagnose_and_recommend():
    problem = problem_var.get()
    symptom = symptom_var.get()

    # Diagnosis based on backward chaining logic
    diagnosis = ""
    
    # Engine Problems
    if problem == "Engine":
        if symptom == "Slow to start":
            diagnosis = "Battery problem"
        elif symptom == "Clicking sound":
            diagnosis = "Starter motor issue"
        elif symptom == "Whining noise":
            diagnosis = "Bad alternator"
        elif symptom == "Smoke from engine" or symptom == "Temperature gauge high":
            diagnosis = "Engine overheating"
        elif symptom == "Engine knocking":
            diagnosis = "Faulty piston rings"
    
    # Transmission Problems
    elif problem == "Transmission":
        if symptom == "Gears slipping" or symptom == "Burning smell":
            diagnosis = "Transmission fluid leak"
        elif symptom == "Grinding noise":
            diagnosis = "Worn-out clutch"
        elif symptom == "Transmission overheating":
            diagnosis = "Overheating transmission"
    
    # Brakes Problems
    elif problem == "Brakes":
        if symptom == "Brakes squeaking":
            diagnosis = "Warped rotors"
        elif symptom == "Brakes grinding":
            diagnosis = "Worn brake pads"
    
    # Exhaust Problems
    elif problem == "Exhaust":
        if symptom == "Smoke from exhaust":
            diagnosis = "Rich fuel mixture"
    
    # Overheating Problems
    elif problem == "Overheating":
        if symptom == "Temperature gauge high":
            diagnosis = "Engine overheating"
    
    # Steering Problems
    elif problem == "Steering":
        if symptom == "Steering off":
            diagnosis = "Wheel alignment issue"
    
    # Suspension Problems
    elif problem == "Suspension":
        if symptom == "Vibration from suspension":
            diagnosis = "Vibration from suspension"
    
    # Fuel Problems
    elif problem == "Fuel":
        if symptom == "Fuel tank leak":
            diagnosis = "Fuel tank leak"

    recommendation = forward_chain(diagnosis)
    
    diagnosis_label.config(text=f"Diagnosis: {diagnosis}")
    recommendation_label.config(text=f"Recommendation: {recommendation}")

# Setup GUI
root = tk.Tk()
root.title("Automotive Diagnostic Tool")

# Create StringVars
problem_var = tk.StringVar()
symptom_var = tk.StringVar()  
symptom_var.set("")  

# Heading Labels
ttk.Label(root, text="Select the Problem Area:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")

problem_options = ["Engine", "Transmission", "Brakes", "Exhaust", "Overheating", "Steering", "Suspension", "Fuel"]
problem_dropdown = ttk.Combobox(root, textvariable=problem_var, values=problem_options)
problem_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")

ttk.Label(root, text="Select the Symptom:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")

symptom_dropdown = ttk.Combobox(root, textvariable=symptom_var)
symptom_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Trace the changes to problem_var to update symptoms accordingly
problem_var.trace("w", update_symptoms)

# Diagnose Button
ttk.Button(root, text="Diagnose & Recommend Repair", command=diagnose_and_recommend).grid(row=2, columnspan=2, padx=10, pady=20)

# Diagnosis and Recommendation Labels
diagnosis_label = ttk.Label(root, text="Diagnosis: ", font=("Arial", 14))
diagnosis_label.grid(row=3, columnspan=2, padx=10, pady=10)

recommendation_label = ttk.Label(root, text="Repair Recommendation: ", font=("Arial", 14))
recommendation_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Symptoms mapping
symptom_options = {
    "Engine": ["Slow to start", "Clicking sound", "Whining noise", "Smoke from engine", "Temperature gauge high", "Engine knocking"],
    "Transmission": ["Gears slipping", "Burning smell", "Grinding noise", "Transmission overheating"],
    "Brakes": ["Brakes squeaking", "Brakes grinding"],
    "Exhaust": ["Smoke from exhaust"],
    "Overheating": ["Temperature gauge high", "Coolant low", "Smoke from engine"],
    "Steering": ["Steering off", "Vibrating at speed"],
    "Suspension": ["Vibration from suspension"],
    "Fuel": ["Fuel tank leak"],
}

# Initialize symptom dropdown
update_symptoms()

# Run the GUI loop
root.mainloop()