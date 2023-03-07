from django.test import TestCase,Client
from django.urls import reverse
import json
from rest_framework import status

client=Client()
class CreateNewPuppyTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {

        "admin_id": "A017",
        "admin_name": "vki",
        "admin_designation": "developer",
        "admin_mailid": "vikines.p1996@gmail.com",
        "admin_password": "poogvk@2388"
}
        self.invalid_payload ={

        "admin_id": "A009",
        "admin_name": "",
        "admin_designation": "developer",
        "admin_mailid": "vkines.p1996@gmail.com",
        "admin_password": "ppgvk@2388"
}

    def test_create_valid_admin(self):
        response = client.post(
            reverse('/api/add_admin'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_admin(self):
        response = client.post(
            reverse('/api/add_admin'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)