import axios from "axios"

// const HOST = "http://10.0.2.2:8000"
// const HOST = "http://127.0.0.1:8000"
const HOST = "https://thanhduong.pythonanywhere.com"

export const endpoints = {
    'categories':'/categories/',
    'courses':'/courses/'
}

export const authApi = () => {
    return axios.create({
        baseURL: HOST,
        headers: {
            'Authorization': `Bearer ...`
        }
    })
}

export default axios.create({
    baseURL: HOST
})
