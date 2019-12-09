import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from front import app, db
from front.models import User, Chara, Campaign
from flask_login import login_user, current_user


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

        # create test user1
        dm2019 = User(user_name="dm2019", email="dm2019@admin.com", password="admin2016")

        # create test  user2
        friend = User(user_name="friend", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(dm2019)
        db.session.add(friend)
        db.session.commit()

        character1 = Chara(character_name='Leeroy Jenkins The 3rd', level=1, race='dragonkin', character_class='Fighter', user_id=1)

        character2 = Chara(character_name='Samus', level=12, race='elf', character_class='Ranger', user_id=2)

        campaign1 = Campaign(camp_name='The Meme Wars', start_date='1/1/2000', end_date='TBD', status='Active', dm=1)

        campaign2 = Campaign(camp_name='The last quip', start_date='23/9/2016', end_date='5/2/2017', status='Inactive', dm=2)

        db.session.add(character1)
        db.session.add(character2)
        db.session.add(campaign1)
        db.session.add(campaign2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class testview(TestBase):

    def test_homepage_view(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_account_if_not_user_view(self):
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

    
    def test_character_if_not_user_view(self):
        target_url = url_for('character')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


    def test_campaign_if_not_user_view(self):
        target_url = url_for('campaign')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


    def test_home_login_if_not_user_view(self):
        target_url = url_for('home_login')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


class testtables(TestBase):

    def test_add_user(self):

        user1 =User(user_name="testuse", email="user@user.com", password="user2019")
        db.session.add(user1)
        db.session.commit()

        self.assertEqual(User.query.count(), 3)




    def test_add_character(self):

        user2=Chara(character_name='Leeroy Jenkins The 4th', level=6, race='dragonkin', character_class='Wizard', user_id=1)
        db.session.add(user2)
        db.session.commit()

        self.assertEqual(Chara.query.count(), 3)


    def test_add_campaign(self):

        user3= Campaign(camp_name='The Meme Wars Part 2: Cat strikes back', start_date='6/9/2014', end_date='TBD', status='Active', dm=1)
        db.session.add(user3)
        db.session.commit()

        self.assertEqual(Campaign.query.count(), 3)



