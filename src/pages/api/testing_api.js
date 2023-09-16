// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default function handler(req, res) {
    // make a get request and display the json from http://localhost:5000
    fetch("http://127.0.0.1:5000")
        .then((response) => response.json())
        .then((data) => console.log(data));
    
    res.status(200).json({ name: "John Doe" });
}
