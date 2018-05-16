# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = 'a2c1e632e1d80403ae002b7fde0fb7dfe4afd5a4093292c24c75a65060ed81c16644cf1d7a5b5a4075c08e3530ee8e125d0405b910e73ee79d2441c990145be4'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': None,
    'group': None,
    'project': None
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
