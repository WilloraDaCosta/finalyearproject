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
import AsyncStorage from "@react-native-async-storage/async-storage";

const GenderAgeOccupationScreen = () => {
  const { userInfo, updateUserInfo } = useUser();

  const [gender, setGender] = useState("");
  const [age, setAge] = useState("");
  const [occupation, setOccupation] = useState("");
  const [physicalActivity, setPhysicalActivity] = useState("");

  const router = useRouter(); // <-- initialize router

  const handleNext = async () => {
    if (!gender || !age || !occupation || !physicalActivity) {
      alert("Please fill all fields!");
      return;
    }

    try {
      const token = await AsyncStorage.getItem("authToken");
      const username = await AsyncStorage.getItem("username");

      if (!token || !username) {
        alert("User not authenticated, please log in again.");
        return;
      }

      // Prepare data to send to backend
      const userData = {
        username,
        gender,
        age,
        occupation,
        physicalActivity,
      };

      console.log("Token being used:", token);
      console.log("Sending userData:", userData);

      const response = await axios.post(
        "http://192.168.1.36:8000/api/page1/",
        userData,
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        }
      );

      if (response.status === 200) {
        updateUserInfo(userData);
        router.push({
          pathname: "/inputScreens/page2",
          params: userData,
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
