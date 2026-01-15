import { Outlet } from "react-router-dom"
import { AppSidebar } from "./AppSidebar"
import { SidebarProvider, SidebarTrigger } from "./ui/sidebar"


const MainLayout = () => {
    return (
        <SidebarProvider>
            <AppSidebar />
            <main className="w-full h-screen flex flex-col">
                <SidebarTrigger />
                {<Outlet />}
            </main>
    </SidebarProvider>
        )
    }

export default MainLayout