
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const GenderAgeOccupationScreen = () => {
  const [gender, setGender] = useState('');
  const [age, setAge] = useState('');
  const [occupation, setOccupation] = useState('');
  const [physicalActivity, setPhysicalActivity] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>Welcome, </Text>

      <Text style={styles.label}>What is your gender?</Text>

      <View style={styles.radioContainer}>
        {['Male', 'Female', 'Prefer not to say'].map((option) => (
          <TouchableOpacity 
            key={option} 
            style={styles.radioButton}
            onPress={() => setGender(option)}
          >
            <View style={[styles.circle, gender === option && styles.selected]} />
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

    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
    justifyContent: 'center',
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  label: {
    marginTop: 20,
    fontSize: 16,
    fontWeight: '500',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 12,
    borderRadius: 8,
    marginTop: 8,
  },
  radioContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: 10,
  },
  radioButton: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 20,
    marginTop: 10,
  },
  circle: {
    width: 16,
    height: 16,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: '#87ceeb',
    marginRight: 8,
  },
  selected: {
    backgroundColor: '#87ceeb',
  },
  radioText: {
    fontSize: 16,
  },
});

export default GenderAgeOccupationScreen;
