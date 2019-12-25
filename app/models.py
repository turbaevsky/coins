from mongoengine import Document
from mongoengine import (
	DateTimeField,
	StringField,
	ReferenceField,
	ListField,
	FileField,
	ImageField,
	URLField,
	FloatField,
	IntField,
)
import datetime
from flask import url_for, Markup

mindate = datetime.date(datetime.MINYEAR, 1, 1)

class Coin(Document):
	country = StringField(max_length=30)
	yr = IntField()
	currency = StringField(max_length=20)
	nominal = FloatField()
	counter = IntField()
	coin_type = StringField(max_length=30) # traditional coin, medal, etc
	material = StringField(max_length=30)
	image = ImageField(size=(350, 250, True), thumbnail_size=(30, 30, True))
	rev = ImageField(size=(350, 250, True), thumbnail_size=(30, 30, True))
	link = StringField()
	estimated_price = StringField(max_length=20)
	added = DateTimeField()
	comm = StringField()
	No = StringField()
	#def month_year(self):
	#	date = self.birthday or mindate
	#	return datetime.datetime(date.year, date.month, 1) or mindate

	def year(self):
		date = self.yr or mindate
		return datetime.datetime(date.year, 1, 1)

	def __repr__(self):
		return "%s : %s\n" % (self.country, self.nominal)

	def file_show(self):
		if self.file:
			return Markup(
				'<a href="' + url_for('CoinView.mongo_download', pk=str(self.id)) + '">Download {0}</a>'.format(self.file.name))
		else:
			return Markup('')

	def image_show(self):
		if self.image:
			return Markup('<a href="' + url_for('CoinView.show',pk=str(self.id)) + \
					  '" class="thumbnail"><img src="' + url_for('CoinView.img', pk=str(self.id)) + \
					  '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('')

	def rev_show(self):
		if self.rev:
			return Markup('<a href="' + url_for('CoinView.show',pk=str(self.id)) + \
					  '" class="thumbnail"><img src="' + url_for('CoinView.rev', pk=str(self.id)) + \
					  '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('')

	def image_thumb_show(self):
		print(self.image, self.id)
		if self.image:
			return Markup('<a href="' + url_for('CoinView.show',pk=str(self.id)) + \
					  '" class="thumbnail"><img src="' + url_for('CoinView.img_thumb', pk=str(self.id)) + \
					  '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('')

	def rev_thumb_show(self):
		print(self.rev, self.id)
		if self.rev:
			return Markup('<a href="' + url_for('CoinView.show',pk=str(self.id)) + \
					  '" class="thumbnail"><img src="' + url_for('CoinView.rev_thumb', pk=str(self.id)) + \
					  '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('')
