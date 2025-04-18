import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  Alert,
  Image,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router'; //  Import router

const Login = () => {
  const [emailOrUsername, setEmailOrUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter(); //  Initialize router


  const handleLogin = () => {
    if (!emailOrUsername || !password) {
      Alert.alert('Error', 'Please enter your credentials.');
      return;
    }

    // You would typically verify credentials here
    console.log('Logging in with:', { emailOrUsername, password });
    Alert.alert('Success', 'Logged in successfully!');
    
    // Clear inputs
    setEmailOrUsername('');
    setPassword('');
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Image source={require('@/assets/images/login/top.png')} style={styles.up_image} />
      <Text style={styles.heading}>LOGIN</Text>

      <TextInput
        style={styles.input}
        placeholder="Email or Username"
        value={emailOrUsername}
        onChangeText={setEmailOrUsername}
        autoCapitalize="none"
        keyboardType="email-address"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />

      <TouchableOpacity style={styles.buttonContainer} onPress={handleLogin}>
        <LinearGradient colors={['#5A9BD5', '#6BAED6']} style={styles.button}>
          <Text style={styles.buttonText}>Log in</Text>
        </LinearGradient>
      </TouchableOpacity>

      <Text style={styles.footerText}>
        Don't have an account?{' '}
        <Text style={styles.loginText}
         onPress={() => router.push('/auth/signUp')}
         >SIGN UP</Text>
      </Text>

      <Image source={require('@/assets/images/login/bottom.png')} style={styles.bottom_image} />

    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    padding: 20,
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  heading: {
    fontSize: 26,
    color: '#3A7CA5',
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '100%',
    backgroundColor: '#f9f9f9',
    borderColor: '#ccc',
    borderWidth: 1,
    padding: 12,
    marginVertical: 8,
    borderRadius: 8,
  },
  buttonContainer: {
    width: '100%',
    marginTop: 20,
  },
  button: {
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  footerText: {
    marginTop: 15,
    fontSize: 13,
    color: '#666',
  },
  loginText: {
    color: '#3A7CA5',
    fontWeight: 'bold',
  },
  up_image: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    // width: '100%',
    height: 200,
  },
  bottom_image: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    // width: '100%',
    height: 200,
  }
});

export default Login;

