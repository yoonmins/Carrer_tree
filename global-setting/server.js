const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

let posts = []; // 메모리에 게시글 데이터를 저장할 배열
let idCounter = 1;

// 게시글 목록 조회
app.get('/api/posts', (req, res) => {
    res.json({ posts });
});

// 게시글 작성
app.post('/api/posts', (req, res) => {
    const { title, content } = req.body;
    const newPost = { id: idCounter++, title, content, createdAt: new Date() };
    posts.push(newPost);
    res.status(201).json(newPost);
});

// 서버 실행
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});