import React from "react"
import { ActivityIndicator, Image, Text, View } from "react-native"
import { ScrollView } from "react-native-gesture-handler"
import API, { endpoints } from "../../configs/API"
import MyStyles from "../../styles/MyStyles"
import Styles from "./Styles"

const Home = () => {
    const [courses, setCourses] = React.useState(null)

    React.useEffect(() => {
        console.log("🔥🔥🔥 useEffect đang chạy...");
        const loadCourses = async () => {
            try {
                let res = await API.get(endpoints.courses)
                console.log("Dữ liệu lấy được:", res.data)
                setCourses(res.data.results)
            } catch (error) {
                console.error("❌ Lỗi khi tải dữ liệu:", error);
            }
        }
        loadCourses();
        console.log("🔥🔥 đã chạy qua loadCoursees");
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={Styles.subject}>HOME - trang chủ</Text>
            <ScrollView style={{ flex: 1, flexDirection: 'row' }}>
                {courses === null ? <ActivityIndicator /> : <>
                    {courses.map(c => (
                        <View key={c.id}>
                            <View>
                                <Image
                                    style={{ width: 100, height: 100, resizeMode: "cover", borderRadius: 5 }}
                                    source={{ uri: c.image }}
                                />
                            </View>
                            <View >
                                <Text style={{ marginTop: 5, fontSize: 16, fontWeight: "bold" }}>{c.subject}</Text>
                            </View>
                        </View>
                    ))}
                </>}
            </ScrollView>
        </View >
    )
}

export default Home