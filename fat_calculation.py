import streamlit as st
import json

#Example
data = {
      "dish_name": "Dal Dhokli",
      "ingredients": [
        {
          "name": "Split Pigeon Peas (Toor Dal)",
          "quantity": "100",
          "unit": "g"
        },
        {
          "name": "Water",
          "quantity": "500",
          "unit": "ml"
        },
        {
          "name": "Salt",
          "quantity": "3",
          "unit": "g"
        },
        {
          "name": "Turmeric powder",
          "quantity": "1",
          "unit": "g"
        },
        {
          "name": "Red chili powder",
          "quantity": "2",
          "unit": "g"
        },
        {
          "name": "Coriander powder",
          "quantity": "2",
          "unit": "g"
        },
        {
          "name": "Cumin powder",
          "quantity": "1",
          "unit": "g"
        },
        {
          "name": "Garam masala",
          "quantity": "1",
          "unit": "g"
        },
        {
          "name": "Oil",
          "quantity": "10",
          "unit": "ml"
        },
        {
          "name": "All-purpose flour",
          "quantity": "100",
          "unit": "g"
        },
        {
          "name": "Water",
          "quantity": "50",
          "unit": "ml"
        },
        {
          "name": "Salt",
          "quantity": "1",
          "unit": "g"
        },
        {
          "name": "Ghee/Oil",
          "quantity": "10",
          "unit": "ml"
        }
      ],
      "allergic_content": {},
      "serving": {
        "size": "200",
        "unit": "g"
      },
      "nutrients": {
        "macro_nutrients": [
          {
            "name": "energy",
            "value": 618.35,
            "unit": "kcal"
          },
          {
            "name": "carbs",
            "value": 97.04,
            "unit": "g"
          },
          {
            "name": "proteins",
            "value": 21.62,
            "unit": "g"
          },
          {
            "name": "fats",
            "value": 15.91,
            "unit": "g"
          },
          {
            "name": "fibers",
            "value": 11.74,
            "unit": "g"
          }
        ],
        "water_soluble_vitamin": [
          {
            "name": "thiamin",
            "value": 0.51,
            "unit": "mg"
          },
          {
            "name": "riboflavin",
            "value": 0.12,
            "unit": "mg"
          },
          {
            "name": "niacin",
            "value": 3.1,
            "unit": "mg"
          },
          {
            "name": "vitamin_b5",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "vitamin_b6",
            "value": 0.31,
            "unit": "mg"
          },
          {
            "name": "vitamin_c",
            "value": 12.83,
            "unit": "mg"
          },
          {
            "name": "biotin",
            "value": 0.01,
            "unit": "µg"
          },
          {
            "name": "folate",
            "value": 202.31,
            "unit": "µg"
          }
        ],
        "fat_soluble_vitamin": [
          {
            "name": "vitamin_a",
            "value": 69.17,
            "unit": "µg"
          },
          {
            "name": "vitamin_d2",
            "value": 0,
            "unit": "µg"
          },
          {
            "name": "vitamin_d3",
            "value": 0,
            "unit": "µg"
          },
          {
            "name": "vitamin_k1",
            "value": 48.75,
            "unit": "µg"
          },
          {
            "name": "vitamin_k2",
            "value": 0,
            "unit": "µg"
          },
          {
            "name": "carotenoids",
            "value": 4.27,
            "unit": "µg"
          },
          {
            "name": "vitamin_e",
            "value": 2.25,
            "unit": "mg"
          }
        ],
        "minerals": [
          {
            "name": "aluminium",
            "value": 0.13,
            "unit": "mg"
          },
          {
            "name": "cadmium",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "calcium",
            "value": 84,
            "unit": "mg"
          },
          {
            "name": "chromium",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "cobalt",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "copper",
            "value": 0.52,
            "unit": "mg"
          },
          {
            "name": "iron",
            "value": 6.69,
            "unit": "mg"
          },
          {
            "name": "lead",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "lithium",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "magnesium",
            "value": 93.29,
            "unit": "mg"
          },
          {
            "name": "manganese",
            "value": 0.08,
            "unit": "mg"
          },
          {
            "name": "molybdenum",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "nickel",
            "value": 0,
            "unit": "mg"
          },
          {
            "name": "phosphorus",
            "value": 330.07,
            "unit": "mg"
          },
          {
            "name": "potassium",
            "value": 673.39,
            "unit": "mg"
          },
          {
            "name": "sodium",
            "value": 1925.78,
            "unit": "mg"
          },
          {
            "name": "zinc",
            "value": 2.63,
            "unit": "mg"
          },
          {
            "name": "arsenic",
            "value": 0.02,
            "unit": "µg"
          },
          {
            "name": "mercury",
            "value": 0.02,
            "unit": "µg"
          },
          {
            "name": "selenium",
            "value": 23.95,
            "unit": "µg"
          }
        ],
        "fatty_acid_profile": [
          {
            "name": "total_saturated_fats",
            "value": 4129.39,
            "unit": "mg"
          },
          {
            "name": "total_monounsaturated_fats",
            "value": 3594.22,
            "unit": "mg"
          },
          {
            "name": "total_polyunsaturated_fats",
            "value": 6260.87,
            "unit": "mg"
          }
        ],
        "cholesterol": [
          {
            "name": "cholesterol",
            "value": 10,
            "unit": "mg"
          }
        ],
        "sugar": [
          {
            "name": "total_carbohydrates",
            "value": 0.46,
            "unit": "g"
          },
          {
            "name": "starch",
            "value": 0.44,
            "unit": "g"
          },
          {
            "name": "fructose",
            "value": 0,
            "unit": "g"
          },
          {
            "name": "glucose",
            "value": 0,
            "unit": "g"
          },
          {
            "name": "sucrose",
            "value": 0.01,
            "unit": "g"
          },
          {
            "name": "maltose",
            "value": 0,
            "unit": "g"
          },
          {
            "name": "total_free_sugars",
            "value": 2.31,
            "unit": "g"
          }
        ],
        "other": [
          {
            "name": "total_minerals",
            "value": 0.06,
            "unit": "g"
          },
          {
            "name": "soluble_fiber",
            "value": 0.03,
            "unit": "g"
          },
          {
            "name": "insoluble_fiber",
            "value": 0.19,
            "unit": "g"
          }
        ]
      }
    }

