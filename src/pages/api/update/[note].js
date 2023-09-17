// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { MongoClient } from "mongodb";

export default function handler(req, res) {
    const { note } = req.query;

    const uri = `mongodb+srv://HTN2023:${process.env.MONGODB_PASS}@studeye1.frh4mrj.mongodb.net/?retryWrites=true&w=majority`;
    const client = new MongoClient(uri);
    const collection = client.db("StudEye").collection("notes");

    let found = collection.findOne({ id: "note" });
    found.then((result) => {
        collection.updateOne(
            { id: "note" },
            { $set: { note: result.note + "\n" + note } },
        );
    });
    res.status(200).json({ note: note });
    // collection.updateOne({ id: "1" }, { $set: { note: note } });
}
