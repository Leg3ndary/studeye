// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { MongoClient } from "mongodb";

export default async function handler(req, res) {
    const uri = `mongodb+srv://HTN2023:${process.env.MONGODB_PASS}@studeye1.frh4mrj.mongodb.net/?retryWrites=true&w=majority`;
    const client = new MongoClient(uri);
    const collection = client.db("StudEye").collection("notes");

    await collection.findOne({ id: "note" }).then((result) => {
        res.status(200).json({ note: result.note });
    }
    ).catch((err) => {
        return res.status(500).json({ error: err });
    });
}