rda_values = {
    "fiber": 40, # g/day done
    "protein": 50, # g/day done
    "thiamin": 0.0018,  # g/day done
    "riboflavin": 0.0025,  # g/day done
    "niacin": 0.018,  # g/day done
    "vitamin_b5": 0.005,  # g/day done
    "vitamin_b6": 0.0024,  # g/day done
    "vitamin_c": 0.08,  # g/day done
    "biotin": 0.000025,  # g/day
    "folate": 0.0003,  # g/day done
    "vitamin_a": 0.001,  # g/day done
    "vitamin_d2": 0.000015,  # g/day done e
    "vitamin_d3": 0.000015,  # g/day done e
    "vitamin_k1": 0.000055,  # g/day done e
    "vitamin_k2": 0.000055,  # g/day done e
    "carotenoids": 1,  # Not specified
    "vitamin_e": 0.009,  # g/day done
    "aluminium": 0.002,  # g/day
    "cadmium": 0.01,  # g/day
    "calcium": 1,  # g/day done
    "chromium": 0.00005,  # g/day done
    "cobalt": 0.00001,  # g/day
    "copper": 0.0017,  # g/day done
    "iron": 0.019,  # g/day done
    "lead": 0.01,  # g/day
    "lithium": 0,  # Not specified
    "magnesium": 0.44,  # g/day done
    "manganese": 0.004,  # g/day done
    "molybdenum": 0.000045,  # g/day
    "nickel": 0.001,  # g/day
    "phosphorus": 0.6,  # g/day
    "potassium": 3.5,  # g/day done
    "zinc": 0.017,  # g/day done
    "arsenic": 0.00001,  # g/day
    "mercury": 0.000002,  # g/day
    "selenium": 0.00004  # g/day done
}

unit_conversion = {
    "g": 1,        # 1 gram = 1 gram
    "kg": 1000,    # 1 kilogram = 1000 grams
    "mg": 0.001,   # 1 milligram = 0.001 grams
    "µg": 0.000001, # 1 microgram = 0.000001 grams
}

gluten_ingredients = ["wheat","flour","barley","rye","malt","farina","semolina","spelt","triticale","bulgur","couscous"]

lactose_ingredients = ["milk","cream","butter","yogurt","cheese","whey","curd","milk powder","milk solids","evaporated milk","condensed milk","paneer"]


serving_size = 200 #st.text_input("serving size")  # Serving size in grams or milliliters
unit = "g"#data["serving"]["unit"].lower()  # Get the unit (g or ml)

