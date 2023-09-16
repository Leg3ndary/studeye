import { Ubuntu } from "next/font/google";
import { useState } from "react";

const ubuntu = Ubuntu({ subsets: ["latin"], weight: ["400", "700"] });

export default function Home() {
    const [notes, setNotes] = useState("Your **notes** will go **here**!");

    function formatText(text) {
        const regex = /\*\*(.*?)\*\*/g;

        return text.split(regex).map((part, index) => {
            if (index % 2 === 0) {
                return part;
            } else {
                return (
                    <span key={index} className="font-black drop-shadow-glow">
                        {part}
                    </span>
                );
            }
        });
    }

    const handleContentChange = (e) => {
        const newContent = e.target.value;
        setNotes(newContent);
    };

    return (
        <main
            className={`flex min-h-screen flex-col items-center justify-between ${ubuntu.className}`}
        >
            <h1 className="p-8 text-6xl font-bold text-center drop-shadow-glow">
                Studeye
            </h1>
            <div className="w-[950px] bg-htn">
                
                <div className="w-full h-screen p-4 text-3xl text-white">
                    {formatText(notes)}
                </div>
                <textarea
                    className="w-full h-screen grid-cols-2 gap-24 p-4 text-3xl text-white bg-inherit"
                    value={notes}
                    onChange={handleContentChange}
                />
            </div>
        </main>
    );
}
