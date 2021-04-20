class PluginResource(object):
    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    def __url_plugins_subscription(resource = ""):
        return f"/plugins/subscription{resource}"

    @staticmethod
    def __url_plugin_connect(resource):
        return f"/plugin/connect{resource}"

    def list_all_active_subscriptions(self):
        return self.parent.get(self.__url_plugins_subscription())

    def list_subscriptions_website(self, website_id):
        return self.parent.get(self.__url_plugins_subscription(f"/{website_id}"))

    def get_subscription_details(self, website_id, plugin_id):
        return self.parent.get(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}"))

    def subscribe_plugin_to_website(self, website_id):
        return self.parent.post(self.__url_plugins_subscription(f"/{website_id}"))

    def unsubscribe_plugin_from_website(self, website_id, plugin_id):
        return self.parent.delete(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}"))

    def get_subscription_settings(self, website_id, plugin_id):
        return self.parent.get(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}/settings"))

    def save_subscription_settings(self, website_id, plugin_id, settings):
        return self.parent.put(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}/settings"), settings)

    def update_subscription_settings(self, website_id, plugin_id, settings):
        return self.parent.patch(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}/settings"), settings)

    def forward_plugin_payload_to_channel(self, website_id, plugin_id, data):
        return self.parent.post(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}/channel"), data)

    def dispatch_plugin_event(self, website_id, plugin_id, data):
        return self.parent.post(self.__url_plugins_subscription(f"/{website_id}/{plugin_id}/event"), data)

    def get_connect_account(self):
        return self.parent.get(self.__url_plugin_connect("/account"))

    def check_connect_session_validity(self):
        return self.parent.head(self.__url_plugin_connect("/session"))

    def list_all_connect_websites(self, page_number, filter_configured):
        return self.parent.get(
            self.__url_plugin_connect(f"/websites/all/{page_number}?filter_configured={filter_configured}")
        )

    def list_connect_websites_since(self, date_since, filter_configured):
        return self.parent.get(
            self.__url_plugin_connect(f"/websites/since?date_since={date_since}&filter_configured={filter_configured}")
        )
