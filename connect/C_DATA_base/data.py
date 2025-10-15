import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

# basic data
diseases = ["Diabetes", "Flu", "COVID-19", "Hypertension", "Asthma", "Pneumonia", "Cancer", "Migraine"]
medicines = {
    "Diabetes": ["Metformin", "Insulin"],
    "Flu": ["Paracetamol", "Antihistamine"],
    "COVID-19": ["Remdesivir", "Dexamethasone"],
    "Hypertension": ["Amlodipine", "Lisinopril"],
    "Asthma": ["Salbutamol", "Corticosteroid"],
    "Pneumonia": ["Azithromycin", "Amoxicillin"],
    "Cancer": ["Chemotherapy", "Targeted Therapy"],
    "Migraine": ["Ibuprofen", "Triptans"]
}
statuses = ["Under Treatment", "Recovered", "Deceased"]
genders = ["Male", "Female"]
rooms = [f"{floor}{room:02d}" for floor in range(1, 6) for room in range(1, 21)]  # 5 طوابق × 20 غرفة
specializations = ["Internal Medicine", "Cardiology", "Neurology", "Orthopedics", "Oncology", "Pediatrics"]
nurses = ["Nurse A", "Nurse B", "Nurse C", "Nurse D", "Nurse E"]
surgery_types = ["Appendectomy", "Bypass Surgery", "Tumor Removal", "Gallbladder Removal"]
# plans
treatment_plans = {
    "Diabetes": "Regular insulin shots, exercise, low sugar diet",
    "Flu": "Rest, fluids, antiviral medication if severe",
    "COVID-19": "Oxygen support, antivirals, isolation",
    "Hypertension": "Daily medication, low salt diet, regular BP check",
    "Asthma": "Inhalers, avoid allergens, pulmonary exercises",
    "Pneumonia": "Antibiotics, bed rest, hydration",
    "Cancer": "Chemotherapy sessions, regular scans, pain management",
    "Migraine": "Painkillers, avoid triggers, proper sleep schedule"
}
diet_plans = {
    "Diabetes": "Low sugar, high fiber, whole grains, lean protein",
    "Flu": "Vitamin C rich fruits, warm fluids, light meals",
    "COVID-19": "High protein, vitamin supplements, hydration",
    "Hypertension": "Low sodium, lots of vegetables, avoid red meat",
    "Asthma": "Anti-inflammatory diet, omega-3 foods, avoid dairy excess",
    "Pneumonia": "Soups, hydration, foods rich in zinc and vitamins",
    "Cancer": "High calorie, nutrient dense, soft foods",
    "Migraine": "Magnesium rich diet, avoid caffeine and chocolate"
}

# create records
records = []
for i in range(1, 301):  # 300 مريض
    patient_id = f"P{i:03d}"
    name = fake.first_name() + " " + fake.last_name()
    age = random.randint(1, 90)
    gender = random.choice(genders)
    address = fake.city()
    contact = fake.phone_number()
    admission_date = fake.date_between(start_date="-90d", end_date="today")
    discharge_date = admission_date + timedelta(days=random.randint(2, 20))
    length_of_stay = (discharge_date - admission_date).days

    disease = random.choice(diseases)
    severity = random.choice(["Mild", "Moderate", "Severe"])
    symptoms = random.choice(["Fever, cough", "Headache, fatigue", "Chest pain, dizziness", "Breathing difficulty", "Stomach pain"])
    comorbidities = random.choice(["None", "Diabetes", "Hypertension", "Asthma", "Multiple"])
    status = random.choices(statuses, weights=[0.6, 0.3, 0.1])[0]

    doctor = fake.first_name() + " " + fake.last_name()
    specialization = random.choice(specializations)
    nurse = random.choice(nurses)
    room = random.choice(rooms)

    medicine = random.choice(medicines[disease])
    dose = str(random.choice([100, 250, 500])) + "mg"
    frequency = random.choice(["1/day", "2/day", "3/day"])
    treatment = treatment_plans[disease]
    diet = diet_plans[disease]
    note = random.choice([
        "Patient is responding well to treatment",
        "Patient is not eating properly, needs nutritional support",
        "Medication is causing mild side effects",
        "Patient shows good improvement",
        "Condition is stable but requires monitoring",
        "Patient is weak, further tests recommended"
    ])

    surgery_needed = random.choice(["Yes", "No"])
    surgery_type = random.choice(surgery_types) if surgery_needed == "Yes" else "None"
    surgery_success_rate = random.randint(60, 95) if surgery_needed == "Yes" else None

    if status == "Recovered":
        follow_up = admission_date + timedelta(days=random.randint(15, 60))
    elif status == "Under Treatment":
        follow_up = admission_date + timedelta(days=random.randint(3, 15))
    else:
        follow_up = None
    missed = random.randint(0, 3) if follow_up else None

    treatment_cost = random.randint(2000, 20000)
    insurance = random.choice(["Yes", "No"])
    insurance_coverage = random.randint(30, 90) if insurance == "Yes" else 0
    patient_bill = treatment_cost - (treatment_cost * insurance_coverage // 100)

    records.append([
        patient_id, name, age, gender, address, contact, admission_date, discharge_date, length_of_stay,
        disease, severity, symptoms, comorbidities, status,
        doctor, specialization, nurse, room,
        medicine, dose, frequency, treatment, diet, note,
        surgery_needed, surgery_type, surgery_success_rate,
        follow_up, missed, treatment_cost, insurance, insurance_coverage, patient_bill
    ])

#  create DataFrame
df_full = pd.DataFrame(records, columns=[
    "Patient_ID", "Name", "Age", "Gender", "Address", "Contact_Info",
    "Admission_Date", "Discharge_Date", "Length_of_Stay",
    "Disease", "Severity_Level", "Symptoms", "Comorbidities", "Status",
    "Doctor_Name", "Specialization", "Nurse_Assigned", "Room",
    "Medicine", "Dose", "Frequency", "Treatment_Plan", "Diet_Plan", "Doctor_Notes",
    "Surgery_Needed", "Surgery_Type", "Surgery_Success_Rate",
    "Follow_Up_Date", "Missed_Appointments",
    "Treatment_Cost", "Insurance", "Insurance_Coverage", "Patient_Bill"
])

#  copy file as CSV
df_full.to_csv("hospital_dataset_full.csv", index=False)
print("The file hospital_dataset_full.csv had maded succefully ✅")