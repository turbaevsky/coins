from flask import render_template
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask_appbuilder import expose, has_access, permission_name
from flask import make_response, Response
from app import appbuilder
from .models import *

class CoinView(ModelView):
	datamodel = MongoEngineInterface(Coin)

	list_columns = [
		"country",
		"yr",
		"currency",
		"nominal",
		"image_thumb_show",
		#"rev_thumb_show",
		"counter",
		"estimated_price",
		]


	show_columns = [
		"country",
		"yr",
		"currency",
		"nominal",
		"coin_type",
		"material",
		"image_show",
		"rev_show",
		"counter",
		"link",
		"estimated_price",
		"added",
		"comm",
		]

	@expose("/mongo_download/<pk>")
	@has_access
	def mongo_download(self, pk):
		item = self.datamodel.get(pk)
		file = item.file.read()
		response = make_response(file)
		response.headers["Content-Disposition"] = "attachment; filename={0}".format(
			item.file.name
		)
		return response

	@expose("/img/<pk>")
	@has_access
	@permission_name("show_img")
	def img(self, pk):
		item = self.datamodel.get(pk)
		mime_type = item.image.content_type
		return Response(item.image.read(), mimetype=mime_type, direct_passthrough=True)

	@expose("/rev/<pk>")
	@has_access
	@permission_name("show_rev")
	def rev(self, pk):
		item = self.datamodel.get(pk)
		mime_type = item.rev.content_type
		return Response(item.rev.read(), mimetype=mime_type, direct_passthrough=True)

	@expose("/img_thumb/<pk>")
	@has_access
	@permission_name("show_img")
	def img_thumb(self, pk):
		item = self.datamodel.get(pk)
		mime_type = item.image.content_type
		return Response(
			item.image.thumbnail.read(), mimetype=mime_type, direct_passthrough=True
		)

	@expose("/rev_thumb/<pk>")
	@has_access
	@permission_name("show_rev")
	def rev_thumb(self, pk):
		item = self.datamodel.get(pk)
		mime_type = item.rev.content_type
		return Response(
			item.rev.thumbnail.read(), mimetype=mime_type, direct_passthrough=True
		)

"""
	Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

appbuilder.add_view(
	CoinView,
	"Coins",
	icon="fa-folder-open-o",
	category="Coins",
	category_icon="fa-envelope",
)

#appbuilder.security_cleanup()