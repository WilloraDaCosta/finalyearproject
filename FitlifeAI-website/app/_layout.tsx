import { Slot } from 'expo-router';
import { SafeAreaView } from 'react-native';
import { UserProvider } from '@/contexts/userContext';


export default function Layout() {
  return (
    <SafeAreaView style={{ flex: 1 }}>
          <UserProvider>
      <Slot /> {/* 👈 Renders whatever route is active */}
      </UserProvider>
    </SafeAreaView>
  );
}

