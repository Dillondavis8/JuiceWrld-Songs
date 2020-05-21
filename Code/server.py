from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# Death Race for love link:
# https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png

#Goodbye and Good Riddance link:
#https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg

#Collab w Future album:
#https://upload.wikimedia.org/wikipedia/en/0/02/Wrld_on_Drugs.jpg

#Non-album songs
#https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg

current_id = 30

juiceWrldSongs = [ {
        "id": 1,
        "title": 'Lucid Dreams',
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg" ,
        "songDescription": "Lucid dreams is about a hard break-up in a relationship. It talks about how you cannot get the time spent with a person back. Juice talks about how this heartbreak pushes him to substance abuse sometimes. This is Juice Wrld's most played and successful song.",
        "plays":"124,000,000,000" ,
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 2,
        "title": "Robbery",
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Robbery is about finding a lover who promised not to hurt you. It talks about being confident in one's self and not showing insecurities. Although he tries to sound tough, he questions whether or not this girl loves him or not. The most famous line is 'She told me put my heart in the bag, and no body gets hurt.",
        "plays":"336,340,744" ,
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 3,
        "title": "All Girls Are The Same",
        "albumCover":"https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg" ,
        "songDescription":"This is the very first song I ever heard by Juice Wrld. This song alongside Lucid Dreams became the biggest hits from his Goodbye and Good Riddance album. Juice Wrld in an interview said he was going through relationship troubles when he wrote this song, and he wanted to make a 'biased ass statement'. He claims that all girls are the same, and that they all will break his heart in the end." ,
        "plays":"454,915,200" ,
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 4,
        "title": "Legends",
        "albumCover":"https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg" ,
        "songDescription":"Juice Wrld is speaking on how all of the so called 'legendary' young and upcoming artists are dying so young. He talks about how he wants to make a change, and that he is scared to succumb to the same fate. This song is now very heart wrenching to listen to now that Juice has tragically passed away only 6 days after his 21st birthday. Juice Wrld will indeed be remembered for the rest of time as a legend for his musical influence." ,
        "plays":"248,268,428" ,
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 5,
        "title": "Righteous",
        "albumCover":"https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg" ,
        "songDescription": "Righteous is a song about feeling holy. And it also speaks upon his constant struggle with anxiety and drug abuse. He speaks upon how his heart feels cold due to all of his vices. He talks about pushing through these issues and making it out in the end. This song was never offically released but leaked after his passing.",
        "plays": "500,000",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 6,
        "title":"Lean Wit Me" ,
        "albumCover":"https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg" ,
        "songDescription":"This song talks about drug abuse and the life struggles that come along with it. He speaks about how he tries to overcome, but he ends up falling into the same struggle of relapsing again. He then asks is the song who will do these drugs with him, becuase he might as well have fun doing them with people if he can't quit. This along with Lucid Dreams and All Girls Are The Same ended up being the most popular on this album." ,
        "plays": "314,079,060",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 7,
        "title":"Run" ,
        "albumCover":"https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg" ,
        "songDescription": "Run is a song about trying to run away from your own darkside. He talks about how in our souls, dark and light fight for the control. He says that no one knows though because no one truly understands what is going on in someone else's life. He says that it's hard for him to come down from his highs, and that he would rather stay there.",
        "plays":"29,000,000" ,
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 8,
        "title": "Flaws And Sins",
        "albumCover":"https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png" ,
        "songDescription": "Flaws And Sins in a song about exaclty the title. Juice raps about how this girl he has now met is the lighting to his thunder. He compliments he scars, saying that all of her imperfections are actually what he loves about her the most. He says that his new girl has completely changed his life for the better. ",
        "plays": "53,344,453",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 9,
        "title":"Empty" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice in an interview said that this song was him saying that even though he feels broken down at times, he still thanks God for all of the blessings in his life. He speaks about being completely empty and being on edge. He talks about how he doesn't understand how to deal with his pain besides numbing it with pills. This song is very moving and can help people who are feeling empty as well.",
        "plays": "108,700,234",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 10,
        "title":"Who Shot Cupid?" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice Wrld refers to Cupid a lot as a figure that forces him into negative love situations. Cupid always leads him to heart break, and he talks about his ex in the beginning and how she made him feel worthless. He references how all girls are the same and he has to continue to abuse drugs to stay sane. He then goes to talk about how there is a new girl in his life at the end of the song, and how he finally has overcome the trials Cupid has given him by shooting the wrong person for him. He then talks about hoping one day he would put the drugs away.",
        "plays": "38,278,227",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 11,
        "title":"Black & White" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "Black & White is about Juice's black and white friends. He talks about partying and doing drugs with both friend groups. He talks about having a good time, but how drugs still make him feel shitty at the end of the day. However, he still is going to do them and have a good time doing them with his black and white homies.",
        "plays": "191,234,404",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 12,
        "title":"Candles" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "Juice talks about how he still feels hurt and insecure from his past heartbreaks. He talks about how if someone wants to be with them, they are going to have to be the ones taking the first step. His last relationship was a blacked out blurr and full of hurt. He talks about how the devil tempts him to stay with negative company.",
        "plays": "98,127,490",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 13,
        "title":"Let Her Leave" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "Let Her Leave is about letting a good girl go. A girl is remarkable, and yet she was the one that slipped away. He then says that love is not meant for him. He thinks that drugs are the only source of happiness he deserves or will ever have. This song is also unreleased and was leaked.",
        "plays": "100,000",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 14,
        "title":"Never Cared" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "This song is about how Juice is won't take shit, and how he views his experience in the streets. He talks about how if someone comes at him, Juice and his brodies will go after them. He then also thanks God that he gave him his musical talent to now 'go hard'. This song was never officially released by Juice and is still unreleased.",
        "plays":"50,000" ,
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 15,
        "title":"In The Air" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "This song is about how Juice rose to the top on his own, and how people try to ride his wave. He talks about how people want to be his friend now that he is up and successful. He then hypes himself and his fame up. This song is a great showing of Juice's insane freestyle flow and melodic switch-up. Very catchy hook as well, and this song is unreleased as well.",
        "plays": "150,000",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 16,
        "title":"Maze" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice sings about being stuck in the maze of life. He feels like his life is a deathrace, most likely due to his struggle with addiction. He talks about numbing his pain with codine and going insane. He really struggles with his addiction in this song and opens up to his fans about it.",
        "plays": "67,687,729",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 17,
        "title":"Hear Me Calling" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "This song is a cry out to a girl asking if she hears him calling out to her. He talks about how he does not want any drama, but just wants to talk. This song is a very sweet song to the girl he is with. He talks about how in love he is with her.",
        "plays": "127,104,574",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 18,
        "title":"Desire" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "This song is quite simple. It is Juice talking about the girl of his dreams. He is saying that she is sitting right next to him. He talks about how he has his struggles, but that he wants the world to know how much he loves her. This song is very melodic and catchy, and that he won't let this girl go",
        "plays": "23,574,209",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 19,
        "title":"Rider" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice WRLD recorded Rider for his Death Race for Love album. The song was inspired by the Twisted Metal and Death Race vehicle combat video games that the rapper played growing up. It was the writing of this track that prompted the album's title. He sings about a girl, asking if she will always ride for him.",
        "plays": "21,805,987",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 20,
        "title":"Wasted" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "This song is a reference to GTA's death feature where if you die it says 'Wasted' on the screen. He talks about how a girl's love leaves him wasted. She broke his heart and now he feels like dying. This is one of Juice's first top songs.",
        "plays": "231,387,650",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 21,
        "title": "I'll Be Fine",
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "Juice talks about how he deals with his heartbreak. He feels broken and takes drugs to cope with his struggles. He does not want others to worry about him. He thinks he can get over it himself, and doesnt need anyone to be involved. ",
        "plays": "78,276,153",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 22,
        "title":"Scared Of Love" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "Juice talks about being scared of loving a person again. His last relationship hurt him so bad, so he doesn't want to give his love freely again. He talks about not being enough and being on drugs too much. He opens up about struggling in a relationship.",
        "plays": "94,384,758",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 23,
        "title":"Hurt Me" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "songDescription": "Juice talks about turning into a new person. He talks about how life throws shit at him, but the drugs he uses will not hurt him. He is saying that no girl can hurt him anymore. He is saying that the drugs are the only love he needs.",
        "plays": "85,736,098",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 24,
        "title":"Rockstar Girl" ,
        "albumCover": "https://i1.sndcdn.com/artworks-000232701370-a7rwom-t500x500.jpg",
        "songDescription": "This song is about meeting a rockstar girl. This girl loves to party and take drugs. She convices Juice to party with her, and he is never the same after. He talks about racing her to death because of all of the drugs they are taking.",
        "plays": "7,200,000",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 25,
        "title":"Won't Let Go" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice talks about there being no such thing as being too close to a person. He is referring to his current girlfriend. He says that he will never let her go. He is very in love and happy with this girl.",
        "plays": "19,142,675",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 26,
        "title":"Ring Ring" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice is talking about not wanting to do anything for the day. He doesn't want to be bothered by anyone, but he also does not like being alone. He talks his struggle with drugs, and that it is the devils fault. He talks about his vices with drugs throughout the song, and it is this struggle that makes him depressed and want to be alone.",
        "plays": "42,079,765",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 27,
        "title":"Fast" ,
        "albumCover": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "songDescription": "Juice sings about how fast life is going for him right now. He also talks about how his fame and living 'the fast life' has taken a toll on him. He is telling people to chase their dreams before it is too late. He also refers to his drug addiction here as well. His message is one of hope.",
        "plays": "144,725,019",
        "platforms": [
            {
                "name": "Spotify", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "Apple Music", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 28,
        "title":"Underworld" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "This song is about a demon girl that has control of him. He said that he does not want her, but he likes the comfort he gets when she holds him. He talks about the drugs he doing, and he refers to him dying young due to his demons. He then says that him and this demon girl will roam the Underworld for eternity.",
        "plays": "98,432",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 29,
        "title":"Autograph" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "This song was Juice's first single to make with a music video. He released this song whenever he was still getting under 10k views per song. This is a very special song to the fans that supported him from the start. This song is about people trying to keep him down due to his small success at the time.",
        "plays": "18,520,837",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    {
        "id": 30,
        "title":"Forever" ,
        "albumCover": "https://t2.genius.com/unsafe/440x440/https%3A%2F%2Fimages.genius.com%2F2caaa365d75ba8420e55d1da0c55c65f.500x500x1.jpg",
        "songDescription": "This was Juice Wrld's first song to ever drop. It was recorded on his phone due to not having any access to studio equipment at the time. This song started his career, and the song is talking about a girl that he will love forever. Juice Wrld you will always be remembered <3",
        "plays": "8,308,467",
        "platforms": [
            {
                "name": "SoundCloud", 
                "marked_as_deleted": "false"
            }, 
            {
                "name": "YouTube", 
                "marked_as_deleted": "false"
            }
        ]
    },

    ]

newSong = []

@app.route('/')
def songSearch():
    return render_template('home.html', songs=juiceWrldSongs)

@app.route('/search_list', methods=['GET'])
def searchList():
    global juiceWrldSongs
    songTitle = request.args.get('q')
    searchResults = []
    
    for i, song in enumerate(juiceWrldSongs):
        idNum = song["id"]
        songDesc = song["songDescription"]
        name = song["title"]
        
        if(name.lower().find(songTitle.lower()) != -1 or songDesc.lower().find(songTitle.lower()) != -1):
            startIndex = songDesc.lower().find(songTitle.lower())
            if(startIndex != -1):

                
                newDesc = songDesc.replace(songTitle, '<span class="lit">' + songTitle + '</span>')

                new_song_entry = {
                    "id" : idNum,
                    "title" : name,
                    "songDescription" : newDesc
                }       
                searchResults.append(new_song_entry)
            elif (startIndex == -1):
                new_song_entry = {
                    "id" : idNum,
                    "title" : name,
                    "songDescription" : songDesc
                }       
                searchResults.append(new_song_entry)
            
    return render_template('results.html', songs=searchResults)

@app.route('/view/<id>', methods=['Post'])
def saveEdit(id):
    global juiceWrldSongs

    json_data = request.get_json()

    songDesc = json_data["songDescription"]
    
    for i, song in enumerate(juiceWrldSongs):
        idNum = song["id"]
        title = song["title"]
        albumCover = song["albumCover"]
        plays = song["plays"]
        platforms = song["platforms"]
        if(idNum == int(id)):
            song["songDescription"] = songDesc
            song_entry = {
                "id": idNum,
                "title" : title,
                "albumCover" : albumCover,
                "songDescription" : songDesc,
                "plays" : plays,
                "platforms" : platforms

            }

    return jsonify(song= song_entry)

@app.route('/num/<id>', methods=['Post'])
def saveNumEdit(id):
    global juiceWrldSongs

    json_data = request.get_json()

    songPlays = json_data["plays"]
    
    for i, song in enumerate(juiceWrldSongs):
        idNum = song["id"]
        title = song["title"]
        albumCover = song["albumCover"]
        songDesc = song["songDescription"]
        platforms = song["platforms"]
        if(idNum == int(id)):
            song["plays"] = songPlays
            song_entry = {
                "id": idNum,
                "title" : title,
                "albumCover" : albumCover,
                "songDescription" : songDesc,
                "plays" : songPlays,
                "platforms" : platforms

            }

    return jsonify(song= song_entry)

@app.route('/view/<id>', methods=['GET'])
def viewSong(id):
    global juiceWrldSongs
    for i, song in enumerate(juiceWrldSongs):
        idNum = song["id"]
        title = song["title"]
        albumCover = song["albumCover"]
        songDescription = song["songDescription"]
        plays = song["plays"]
        platforms = song["platforms"]
        if(idNum == int(id)):
            song_entry = {
                "id": idNum,
                "title" : title,
                "albumCover" : albumCover,
                "songDescription" : songDescription,
                "plays" : plays,
                "platforms" : platforms
            }

    return render_template('view.html', song = song_entry)

@app.route('/view/<int:id>/<int:index>', methods=['DELETE'])
def delete_platform(id, index):
        global juiceWrldSongs
        
        plat_index = index
        for idx, song in enumerate(juiceWrldSongs):
            idNum = song["id"]
            title = song["title"]
            albumCover = song["albumCover"]
            songDescription = song["songDescription"]
            plays = song["plays"]
            platforms = song["platforms"]
            if(song["id"] == id):
                song["platforms"][plat_index]["marked_as_deleted"] = "true"
                
                new_song = {
                    "id": idNum,
                    "title": title,
                    "albumCover": albumCover,
                    "songDescription": songDescription,
                    "plays": plays,
                    "platforms": platforms
                }
        
        return jsonify(songs= new_song)

@app.route('/undo/<int:id>/<int:index>', methods=['DELETE'])
def undo_delete_platform(id, index):
        global juiceWrldSongs

        plat_index = index
        for idx, song in enumerate(juiceWrldSongs):
            idNum = song["id"]
            title = song["title"]
            albumCover = song["albumCover"]
            songDescription = song["songDescription"]
            plays = song["plays"]
            platforms = song["platforms"]
            if(song["id"] == id):
                song["platforms"][plat_index]["marked_as_deleted"] = "false"
                
                new_song = {
                    "id": idNum,
                    "title": title,
                    "albumCover": albumCover,
                    "songDescription": songDescription,
                    "plays": plays,
                    "platforms": platforms
                }
                

        
        return jsonify(songs= new_song)

@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html', newSong=newSong)

@app.route('/create_song', methods=['GET', 'POST'])
def create_song():
    global juiceWrldSongs
    global current_id

    json_data = request.get_json()

    current_id += 1
    new_id = current_id 

    title = json_data["title"]
    albumCover = json_data["albumCover"]
    songDescription = json_data["songDescription"]
    plays = json_data["plays"]
    platforms = json_data["platforms"]
    platformsArr = []

    for idx, song in enumerate(platforms):
        platformsArr.append({"name": song, "marked_as_deleted" : "false"})

    new_song = {
        "id": new_id,
        "title": title,
        "albumCover": albumCover,
        "songDescription": songDescription,
        "plays": plays,
        "platforms": platformsArr 
    }
    juiceWrldSongs.append(new_song)

    return jsonify(newSong= new_song)



if __name__ == '__main__':
   app.run(debug = True)




