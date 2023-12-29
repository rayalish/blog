const sendRate = (e) => {
    e.preventDefault();
    const commentText = document.querySelector('#commentText').value;
    const blogId = document.querySelector('#blog_id').value;
    const userId = document.querySelector('#user_id').value;
    
    axios.post(
        'http://localhost:8000/comment/',
        {
            blog_id: blogId,
            text: commentText,
            user_id: userId,
        }
    ).then((data) => {
        console.log(data);
    }).catch((error) => {
        console.log(error);
    })

    window.location.reload();
}