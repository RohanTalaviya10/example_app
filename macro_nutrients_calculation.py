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


serving_size = 100
unit = "g"

import streamlit as st

unit_conversion = {
    "g": 1,
    "kg": 1000,
    "mg": 0.001,
    "µg": 0.000001,
}
import streamlit as st

# Define constants
rda_values = {
    "fiber": 40,  # g/day
    "protein": 50,  # g/day
}

unit_conversion = {
    "g": 1,
    "kg": 1000,
    "mg": 0.001,
    "µg": 0.000001,
}

# Streamlit-based Macro Nutrient Analysis
def get_macro_nutrients():
    st.title("Macro-Nutrient Analysis")


    serving_size = float(st.number_input("Serving size in gram:",100))
    unit = st.selectbox("Select unit for Serving size:", options=["g","ml"])
    # Energy limits
    energy_low = 40 if unit == "g" else 20
    energy_free = 0 if unit == "g" else 4

    # Fats limits
    fats_low = 3 if unit == "g" else 1.5
    fats_free = 0.5

    # Protein limits
    rda_protein = rda_values["protein"]
    proteins_high = 0.2 * rda_protein if unit == "g" else 0.1 * rda_protein
    proteins_source = 0.1 * rda_protein if unit == "g" else 0.05 * rda_protein

    # Fiber limits
    fibre_high = 6 if unit == "g" else 0
    fibre_source = 3 if unit == "g" else 0

    # Collect user inputs and show results dynamically
    st.write("### Input Values for Macro Nutrients")
    

    # Energy Input
    st.write("#### Energy")
    st.write("##### Low : Not more than   40 kcal per 100 g   and   20 kcal per 100 ml")
    st.write("##### Free : Not more than    4 kcal per 100 ml")
    energy_value = st.number_input("Enter value for Energy:", min_value=0.0, step=1.00, key="energy_value")
    energy_unit = st.selectbox("Select unit for Energy:", options=["kcal"], key="energy_unit")
    energy_per_100g = (energy_value / serving_size) * 100
    if energy_per_100g <= energy_free:
      st.write("Result: Energy Free")
    elif energy_per_100g <= energy_low:
      st.write("Result: Low in Energy")
    else:
        excess_energy = energy_per_100g - energy_low
        st.write(f"Result: Energy exceeds the low limit by {excess_energy:.2f} kcal per 100{unit}")

    # Fats Input
    st.write("#### Fats")
    st.write("##### Low : Not more than   3 g of fat per 100 g   and   1.5 g of fat per 100ml")
    st.write("##### Free : Not more than    0.5 g of fat per 100 g or 100 ml")
    fats_value = st.number_input("Enter value for Fats:", min_value=0.0, step=1.00, key="fats_value")
    fats_unit = st.selectbox("Select unit for Fats:", options=["g", "mg", "kg"], key="fats_unit")
    
    fats_per_100g = (fats_value * unit_conversion[fats_unit] / serving_size) * 100
    if fats_per_100g <= fats_free:
        st.write("Result: Fats Free")
    elif fats_per_100g <= fats_low:
        st.write("Result: Low in Fats")
    else:
        excess_fats = fats_per_100g - fats_low
        st.write(f"Result: Fats exceed the low limit by {excess_fats:.2f}g per 100{unit}")

    # Proteins Input
    st.write("#### Proteins")
    st.write(f"##### Source : More than   {proteins_source}g of per 100 g or ml (10% for solid and 5% for liquid of RDA(50g/day))")
    st.write(f"##### High : More than    {proteins_high}g of per 100 g or ml (20% for solid and 10% for liquid of RDA(50g/day))")
    proteins_value = st.number_input("Enter value for Proteins:", min_value=0.0, step=1.00, key="proteins_value")
    proteins_unit = st.selectbox("Select unit for Proteins:", options=["g", "mg", "kg"], key="proteins_unit")
    
    proteins_per_100g = (proteins_value * unit_conversion[proteins_unit] / serving_size) * 100
    if proteins_per_100g >= proteins_high:
        st.write("Result: High in Protein")
    elif proteins_per_100g >= proteins_source:
        st.write("Result: Contains Protein")
    else:
        deficit_protein = proteins_source - proteins_per_100g
        st.write(f"Result: Proteins are below the source limit by {deficit_protein:.2f}g per 100{unit}")

    # Fibers Input
    st.write("#### Fibers")
    st.write("##### Source : Contains at least    3 g of Fibers per 100 g")
    st.write("##### High : Contains at least     6 g of Fibers per 100 g")
    fibers_value = st.number_input("Enter value for Fibers:", min_value=0.0, step=1.00, key="fibers_value")
    fibers_unit = st.selectbox("Select unit for Fibers:", options=["g", "mg", "kg"], key="fibers_unit")
    
    fibers_per_100g = (fibers_value * unit_conversion[fibers_unit] / serving_size) * 100
    if fibers_per_100g >= fibre_high:
        st.write("Result: High in Fibers")
    elif fibers_per_100g >= fibre_source:
        st.write("Result: Contains Fibers")
    else:
        deficit_fiber = fibre_source - fibers_per_100g
        st.write(f"Result: Fibers are below the source limit by {deficit_fiber:.2f}g per 100{unit}")

# Call the function to display the Streamlit UI
get_macro_nutrients()

