const Stack = createNativeStackNavigator();
import * as React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { useFonts } from "expo-font";
import Home from "./screens/Home";
import HomeEnterYourName from "./screens/HomeEnterYourName";
import Records from "./screens/Records";
import MatchSenario from "./screens/MatchSenario";
import MatchSenario18Result from "./screens/MatchSenario18Result";

import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { View, Text, Pressable, TouchableOpacity } from "react-native";

const App = () => {
  const [hideSplashScreen, setHideSplashScreen] = React.useState(true);

  const [fontsLoaded, error] = useFonts({
    "Inter-Light": require("./assets/fonts/Inter-Light.ttf"),
    "Inter-Regular": require("./assets/fonts/Inter-Regular.ttf"),
    "Inter-SemiBold": require("./assets/fonts/Inter-SemiBold.ttf"),
  });

  if (!fontsLoaded && !error) {
    return null;
  }

  return (
    <>
      <NavigationContainer>
        {hideSplashScreen ? (
          <Stack.Navigator screenOptions={{ headerShown: false }}>
            <Stack.Screen
              name="Home"
              component={Home}
              options={{ headerShown: false }}
            />
            <Stack.Screen
              name="HomeEnterYourName"
              component={HomeEnterYourName}
              options={{ headerShown: false }}
            />
            <Stack.Screen
              name="Records"
              component={Records}
              options={{ headerShown: false }}
            />
            <Stack.Screen
              name="MatchSenario"
              component={MatchSenario}
              options={{ headerShown: false }}
            />
            <Stack.Screen
              name="MatchSenario18Result"
              component={MatchSenario18Result}
              options={{ headerShown: false }}
            />
          </Stack.Navigator>
        ) : null}
      </NavigationContainer>
    </>
  );
};
export default App;
