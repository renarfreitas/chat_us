const $chatMessages = document.querySelector(".messages")

const getMessage = async (room_id) => {
    const response = await fetch(`/${room_id}`);
    const html = await response.text();
    console.log(html);
    $chatMessages.innerHTML = html
};

