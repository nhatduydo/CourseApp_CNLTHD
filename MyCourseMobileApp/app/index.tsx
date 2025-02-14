import { StyleSheet, Text, View } from "react-native";
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
      <Text style={styles.txt}>Xin chào nhất duy, đây là điện thoại ảo</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  txt: {
    fontSize: 30,
    color: "blue",
  }
})
