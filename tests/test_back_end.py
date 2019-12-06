import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from front import app, db
from front.models import User


class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
                SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASS'))+'@'+str(getenv('MY_SQL_HOST'))+'/'+str(getenv('MY_SQL_DB_TEST')))
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        dm2019 = User(user_name="dm2019", email="dm2019@admin.com", password="admin2016")

        # create test non-admin user
        friend = User(user_name="friend", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(dm2019)
        db.session.add(friend)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class testapp(TestBase):

    def test_homepage_view(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_view(self):
        target_url = url_for('account')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)


    def test_register_view(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    





