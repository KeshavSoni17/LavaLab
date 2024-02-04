function connectToCompany(buttonElement) {
    var container = buttonElement.closest('.tool-container');
    var companyName = container.dataset.companyName;

    if (container.classList.contains('connected')) {
        axios.post('/disconnect/' + encodeURIComponent(companyName))
            .then(function (response) {
                if (response.data.status === 'disconnected') {
                    container.classList.remove('connected');
                    buttonElement.innerText = 'Connect';
                    buttonElement.style.backgroundColor = '';
                    buttonElement.style.border = "1px solid #C8C8C8";
                    buttonElement.style.color = "#000000";
                }
            })
            .catch(function (error) {
                console.error('Error disconnecting from company:', error);
            });
    } else {
        axios.post('/connect/' + encodeURIComponent(companyName))
            .then(function (response) {
                if (response.data.status === 'connected') {
                    container.classList.add('connected');
                    buttonElement.innerText = 'Connected';
                    buttonElement.style.backgroundColor = '#dffde0';
                    buttonElement.style.border = "0px solid #000000";
                    buttonElement.style.color = "#558451";
                }
            })
            .catch(function (error) {
                console.error('Error connecting to company:', error);
            });
    }
}
