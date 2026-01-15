import { BrowserRouter, Route, Routes } from "react-router-dom"
import MainLayout from "./components/MainLayout"
import HomePage from "./pages/HomePage"

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainLayout />}>
                    <Route index element={<HomePage />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default App