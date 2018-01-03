# python-crisp-api

The Crisp API Python wrapper. Authenticate, send messages, fetch conversations, access your agent accounts from your Python code.

Copyright 2018 Crisp IM SARL. See LICENSE for copying information.

* **📝 Implements**: [Crisp Platform - API ~ v1](https://docs.crisp.chat/api/v1/) at reference revision: 12/31/2017
* **😘 Maintainer**: [@valeriansaliou](https://github.com/valeriansaliou)

## Usage

Install the library:

```bash
pip install crisp-api
```

Then, import it:

```python
from crisp_api import Crisp
```

Construct a new authenticated Crisp client with your `user_id` and `secret_key` tokens.

```python
client = Crisp()

client.authenticate(identifier, key)
```

Then, your client is ready to be consumed!

## Authentication

To authenticate against the API, generate your session identifier and session key **once** using the following cURL request in your terminal (replace `YOUR_ACCOUNT_EMAIL` and `YOUR_ACCOUNT_PASSWORD`):

```bash
curl -H "Content-Type: application/json" -X POST -d '{"email":"YOUR_ACCOUNT_EMAIL","password":"YOUR_ACCOUNT_PASSWORD"}' https://api.crisp.chat/v1/user/session/login
```

If authentication succeeds, you will get a JSON response containing your authentication keys: `identifier` and `key`. **Keep those 2 values private, and store them safely for long-term use**.

Then, add authentication parameters to your `client` instance right after you create it:

```python
client = Crisp()

# Authenticate to API (identifier, key)
# eg. client.authenticate("7c3ef21c-1e04-41ce-8c06-5605c346f73e", "cc29e1a5086e428fcc6a697d5837a66d82808e65c5cce006fbf2191ceea80a0a")
client.authenticate(identifier, key)

# Now, you can use authenticated API sections.
```

**🔴 Important: Be sure to login once, and re-use the same authentication keys (same `identifier` + `key`) in all your subsequent requests to the API. Do not generate new tokens from your code for every new request to the API (you will be heavily rate-limited; that will induce HTTP failures for some of your API calls).**

## Resource Methods

Most of the available Crisp API resources are implemented. **Programmatic methods names are named after their label name in the [API Reference](https://docs.crisp.chat/api/v1/)**.

Thus, it is straightforward to look for them in the library while reading the [API Reference](https://docs.crisp.chat/api/v1/).

In the following method prototypes, `crisp` is to be replaced with your Crisp API instance. For example, instanciate `client = Crisp()` and then call eg: `client.user.check_session_validity()`.

When calling a method that writes data to the API (eg: `client.user.create_user_account()`), you need to build an account instance and submit it this way:

```python
client.user.create_user_account({
  "email": "john@acme-inc.com",
  "password": "SecurePassword",
  "first_name": "John",
  "last_name": "Doe"
})
```
