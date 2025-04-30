# import os
# import pandas as pd
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.ensemble import RandomForestClassifier
# from django.conf import settings

# # Load updated dataset with images
# data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/newfood.csv"))

# # Load nutrition dataset
# nutrition_data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/nutrition_distriution.csv")).T

# # Define category indices for weight loss, gain, and healthy eating
# category_indices = {
#     "weight_loss": [1, 2, 7, 8],
#     "weight_gain": [0, 1, 2, 3, 4, 7, 9, 10],
#     "healthy": [1, 2, 3, 4, 6, 7, 9]
# }

# # Extract columns
# food_items = data['Food_items']
# breakfast_data = data['Breakfast'].to_numpy()
# lunch_data = data['Lunch'].to_numpy()
# dinner_data = data['Dinner'].to_numpy()

# def get_food_details(food_name):
#     """Retrieve nutrient values and image URL for a given food item."""
#     food_info = data[data["Food_items"] == food_name].iloc[0]
#     return {
#         "name": food_info["Food_items"],
#         "calories": food_info["Calories"],
#         "protein": food_info["Proteins"],
#         "fat": food_info["Fats"],
#         "carbs": food_info["Carbohydrates"],
#         "image_url": f"http://127.0.0.1:8000{food_info['URL']}"  # Full path for frontend
#     }

# def extract_food_by_meal(meal_data):
#     """Extract food items and their indices based on meal data (breakfast, lunch, dinner)."""
#     food_separated, food_separated_id = [], []
#     for i in range(len(meal_data)):
#         if meal_data[i] == 1:
#             food_separated.append(food_items[i])
#             food_separated_id.append(i)
#     return food_separated, food_separated_id

# def calculate_bmi(weight, height):
#     """Calculate BMI and determine category."""
#     bmi = weight / ((height / 100) ** 2)
#     if bmi < 16:
#         return bmi, "Severely Underweight", 4
#     elif bmi < 18.5:
#         return bmi, "Underweight", 3
#     elif bmi < 25:
#         return bmi, "Healthy", 2
#     elif bmi < 30:
#         return bmi, "Overweight", 1
#     return bmi, "Severely Overweight", 0

# def determine_age_class(age):
#     """Determine age classification."""
#     for lp in range(0, 80, 20):
#         if age in np.arange(lp, lp + 20):
#             return round(lp / 20)
#     return 0

# def process_food_recommendation(age, weight, height, category="weight_loss"):
#     """Returns categorized food recommendations using machine learning."""

#     # Extract recommended food names
#     breakfast_food, breakfast_ids = extract_food_by_meal(breakfast_data)
#     lunch_food, lunch_ids = extract_food_by_meal(lunch_data)
#     dinner_food, dinner_ids = extract_food_by_meal(dinner_data)

#     # Calculate BMI and age classification
#     bmi, bmi_info, bmi_class = calculate_bmi(weight, height)
#     age_class = determine_age_class(age)

#     # Select nutrition category based on user goal
#     selected_category = nutrition_data.iloc[category_indices[category]].T.to_numpy()
#     selected_category = selected_category[1:, :]

#     feature_matrix = np.zeros((len(selected_category) * 5, selected_category.shape[1] + 2), dtype=np.float32)
#     labels = []

#     index = 0
#     for zz in range(5):
#         for jj in range(len(selected_category)):
#             row = list(selected_category[jj]) + [bmi_class, age_class]
#             feature_matrix[index] = np.array(row)
#             labels.append(jj % 3)  # Assigning labels randomly (for now)
#             index += 1

#     # Prepare test data
#     X_test = np.zeros((len(selected_category), feature_matrix.shape[1]), dtype=np.float32)
#     ti = (bmi_class + age_class) / 2

#     for jj in range(len(selected_category)):
#         row = list(selected_category[jj]) + [age_class, bmi_class]
#         X_test[jj] = np.array(row) * ti

#     # Train RandomForest Model
#     clf = RandomForestClassifier(n_estimators=100)
#     clf.fit(feature_matrix, labels)

#     # Predict food recommendations
#     y_pred = clf.predict(X_test)

#     # Select recommended food items based on prediction
#     recommended_breakfast = [get_food_details(breakfast_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]
#     recommended_lunch = [get_food_details(lunch_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]
#     recommended_dinner = [get_food_details(dinner_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]

#     return {
#         "breakfast": recommended_breakfast,
#         "lunch": recommended_lunch,
#         "dinner": recommended_dinner,
#         "bmi": bmi,
#         "bmi_info": bmi_info
#     }

# # Wrapper functions for different goals
# def Weight_Loss(age, weight, height):
#     return process_food_recommendation(age, weight, height, category="weight_loss")

# def Weight_Gain(age, weight, height):
#     return process_food_recommendation(age, weight, height, category="weight_gain")

