var submit = document.getElementById('chat-form');

    submit.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the form from submitting

      // Code to be executed when the form is submitted
      getAIMessage(event, document);
});



function getAIMessage(event, document){

    var comp_log = document.getElementById('chat-log-2')
    var gpt_model;

    const user_input = document.getElementById('user-input').value;

//    Checks if we are doing a single or comparison chat
    if( comp_log == null ){
        gpt_model = document.getElementById('gpt-model').value;
    } else {
        gpt_model = null
    }

    document.getElementById('user-input').value = '';
    document.getElementById('chat-log').innerHTML += `<div class="user-message">${user_input}</div>`;

    if (comp_log !== null){
        comp_log.innerHTML += `<div class="user-message">${user_input}</div>`;
    }

    // Scroll to bottom
    var chatBox = document.getElementById('chat-log')
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: user_input, gpt_model: gpt_model }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chat-log').innerHTML += `<div class="ai-message">${data.message}</div>`;

        if( comp_log !== null){
            comp_log.innerHTML += `<div class="ai-message">${data.message2}</div>`;
        }

        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;

    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('chat-log').innerHTML += "<div>Error retrieving response from server.</div>";

        if( comp_log !== null){
            comp_log.innerHTML += "<div>Error retrieving response from server.</div>";
        }
    });



}

