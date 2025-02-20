import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from django.conf import settings

# Load dataset
data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/food.csv"))

# Extract columns
food_items = data['Food_items']
breakfast_data = data['Breakfast'].to_numpy()
lunch_data = data['Lunch'].to_numpy()
dinner_data = data['Dinner'].to_numpy()

def extract_food_by_meal(meal_data):
    """Extract food items and their indices based on meal data (breakfast, lunch, dinner)."""
    food_separated, food_separated_id = [], []
    for i in range(len(meal_data)):
        if meal_data[i] == 1:
            food_separated.append(food_items[i])
            food_separated_id.append(i)
    return food_separated, food_separated_id

def retrieve_meal_data(food_ids):
    """Retrieve meal data using the extracted food IDs."""
    meal_data = data.iloc[food_ids].T
    relevant_columns = [0] + list(np.arange(5, 15))  # Selecting relevant features
    return meal_data.iloc[relevant_columns].T.to_numpy()

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

def cluster_food_data(data_array):
    """Perform KMeans clustering on food data."""
    if len(data_array) <= 1:
        return np.zeros(len(data_array))  # Avoid issues with empty clusters
    kmeans = KMeans(n_clusters=3, random_state=0).fit(data_array[:, 1:])
    return kmeans.labels_

def process_food_recommendation(age, weight, height, category="weight_loss"):
    """Generalized function for food recommendations based on goal."""
    
    # Extract meal data
    breakfast_food, breakfast_ids = extract_food_by_meal(breakfast_data)
    lunch_food, lunch_ids = extract_food_by_meal(lunch_data)
    dinner_food, dinner_ids = extract_food_by_meal(dinner_data)

    # Retrieve meal data for clustering
    breakfast_meal_data = retrieve_meal_data(breakfast_ids)
    lunch_meal_data = retrieve_meal_data(lunch_ids)
    dinner_meal_data = retrieve_meal_data(dinner_ids)

    # Calculate BMI and age classification
    bmi, bmi_info, bmi_class = calculate_bmi(weight, height)
    age_class = determine_age_class(age)
    
    # Clustering food items
    breakfast_labels = cluster_food_data(breakfast_meal_data)
    lunch_labels = cluster_food_data(lunch_meal_data)
    dinner_labels = cluster_food_data(dinner_meal_data)

    # Load nutrition dataset
    nutrition_data = pd.read_csv(os.path.join(settings.BASE_DIR, "static/data/nutrition_distriution.csv")).T

    category_indices = {
        "weight_loss": [1, 2, 7, 8],
        "weight_gain": [0, 1, 2, 3, 4, 7, 9, 10],
        "healthy": [1, 2, 3, 4, 6, 7, 9]
    }
    
    selected_category = nutrition_data.iloc[category_indices[category]].T.to_numpy()
    selected_category = selected_category[1:, :]

    feature_matrix = np.zeros((len(selected_category) * 5, selected_category.shape[1] + 2), dtype=np.float32)
    labels = []
    
    index = 0
    for zz in range(5):
        for jj in range(len(selected_category)):
            row = list(selected_category[jj]) + [bmi_class, age_class]
            feature_matrix[index] = np.array(row)
            labels.append(breakfast_labels[jj] if category == "weight_loss" else 
                          lunch_labels[jj] if category == "weight_gain" else 
                          dinner_labels[jj])
            index += 1

    # Prepare test data
    X_test = np.zeros((len(selected_category), feature_matrix.shape[1]), dtype=np.float32)
    ti = (bmi_class + age_class) / 2

    for jj in range(len(selected_category)):
        row = list(selected_category[jj]) + [age_class, bmi_class]
        X_test[jj] = np.array(row) * ti

    # Train RandomForest Model
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(feature_matrix, labels)
    
    # Predict food recommendations
    y_pred = clf.predict(X_test)
    
    recommended_foods = [food_items[ii] for ii in range(len(y_pred)) if y_pred[ii] == 2]
    
    return recommended_foods + [bmi, bmi_info]

# Wrapper functions for different goals
def Weight_Loss(age, weight, height):
    return process_food_recommendation(age, weight, height, category="weight_loss")

def Weight_Gain(age, weight, height):
    return process_food_recommendation(age, weight, height, category="weight_gain")

def Healthy(age, weight, height):
    return process_food_recommendation(age, weight, height, category="healthy")
