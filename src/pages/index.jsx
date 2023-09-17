import { useState, useEffect } from "react";
import { Ubuntu } from "next/font/google";

const ubuntu = Ubuntu({ subsets: ["latin"], weight: ["400", "700"] });

async function getNotes() {
    const res = await fetch("/api/get_notes");
    const { note } = await res.json();
    return note;
}

async function apiSetNote(note) {
    await fetch("/api/set/" + note);
}

export default function Home() {
    const [notes, setNotes] = useState("");

    useEffect(() => {
        getNotes().then((note) => setNotes(note));
    }, []);

    function formatText(text) {
        const boldRegex = /\*\*(.*?)\*\*/g;
        const italicRegex = /\*(.*?)\*/g;
        const newlineRegex = /(\r\n|\n|\r)/g;

        return text.split(newlineRegex).map((line, lineIndex) => {
            return (
                <div key={lineIndex}>
                    {line.split(boldRegex).map((part, index) => {
                        if (index % 2 === 0) {
                            return part
                                .split(italicRegex)
                                .map((subpart, subIndex) => {
                                    if (subIndex % 2 === 0) {
                                        return subpart;
                                    } else {
                                        return (
                                            <span
                                                key={subIndex}
                                                className="italic animate-glow"
                                            >
                                                {subpart}
                                            </span>
                                        );
                                    }
                                });
                        } else {
                            return (
                                <span
                                    key={index}
                                    className={`font-black animate-glow`}
                                >
                                    {part}
                                </span>
                            );
                        }
                    })}
                </div>
            );
        });
    }

    // Function to handle form submission
    function handleSubmit(e) {
        e.preventDefault();
        setNotes(notes);
        apiSetNote(notes);
    };

    return (
        <main
            className={`flex min-h-screen flex-col items-center justify-between ${ubuntu.className}`}
        >
            <title>Studeye</title>
            <h1 className="p-8 text-6xl font-bold text-center animate-glow">
                Studeye
            </h1>
            <div className="w-[950px] bg-htn">
                <div className="w-full min-h-screen p-4 text-3xl text-white">
                    {notes ? formatText(notes) : "Loading..."}
                </div>
                <form onSubmit={handleSubmit}>
                    <textarea
                        className="w-full min-h-screen grid-cols-2 gap-24 p-4 text-3xl text-white bg-[#1a1a1a] rounded-3xl"
                        value={notes}
                        onChange={(e) => setNotes(e.target.value)}
                        placeholder="Add a new note..."
                    />
                    <button type="submit" className="px-4 py-2 mt-4 text-white bg-blue-500 rounded">
                        Add Note
                    </button>
                </form>
            </div>
        </main>
    );
}
