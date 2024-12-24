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


serving_size = 200
unit = "g"

st.title("Nutrition Analysis")

serving_size = float(st.number_input("Serving size in gram:",100))
unit = st.selectbox("Select unit for Serving size:", options=["g","ml"])

import json
# Function Definitions
def convert_to_grams(value, nutrient_unit):
    """Converts nutrient value to grams based on the unit."""
    return (value * unit_conversion.get(nutrient_unit.lower(), 1) / serving_size) * 100

def calculate_rda_percentage(value, rda_value):
    """Calculates percentage of RDA based on value and recommended daily allowance."""
    return (value / rda_value) * 100

def process_nutrient(nutrient_name, value, nutrient_unit):
    """Processes nutrient and calculates its RDA percentage."""
    if nutrient_name not in rda_values:
        return f"RDA for {nutrient_name} not defined."

    rda_value = rda_values[nutrient_name]
    converted_value = convert_to_grams(value, nutrient_unit)
    percentage = calculate_rda_percentage(converted_value, rda_value)

    
    if unit == "g":
      if percentage >= 15:
          if percentage >= 30:
              return f"High in {nutrient_name} ({percentage:.2f}% of RDA)"
          return f"Contains {nutrient_name} ({percentage:.2f}% of RDA)"
      else:
          return f"Lacks {nutrient_name} by {15 - percentage:.2f}% of RDA"
    else:
      if percentage >= 7.5:
          if percentage >= 15:
              return f"High in {nutrient_name} ({percentage:.2f}% of RDA)"
          return f"Contains {nutrient_name} ({percentage:.2f}% of RDA)"
      else:
          return f"Lacks {nutrient_name} by {15 - percentage:.2f}% of RDA"




results = []
for nutrient_name in rda_values.keys():
    st.write(f"#### {nutrient_name.title()}")
    st.write(f"##### Source : The food provides at least {"{:.6f}".format(rda_values[nutrient_name]*0.15)}g per 100g for solids or {"{:.6f}".format(rda_values[nutrient_name]*0.075)}g of RDA of the vitamin/mineral per 100 ml for liquids ")
    st.write(f"##### High : The food provides at least {"{:.6f}".format(rda_values[nutrient_name]*0.30)}g of RDA per 100 g for solids or {"{:.6f}".format(rda_values[nutrient_name]*0.15)}g per 100 ml for liquids")
    nutrient_value = st.number_input(f"Enter value for {nutrient_name}:", min_value=0.0, step=1.00)
    nutrient_unit = st.selectbox(f"Select unit for {nutrient_name}:", options=["g", "mg", "µg", "kg"], key=f"{nutrient_name}_unit")

    if st.button(f"Process {nutrient_name}"):
        result = process_nutrient(nutrient_name, nutrient_value, nutrient_unit)
        st.success(result)
