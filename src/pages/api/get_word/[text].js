import OpenAI from "openai";

const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

export default function handler(req, res) {
    const { text } = req.query;

    openai.chat.completions
        .create({
            messages: [
                {
                    role: "system",
                    content:
                        "You will reply in 4 sentences at most, though the more concise the better.",
                },
                {
                    role: "system",
                    content:
                        "Given text that an individual is looking at, you will return what word or concept they would most likely want defined. Reply with only one prompt followed by a colon and the definition with proper punctuation.",
                },
                {
                    role: "system",
                    content:
                        "In your response you may include the special symbols ** to enclose a word indicating that it is important and a keyword for the concept. For example, if the word is 'dog', you may respond with 'A **dog** is a furry animal that barks.'",
                },
                {
                    role: "system",
                    content:
                        "In your response you may also include the special symbols * to enclose a word indicating that it is another important word for the concept. For example, if the word is 'dog', you may respond with 'A **dog** is a furry *animal* that barks.'",
                },
                { role: "user", content: text },
            ],
            model: "gpt-3.5-turbo",
        })
        .then(
            (data) => {
                res.status(200).json({
                    detected: data.choices[0].message.content
                        .split(":")[0]
                        .trim(),
                    answer: data.choices[0].message.content
                        .split(":")[1]
                        .trim(),
                });
            },
            (error) => {
                res.status(400).json({ error: "Error" });
            },
        );
}
