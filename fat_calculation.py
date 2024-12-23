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


st.title("Fats Analysis")

serving_size = 200 #st.text_input("serving size")  # Serving size in grams or milliliters
unit = "g"#data["serving"]["unit"].lower()  # Get the unit (g or ml)

#____________________________ saturated_fats _______________________________________________________________________________________________________________________________
def get_saturated_fats():

    serving_size = float(st.number_input("Serving size in gram:",100))
    unit = st.selectbox("Select unit for Serving size:", options=["g","ml"])

    saturated_fats_low = 1.5 if unit == "g" else 0.75 #in gram
    saturated_fats_free = 0.1 #in gram

    
    # Total energy
    total_energy = float(st.text_input("energy value : ",1))

    fat = float(st.text_input("fats value : ",1))
    fat_unit = st.selectbox("fats unit :", options=["g", "mg", "kg"])

    saturated_fats_unit = st.selectbox("total_saturated_fats unit :", options=["g", "mg", "kg"])
    total_saturated_fats =  float(st.text_input("total_saturated_fats value : ",1))

    monounsaturated_fats_unit = st.selectbox("total_monounsaturated_fats unit :", options=["g", "mg", "kg"])
    total_monounsaturated_fats = float(st.text_input("total_monounsaturated_fats value : ",1))

    polyunsaturated_fats_unit = st.selectbox("total_polyunsaturated_fats unit :", options=["g", "mg", "kg"])
    total_polyunsaturated_fats = float(st.text_input("total_polyunsaturated_fats value : ",1))

    saturated_fats_in_grams = total_saturated_fats * unit_conversion.get(saturated_fats_unit, 1)

    # Calculate saturated fats per 100g
    saturated_fats_per_100g = (saturated_fats_in_grams / serving_size) * 100

    st.write("### saturated fats")
    st.write("##### Low : Not more than    1.5 g per 100 g    and   0.75 g per 100 ml")
    st.write("##### Free : Not more than    4 kcal per 100 ml")

    if saturated_fats_per_100g <= saturated_fats_free:
        st.write("Saturated Fats Free")
    elif saturated_fats_per_100g <= saturated_fats_low:
        st.write("low in Saturated Fats")
    else:
        # Calculate how much excess it is
        excess_saturated_fats = saturated_fats_per_100g - saturated_fats_low
        st.write(f"High in Saturated Fats: {excess_saturated_fats:.2f}g per 100{unit}")

    

    total_saturated_fats = total_saturated_fats * unit_conversion.get(saturated_fats_unit, 1)
    total_monounsaturated_fats = total_monounsaturated_fats * unit_conversion.get(monounsaturated_fats_unit, 1)
    total_polyunsaturated_fats = total_polyunsaturated_fats * unit_conversion.get(polyunsaturated_fats_unit, 1)

    # Calculate total fatty acids
    total_fats = total_saturated_fats + total_monounsaturated_fats + total_polyunsaturated_fats

    

    # Energy from PUFA (polyunsaturated fats)
    energy_from_pufa = total_polyunsaturated_fats * 9  # 1g PUFA = 9 kcal

    # Calculate percentage of PUFA in total fatty acids
    pufa_percentage_in_fats = (total_polyunsaturated_fats / total_fats) * 100

    # Calculate percentage of energy from PUFA
    pufa_energy_percentage = (energy_from_pufa / total_energy) * 100

    st.write("### PUFA")
    st.write("##### High : Shall only be made where at least 45% of the total fatty acids present in the product are derived from poly unsaturated fat and under the condition that polyunsaturated fat provides more than 20% of energy of the product")

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

    st.write("### MUFA")
    st.write("##### High : Shall only be made where at least 45% of the total fatty acids present in the product are derived from mono unsaturated fat and under the condition that monounsaturated fat provides more than 20% of energy of the product ")

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

    st.write("### Unsaturated Fat")
    st.write("##### High : At least 70% of the fatty acids present in the product are derive from unsaturated fat under the condition that unsaturated fat provides more than 20% of energy of the product")

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

    st.write("### Trans Fat")
    st.write("##### Free : contains less than 0.2g trans fat per 100 g or 100ml")

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