# def Healthy(age, weight, height):
#     return process_food_recommendation(age, weight, height, category="healthy")

import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.conf import settings

# Load updated dataset with images
data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/newfood.csv"))

# Load nutrition dataset
nutrition_data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/nutrition_distriution.csv")).T

# Define category indices for weight loss, gain, and healthy eating
category_indices = {
    "weight_loss": [1, 2, 7, 8],
    "weight_gain": [0, 1, 2, 3, 4, 7, 9, 10],
    "healthy": [1, 2, 3, 4, 6, 7, 9]
}

# Extract columns
food_items = data['Food_items']
breakfast_data = data['Breakfast'].to_numpy()
lunch_data = data['Lunch'].to_numpy()
dinner_data = data['Dinner'].to_numpy()

def get_food_details(food_name):
    """Retrieve nutrient values and image URL for a given food item."""
    food_info = data[data["Food_items"] == food_name].iloc[0]
    return {
        "name": food_info["Food_items"],
        "calories": food_info["Calories"],
        "protein": food_info["Proteins"],
        "fat": food_info["Fats"],
        "carbs": food_info["Carbohydrates"],
        "image_url": f"http://127.0.0.1:8000{food_info['URL']}"  # Full path for frontend
    }

def extract_food_by_meal(meal_data):
    """Extract food items and their indices based on meal data (breakfast, lunch, dinner)."""
    food_separated, food_separated_id = [], []
    for i in range(len(meal_data)):
        if meal_data[i] == 1:
            food_separated.append(food_items[i])
            food_separated_id.append(i)
    return food_separated, food_separated_id

def calculate_bmi(weight, height):
    """Calculate BMI and determine category."""
    bmi = weight / ((height / 100) ** 2)
    if bmi < 16:
        return bmi, "Severely Underweight", 4
    elif bmi < 18.5:
        return bmi, "Underweight", 3
    elif bmi < 25:
        return bmi, "Healthy", 2
    elif bmi < 30:
        return bmi, "Overweight", 1
    return bmi, "Severely Overweight", 0

def determine_age_class(age):
    """Determine age classification."""
    for lp in range(0, 80, 20):
        if age in np.arange(lp, lp + 20):
            return round(lp / 20)
    return 0

def calculate_model_accuracy(clf, X, y):
    """Calculate and return accuracy of the RandomForest model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def process_food_recommendation(age, weight, height, category="weight_loss"):
    """Returns categorized food recommendations using machine learning."""

    # Extract recommended food names
    breakfast_food, breakfast_ids = extract_food_by_meal(breakfast_data)
    lunch_food, lunch_ids = extract_food_by_meal(lunch_data)
    dinner_food, dinner_ids = extract_food_by_meal(dinner_data)

    # Calculate BMI and age classification
    bmi, bmi_info, bmi_class = calculate_bmi(weight, height)
    age_class = determine_age_class(age)

    # Select nutrition category based on user goal
    selected_category = nutrition_data.iloc[category_indices[category]].T.to_numpy()
    selected_category = selected_category[1:, :]

    feature_matrix = np.zeros((len(selected_category) * 5, selected_category.shape[1] + 2), dtype=np.float32)
    labels = []

    index = 0
    for zz in range(5):
        for jj in range(len(selected_category)):
            row = list(selected_category[jj]) + [bmi_class, age_class]
            feature_matrix[index] = np.array(row)
            labels.append(jj % 3)  # Assigning labels randomly (for now)
            index += 1

    # Prepare test data
    X_test = np.zeros((len(selected_category), feature_matrix.shape[1]), dtype=np.float32)
    ti = (bmi_class + age_class) / 2

    for jj in range(len(selected_category)):
        row = list(selected_category[jj]) + [age_class, bmi_class]
        X_test[jj] = np.array(row) * ti

    # Train RandomForest Model
    clf = RandomForestClassifier(n_estimators=100)
    accuracy = calculate_model_accuracy(clf, feature_matrix, labels)

    # Predict food recommendations
    y_pred = clf.predict(X_test)

    # Select recommended food items based on prediction
    recommended_breakfast = [get_food_details(breakfast_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]
    recommended_lunch = [get_food_details(lunch_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]
    recommended_dinner = [get_food_details(dinner_food[ii]) for ii in range(len(y_pred)) if y_pred[ii] == 2]

    return {
        "breakfast": recommended_breakfast,
        "lunch": recommended_lunch,
        "dinner": recommended_dinner,
        "bmi": bmi,
        "bmi_info": bmi_info,
        "model_accuracy": accuracy
    }

# Wrapper functions for different goals
def Weight_Loss(age, weight, height):
    return process_food_recommendation(age, weight, height, category="weight_loss")

def Weight_Gain(age, weight, height):
    return process_food_recommendation(age, weight, height, category="weight_gain")

def Healthy(age, weight, height):
    return process_food_recommendation(age, weight, height, category="healthy")
