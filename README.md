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

Construct a new authenticated Crisp client with your `identifier` and `key` tokens.

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
# eg. client.authenticate("13937834-f6ce-4556-ae4f-9e0c54faf038", "eb6c3623245521d7a6c35f5b29f3fa756e893f034ed551d84518961c5ff16dec")
client.authenticate(identifier, key)

# Now, you can use authenticated API sections.
```

**🔴 Important: Be sure to login once, and re-use the same authentication keys (same `identifier` + `key`) in all your subsequent requests to the API. Do not generate new tokens from your code for every new request to the API (you will be heavily rate-limited; that will induce HTTP failures for some of your API calls).**

## Resource Methods

Most useful available Crisp API resources are implemented. **Programmatic methods names are named after their label name in the [API Reference](https://docs.crisp.chat/api/v1/)**.

Thus, it is straightforward to look for them in the library while reading the [API Reference](https://docs.crisp.chat/api/v1/).

In the following method prototypes, `crisp` is to be replaced with your Crisp API instance. For example, instanciate `client = Crisp()` and then call eg: `client.user.check_session_validity()`.

When calling a method that writes data to the API (eg. send a message with: `client.website.send_message_in_conversation()`), you need to submit it this way:

```python
website_id = "88972681-a00c-4b3b-a383-cab281636484"
session_id = "session_9df2a21e-f113-41d4-8ed2-bad8b49cafd1"

client.website.send_message_in_conversation(
  website_id, session_id,

  {
    "type": "text",
    "content": "This message was sent from python-crisp-api! :)",
    "from": "operator",
    "origin": "chat"
  }
)
```

### Website

* **Website Conversations**
  * **List Conversations**: `client.website.list_conversations`

* **Website Conversation**
  * **Create A New Conversation**: `client.website.create_new_conversation`
  * **Check If Conversation Exists**: `client.website.check_conversation_exists`
  * **Get A Conversation**: `client.website.get_conversation`
  * **Remove A Conversation**: `client.website.remove_conversation`
  * **Initiate A Conversation With Existing Session**: `client.website.initiate_conversation_with_existing_session`
  * **Get Messages In Conversation**: `client.website.get_messages_in_conversation`
  * **Send A Message In Conversation**: `client.website.send_message_in_conversation`
  * **Update A Message In Conversation**: `client.website.update_message_in_conversation`
  * **Compose A Message In Conversation**: `client.website.compose_message_in_conversation`
  * **Mark Messages As Read In Conversation**: `client.website.mark_messages_read_in_conversation`
  * **Mark Messages As Delivered In Conversation**: `client.website.mark_messages_delivered_in_conversation`
  * **Get Conversation Routing Assign**: `client.website.get_conversation_routing_assign`
  * **Assign Conversation Routing**: `client.website.assign_conversation_routing`
  * **Get Conversation Metas**: `client.website.get_conversation_metas`
  * **Update Conversation Metas**: `client.website.update_conversation_metas`
  * **List Conversation Pages**: `client.website.list_conversation_pages`
  * **List Conversation Events**: `client.website.list_conversation_events`
  * **Get Conversation State**: `client.website.get_conversation_state`
  * **Change Conversation State**: `client.website.change_conversation_state`
  * **Get Block Status For Conversation**: `client.website.get_block_status_for_conversation`
  * **Block Incoming Messages For Conversation**: `client.website.block_incoming_messages_for_conversation`
  * **Request Email Transcript For Conversation**: `client.website.request_email_transcript_for_conversation`

* **Website People**
  * **Get People Statistics**: `client.website.get_people_statistics`
  * **List People Segments**: `client.website.list_people_segments`
  * **List People Profiles**: `client.website.list_people_profiles`
  * **Add New People Profile**: `client.website.add_new_people_profile`
  * **Check If People Profile Exists**: `client.website.check_people_profile_exists`
  * **Get People Profile**: `client.website.get_people_profile`
  * **Save People Profile**: `client.website.save_people_profile`
  * **Update People Profile**: `client.website.update_people_profile`
  * **Remove People Profile**: `client.website.remove_people_profile`
  * **List People Conversations**: `client.website.list_people_conversations`
  + **Add A People Event**: `client.website.add_people_event`
  + **List People Events**: `client.website.list_people_events`
  + **Get People Data**: `client.website.get_people_data`
  + **Save People Data**: `client.website.save_people_data`
  + **Get People Subscription Status**: `client.website.get_people_subscription_status`
  + **Update People Subscription Status**: `client.website.update_people_subscription_status`

* **Website Base**
  * **Create Website**: `client.website.create_website`
  * **Get A Website**: `client.website.get_website`
  * **Delete A Website**: `client.website.delete_website`

* **Website Batch**
  * **Batch Resolve Items**: `client.website.batch_resolve_items`
  * **Batch Read Items**: `client.website.batch_read_items`
  * **Batch Remove Items**: `client.website.batch_remove_items`

* **Website Availability**
  * **Get Website Availability Status**: `client.website.get_website_availability_status`

* **Website Operator**
  * **List Website Operators**: `client.website.list_website_operators`
  * **List Last Active Website Operators**: `client.website.list_last_active_website_operators`

* **Website Settings**
  * **Get Website Settings**: `client.website.get_website_settings`
  * **Update Website Settings**: `client.website.update_website_settings`

* **Website Visitors**
  * **Count Visitors**: `client.website.count_visitors`
  * **List Visitors**: `client.website.list_visitors`

### Bucket

* **Bucket URL**
  * **Generate Bucket URL**: `client.bucket.generate_bucket_url`

### User

* **User Availability**
  * **Get User Availability**: `client.user.get_user_availability`
  * **Update User Availability**: `client.user.update_user_availability`
  * **Get User Availability Status**: `client.user.get_user_availability_status`

* **User Account Base**
  * **Get User Account**: `client.user.get_user_account`
  * **Create User Account**: `client.user.create_user_account`

* **User Account Websites**
  * **List Websites**: `client.user.list_websites`

* **User Account Profile**
  * **Get Profile**: `client.user.get_profile`
  * **Update Profile**: `client.user.update_profile`

* **User Session**
  * **Check Session Validity**: `client.user.check_session_validity`
  * **Create A New Session**: `client.user.create_new_session`
  * **Destroy A Session**: `client.user.destroy_session`

* **User Statistics**
  * **Count Total Unread Messages**: `client.user.count_total_unread_messages`
