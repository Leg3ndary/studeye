import { Ubuntu } from "next/font/google";

const ubuntu = Ubuntu({ subsets: ["latin"], weight: ["400", "700"] });

export default function Home() {
    return (
        <main
            className={`flex min-h-screen flex-col items-center justify-between p-24 ${ubuntu.className}`}
        >
            <div className="w-[800px] bg-border-2 bg-htn border-white absolute">
                <h1 className="p-4 text-6xl text-center">Studeye</h1>
            </div>
        </main>
    );
}