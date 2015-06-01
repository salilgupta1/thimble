from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from thimble.apps.Users.models.schemas.Follow import Follow

class PortfoliosViewsTestCase(LiveServerTestCase):
	fixtures = ['auth_user.json','users.json','portfolio_test_data.json']

	def setUp(self):
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		self.login()

		super(PortfoliosViewsTestCase, self).setUp()
	def tearDown(self):
		self.selenium.quit()
		super(PortfoliosViewsTestCase, self).tearDown()

	def login(self):
		# send them to the login page
		self.selenium.get("%s%s" % (self.live_server_url, "/accounts/login/"))

		# login 
		username = self.selenium.find_element_by_id("id_username")
		username.send_keys("sdasbooty")

		password = self.selenium.find_element_by_id("id_password")
		password.send_keys("test")
		self.selenium.find_element_by_id("login_form").submit()

		# go to designer home page
		self.selenium.get("%s%s" % (self.live_server_url, "/devpat/"))

	def test_following(self):
		num_followers = self.selenium.find_element_by_css_selector(".text-followers>span").text
		
		# find follow button and check text
		follow_button = self.selenium.find_element_by_id("follow-btn")
		self.assertEquals(follow_button.text, "Follow")

		follow_button.click()
		unfollow_btn = self.selenium.find_element_by_id("unfollow-btn")
		self.assertEquals(unfollow_btn.text, "Following")

		# make sure the Followers updated
		new_num_followers = self.selenium.find_element_by_css_selector(".text-followers>span").text
		self.assertEquals(int(num_followers)+1, int(new_num_followers))

		# follow = Follow.objects.get(pk=1)
		# print follow

		self.selenium.refresh()
		#new_num_followers = self.selenium.find_element_by_css_selector(".text-followers>span").text
		#self.assertEquals(int(num_followers)+1, int(new_num_followers))

	# def test_unfollowing(self):
	# 	num_followers = self.selenium.find_element_by_css_selector(".text-followers>span").text
		
	# 	# find follow button and check text
	# 	unfollow_button = self.selenium.find_element_by_id("unfollow-btn")
	# 	self.assertEquals(unfollow_button.text, "Following")

	# 	unfollow_button.click()
	# 	follow_btn = self.selenium.find_element_by_id("follow-btn")
	# 	self.assertEquals(follow_btn.text, "Follow")

	# 	# make sure the Followers updated
	# 	new_num_followers = self.selenium.find_element_by_css_selector(".text-followers>span").text
	# 	self.assertEquals(int(num_followers)+1, int(new_num_followers))

	# 	self.selenium.refresh()

	# def test_liking(self):
	# 	pass

	# def test_unliking(self):
	# 	pass

	# def test_commenting(self):
	# 	pass