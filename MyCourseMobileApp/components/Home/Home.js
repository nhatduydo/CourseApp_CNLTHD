import React from "react"
import { ActivityIndicator, Text, View } from "react-native"
import API, { endpoints } from "../../configs/API"
import MyStyles from "../../styles/MyStyles"
import Styles from "./Styles"

const Home = () => {
    const [courses, setCourses] = React.useState(null)

    React.useEffect(() => {
        const loadCourses = async () => {
            try {
                let res = await API.get(endpoints('courses'))
                setCourses(res.data.results)
            } catch {
                console.error(ex);
            }
        }
        loadCourses();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={Styles.subject}>HOME - trang chủ</Text>

            {courses === null ? <ActivityIndicator/> : <>
                {courses.map(c => (
                     <View key={c.id}>
                        <Text>{ c.subject }</Text>
                    </View>
                ))}
            </>}
        </View>
    )
}

export default Home