#____________________________ saturated_fats _______________________________________________________________________________________________________________________________
def get_saturated_fats():

    saturated_fats_low = 1.5 if unit == "g" else 0.75 #in gram
    saturated_fats_free = 0.1 #in gram

    fat = float(st.text_input("fats value : ",1))
    fat_unit = str(st.text_input("fats unit : ","g"))

    saturated_fats_unit = str(st.text_input("total_saturated_fats unit : ","g"))
    total_saturated_fats =  float(st.text_input("total_saturated_fats value : ",1))

    monounsaturated_fats_unit = str(st.text_input("total_monounsaturated_fats unit : ","g"))
    total_monounsaturated_fats = float(st.text_input("total_monounsaturated_fats value : ",1))

    polyunsaturated_fats_unit = str(st.text_input("total_polyunsaturated_fats unit : ","g"))
    total_polyunsaturated_fats = float(st.text_input("total_polyunsaturated_fats value : ",1))

    saturated_fats_in_grams = total_saturated_fats * unit_conversion.get(saturated_fats_unit, 1)

    # Calculate saturated fats per 100g
    saturated_fats_per_100g = (saturated_fats_in_grams / serving_size) * 100

    if saturated_fats_per_100g <= saturated_fats_free:
        st.write("Saturated Fats Free")
    elif saturated_fats_per_100g <= saturated_fats_low:
        st.write("low in Saturated Fats")
    else:
        # Calculate how much excess it is
        excess_saturated_fats = saturated_fats_per_100g - saturated_fats_low
        st.write(f"High in Saturated Fats: {excess_saturated_fats:.2f}g per 100g")

    

    total_saturated_fats = total_saturated_fats * unit_conversion.get(saturated_fats_unit, 1)
    total_monounsaturated_fats = total_monounsaturated_fats * unit_conversion.get(monounsaturated_fats_unit, 1)
    total_polyunsaturated_fats = total_polyunsaturated_fats * unit_conversion.get(polyunsaturated_fats_unit, 1)

    # Calculate total fatty acids
    total_fats = total_saturated_fats + total_monounsaturated_fats + total_polyunsaturated_fats

    # Total energy
    total_energy = float(st.text_input("energy value : ",1))

    # Energy from PUFA (polyunsaturated fats)
    energy_from_pufa = total_polyunsaturated_fats * 9  # 1g PUFA = 9 kcal

    # Calculate percentage of PUFA in total fatty acids
    pufa_percentage_in_fats = (total_polyunsaturated_fats / total_fats) * 100

    # Calculate percentage of energy from PUFA
    pufa_energy_percentage = (energy_from_pufa / total_energy) * 100

    # Check if the dish qualifies as "PUFA High"
    if pufa_percentage_in_fats >= 45 and pufa_energy_percentage > 20:
        st.write("High in PUFA")
    else:
    # If PUFA does not meet the high criteria, calculate how much it is short
      if pufa_percentage_in_fats < 45:
          pufa_fats_excess = 45 - pufa_percentage_in_fats
          st.write(f"PUFA is short by {pufa_fats_excess:.2f}% in total fatty acids")

      if pufa_energy_percentage <= 20:
          pufa_energy_excess = 20 - pufa_energy_percentage
          st.write(f"PUFA energy is short by {pufa_energy_excess:.2f}% of total energy")

# __________________________________ MUFA ___________________________________________________________________________________________________________________________________

    total_fatty_acids = total_saturated_fats + total_monounsaturated_fats + total_polyunsaturated_fats

    # Convert MUFA to kcal (1 g of fat = 9 kcal)
    mufa_energy = (total_monounsaturated_fats) * 9  # converting mg to g and multiplying by kcal/g

    # Calculate MUFA percentage and energy contribution
    mufa_percentage = (total_monounsaturated_fats / total_fatty_acids) * 100
    mufa_energy_contribution = (mufa_energy / total_energy) * 100

    if mufa_percentage >= 45 and mufa_energy_contribution > 20:
      st.write("High in MUFA")
    else:
      # If MUFA does not meet the high criteria, calculate the shortfall or how close it is
      if mufa_percentage < 45:
          mufa_percentage_shortfall = 45 - mufa_percentage
          st.write(f"MUFA is short by {mufa_percentage_shortfall:.2f}% in total fatty acids")
      else:
          mufa_percentage_excess = mufa_percentage - 45
          st.write(f"MUFA exceeds by {mufa_percentage_excess:.2f}% in total fatty acids")

      if mufa_energy_contribution <= 20:
          mufa_energy_shortfall = 20 - mufa_energy_contribution
          st.write(f"MUFA energy is short by {mufa_energy_shortfall:.2f}% of total energy")
      else:
          mufa_energy_excess = mufa_energy_contribution - 20
          st.write(f"MUFA energy exceeds by {mufa_energy_excess:.2f}% of total energy")

