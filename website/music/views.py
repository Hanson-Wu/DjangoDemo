from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.shortcuts import render
from django.http import Http404
# Create your views here.

def index(request):
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	# html = ''
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) + '/'
	# 	html += '<a href = "'+ url +'">' + album.album_title + '</a><br>'
	# return HttpResponse(html)

	context  = {
		'all_albums':all_albums,
	}
	# return HttpResponse(template.render(context, request))

	return render(request, 'music/index.html', context)

def detail(request, album_id):
	#return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

	try:
		album = Album.objects.get(pk = album_id)
		context = {
			'album': album,
		}
	except Album.DoesNotExist:
		raise Http404("Album does not exits")
	return render(request, 'music/detail.html', context)

