

def check_read_articles(request):
    try:
        read_articles = request.session["read_articles"]
    except:
        request.session["read_articles"] = []
        read_articles = request.session.get("read_articles")
    return read_articles