#__________________________________ Unsaturated Fat ___________________________________________________________________________________________________________________________

    # Energy from Unsaturated Fats (Monounsaturated + Polyunsaturated fats)
    energy_from_unsaturated_fats = (total_monounsaturated_fats + total_polyunsaturated_fats) * 9  # 1g unsaturated fats = 9 kcal

    # Calculate percentage of unsaturated fats in total fatty acids
    unsaturated_percentage_in_fats = ((total_monounsaturated_fats + total_polyunsaturated_fats) / total_fats) * 100

    # Calculate percentage of energy from unsaturated fats
    unsaturated_energy_percentage = (energy_from_unsaturated_fats / total_energy) * 100

    # Check if the dish qualifies as "Unsaturated Fat High"
    if unsaturated_percentage_in_fats >= 70 and unsaturated_energy_percentage > 20:
        st.write("High in Unsaturated Fat")
    else:
        # Detailed analysis for Unsaturated Fat shortfall or excess
        if unsaturated_percentage_in_fats < 70:
            unsaturated_percentage_shortfall = 70 - unsaturated_percentage_in_fats
            st.write(f"Unsaturated fats are short by {unsaturated_percentage_shortfall:.2f}% in total fatty acids")
        else:
            unsaturated_percentage_excess = unsaturated_percentage_in_fats - 70
            st.write(f"Unsaturated fats exceed by {unsaturated_percentage_excess:.2f}% in total fatty acids")

        if unsaturated_energy_percentage <= 20:
            unsaturated_energy_shortfall = 20 - unsaturated_energy_percentage
            st.write(f"Energy from unsaturated fats is short by {unsaturated_energy_shortfall:.2f}% of total energy")
        else:
            unsaturated_energy_excess = unsaturated_energy_percentage - 20
            st.write(f"Energy from unsaturated fats exceeds by {unsaturated_energy_excess:.2f}% of total energy")

#________________________________ Trans Fat ____________________________________________________________________________________________________________________________________

    
    fat = fat * unit_conversion.get(fat_unit, 1)

    # Calculate Trans Fat
    trans_fat = fat - total_fats

    trans_fat_per_100ml = trans_fat / serving_size * 100

    if trans_fat_per_100ml < 0.2:
      st.write("Trans Fat Free")
    else:
      trans_fat_excess = trans_fat_per_100ml - 0.2
      st.write(f"Trans fat exceeds the limit by {trans_fat_excess:.2f}g per 100ml")

get_saturated_fats()

#________________________________ macro_nutrients ______________________________________________________________________________________________________________________________
def get_macro_nutrients(data):

    # energy limits
    energy_low = 40 if unit == "g" else 20
    energy_free = 4 if unit == "ml" else 0

    # fats limits
    fats_low = 3 if unit == "g" else 1.5
    fats_free = 0.5

    # proteins limits
    rda_protein = rda_values["protein"]
    proteins_high = 0.2 * rda_protein if unit == "g" else 0.1 * rda_protein
    proteins_source = 0.1 * rda_protein if unit == "g" else 0.05 * rda_protein

    # fibre limits
    fibre_high = 6 if unit == "g" else 0
    fibre_source = 3 if unit == "g" else 0

    for nutrient in data["nutrients"].get("macro_nutrients", []):

        # Convert nutrient value to grams if needed
        nutrient_unit = nutrient.get("unit", "g").lower()
        nutrient_value_in_grams = nutrient["value"] * unit_conversion.get(nutrient_unit, 1)

        if nutrient["name"] == "energy":

            energy_per_100g = (nutrient["value"] / serving_size) * 100

            if energy_per_100g <= energy_free:
                st.write("Energy Free")
            elif energy_per_100g <= energy_low:
                st.write("Low in Energy")
            else:
                energy_excess = energy_per_100g - energy_low
                st.write(f"Energy exceeds the low limit by {energy_excess:.2f} kcal per 100g")

        if nutrient["name"] == "fats":
            fats_per_100g = (nutrient["value"] / serving_size) * 100
            if fats_per_100g <= fats_free:
                st.write("Fats Free")
            elif fats_per_100g <= fats_low:
                st.write("Low in Fats")
            else:
              fats_excess = fats_per_100g - fats_low
              st.write(f"Fats exceed the low limit by {fats_excess:.2f}g per 100g")

        if nutrient["name"] == "proteins":
            proteins_per_100g = (nutrient["value"] / serving_size) * 100
            if proteins_per_100g >= proteins_high:
                st.write("High in protein")
            elif proteins_per_100g >= proteins_source:
                st.write("Has protein")
            else:
                proteins_deficit = proteins_source - proteins_per_100g
                st.write(f"Proteins are below the source limit by {proteins_deficit:.2f}g per 100g")


        if nutrient["name"] == "fibers":
            fibers_per_100g = (nutrient["value"] / serving_size) * 100
            if fibers_per_100g >= fibre_high:
                st.write("High in Fibers")
            elif fibers_per_100g >= fibre_source:
                st.write("Has Fibers")
            else:
                fibers_deficit = fibre_source - fibers_per_100g
                st.write(f"Fibers are below the source limit by {fibers_deficit:.2f}g per 100g")

