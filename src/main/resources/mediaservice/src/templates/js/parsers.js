fetch("our_url", {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "url": "some_url",
      "parser_type": 1,
      "action": 1})
})
   .then(response => response.json())
   .then(response => (
      console.log(JSON.stringify(response));
      console.log("finished");)

