##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class WebsiteResource(object):
  def __init__(self, parent):
    self.parent = parent

  def create_website(self, data):
    # TODO

  def get_website(self, website_id):
    # TODO

  def delete_website(self, website_id):
    # TODO

  def batch_resolve_items(self, website_id, data):
    # TODO

  def batch_read_items(self, website_id, data):
    # TODO

  def batch_remove_items(self, website_id, data):
    # TODO

  def get_website_availability_status(self, website_id):
    # TODO

  def list_website_operators(self, website_id):
    # TODO

  def list_last_active_website_operators(self, website_id):
    # TODO

  def get_website_settings(self, website_id):
    # TODO

  def update_website_settings(self, website_id, data):
    # TODO

  def count_visitors(self, website_id):
    # TODO

  def list_visitors(self, website_id, page_number):
    # TODO

  def list_conversations(self, website_id, page_number):
    # TODO

  def create_new_conversation(self, website_id, data):
    # TODO

  def check_conversation_exists(self, website_id, session_id):
    # TODO

  def get_conversation(self, website_id, session_id):
    # TODO

  def remove_conversation(self, website_id, session_id):
    # TODO

  def initiate_conversation_with_existing_session(self, website_id, session_id):
    # TODO

  def get_messages_in_conversation(self, website_id, session_id, timestamp_before):
    # TODO

  def send_message_in_conversation(self, website_id, session_id, data):
    # TODO

  def update_message_in_conversation(self, website_id, session_id, fingerprint, data):
    # TODO

  def compose_message_in_conversation(self, website_id, session_id, data):
    # TODO

  def mark_messages_read_in_conversation(self, website_id, session_id, data):
    # TODO

  def mark_messages_delivered_in_conversation(self, website_id, session_id, data):
    # TODO

  def get_conversation_routing_assign(self, website_id, session_id):
    # TODO

  def assign_conversation_routing(self, website_id, session_id, data):
    # TODO

  def get_conversation_metas(self, website_id, session_id):
    # TODO

  def update_conversation_metas(self, website_id, session_id, data):
    # TODO

  def list_conversation_pages(self, website_id, session_id, page_number):
    # TODO

  def list_conversation_events(self, website_id, session_id, page_number):
    # TODO

  def get_conversation_state(self, website_id, session_id):
    # TODO

  def change_conversation_state(self, website_id, session_id, data):
    # TODO

  def get_block_status_for_conversation(self, website_id, session_id, data):
    # TODO

  def block_incoming_messages_for_conversation(self, website_id, session_id):
    # TODO

  def request_email_transcript_for_conversation(self, website_id, session_id, data):
    # TODO

  def get_people_statistics(self, website_id):
    # TODO

  def list_people_segments(self, website_id, page_number):
    # TODO

  def list_people_profiles(self, website_id, page_number):
    # TODO

  def add_new_people_profile(self, website_id, data):
    # TODO

  def check_people_profile_exists(self, website_id, people_id):
    # TODO

  def get_people_profile(self, website_id, people_id):
    # TODO

  def save_people_profile(self, website_id, people_id, data):
    # TODO

  def update_people_profile(self, website_id, people_id, data):
    # TODO

  def remove_people_profile(self, website_id, people_id):
    # TODO

  def list_people_conversations(self, website_id, people_id, page_number):
    # TODO

  def add_people_event(self, website_id, people_id, data):
    # TODO

  def list_people_events(self, website_id, people_id, page_number):
    # TODO

  def get_people_data(self, website_id, people_id):
    # TODO

  def save_people_data(self, website_id, people_id, data):
    # TODO

  def get_people_subscription_status(self, website_id, people_id):
    # TODO

  def update_people_subscription_status(self, website_id, people_id, data):
    # TODO
