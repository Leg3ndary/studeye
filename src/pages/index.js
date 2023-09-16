import { Ubuntu } from "next/font/google";

const ubuntu = Ubuntu({ subsets: ["latin"], weight: ["400", "700"]});

export default function Home() {
    return (
        <main
            className={`flex min-h-screen flex-col items-center justify-between p-24 ${ubuntu.className}`}
        >
            <div className="w-[800px] border-2">
                <h1 className="text-6xl">Htn title thing</h1>
            </div>
        </main>
    );
}
