async function work(username) {
    // Get username from form
    try {
        // Send POST request to Flask server
        console.log("sending")

        const response = await fetch('https://4321-starkeeper11-gooslesearc-5g97oob99m.app.codeanywhere.com/getusername', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: username })
        });

        console.log("sent")

        // Parse response
        const result = await response.json();
        if (result["status"] == "success") {
            console.log(result["username"])
            console.log('Server response:', result);
        } else {
            console.log("but ypu sent it man and then u do an error like come on man :(")
            console.log('Server response:', result);
        }

        // Close modal on successful submission
        closeModal();
    } catch (error) {
        console.log("ERROR OH MY GOD PLEASE WORK ALREADY")
        console.log(error)
    }
};

work("1")