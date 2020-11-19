from django.http import HttpResponse
from .makeProfile import makeProfile


def index(request):
    profile = makeProfile(False, False)

    positionString = ", ".join(profile["positions"])
    factsHTML = "<br />".join(profile["facts"])
    html = ("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>{0} ({1}) Profile</title>
    </head>
        <body style="font-family: Courier New; font-size: 20px;" >
            <p style="text-align: center"><strong>{0} ({1}) Profile</strong><br />
            <span>Positions:</span> {2}<br />
            <span>Sign:</span> {3}<br />
            <span>Blood Type:</span> {4}<br />
            <span>MBTI:</span> {5}<br />

            <p style="text-align: center"><span><strong>{0} facts:</strong></span><br />
            {6}
        </body>
    </html>"""
    .format(profile["name"], profile["group"],
        positionString,
        profile["sign"],
        profile["bloodType"],
        profile["MBTI"]),
        factsHTML)
    return HttpResponse(html)
