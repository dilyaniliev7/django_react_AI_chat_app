import { Outlet } from "react-router-dom"
import { AppSidebar } from "./AppSidebar"
import { SidebarProvider, SidebarTrigger } from "./ui/sidebar"


const MainLayout = () => {
    return (
        <SidebarProvider>
            <AppSidebar />
            <main>
                <SidebarTrigger />
                {<Outlet />}
            </main>
    </SidebarProvider>
        )
    }

export default MainLayout