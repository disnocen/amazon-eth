
    // connect to the metamask extension
    function handleAccountsChanged(accounts) {
            console.log('Calling HandleChanged')
            
            if (accounts.length === 0) {
                console.log('Please connect to MetaMask.');
                $('#enableMetamask').html('Connect with Metamask')
            } else if (accounts[0] !== currentAccount) {
                let currentAccount = accounts[0];
                $('#enableMetamask').html(currentAccount)
                $('#status').html('')
                
                if(currentAccount != null) {
                    // Set the button label
                    $('#enableMetamask').html(currentAccount)
                }
            }
            console.log('WalletAddress in HandleAccountChanged ='+walletAddress)
        }

    function metaconnect() {
            connect();
            changeButtonLabel();
        }

    function connect() {
            console.log('Calling connect()')
            ethereum
            .request({ method: 'eth_requestAccounts' })
            .then(handleAccountsChanged)
            .catch((err) => {
            if (err.code === 4001) {
                // EIP-1193 userRejectedRequest error
                // If this happens, the user rejected the connection request.
                console.log('Please connect to MetaMask.');
                $('#status').html('You refused to connect Metamask')
            } else {
                console.error(err);
            }
            });
        }
    function changeButtonLabel() {
        document.getElementById("enableMetamask").innerHTML = "Connected to Metamask";
        // document.getElementById("enableMetamask").style.display = "none";
    }


