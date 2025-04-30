import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
} from "react-native";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useUser } from "@/contexts/userContext";
import axios from "axios";

const GenderAgeOccupationScreen = () => {
  const { userInfo, updateUserInfo } = useUser();

  const [gender, setGender] = useState("");
  const [age, setAge] = useState("");
  const [occupation, setOccupation] = useState("");
  const [physicalActivity, setPhysicalActivity] = useState("");

  const { username } = useLocalSearchParams(); // <-- get username
  const router = useRouter(); // <-- initialize router

  const handleNext = async () => {
    if (!gender || !age || !occupation || !physicalActivity) {
      alert("Please fill all fields!");
      return;
    }

    // Prepare data to send to backend
    const userData = {
      gender,
      age,
      occupation,
      physicalActivity,
    };

    try {
      // Send POST request using axios
      const response = await axios.post(
        "http://127.0.0.1:8000/api/recommendations/",
        userData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      // Check if the response is successful
      if (response.status === 200) {
        updateUserInfo(userData); // Store updated data in context
        // Navigate to the next page
        router.push({
          pathname: "/inputScreens/page2",
          params: {
            username,
            gender,
            age,
            occupation,
            physicalActivity,
          },
        });
      } else {
        alert("Failed to update data");
      }
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>Welcome, {username}</Text>

      <Text style={styles.label}>What is your gender?</Text>
      <View style={styles.radioContainer}>
        {["Male", "Female", "Prefer not to say"].map((option) => (
          <TouchableOpacity
            key={option}
            style={styles.radioButton}
            onPress={() => setGender(option)}
          >
            <View
              style={[styles.circle, gender === option && styles.selected]}
            />
            <Text style={styles.radioText}>{option}</Text>
          </TouchableOpacity>
        ))}
      </View>

      <Text style={styles.label}>Please enter your age</Text>
      <TextInput
        style={styles.input}
        placeholder="age"
        value={age}
        onChangeText={setAge}
        keyboardType="numeric"
      />

      <Text style={styles.label}>Occupation</Text>
      <TextInput
        style={styles.input}
        placeholder="occupation"
        value={occupation}
        onChangeText={setOccupation}
      />

      <Text style={styles.label}>Physical Activity Level</Text>
      <TextInput
        style={styles.input}
        placeholder="physical activity level"
        value={physicalActivity}
        onChangeText={setPhysicalActivity}
      />

      {/* Next Button */}
      <TouchableOpacity style={styles.nextButton} onPress={handleNext}>
        <Text style={styles.nextButtonText}>Next</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#fff",
    justifyContent: "center",
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
  },
  label: {
    marginTop: 20,
    fontSize: 16,
    fontWeight: "500",
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 12,
    borderRadius: 8,
    marginTop: 8,
  },
  radioContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
    marginTop: 10,
  },
  radioButton: {
    flexDirection: "row",
    alignItems: "center",
    marginRight: 20,
    marginTop: 10,
  },
  circle: {
    width: 16,
    height: 16,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: "#87ceeb",
    marginRight: 8,
  },
  selected: {
    backgroundColor: "#87ceeb",
  },
  radioText: {
    fontSize: 16,
  },
  nextButtonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  nextButton: {
    backgroundColor: "#3A7CA5",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 20,
  },
});

export default GenderAgeOccupationScreen;
