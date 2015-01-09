# -*- coding: utf-8 -*-
"""
Last Generated: 2015-01-09 11:09:12.508915

This module (access_methods.py) is autogenerated from the Eventbrite API
documentation. Any and all changes to this module must be implemented as
p art of that autogeneration. Therefore, we cannot accept any pull requests,
as the next generation of this module will the changes to be overwritten.
"""

class AccessMethodsMixin(object):

    def get_categories(self):
        """
        GET /categories/

        Returns a list of :format:`category` as ``categories``, including
        subcategories nested.

        """
        return self.get("/categories/")

    def get_categories(self, id):
        """
        GET /categories/:id/

        Gets a :format:`category` by ID as ``category``.

        """
        
        return self.get("/categories/{0}/".format(id))

    def get_subcategories(self):
        """
        GET /subcategories/

        Returns a list of :format:`subcategory` as ``subcategories``.

        """
        return self.get("/subcategories/")

    def get_subcategories(self, id):
        """
        GET /subcategories/:id/

        Gets a :format:`subcategory` by ID as ``subcategory``.

        """
        
        return self.get("/subcategories/{0}/".format(id))

    def get_format(self):
        """
        GET /format/

        Returns a list of :format:`format` as ``formats``.

        """
        return self.get("/format/")

    def get_format(self, id):
        """
        GET /format/:id/



        Gets a :format:`format` by ID as ``format``.
        """
        
        return self.get("/format/{0}/".format(id))

    def get_media(self, id):
        """
        GET /media/:id/

        Return an :format:`image` for a given id.

        .. _get-media-upload:

        """
        
        return self.get("/media/{0}/".format(id))

    def get_media_upload(self):
        """
        GET /media/upload/

        See :ref:`media-uploads`.
        .. _post-media-upload:

        """
        return self.get("/media/upload/")

    def post_media_upload(self):
        """
        POST /media/upload/



        See :ref:`media-uploads`.
        """
        return self.post("/media/upload/")

    def get_orders(self, id):
        """
        GET /orders/:id/



        Gets an :format:`order` by ID as the key ``order``.
        """
        
        return self.get("/orders/{0}/".format(id))

    def post_organizers(self):
        """
        POST /organizers/


        Makes a new organizer.
        Returns an :format:`organizer` as ``organizer``.

        """
        return self.post("/organizers/")

    def get_organizers(self, id):
        """
        GET /organizers/:id/


        Gets an :format:`organizer` by ID as ``organizer``.

        """
        
        return self.get("/organizers/{0}/".format(id))

    def post_organizers(self, id):
        """
        POST /organizers/:id/




        Updates an :format:`organizer` and returns it as as ``organizer``.
        """
        
        return self.post("/organizers/{0}/".format(id))

    def get_system_timezones(self):
        """
        GET /system/timezones/


        Returns a paginated response with a key of ``timezones``,
        containing a list of :format:`timezones <timezone>`.

        """
        return self.get("/system/timezones/")

    def get_users(self, id):
        """
        GET /users/:id/

        Returns a :format:`user` for the specified user as ``user``. If you want
        to get details about the currently authenticated user, use ``/users/me/``.

        """
        
        return self.get("/users/{0}/".format(id))

    def get_users_orders(self, id):
        """
        GET /users/:id/orders/

        Returns a paginated response of :format:`orders <order>`, under
        the key ``orders``, of all orders the user has placed (i.e. where the user
        was the person buying the tickets).

        """
        
        return self.get("/users/{0}/orders/".format(id))

    def get_users_owned_events(self, id):
        """
        GET /users/:id/owned_events/

        Returns a paginated response of :format:`events <event>`, under
        the key ``events``, of all events the user owns (i.e. events they are organising)

        """
        
        return self.get("/users/{0}/owned_events/".format(id))

    def get_users_owned_event_attendees(self, id):
        """
        GET /users/:id/owned_event_attendees/

        Returns a paginated response of :format:`attendees <attendee>`, under
        the key ``attendees``, of attendees visiting any of the events the user owns
(events that would be returned from ``/users/:id/owned_events/``)

        """
        
        return self.get("/users/{0}/owned_event_attendees/".format(id))

    def get_users_owned_event_orders(self, id):
        """
        GET /users/:id/owned_event_orders/

        Returns a paginated response of :format:`orders <order>`, under
        the key ``orders``, of orders placed against any of the events the user owns
(events that would be returned from ``/users/:id/owned_events/``)

        """
        
        return self.get("/users/{0}/owned_event_orders/".format(id))

    def get_users_contact_lists(self, id):
        """
        GET /users/:id/contact_lists/

        Returns a list of :format:`contact_list` that the user owns as the key
        ``contact_lists``.

        """
        
        return self.get("/users/{0}/contact_lists/".format(id))

    def post_users_contact_lists(self, id):
        """
        POST /users/:id/contact_lists/

        Makes a new :format:`contact_list` for the user and returns it as
        ``contact_list``.

        """
        
        return self.post("/users/{0}/contact_lists/".format(id))

    def get_users_contact_lists(self, id, contact_list_id):
        """
        GET /users/:id/contact_lists/:contact_list_id/

        Gets a user's :format:`contact_list` by ID as ``contact_list``.

        """
        
        return self.get("/users/{0}/contact_lists/{1}/".format(id,contact_list_id))

    def post_users_contact_lists(self, id, contact_list_id):
        """
        POST /users/:id/contact_lists/:contact_list_id/

        Updates the :format:`contact_list` and returns it as ``contact_list``.

        """
        
        return self.post("/users/{0}/contact_lists/{1}/".format(id,contact_list_id))

    def delete_users_contact_lists(self, id, contact_list_id):
        """
        DELETE /users/:id/contact_lists/:contact_list_id/

        Deletes the contact list. Returns ``{"deleted": true}``.

        """
        
        return self.delete("/users/{0}/contact_lists/{1}/".format(id,contact_list_id))

    def get_users_contact_lists_contacts(self, id, contact_list_id):
        """
        GET /users/:id/contact_lists/:contact_list_id/contacts/

        Returns the :format:`contacts <contact>` on the contact list
        as ``contacts``.

        """
        
        return self.get("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id))

    def post_users_contact_lists_contacts(self, id, contact_list_id):
        """
        POST /users/:id/contact_lists/:contact_list_id/contacts/

        Adds a new contact to the contact list. Returns ``{"created": true}``.
        There is no way to update entries in the list; just delete the old one
        and add the updated version.

        """
        
        return self.post("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id))

    def delete_users_contact_lists_contacts(self, id, contact_list_id):
        """
        DELETE /users/:id/contact_lists/:contact_list_id/contacts/



        Deletes the specified contact from the contact list.
        Returns ``{"deleted": true}``.


        """
        
        return self.delete("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id))

    def get_webhooks(self, id):
        """
        GET /webhooks/:id/

        Returns a :format:`webhook` for the specified webhook as ``webhook``.

        """
        
        return self.get("/webhooks/{0}/".format(id))

    def delete_webhooks(self, id):
        """
        DELETE /webhooks/:id/

        Deletes the specified :format:`webhook` object.

        """
        
        return self.delete("/webhooks/{0}/".format(id))

    def get_webhooks(self):
        """
        GET /webhooks/

        Returns the list of :format:`webhook` objects that belong to the authenticated user.

        """
        return self.get("/webhooks/")

    def post_webhooks(self):
        """
        POST /webhooks/



        Creates a :format:`webhook` object. The topic_patterns parameter accepts a comma-seperated value that can include any or all of the following:

        * ``event:{id}:*`` - Any changes to a specific event
        * ``event:{id}:order:*:placed`` - Any orders for the specified event.
        * ``user:me:event:*`` - Covers changes to any event.

        .. note:: {id} must be replaced with the correct Event ID.
        """
        return self.post("/webhooks/")