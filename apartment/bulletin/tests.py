from django.test import TestCase
import datetime
from apartmentApp.models import BulletinPost
from apartmentApp.models import BulletinReply
from lib.dynamo import Dynamo

class BulletinPostTestCase(TestCase):

    def test_create_bulletin(self):
        bulletin_id = 0;
        pub_date = datetime.datetime.now()
        post_text = "This is a back end test in bulletin board"
        posted_by = "Tester Qing"
        bulletin = BulletinPost(bulletin_id=bulletin_id,post_text=post_text,pub_date=pub_date,posted_by=posted_by)
        bulletin.save()
        testBulletin = BulletinPost.objects.get(bulletin_id=bulletin_id)
        self.assertTrue(testBulletin.bulletin_id==bulletin_id)
        self.assertTrue(testBulletin.pub_date==pub_date)
        self.assertTrue(testBulletin.post_text==post_text)
        self.assertTrue(testBulletin.posted_by==posted_by)

    def test_create_bulletin_no_content(self):
        bulletin_id = 0;
        pub_date = datetime.datetime.now()
        post_text = "This is a back end test in bulletin board"
        posted_by = ""
        bulletin = BulletinPost(bulletin_id=bulletin_id,post_text=post_text,pub_date=pub_date,posted_by=posted_by)
        bulletin.save()
        self.assertFalse(BulletinPost.objects.get(bulletin_id=bulletin_id))

    def test_create_bulletin_no_sender(self):
        bulletin_id = 0;
        pub_date = datetime.datetime.now()
        post_text = ""
        posted_by = "Tester Qing"
        bulletin = BulletinPost(bulletin_id=bulletin_id,post_text=post_text,pub_date=pub_date,posted_by=posted_by)
        bulletin.save()
        self.assertFalse(BulletinPost.objects.get(bulletin_id=bulletin_id))


    def test_bulletin_delete(self):
        bulletin_id = 0;
        pub_date = datetime.datetime.now()
        post_text = "This is a back end test about create new bulletin in bulletin board"
        posted_by = "Tester 1"
        bulletin = BulletinPost(bulletin_id=bulletin_id,post_text=post_text,pub_date=pub_date,posted_by=posted_by)
        bulletin.save()
        BulletinPost.objects.get(bulletin_id=bulletin_id)
        self.assertTrue(BulletinPost.objects.get(bulletin_id = bulletin_id).delete())

"""
class BulletinReplyTestCase(TestCase):

    def test_send_comment(self):
        bulletin_id = 0;
        pub_date = datetime.datetime.now()
        post_text = "This is a back end test in bulletin board"
        posted_by = "Tester Qing"
        bulletin = BulletinPost(bulletin_id=bulletin_id,post_text=post_text,pub_date=pub_date,posted_by=posted_by)
        bulletin.save()
        testBulletin = BulletinPost.objects.get(bulletin_id=bulletin_id)
        reply_text = "This is a back end test about adding comment in one bulletin"
        pub_date = datetime.datetime.now()
        posted_by = "Tester2"
        replied_to = testBulletin
        comment = BulletinReply()
"""