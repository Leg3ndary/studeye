/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            backgroundImage: {
                "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
                "gradient-conic":
                    "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
            },
            colors: {
                htn: "#201c2c",
            },
            dropShadow: {
                glow1: ["0 0px 20px #2EFFFF", "0 0px 65px #2EFFFF"],
                glow2: ["0 0px 20px #FF0000", "0 0px 65px #FF0000"],
                glow3: ["0 0px 20px #FFFF00", "0 0px 65px #FFFF00"],
                glow4: ["0 0px 20px #FFA500", "0 0px 65px #FFA500"],
                glow5: ["0 0px 20px #008000", "0 0px 65px #008000"],
                glow6: ["0 0px 20px #800080", "0 0px 65px #800080"],
            },
            animation: {
                glow: "glow 12s ease-in-out infinite",
            },
        },
    },
    plugins: [],
};
