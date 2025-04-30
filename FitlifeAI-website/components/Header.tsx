import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import { usePathname } from 'expo-router';

const Header = () => {
  const pathname = usePathname();

  // Routes where header should be hidden
  const hiddenRoutes = ['/', '/auth/login', '/auth/signUp'];

  if (hiddenRoutes.includes(pathname)) return null;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>FitLifeAI</Text>
      <Image
        source={require('../assets/logo.png')}
        style={styles.logo}
        resizeMode="contain"
      />
    </View>
  );
};

export default Header;

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 16,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'space-between',
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#2E6D9C',
  },
  logo: {
    width: 80,
    height: 40,
  },
});
