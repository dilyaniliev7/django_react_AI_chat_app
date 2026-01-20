import axios from "axios"

const BASE_URL = "http://127.0.0.1:8000"

const api = axios.create({
    baseURL: BASE_URL
    })

export function promptGPT(data: {chat_id: string, content: string}){
    try{
        const response = await api.post("/prompt_gpt/", data)
        return response.data
        }
    catch(err:unknown){
        if (err instanceof Error){
            throw new Error(err.message)
            }
        throw new Error("an unknown error occured!");
        }
    }