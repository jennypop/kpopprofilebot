import csv
import random
import re
import csvPaths, factProcessor

words = {"movie": [],
"disneyMovie": [],
"movieHabit": ["chew loudly", "unwrap sweet wrappers", "spill popcorn", "laugh out loud", "shout at the screen", "scream", "cackle", "curse at the characters", "go to the toilet", "fall asleep", "dance", "cry", "hit others", "sing along", "repeat the lines", "munch !HER! popcorn so much !SHE! hurts !HER! jaw", ],
"hatedMovieReason": ["!SHE! can't stay focused on them", "they make !HER! scared", "!SHE! just doesn't look them up on purpose"],
"favoriteMovieFact": ["!SHE! cries(( every time)) while watching it", "!SHE! watched it ((about ))!SMALLINT! times(( as a kid))", "it has !HER! favorite actor", "!SHE! watched it at !HER! first date", "!SHE! loves the ending", "!SHE! watched it after passing !HER! exam", "it was [closePerson]'s favorite movie", "it was the only movie that played at !HER! cinema"],
"movieGenre": ["horror", "Pixar/Disney movies", "romance", "Sci-Fi", "comedy", "family", "action", "fantasy", "thriller", "mellow", "drama", "anime", "European", "arthouse", "superhero", "zombie", "French", "Hong Kong", "anti-capitalist", "mafia", "romantic comedy", "basketball", "biographical", "classic", "black and white", "silent", "Western", "Gay & Lesbian drama", "indie", "documentary", "musical", "detective"],
}


favoriteMovieFactTemplates = [
    "!HER! favorite Disney movie is [disneyMovie]",
    "[disneyMovie] was the first Disney film that !SHE! saw",
    "!HER! favorite movie is [movie]",
    "!SHE! is a fan of ([movie])*2( and )",
    "!SHE! loves the movie ([movie])*2( and )",
    "!HER! recommended movie is ([movie])*2( and )",
    "[movie] was the first movie that !SHE! saw",
    "[movie] is !HER! {favorite/most watched} movie",
    "The most memorable movie for !HERHIM! is [movie]",
    "!SHE! watches [movie] [oftenTimePeriod]"]
#+ "([favoriteMovieFact])"

favoriteGenreFactTemplates = ["!HER! favorite {genre of movies/movie type/type of movies} is ([movieGenre])*2( and )",
"!SHE! enjoys ([movieGenre])*2( and ) movies",
"!SHE! likes [movieGenre] movies more than [movieGenre] movies",
"!SHE! prefers [movieGenre] movies over [movieGenre] ones",
"!SHE! likes to watch [movieGenre] movies with !IDOLNAME!",
"The only type of movie !SHE! doesn't fall asleep during is ([movieGenre])*2( and ) movies"]
# + ", one of !HER! favorite movies is [movie]"
# + ", !SHE!'s the type to [movieHabit]"

hatedGenreFactTemplates = [  # "!SHE! doesn't watch [movieGenre] movies because [hatesMovieGenreReason]",
"!SHE! can't watch ([movieGenre])*2( or ) movies",
"!SHE! falls asleep when watching [movieGenre] movies",
"!SHE! has a love hate relationship with [movieGenre] movies",
"!SHE! is a fan of movies but hates [movieGenre] genre", ]

otherMovieFactTemplates = ["!SHE! likes to watch movies [whenSituation]",
"[whenSituation] !SHE! watches {[movie]/[movieGenre] movies}",
"!SHE!'s the type to [movieHabit] when watching movies",
"!HER! members complained that !SHE! will [movieHabit] when watching movies",
"!SHE! made a cover for the OST of the film [movie]",
# "!SHE! sang the theme song of the film [kmovie]",
"!SHE! voiced a character in the Korean dub of [movie]",
"!SHE! dressed up as a character from [movie]", ]


# movielist generator
def getMovies():
    moviePath = csvPaths.moviesPath
    moviefile = open(moviePath, 'r', encoding="utf8")
    movies = []
    with moviefile:
        movieReader = csv.reader(moviefile)
        for line in movieReader:
            movies.append(line[0])

    disneyMoviePath = csvPaths.moviesDisneyPath
    disneyMovieFile = open(disneyMoviePath, 'r', encoding="utf8")
    disneyMovies = []
    with disneyMovieFile:
        disneyMovieReader = csv.reader(disneyMovieFile)
        for line in disneyMovieReader:
            disneyMovies.append(line[0])
            movies.append(line[0])
    return movies, disneyMovies


def processFactTemplate(txt):
    txt = factProcessor.processABCChoice(txt)
    txt = factProcessor.processAsterisk(txt)
    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    return txt


words["movie"], words["disneyMovie"] = getMovies()
movieFactTemplates = favoriteMovieFactTemplates + favoriteGenreFactTemplates + hatedGenreFactTemplates + otherMovieFactTemplates


def getFacts(n):
    factList = random.sample(movieFactTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
