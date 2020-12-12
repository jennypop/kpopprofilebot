from django.http import HttpResponse
from .makeProfile import makeProfile


def index(request):
    profile = makeProfile(False, False)

    positionString = ", ".join(profile.positions)
    factsHTML = "<br />".join(profile.facts)
    html = ("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>{0} ({1}) Profile</title>
    </head>
        <body style="font-family: Courier New; font-size: 20px;" >
            <p style="text-align: center"><strong>{0} ({1}) Profile</strong><br />
            <span>Positions:</span> {2}<br />
            <span>Age:</span> {3} (born {4})<br />
            <span>Debuted:</span> {5}<br />
            <span>Sign:</span> {6}<br />
            <span>Blood Type:</span> {7}<br />
            <span>MBTI:</span> {8}<br />

            <p style="text-align: center"><span><strong>{0} facts:</strong></span><br />
            {9}
        </body>
    </html>""").format(profile.name, profile.group,
        positionString,
        profile.ageString,
        profile.birthDateString,
        profile.debutDateString,
        profile.sign,
        profile.bloodType,
        profile.MBTI,
        factsHTML)
    return HttpResponse(html)
