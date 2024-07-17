import express from 'express';
import path from 'path';

const app = express();
const port = 8080;

app.use(express.static(path.join(__dirname, "/public")));

app.listen(port, () => {
  console.log(`[Server]: Listening on port ${port}`);
});
