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
                        "You will fix the text provided, if there are no issues, reply with the original text.",
                },
                {
                    role: "system",
                    content:
                        "Only fix the texts errors, do not expand or add information that was not already present.",
                },
                { role: "user", content: text },
            ],
            model: "gpt-3.5-turbo",
        })
        .then(
            (data) => {
                res.status(200).json({
                    fixed: data.choices[0].message.content.trim(),
                });
            },
            (error) => {
                res.status(400).json({ error: "Error" });
            },
        );
}
