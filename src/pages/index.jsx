import { Ubuntu } from "next/font/google";
import { useState } from "react";

const ubuntu = Ubuntu({ subsets: ["latin"], weight: ["400", "700"] });

export default function Home() {
    const [notes, setNotes] = useState("Your **notes** will go *here*!\nYour voila");

    function formatText(text) {
        const boldRegex = /\*\*(.*?)\*\*/g;
        const italicRegex = /\*(.*?)\*/g;
        const newlineRegex = /(\r\n|\n|\r)/g;

        return text
            .split(newlineRegex)
            .map((line, lineIndex) => {
                return (
                    <div key={lineIndex}>
                        {line.split(boldRegex).map((part, index) => {
                            if (index % 2 === 0) {
                                return part.split(italicRegex).map((subpart, subIndex) => {
                                    if (subIndex % 2 === 0) {
                                        return subpart;
                                    } else {
                                        return (
                                            <span key={subIndex} className="italic animate-glow">
                                                {subpart}
                                            </span>
                                        );
                                    }
                                });
                            } else {
                                return (
                                    <span key={index} className={`font-black animate-glow`}>
                                        {part}
                                    </span>
                                );
                            }
                        })}
                    </div>
                );
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
            <h1 className="p-8 text-6xl font-bold text-center animate-glow">
                Studeye
            </h1>
            <div className="w-[950px] bg-htn">
                <div className="w-full min-h-screen p-4 text-3xl text-white">
                    {formatText(notes)}
                </div>
                <textarea
                    className="w-full min-h-screen grid-cols-2 gap-24 p-4 text-3xl text-white bg-[#1a1a1a] rounded-3xl"
                    value={notes}
                    onChange={handleContentChange}
                />
            </div>
        </main>
    );
}
