[jQuery-File-Upload](http://aquantum-demo.appspot.com/file-upload) is developed by Sebastian Tschan, with the source available on [github](https://github.com/blueimp/jQuery-File-Upload). Example code is [ported to Django](https://github.com/sigurdga/django-jquery-file-upload) by Sigurd Gartmann ([sigurdga on github](https://github.com/sigurdga/)).

Introduction
============

This is a small example on how to setup Sebastian Tschan's jQuery File Upload in Django. He has a working demo on his [webpage](http://aquantum-demo.appspot.com/file-upload) and a [github repository](https://github.com/blueimp/jQuery-File-Upload) with an example on how to do it in PHP.

Here, you'll find a minimal Django project with a minimal app. You can run the example standalone by cloning the repository, running the migrations and starting the server.

I want to give a thank to [Sebastian Tschan](https://github.com/blueimp), the original author, [Etay Cohen-Solal](https://github.com/et-cs), for the latest major update, and [Jørgen Bergquist](https://github.com/bergquis) for helping me over the first hurdles.

Features
========

* Drag and drop files
* Select multiple files
* Cancel upload
* Delete uploaded file (from database only)
* No flash (or other browser plugins) needed
* … more at the [upstream's features page](http://aquantum-demo.appspot.com/file-upload#features)

Requirements
============

* Django
* Python Imaging Library

If you do not get PIL to work (_pillow_ is a replacement package that works
with virtulalenvs), use FileField instead of ImageField in
fileupload/models.py as commented in the file.

Installation
============

I recommend to install this within a virtualenv.

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

And then go to localhost:8000 and try to upload some files.

License
=======
MIT, as the original project. See LICENSE.txt.
