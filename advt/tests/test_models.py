import datetime
import unittest
from unittest import TestCase

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from advt.models import Advert, Like, Comment


class AdvertModelTest(TestCase):

    def setUp(self):

        self.advert = Advert(
            title="Продам IPhone XS 256gb",
            text="Отличное состояние, телефону 2 месяца",
            price=1500.00,
            address="ул. Комсомольская 7/2, д. 133"
        )
        self.advert.save()

        self.like = Like()

        super().setUp()

    def test_model_creation_with_object_manager(self):

        advt = Advert.objects.create(
            title="Продам IPhone XS 256gb",
            text="Отличное состояние, телефону 2 месяца",
            price=1500.00,
            address="ул. Комсомольская 7/2, д. 133"
        )
        self.assertTrue(isinstance(advt, Advert))
        self.assertEqual(self.advert.title, advt.title)

    @unittest.expectedFailure
    def test_update_date_at_future(self):

        with self.assertRaises(ValidationError):
            self.advert.update_at = datetime.datetime.now() + datetime.timedelta(days=1)

    @unittest.expectedFailure
    def test_update_date_at_past(self):

        with self.assertRaises(ValidationError):
            self.advert.update_at = datetime.datetime.now() - datetime.timedelta(weeks=1000)

    @unittest.expectedFailure
    def test_create_date_at_future(self):

        with self.assertRaises(ValidationError):
            self.advert.create_at = datetime.datetime.now() + datetime.timedelta(days=1)

    @unittest.expectedFailure
    def test_create_date_at_past(self):

        with self.assertRaises(ValidationError):
            self.advert.create_at = datetime.datetime.now() - datetime.timedelta(weeks=1000)


class LikeModelTest(TestCase):

    def create_advert(self):

        return Advert.objects.create(
            title="Продам IPhone XS 256gb",
            text="Отличное состояние, телефону 2 месяца",
            price=1500.00,
            address="ул. Комсомольская 7/2, д. 133"
        )

    def create_user(self):

        return User.objects.create(
            username="user_test",
            password="qwerty123@"
        )

    def test_model_creation_with_object_manager(self):

        User.objects.filter(username="user_test").delete()

        like = Like.objects.create(
            advt=self.create_advert(),
            user=self.create_user()
        )

        self.assertTrue(isinstance(like, Like))
        self.assertIsNotNone(like.user)
        self.assertIsNotNone(like.advt)

    @unittest.expectedFailure
    def test_model_creation_with_user_and_advert_that_already_exist(self):

        with self.assertRaises(ValidationError):
            like = Like.objects.create(
                advt=self.create_advert(),
                user=self.create_user()
            )

    @unittest.expectedFailure
    def test_update_date_at_future(self):

        with self.assertRaises(ValidationError):
            like = Like.objects.create(
                advt=self.create_advert(),
                user=self.create_user()
            )
            like.update_at = datetime.datetime.now() + datetime.timedelta(days=1)

    @unittest.expectedFailure
    def test_update_date_at_past(self):

        with self.assertRaises(ValidationError):
            like = Like.objects.create(
                advt=self.create_advert(),
                user=self.create_user()
            )
            like.update_at = datetime.datetime.now() - datetime.timedelta(weeks=1000)

    @unittest.expectedFailure
    def test_create_date_at_future(self):

        with self.assertRaises(ValidationError):
            like = Like.objects.create(
                advt=self.create_advert(),
                user=self.create_user()
            )
            like.create_at = datetime.datetime.now() + datetime.timedelta(days=1)

    @unittest.expectedFailure
    def test_create_date_at_past(self):

        with self.assertRaises(ValidationError):
            like = Like.objects.create(
                advt=self.create_advert(),
                user=self.create_user()
            )
            like.create_at = datetime.datetime.now() - datetime.timedelta(weeks=1000)