#______________________________ sodium _______________________________________________________________________________________________________________________________________
def get_sodium(data):

    # Sodium limits
    sodium_free = 0.0005
    sodium_very_low = 0.04
    sodium_low = 0.12

    for nutrient in data["nutrients"].get("minerals", []):

        if nutrient["name"] == "sodium":

            sodium_unit = nutrient.get("unit").lower()
            sodium = nutrient["value"] * unit_conversion.get(sodium_unit, 1)
            sodium_per_100g = ((sodium / serving_size) * 100)

            if sodium_per_100g <= sodium_free:
                st.write("Sodium Free")
            elif sodium_per_100g <= sodium_very_low:
                st.write("Very Low in Sodium")
            elif sodium_per_100g <= sodium_low:
                st.write("Low in Sodium")
            else:
                # Calculate how much sodium exceeds the low threshold if it's above
                sodium_excess = sodium_per_100g - sodium_low
                st.write(f"Sodium exceeds the low limit by {sodium_excess:.4f}g per 100g")

#_____________________________ Lactose ______________________________________________________________________________________________________________________________________
def get_lactose(data):

    for ing in data["ingredients"]:
        ingredient_name = ing["name"].lower()
        for lactose_item in lactose_ingredients:
            if lactose_item in ingredient_name:
                st.write("lactose Free")

#_____________________________ Gluten ________________________________________________________________________________________________________________________________________
def get_gluten(data):

    for ing in data["ingredients"]:
        ingredient_name = ing["name"].lower()
        for gluten_item in gluten_ingredients:
            if gluten_item in ingredient_name:
                st.write("Gluten Free")

#_______________________________ minerals, vitamins ___________________________________________________________________________________________________________________________
def get_minerals_vitamins(data):

    for category in ['water_soluble_vitamin', 'fat_soluble_vitamin', 'minerals']:
        for nutrient in data["nutrients"][category]:
            nutrient_name = nutrient["name"]
            nutrient_value = nutrient["value"]
            nutrient_unit = nutrient["unit"]

            if nutrient_name in rda_values:
                rda_value = rda_values[nutrient_name]


            nutrient_value = nutrient_value * unit_conversion.get(nutrient_unit.lower(), 1)

            if unit.lower() == "ml":
                if nutrient_value != 0:
                    percentage = (nutrient_value / rda_value) * 100
                    if percentage >= 7.5:
                        if percentage >= 15:
                            st.write(f"High in {nutrient_name}")
                        else:
                            st.write(f"Contains {nutrient_name}")
                else:
                    remaining_percentage = 7.5 - percentage
                    st.write(f"{nutrient_name} lack by: {remaining_percentage:.2f}% of RDA")

            elif unit.lower() == "g":
                if nutrient_value != 0:
                    percentage = (nutrient_value / rda_value) * 100
                    if percentage >= 15:
                        if percentage >= 30:
                            st.write(f"High in {nutrient_name}")
                        else:
                            st.write(f"Contains {nutrient_name}")
                    else:
                        remaining_percentage = 15 - percentage
                        st.write(f"{nutrient_name} lack by: {remaining_percentage:.2f}% of RDA")

