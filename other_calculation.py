import streamlit as st
import json

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

#__________________________________ Cholesterol _______________________________________________________________________________________________________________________________
def get_cholesterol():

    cholesterol_low = 0.02 if unit == "g" else 0.01 # in gram
    cholesterol_free = 0.005 # in gram
    saturated_fats_cholesterol = 1.5 if unit == "g" else 0.75 # in gram

    cholesterol_unit = str(st.text_input("cholesterol unit : ","g"))
    cholesterol = float(st.text_input("cholesterol value : ",1))
    cholesterol = cholesterol * unit_conversion.get(cholesterol_unit, 1)

    Cholesterol_per_100g = ( cholesterol / serving_size) * 100

    if Cholesterol_per_100g <= cholesterol_free and saturated_fats_per_100g <= saturated_fats_cholesterol:
      st.write("Free Cholesterol")
    elif Cholesterol_per_100g <= cholesterol_low and saturated_fats_per_100g <= saturated_fats_cholesterol:
      st.write("low in Cholesterol")
    else:
      cholesterol_excess = Cholesterol_per_100g - cholesterol_low
      st.write(f"Cholesterol exceeds the low limit by {cholesterol_excess:.2f}mg per 100g or 100ml")

get_cholesterol()

#________________________________ Sugar _______________________________________________________________________________________________________________________________________
def get_sugar():

    total_sugars = float(st.text_input("total_free_sugars value : ",1))
    sugar_unit = str(st.text_input("total_free_sugars unit : ","g"))
    suger_free = 0.5
    suger_low = 5 if unit == "g" else 2.5
    total_sugars = total_sugars * unit_conversion.get(sugar_unit, 1)


    if unit == 'ml':
        # Liquid: Check if the sugars are <= 2.5g per 100ml
        sugars_per_100ml = total_sugars / serving_size * 100
        if sugars_per_100ml <= suger_free:
            st.write("Sugars Free")
        elif sugars_per_100ml <= suger_low:
            st.write("Low in Sugars")
        else:
            sugars_excess = sugars_per_100ml - 2.5
            st.write(f"Sugars exceed the low limit by {sugars_excess:.2f}g per 100ml")

    elif unit == 'g':
        # Solid: Check if the sugars are <= 5g per 100g
        sugars_per_100g = total_sugars / serving_size * 100
        if sugars_per_100g <= suger_free:
            st.write("Sugars Free")
        elif sugars_per_100g <= suger_low:
            st.write("Low in Sugars")
        else:
            sugars_excess = sugars_per_100g - 5
            st.write(f"Sugars exceed the low limit by {sugars_excess:.2f}g per 100g")

get_sugar()

#______________________________ sodium _______________________________________________________________________________________________________________________________________
def get_sodium():

    # Sodium limits
    sodium_free = 0.0005
    sodium_very_low = 0.04
    sodium_low = 0.12

    sodium_unit = str(st.text_input("sodium unit : ","g"))
    sodium = float(st.text_input("sodium value : ",1)) * unit_conversion.get(sodium_unit, 1)
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

get_sodium()
