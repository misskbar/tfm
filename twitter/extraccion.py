import tweepy
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# integracion con twitter
auth = tweepy.OAuthHandler('Nj40NaxlK9QMXAqKQm5HPHUfS', '0gVWDDNAsx6ZIonCoRxHUhg65Xr56ubiumFSK7RE8RVBQjE5yP')
auth.set_access_token('1169441779109814274-3MlhXBObAjbyktwhDECDI0lJ0vx17e', 'Poy8wOSbNCJxg1KRs6jSS77tEsfspD46LkMqmvF8czjjR')
api = tweepy.API(auth)

# creacion de dataframe
tweets = pd.DataFrame()

tweets = pd.DataFrame(columns=['screenname_usuario',
	                           'nombre_usuario',
	                           'descripcion_usuario',
	                           'foto_usuario',
	                           'cantidad_tweets_usuario',
	                           'fecha_creacion_cuenta',
	                           'usuario_verificado',
	                           'followers_usuario',
	                           'following_usuario',
	                           'ubicacion_usuario',
	                           'lenguaje_usuario',
	                           'zona_horaria_usuario',
	                           'tweet', 
	                           'fuente', 
	                           'fecha_publicacion',
	                           'ubicacion_tweet',
	                           'en_respuesta_a',
	                           'lenguaje_tweet',
	                           'tokenized_tweet',
	                           'sentiment'])

# extraccion de tweets
for tweet in tweepy.Cursor(api.search,
                           q="ikea",
                           geocode="40.416775,-3.703790,2000km",
              			   until="2019-08-28",
                           result_type="recent",
                           include_entities=True,
                           lang="es").items(10):
    user = api.get_user(tweet.user.id)
    print ('====================================================')
    print ("Source: "+ tweet.source)
    print ("Tweet: "+ tweet.text)
    print ("Written at: " + str(tweet.created_at))
    print ("User ID: " + str(tweet.user.id))
    print ("Geo: " + str(tweet.geo))
    print ("Id: " + str(tweet.id))
    print ("In reply to: " + str(tweet.in_reply_to_user_id))
    print ("Lang: " + tweet.lang)
    print ('Name: ' + user.name)
    print ('Location: ' + user.location)
    print ('Friends: ' + str(user.friends_count))
    print ('ID: ' + str(user.id))
    print ('Screen Name: ' + str(user.screen_name))
    print ('Creado en: ' + str(user.created_at))
    print ('Descripcion: ' + user.description)
    print ('Favoritos: ' + str(user.favourites_count))
    print ('Geo: ' + str(user.geo_enabled))
    print ('Leguaje: ' + str(user.lang))
    print ('Protegido: ' + str(user.protected))
    print ('Tweets: ' + str(user.statuses_count))
    print ('Followers: ' + str(user.followers_count))
    print ('Time Zone: ' + str(user.time_zone))
    print ('Verificado: ' + str(user.verified))
    print ('Url: ' + str(user.url))
    print ('Url Foto: ' + user.profile_image_url)
    print ('====================================================\n')
    tweets = tweets.append({'screenname_usuario' : user.screen_name,
    	           'nombre_usuario' : user.name,
    	           'descripcion_usuario' : user.description,
    	           'foto_usuario' : user.profile_image_url,
    	           'cantidad_tweets_usuario' : user.statuses_count,
    	           'fecha_creacion_cuenta' : user.created_at,
    	           'usuario_verificado' : user.verified,
    	           'followers_usuario' : user.followers_count,
    	           'following_usuario' : user.friends_count,
    	           'ubicacion_usuario' : user.location,
    	           'lenguaje_usuario' : user.lang,
                   'zona_horaria_usuario' : user.time_zone,
                   'tweet' : tweet.text,
                   'fuente' : tweet.source,
                   'ubicacion_tweet' : tweet.geo,
                   'en_respuesta_a' : tweet.in_reply_to_user_id,
                   'lenguaje_tweet' : tweet.lang,
                   'tokenized_tweet' : '',
                   'sentiment' : ''}, ignore_index=True)
print(tweets.shape)

stopwords_esp = stopwords.words('spanish')

# pasar todo el contenido a minusculas
tweets['tokenized_tweet'] = tweets.apply(lambda row: row['tweet'].lower(), axis=1)

# tokenizar
tweets['tokenized_tweet'] = tweets['tokenized_tweet'].apply(lambda row: nltk.word_tokenize(row))














