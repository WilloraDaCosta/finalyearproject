
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import { useLocalSearchParams, useRouter  } from 'expo-router'; // <-- to get params
import { useUser } from '@/contexts/UserContext';


const SleepScreen = () => {

  const { userInfo, updateUserInfo } = useUser();

  const [sleepHours, setSleepHours] = useState<number>(0 );
  const [qualityOfSleep, setQualityOfSleep] = useState<number>( 0);
  const [stressLevel, setStressLevel ] = useState<number>(0 );
 
  const { username } = useLocalSearchParams(); // <-- get username
  const router = useRouter(); // <-- initialize router

  const handleNext = () => {
    if (!sleepHours || !qualityOfSleep || !stressLevel) {
      alert('Please fill all fields!');
      return;
    }

    updateUserInfo({ sleepHours, qualityOfSleep, stressLevel });

    
  

    router.push('/inputScreens/page3');
 
  };

  
  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>Sleep is Important!</Text>

      <Text style={styles.label}>On average, how many hours do you sleep per night?</Text>

    <TextInput
        style={styles.input}
        placeholder="sleep hours"
        value={sleepHours.toString()}
        onChangeText= {(text) => setSleepHours(Number(text))}
        keyboardType="numeric"
      />

      <Text style={styles.label}>What would you rate your quality of sleep?</Text>
      <TextInput
        style={styles.input}
        placeholder="quality of sleep"
        value= {qualityOfSleep.toString()}
        onChangeText= {(text) => setQualityOfSleep(Number(text))}
        keyboardType="numeric"
      />

      <Text style={styles.label}>Define Your stress level</Text>
      <TextInput
        style={styles.input}
        placeholder="stress level"
        value= {stressLevel.toString()}
        onChangeText= {(text) => setStressLevel(Number(text))}
        keyboardType="numeric"
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
  nextButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  nextButton: {
    backgroundColor: '#3A7CA5',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
  },
});

export default SleepScreen;
