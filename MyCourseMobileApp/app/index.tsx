import { createDrawerNavigator } from "@react-navigation/drawer";
import { StyleSheet } from "react-native";
import Home from "../components/Home/Home";
import Login from "../components/User/Login";

const Drawer = createDrawerNavigator()

export default function Index() {
  return (
    // <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={Home}/>
        <Drawer.Screen name="Login" component={Login}/>
      </Drawer.Navigator>
    //</NavigationContainer>
  );
}

const styles = StyleSheet.create({
  txt: {
    fontSize: 30,
    color: "blue",
  }
})
