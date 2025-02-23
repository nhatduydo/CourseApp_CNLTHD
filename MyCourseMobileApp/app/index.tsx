import { StyleSheet, Text, View } from "react-native";
import Home from "../components/Home/Home";
export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }
      }
    >
      <Text>Edit app/index.tsx to edit this screen.</Text>
      <Text style={styles.txt}>Xin chào nhất duy, hôm nay là ngày 23/2/2025</Text>
    <Home/>
    </View>
  );
}

const styles = StyleSheet.create({
  txt: {
    fontSize: 30,
    color: "blue",
  }
})
