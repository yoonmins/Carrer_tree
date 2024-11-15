// 게시글 목록을 가져와 화면에 표시
        function loadPosts() {
            fetch('http://localhost:3000/api/posts')
                .then(response => response.json())
                .then(data => {
                    const postContainer = document.getElementById('post-container');
                    postContainer.innerHTML = ''; // 기존 내용을 지우고 새로 렌더링
                    data.posts.forEach(post => {
                        const postElement = document.createElement('div');
                        postElement.innerHTML = `
                            <h3>${post.title}</h3>
                            <p>${post.content}</p>
                            <small>${new Date(post.createdAt).toLocaleString()}</small>
                            <hr>
                        `;
                        postContainer.appendChild(postElement);
                    });
                });
        }

        // 새 게시글 작성
        function createPost() {
            const title = document.getElementById('title').value;
            const content = document.getElementById('content').value;

            fetch('http://localhost:3000/api/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, content })
            })
            .then(response => response.json())
            .then(data => {
                alert('게시글이 작성되었습니다.');
                loadPosts();  // 게시글 목록을 다시 로드
                document.getElementById('title').value = '';
                document.getElementById('content').value = '';
            });
        }

        // 페이지 로드 시 게시글 목록 가져오기
        window.onload = loadPosts;