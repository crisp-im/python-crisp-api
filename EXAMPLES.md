https://docs.crisp.chat/references/rest-api/v1/#list-conversations

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
page_number = 1

client.website.list_conversations(website_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-conversations

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
page_number = 1

client.website.search_conversations(website_id, page_number, search_query, search_type, search_operator, include_empty, filter_unread, filter_resolved, filter_not_resolved, filter_mention, filter_assigned, filter_unassigned, filter_date_start, filter_date_end, order_date_created", order_date_updated);

=========================

https://docs.crisp.chat/references/rest-api/v1/#create-a-new-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.create_new_conversation(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#check-if-conversation-exists

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.check_conversation_exists(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-a-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_conversation(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#remove-a-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.remove_conversation(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#initiate-a-conversation-with-existing-session

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.initiate_conversation_with_existing_session(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-messages-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_messages_in_conversation(website_id, session_id, query);

=========================

https://docs.crisp.chat/references/rest-api/v1/#send-a-message-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

query = {
  "type": "text",
  "from": "operator",
  "origin": "chat",
  "content": "Hey there! Need help?"
}

client.website.send_message_in_conversation(website_id, session_id, query);

=========================

https://docs.crisp.chat/references/rest-api/v1/#update-a-message-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"
fingerprint = 524653764345

data = "Hey there! Need help?"

client.website.update_message_in_conversation(website_id, session_id, fingerprint, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#compose-a-message-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "type": "start",
  "from": "operator"
}

client.website.compose_message_in_conversation(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#mark-messages-as-read-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "from": "operator",
  "origin": "urn:crisp.im:slack:0",
  "fingerprints": [
    "5719231201"
  ]
}

client.website.mark_messages_read_in_conversation(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#mark-messages-as-delivered-in-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "from": "operator",
  "origin": "urn:crisp.im:slack:0",
  "fingerprints": [
    "5719231201"
  ]
}

client.website.mark_messages_delivered_in_conversation(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-conversation-routing-assign

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_conversation_routing_assign(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#assign-conversation-routing

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "assigned": {
    "user_id": "a4c32c68-be91-4e29-8a05-976e93abbe3f"
  }
}

client.website.assign_conversation_routing(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-conversation-metas

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_conversation_metas(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#update-conversation-metas

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "nickname": "John Doe",
  "email": "john.doe@acme-inc.com",
  "segments": [
    "happy",
    "customer",
    "love"
  ],
  "data": {
    "type": "customer",
    "signup": "finished"
  }
}

client.website.update_conversation_metas(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-conversation-pages

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"
page_number = 1

client.website.list_conversation_pages(website_id, session_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-conversation-events

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"
page_number = 1

client.website.list_conversation_events(website_id, session_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-conversation-files

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"
page_number = 1

client.website.list_conversation_files(website_id, session_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-conversation-state

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_conversation_state(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#change-conversation-state

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = "unresolved"

client.website.change_conversation_state(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-block-status-for-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

client.website.get_block_status_for_conversation(website_id, session_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#block-incoming-messages-for-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = true

client.website.block_incoming_messages_for_conversation(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#request-email-transcript-for-conversation

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
session_id = "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"

data = {
  "to": "operator",
  "email": "valerian@crisp.chat"
}

client.website.request_email_transcript_for_conversation(website_id, session_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-people-statistics

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.get_people_statistics(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-suggested-people-segments

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
page_number = 1

client.website.list_people_segments(website_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-people-profiles

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
page_number = 1

client.website.list_people_profiles(website_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#add-new-people-profile

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

data = {
  "email": "valerian@crisp.chat",
  "person": {
    "nickname": "Valerian Saliou"
  }
}

client.website.add_new_people_profile(website_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#check-if-people-profile-exists

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"

client.website.check_people_profile_exists(website_id, people_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-people-profile

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"

client.website.get_people_profile(website_id, people_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#save-people-profile

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"

data = {
  "email": "valerian@crisp.chat",
  "person": {
    "nickname": "Valerian Saliou"
  }
}

client.website.save_people_profile(website_id, people_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#update-people-profile

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"

data = {
  "email": "valerian@crisp.chat",
  "person": {
    "nickname": "Valerian Saliou"
  }
}

client.website.update_people_profile(website_id, people_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#remove-people-profile

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"

client.website.remove_people_profile(website_id, people_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-people-conversations

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
people_id = "c5a2f70c-f605-4648-b47f-8c39d4b03a50"
page_number = 1

client.website.list_people_conversations(website_id, people_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#create-website

client.website.create_website(data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-a-website

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.get_website(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#delete-a-website

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.delete_website(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#batch-resolve-items

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.batch_resolve_items(website_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#batch-read-items

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.batch_read_items(website_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#batch-remove-items

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

data = [
  "session_19e5240f-0a8d-461e-a661-a3123fc6eec9",
  "session_700c65e1-85e2-465a-b9ac-ecb5ec2c9881"
]

client.website.batch_remove_items(website_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-website-availability-status

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.get_website_availability_status(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-website-operators

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.list_website_operators(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-last-active-website-operators

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.list_last_active_website_operators(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-website-settings

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.get_website_settings(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#update-website-settings

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

data = {
  "name": "Crisp",
  "domain": "crisp.chat",
  "logo": "https://storage.crisp.chat/users/avatar/website/8c842203-7ed8-4e29-a608-7cf78a7d2fcc/b6c2948d-b061-405e-91a9-2fdf855d1cc0.png",
  "contact": {
    "email": "contact@crisp.chat",
    "phone": "+33757905447"
  },
  "inbox": {
    "lock_removal": false,
    "force_operator_token": false
  },
  "emails": {
    "rating": true,
    "transcript": true,
    "enrich": true,
    "junk_filter": true
  },
  "chatbox": {
    "tile": "default",
    "wait_game": false,
    "last_operator_face": false,
    "ongoing_operator_face": true,
    "activity_metrics": true,
    "operator_privacy": false,
    "availability_tooltip": true,
    "hide_vacation": false,
    "hide_on_away": false,
    "hide_on_mobile": false,
    "position_reverse": false,
    "email_visitors": false,
    "phone_visitors": false,
    "force_identify": false,
    "ignore_privacy": false,
    "visitor_compose": false,
    "file_transfer": true,
    "overlay_search": true,
    "overlay_mode": false,
    "helpdesk_link": true,
    "helpdesk_only": false,
    "status_health_dead": true,
    "check_domain": false,
    "color_theme": "blue",
    "text_theme": "default",
    "welcome_message": "default",
    "locale": "en",
    "allowed_pages": [],
    "blocked_pages": [
      "status/*/",
      "docs.crisp.chat/*",
      "crisp.chat/terms/",
      "https://crisp.chat/privacy/"
    ],
    "blocked_countries": [
      "IT"
    ],
    "blocked_locales": [
      "fa",
      "he"
    ],
    "blocked_ips": [
      "8.8.8.8",
      "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "192.168.1.1/24"
    ]
  }
}

client.website.update_website_settings(website_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#count-visitors

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"

client.website.count_visitors(website_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-visitors

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
page_number = 1

client.website.list_visitors(website_id, page_number);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-connect-account

client.get_connect_account();

=========================

https://docs.crisp.chat/references/rest-api/v1/#check-connect-session-validity

client.check_connect_session_validity();

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-all-connect-websites

page_number = 1

client.list_all_connect_websites(page_number, filter_configured);

=========================

https://docs.crisp.chat/references/rest-api/v1/#list-all-active-subscriptions

client.list_all_active_subscriptions();

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-subscription-details

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

client.get_subscription_details(website_id, plugin_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#unsubscribe-plugin-from-website

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

client.unsubscribe_plugin_from_website(website_id, plugin_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#get-subscription-settings

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

client.get_subscription_settings(website_id, plugin_id);

=========================

https://docs.crisp.chat/references/rest-api/v1/#save-subscription-settings

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

settings = {
  "chatbox": {
    "25": "#bbbbbb"
  }
}

client.save_subscription_settings(website_id, plugin_id, settings);

=========================

https://docs.crisp.chat/references/rest-api/v1/#update-subscription-settings

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

settings = {
  "chatbox": {
    "25": "#bbbbbb"
  }
}

client.update_subscription_settings(website_id, plugin_id, settings);

=========================

https://docs.crisp.chat/references/rest-api/v1/#forward-plugin-payload-to-channel

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

data = {
  "namespace": "bot:step",
  "payload": {
    "step": 1
  }
}

client.forward_plugin_payload_to_channel(website_id, plugin_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#dispatch-plugin-event

website_id = "8c842203-7ed8-4e29-a608-7cf78a7d2fcc"
plugin_id = "c64f3595-adee-425a-8d3a-89d47f7ed6bb"

data = {
  "name": "bot-is-running",
  "data": {
    "bot": "Sales",
    "email": "valerian@crisp.chat"
  }
}

client.dispatch_plugin_event(website_id, plugin_id, data);

=========================

https://docs.crisp.chat/references/rest-api/v1/#generate-bucket-url

client.bucket.generate_bucket_url(data);

=========================

