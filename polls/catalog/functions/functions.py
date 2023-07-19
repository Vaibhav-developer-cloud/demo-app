def handle_uploaded_file(f):
    with open('catalog/static/images'+f.name,'wb+') as filename:
        for chunk in f.chunks():
            filename.write(chunk)